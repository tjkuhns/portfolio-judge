"""Portfolio review orchestrator.

Ties together:

1. Ingest (local path or GitHub tarball)
2. Structural scanner (deterministic)
3. Prose judge on README + top docs (parallel)
4. Code judge on top Python files (parallel)
5. Persona agents — each reads grounding + persona definition + role +
   component outputs, produces a structured review (parallel)
6. Synthesizer — one LLM call across the persona outputs produces the
   final verdict

Output is a PortfolioReview dataclass; the CLI renders it as markdown.
"""

from __future__ import annotations

import asyncio
from dataclasses import asdict, dataclass, field
from importlib import resources
from pathlib import Path
from typing import Any

from portfolio_judge.core.llm import Provider, resolve_provider
from portfolio_judge.core.rubric import DraftScore, load_rubric
from portfolio_judge.ingest import PortfolioArtifacts, fetch_github, fetch_local
from portfolio_judge.judges import code as code_judge
from portfolio_judge.judges import prose as prose_judge
from portfolio_judge.judges.structure import StructuralReport, scan_directory

ROLE_DESCRIPTIONS = {
    "applied-ai": "Applied AI Engineer / Agentic Engineering",
    "fde": "Forward Deployed Engineer",
    "solutions": "AI Solutions Engineer",
    "devrel": "Developer Relations / Developer Advocate",
    "all": "Applied AI Engineer / FDE / Solutions Engineer / DevRel",
}

ALL_PERSONAS = ["recruiter", "applied_ai_hm", "fde_solutions_hm", "devrel_hm"]


@dataclass
class PortfolioReview:
    """Complete output of a portfolio review."""

    source: str
    role: str
    model: str | None
    structural: dict[str, Any]
    prose_scores: list[dict[str, Any]] = field(default_factory=list)
    code_scores: list[dict[str, Any]] = field(default_factory=list)
    persona_reviews: dict[str, str] = field(default_factory=dict)
    synthesis: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


# ── Persona + grounding loading ──


def _pkg_text(relative_path: str) -> str:
    """Read a text file shipped inside the portfolio_judge package."""
    ref = resources.files("portfolio_judge").joinpath(relative_path)
    with resources.as_file(ref) as p:
        return Path(p).read_text(encoding="utf-8")


def _load_persona(name: str) -> str:
    return _pkg_text(f"personas/{name}.md")


def _load_grounding() -> str:
    return _pkg_text("grounding.md")


# ── Component-summary text for the personas ──


def _render_component_summary(
    artifacts: PortfolioArtifacts,
    structural: StructuralReport,
    prose_scores: list[DraftScore],
    code_scores: list[DraftScore],
) -> str:
    """Build the text block each persona reads as 'what the component judges found'."""
    lines: list[str] = []

    lines.append("## Structural findings")
    for f in structural.findings:
        mark = "✅" if f.passed else "❌"
        lines.append(f"- {mark} **{f.check}** ({f.severity}): {f.evidence}")

    if prose_scores:
        lines.append("\n## Prose judge scores")
        for ds in prose_scores:
            total = ds.total_unweighted()
            max_score = 5 * len(ds.criterion_scores)
            lines.append(f"\n### {ds.source} — {total}/{max_score}")
            for c in ds.criterion_scores:
                lines.append(f"- **{c.criterion_id}**: {c.score}/5 — {c.reasoning.strip()}")
    else:
        lines.append("\n## Prose judge scores\nNo prose artifacts scored.")

    if code_scores:
        lines.append("\n## Code judge scores")
        for ds in code_scores:
            total = ds.total_unweighted()
            max_score = 5 * len(ds.criterion_scores)
            lines.append(f"\n### {ds.source} — {total}/{max_score}")
            for c in ds.criterion_scores:
                lines.append(f"- **{c.criterion_id}**: {c.score}/5 — {c.reasoning.strip()}")
    else:
        lines.append("\n## Code judge scores\nNo code artifacts scored.")

    lines.append("\n## Portfolio artifacts seen")
    if artifacts.readme_text:
        readme_preview = artifacts.readme_text[:1500].rstrip()
        lines.append(f"\n### README excerpt\n\n{readme_preview}\n")
    if artifacts.docs:
        lines.append("### Docs/writing sampled:")
        for name, _ in artifacts.docs:
            lines.append(f"- {name}")
    if artifacts.code_files:
        lines.append("\n### Code files sampled:")
        for name, _ in artifacts.code_files:
            lines.append(f"- {name}")

    return "\n".join(lines)


