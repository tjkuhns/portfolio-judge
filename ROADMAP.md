# Roadmap

Public roadmap for `portfolio-judge`. What's in v0.1.0, what's planned, what's explicitly not planned.

Read [`evidence/methodology.md`](evidence/methodology.md#what-this-tool-does-not-measure) first — the tool's current limits determine which items below actually matter.

## v0.1.0 (current)

Shipped 2026-04-19.

- Prose judge — rubric-driven LLM-as-judge for analytical technical writing (methodology inherited from calibrated Explodable essay judge, ρ = 0.841 at panel ceiling)
- Code judge — 6-criterion Python code quality rubric (methodology inherited, NOT independently calibrated)
- Structural scanner — 12 deterministic checks, no LLM
- Four reviewer personas (recruiter, Applied AI HM, FDE/Solutions HM, DevRel HM)
- Orchestrator with GitHub tarball ingest + parallel component runs + cross-reviewer synthesis
- Model-agnostic (Anthropic / OpenAI / Google) via thin adapters
- PyPI trusted-publishing pipeline
- Verbatim dogfood examples in `examples/`

## v0.2.0 (near-term — planned)

Focus: close the biggest credibility gap named in `evidence/methodology.md` — the "surface-good vs actually-good" problem for code quality. The cheapest way to narrow that gap is to integrate execution-adjacent deterministic signals the LLM judge does not see.

- **Pyright integration** — run strict type-check over each code file sampled, include the result alongside the LLM rubric score. A file that scores 5/5 on "testability" in the rubric but fails Pyright strict is a signal the human reviewer should weight higher than the LLM verdict.
- **Ruff integration** — run lint over sampled code, report rule-class counts (not raw lines) as structured findings the personas can read.
- **Test execution (optional)** — if the repo has a `pyproject.toml` + `tests/`, optionally run pytest in an isolated venv and report pass/fail counts. Gated behind a `--run-tests` flag because of sandbox / dependency concerns.
- **Multi-language rubrics** — add `code_typescript_default.yaml`, `code_go_default.yaml` as community contributions land.
- **Initial calibration trials published** — `calibration/` directory in the repo with verbatim reviews against a tiered external sample, modeled on [SWE-bench `experiments/`](https://github.com/SWE-bench/experiments). In progress at v0.1.0.

## v0.3.0+ (medium-term — speculative)

- **Multi-model panel scoring** — current v1 uses a single judge model. The Explodable essay calibration used a 7-model panel to cross-check. Panel-mode orchestration would let users see agreement/disagreement across models as a confidence signal on each criterion.
- **Community calibration intake** — a structured way for users to file "disagreement" issues against specific verdicts, aggregated across users to surface systematically miscalibrated criteria or personas.
- **Rubric versioning + migration** — when rubrics change, existing calibration artifacts should remain interpretable. Version pinning + migration notes.
- **LinkedIn / resume text path** — for candidates whose portfolio isn't primarily code-based. Review prose-only inputs with a role-specific rubric. Requires careful scoping to avoid feature creep.

## Explicitly NOT planned

- **SaaS / hosted version.** The tool is an OSS CLI + library. Not a platform. Not a product. The methodology is the artifact, not the service.
- **Leaderboards.** Ranking portfolios against each other is a different use case (and a nastier one). Out of scope.
- **ATS integration.** Out of scope — different product, different buyer.
- **Private-repo review (credentialed scan).** Security and ops surface we don't need. Public-repo review via tarball is sufficient for the launch use case.
- **Non-English prose rubric.** Non-goal until there's demand; the grounding research is English-language-specific.

## Versioning policy

Semantic versioning. Breaking CLI changes bump minor (v0.x.0 → v0.x+1.0) until v1.0.0. Rubric content changes bump patch (v0.x.y → v0.x.y+1). Once v1.0.0 ships, breaking changes bump major.

## How to influence the roadmap

**Most valuable contribution: disagreement on verdicts.** File an issue with the portfolio you reviewed, the tool's output, and what you disagreed with. See [`CONTRIBUTING.md`](CONTRIBUTING.md). Multiple disagreements on the same axis = a calibration signal that prioritizes roadmap items.

For feature requests specifically, open an issue tagged `enhancement` with the use case first, the proposed feature second. Use-case framing helps distinguish "I need this because X" from "it would be nice if."
