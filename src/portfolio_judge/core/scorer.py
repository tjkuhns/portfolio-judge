"""Shared rubric-driven scoring.

Domain-agnostic LLM-as-judge scoring: given a rubric, an artifact, and a
provider, produce a DraftScore. The prose judge and code judge are both
thin wrappers over this.

Design notes:

* G-Eval-style prompt structure (Liu et al., EMNLP 2023): CoT reasoning
  required before each score.
* Structured output enforced via provider-native mechanisms (tool_use /
  json_schema / response_schema) rather than freeform JSON parsing.
* Flat parallel-primitive schema (one `{id}__reasoning` string + one
  `{id}__score` integer per criterion) avoids a specific failure mode
  where Anthropic Opus serializes nested-object arrays with unescaped
  inner quotes.
"""

from __future__ import annotations

from typing import Any

from portfolio_judge.core.llm import Provider, resolve_provider
from portfolio_judge.core.rubric import CriterionScore, DraftScore, Rubric

DEFAULT_SYSTEM_PROMPT = """You are an editorial judge evaluating an artifact \
against a published rubric. For each criterion:

1. Read the criterion's name, what-it-measures, and 1 / 3 / 5 anchor descriptions.
2. Think through the artifact systematically: does it meet the criterion?
3. Write 2–4 sentences of reasoning citing specific evidence from the artifact.
4. Commit to an integer score from 1 to 5 per the anchor descriptions.

Be strict. A score of 5 means 'commanding' — top quartile. A score of 3 means \
'competent.' A score of 1 is a veto flag. Reserve 4 and 5 for criteria where the \
artifact clearly demonstrates the move; when the evidence is ambiguous, score lower."""


def build_judge_tool_schema(rubric: Rubric) -> dict[str, Any]:
    """Flat parallel-array schema: `{id}__reasoning` + `{id}__score` per criterion."""
    properties: dict[str, Any] = {}
    required: list[str] = []
    for c in rubric.criteria:
        properties[f"{c.id}__reasoning"] = {
            "type": "string",
            "description": (
                f"2–4 sentences of reasoning for '{c.name}', citing specific "
                "evidence from the artifact, written before committing a score."
            ),
        }
        properties[f"{c.id}__score"] = {
            "type": "integer",
            "minimum": 1,
            "maximum": 5,
            "description": f"Integer 1–5 for '{c.name}' per the criterion's anchor descriptions.",
        }
        required.extend([f"{c.id}__reasoning", f"{c.id}__score"])
    return {"type": "object", "properties": properties, "required": required}


def _format_criterion(c) -> str:
    weight_note = f" [weighted {c.weight}x]" if c.weight else ""
    return (
        f"### {c.id}: {c.name}{weight_note}\n\n"
        f"**What it measures:** {c.what_it_measures.strip()}\n\n"
        "**Scoring anchors:**\n"
        f"- **1 (fail):** {c.scale[1]}\n"
        f"- **3 (competent):** {c.scale[3]}\n"
        f"- **5 (commanding):** {c.scale[5]}\n"
    )


def build_judge_prompt(
    artifact_text: str,
    rubric: Rubric,
    artifact_label: str = "artifact",
    custom_instructions: str = "",
) -> tuple[str, str]:
    """Build (system, user) prompts for the judge call.

    `artifact_label` names what's being scored ('draft', 'code file',
    'README', etc.) so the model knows the register. `custom_instructions`
    lets each judge type (prose / code) append domain-specific guidance.
    """
    system = DEFAULT_SYSTEM_PROMPT
    if custom_instructions:
        system += f"\n\n{custom_instructions.strip()}"

    criteria_md = "\n\n".join(_format_criterion(c) for c in rubric.criteria)
    user = (
        f"# {artifact_label.capitalize()} to evaluate\n\n"
        f"<{artifact_label}>\n{artifact_text}\n</{artifact_label}>\n\n"
        f"# Rubric\n\n{criteria_md}\n\n"
        "# Task\n\n"
        "Score every criterion. Write 2–4 sentences of reasoning citing specific "
        "evidence from the artifact BEFORE committing a score. Be strict; reserve "
        "4 and 5 for clear demonstrations."
    )
    return system, user


def _extract_scores(payload: dict[str, Any], rubric: Rubric) -> list[CriterionScore]:
    """Parse the flat-schema tool input into CriterionScore objects."""
    scores: list[CriterionScore] = []
    missing: list[str] = []
    for c in rubric.criteria:
        reasoning_key = f"{c.id}__reasoning"
        score_key = f"{c.id}__score"
        if reasoning_key not in payload or score_key not in payload:
            missing.append(c.id)
            continue
        scores.append(
            CriterionScore(
                criterion_id=c.id,
                reasoning=str(payload[reasoning_key]),
                score=int(payload[score_key]),
            )
        )
    if missing:
        raise ValueError(f"Judge response missing criteria: {missing}")
    return scores


async def score_artifact(
    artifact_text: str,
    rubric: Rubric,
    source: str,
    artifact_label: str = "artifact",
    custom_instructions: str = "",
    model: str | None = None,
    provider: Provider | None = None,
) -> DraftScore:
    """Score an artifact against a rubric via LLM-as-judge.

    Args:
        artifact_text: the full text of the artifact being scored.
        rubric: validated Rubric.
        source: identifier for the artifact (file path, URL, etc.) — recorded
            on the DraftScore.
        artifact_label: what to call the artifact in the prompt ('draft',
            'code file', 'README').
        custom_instructions: extra guidance appended to the system prompt
            (e.g. "Grade Python code, not prose").
        model: model string passed to `resolve_provider`. If None, the provider
            argument must be supplied or a default is chosen from env vars.
        provider: pre-built Provider. If supplied, `model` is used as-is for
            the API call (or None, letting the provider pick its default).

    Returns a DraftScore.
    """
    if provider is None:
        provider, resolved_model = resolve_provider(model)
        model = resolved_model

    system, user = build_judge_prompt(artifact_text, rubric, artifact_label, custom_instructions)
    schema = build_judge_tool_schema(rubric)
    payload = await provider.generate_structured(
        system=system,
        user=user,
        schema=schema,
        schema_name="record_rubric_scores",
        model=model,
    )

    criterion_scores = _extract_scores(payload, rubric)
    return DraftScore(
        source=source,
        criterion_scores=criterion_scores,
        rubric_id=rubric.id,
        rubric_version=rubric.version,
    )