# ── Persona agent invocation ──


async def _run_persona(
    persona_name: str,
    role: str,
    component_summary: str,
    grounding: str,
    provider: Provider,
    model: str | None,
) -> tuple[str, str]:
    persona_prompt = _load_persona(persona_name)

    system = (
        "# Grounding\n\n"
        f"{grounding}\n\n"
        "---\n\n"
        "# Your persona\n\n"
        f"{persona_prompt}"
    )
    user = (
        f"# Candidate\n\n"
        f"The candidate is applying for: {ROLE_DESCRIPTIONS.get(role, role)}.\n\n"
        "You have NOT seen this portfolio directly. Instead, you have the "
        "deterministic structural scan, the component-judge scores on the "
        "prose and code artifacts, and a representative excerpt of the "
        "README. Base your review on those findings and the rubric scores "
        "they yielded. Cite specific findings and scores in your reasoning.\n\n"
        "---\n\n"
        f"{component_summary}\n\n"
        "---\n\n"
        "Produce your review in the persona's output format."
    )
    text = await provider.generate_text(
        system=system,
        user=user,
        model=model,
        max_tokens=4096,
        temperature=0.3,
    )
    return persona_name, text.strip()


# ── Synthesizer ──


_SYNTHESIS_SYSTEM = """You are synthesizing the verdicts of four \
independent reviewers who each evaluated the same AI engineering portfolio. \
Your job: surface what the reviewers converge on, disagree on, and \
collectively recommend. Be decisive. The candidate needs specific signal, \
not political hedging.

Use the same disclosure-forward register the grounding heuristics call out \
(disclosed limits are credibility multipliers)."""


_SYNTHESIS_OUTPUT_FORMAT = """
## Convergent verdict
One-line synthesis of the four reviewers' decisions.

## Convergent strengths
Specific things multiple reviewers praised. Cite which reviewers.

## Convergent gaps
Specific things multiple reviewers flagged. Cite which reviewers.

## Role-fit ranking
Best / stretch / bad-fit call, synthesized from the reviewers.

## Probability estimate
Rough estimate (percentile of inbound for the role type) based on reviewer consensus.

## Top 3 actionable next steps
Ordered by leverage. Specific, not generic.
"""


async def _synthesize(
    persona_reviews: dict[str, str],
    role: str,
    provider: Provider,
    model: str | None,
) -> str:
    body = "\n\n---\n\n".join(
        f"# Reviewer: {name}\n\n{text}" for name, text in persona_reviews.items()
    )
    user = (
        f"The candidate is applying for: {ROLE_DESCRIPTIONS.get(role, role)}.\n\n"
        f"Here are the four reviews:\n\n---\n\n{body}\n\n---\n\n"
        "Produce the synthesis in this format:\n"
        f"{_SYNTHESIS_OUTPUT_FORMAT}"
    )
    text = await provider.generate_text(
        system=_SYNTHESIS_SYSTEM,
        user=user,
        model=model,
        max_tokens=2048,
        temperature=0.3,
    )
    return text.strip()


# ── Public entry point ──


async def review_portfolio(
    source: str,
    role: str = "applied-ai",
    personas: list[str] | None = None,
    model: str | None = None,
    provider: Provider | None = None,
    github_token: str | None = None,
) -> PortfolioReview:
    """Run the full portfolio review pipeline.

    Args:
        source: GitHub URL (https://github.com/owner/repo) or local directory path.
        role: applied-ai | fde | solutions | devrel | all.
        personas: subset of persona names to run (default: all four).
        model: model shortcut / ID.
        provider: pre-built Provider (overrides model-string resolution).
        github_token: GitHub token for API rate-limit lifting.

    Returns a PortfolioReview with component outputs, persona reviews, and synthesis.
    """
    if provider is None:
        provider, resolved_model = resolve_provider(model)
        model = resolved_model
    if personas is None:
        personas = ALL_PERSONAS

    is_github = source.startswith(("http://", "https://"))
    fetch_fn = (lambda: fetch_github(source, github_token)) if is_github else (lambda: fetch_local(source))

    with fetch_fn() as artifacts:
        structural = scan_directory(artifacts.local_path)

        prose_rubric = load_rubric(prose_judge.default_rubric_path())
        code_rubric = load_rubric(code_judge.default_rubric_path())

        # Assemble the prose tasks: README + docs
        prose_tasks: list[asyncio.Task[DraftScore]] = []
        if artifacts.readme_text:
            prose_tasks.append(
                asyncio.create_task(
                    prose_judge.review_prose(
                        text=artifacts.readme_text,
                        source="README.md",
                        rubric=prose_rubric,
                        model=model,
                        provider=provider,
                    )
                )
            )
        for rel_path, text in artifacts.docs:
            prose_tasks.append(
                asyncio.create_task(
                    prose_judge.review_prose(
                        text=text,
                        source=rel_path,
                        rubric=prose_rubric,
                        model=model,
                        provider=provider,
                    )
                )
            )

        # Code tasks
        code_tasks: list[asyncio.Task[DraftScore]] = []
        for rel_path, text in artifacts.code_files:
            code_tasks.append(
                asyncio.create_task(
                    code_judge.review_code(
                        source_code=text,
                        source=rel_path,
                        rubric=code_rubric,
                        model=model,
                        provider=provider,
                    )
                )
            )

        prose_scores = await asyncio.gather(*prose_tasks) if prose_tasks else []
        code_scores = await asyncio.gather(*code_tasks) if code_tasks else []

        component_summary = _render_component_summary(
            artifacts, structural, prose_scores, code_scores
        )

        grounding = _load_grounding()
        persona_results = await asyncio.gather(
            *[
                _run_persona(
                    persona_name=p,
                    role=role,
                    component_summary=component_summary,
                    grounding=grounding,
                    provider=provider,
                    model=model,
                )
                for p in personas
            ]
        )
        persona_reviews = dict(persona_results)

        synthesis = await _synthesize(persona_reviews, role, provider, model)

        return PortfolioReview(
            source=source,
            role=role,
            model=model,
            structural=structural.to_dict(),
            prose_scores=[ds.to_dict() for ds in prose_scores],
            code_scores=[ds.to_dict() for ds in code_scores],
            persona_reviews=persona_reviews,
            synthesis=synthesis,
        )


def render_review_markdown(review: PortfolioReview) -> str:
    """Render a PortfolioReview as a standalone markdown report."""
    lines: list[str] = []
    lines.append(f"# Portfolio review: {review.source}\n")
    lines.append(f"**Role:** {ROLE_DESCRIPTIONS.get(review.role, review.role)}")
    lines.append(f"**Model:** {review.model or 'default'}\n")

    lines.append("---\n\n## Synthesis\n")
    lines.append(review.synthesis)

    lines.append("\n---\n\n## Per-reviewer verdicts\n")
    for name, text in review.persona_reviews.items():
        lines.append(f"\n### Reviewer: {name}\n")
        lines.append(text)

    lines.append("\n---\n\n## Structural findings\n")
    for f in review.structural["findings"]:
        mark = "✅" if f["passed"] else "❌"
        lines.append(f"- {mark} **{f['check']}** ({f['severity']}): {f['evidence']}")

    if review.prose_scores:
        lines.append("\n---\n\n## Prose judge scores\n")
        for ds in review.prose_scores:
            total = ds["total_unweighted"]
            max_score = 5 * len(ds["criterion_scores"])
            lines.append(f"\n### {ds['source']} — {total}/{max_score}")
            for c in ds["criterion_scores"]:
                lines.append(f"- **{c['criterion_id']}**: {c['score']}/5 — {c['reasoning'].strip()}")

    if review.code_scores:
        lines.append("\n---\n\n## Code judge scores\n")
        for ds in review.code_scores:
            total = ds["total_unweighted"]
            max_score = 5 * len(ds["criterion_scores"])
            lines.append(f"\n### {ds['source']} — {total}/{max_score}")
            for c in ds["criterion_scores"]:
                lines.append(f"- **{c['criterion_id']}**: {c['score']}/5 — {c['reasoning'].strip()}")

    return "\n".join(lines)
