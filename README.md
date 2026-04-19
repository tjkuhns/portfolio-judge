# portfolio-judge

> Role-calibrated LLM-as-judge for AI engineering portfolios. Prose judge, code judge, structural scanner, and four-persona synthesis — bundled under one methodology.

[![tests](https://github.com/tjkuhns/portfolio-judge/actions/workflows/test.yml/badge.svg)](https://github.com/tjkuhns/portfolio-judge/actions/workflows/test.yml)
[![PyPI](https://img.shields.io/pypi/v/portfolio-judge.svg)](https://pypi.org/project/portfolio-judge/)
[![Python](https://img.shields.io/pypi/pyversions/portfolio-judge.svg)](https://pypi.org/project/portfolio-judge/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**Status: alpha. N=1 dogfooded. Community feedback on verdicts you disagree with is the calibration mechanism this release is soliciting.** See [`evidence/calibration_state.md`](evidence/calibration_state.md) for honest per-component state.

## Why this exists

I've been building evaluated AI systems while hunting for an Applied AI Engineering role. To validate my own portfolio I built this — using the same LLM-as-judge methodology I'd already [calibrated](https://github.com/tjkuhns/explodable/blob/main/docs/eval-methodology.md) for analytical writing (ρ = 0.841 against a 7-model editorial panel at the panel's own ceiling, with the post-hoc outlier-drop limit disclosed).

The honest gap in this methodology is the lack of human-review calibration. Open-sourcing because running this on your portfolio and telling me where the verdicts are wrong is the fastest way to close that gap.

## Who this is for

This tool was built for people who have an *explicit portfolio repo* — one repo consolidating "here is my AI engineering work" — typically built because they're actively job-hunting into an AI engineering / Applied AI / FDE / Solutions / DevRel role. Specifically:

- **Career switchers** moving into AI engineering from adjacent fields (software, data, product, ops)
- **Bootcamp graduates** (Maven AI Evals cohort, Fast.ai, Zero to Mastery AI track, Springboard ML)
- **University AI/DS capstone students** preparing for the job market
- **Self-taught practitioners** who've built intentional portfolio repos and want structured pre-submission feedback

This tool is **NOT** for:

- **Evaluating accumulated public bodies of work** (blog + multiple project repos + GitHub profile + talks). Most established AI engineers don't have single portfolio repos — their portfolios are their accumulated work. [Phase 1 calibration](calibration/README.md) documents this explicitly: canonical exemplars (Willison, Yan, Huyen) got low percentile scores because their repos are tools/books/curations, not portfolio-shaped.
- **Framework / library / tool repos** being submitted for evaluation as "my portfolio" — the tool correctly flags this as a category error.
- **Predicting actual hiring outcomes** — there is no hiring-outcome calibration yet.
- **Replacing human review** — the code judge pattern-matches on surface features of good code and cannot distinguish code that *is* good from code that *looks* good. See [What this tool does NOT measure](evidence/methodology.md#what-this-tool-does-not-measure).

## What it does

Four runnable entry points:

```bash
portfolio-judge review --github <url> --role applied-ai   # full multi-persona review
portfolio-judge prose  <path>                             # prose quality (README, docs, blog)
portfolio-judge code   <path>                             # Python code quality
portfolio-judge structure <path>                          # deterministic portfolio checks
```

The `review` command orchestrates the three component judges, then runs four role-specific reviewer personas (recruiter, Applied AI hiring manager, FDE / Solutions hiring manager, DevRel hiring manager) over their outputs, then synthesizes a final verdict with convergent strengths, convergent gaps, role-fit ranking, percentile estimate, and top-3 actionable next steps.

## Quickstart

```bash
pip install portfolio-judge

# Set at least one provider key (the CLI auto-picks whichever is present)
export ANTHROPIC_API_KEY=sk-ant-...
# or export OPENAI_API_KEY=sk-...
# or export GOOGLE_API_KEY=...

# Optional: raises GitHub rate limit from 60 → 5000 req/hr
export GITHUB_TOKEN=ghp_...

portfolio-judge review --github https://github.com/yourname/yourrepo --role applied-ai
```

Model shortcuts: `--model sonnet | opus | haiku | gpt-4.1 | gpt-5 | gemini | gemini-pro` or any raw provider model ID. Defaults to Sonnet when `ANTHROPIC_API_KEY` is set.

## Example output

[`examples/explodable_full_review/`](examples/explodable_full_review/) — verbatim output from a full four-persona review run against [Explodable](https://github.com/tjkuhns/explodable). Headline verdict: *ADVANCE TO PHONE SCREEN, 90–95th percentile for Applied AI Engineer roles*. See the [examples README](examples/README.md) for prose and code judge outputs too.

## How it works

- **Component judges** (`src/portfolio_judge/judges/`) — prose and code judges are rubric-driven LLM-as-judge scorers with G-Eval-style CoT prompts, deterministic temperature, and flat parallel-primitive structured output. Structural scanner is deterministic — 12 checks for tests, CI, license, ADRs, README shape, commit recency, etc.
- **Reviewer personas** (`src/portfolio_judge/personas/`) — four role-specific prompts (recruiter, Applied AI HM, FDE/Solutions HM, DevRel HM), each operating fresh-context from a shared grounding doc. Personas read component outputs, not raw portfolio content.
- **Grounding** (`src/portfolio_judge/grounding.md`) — 2025-26 hiring heuristics distilled from Hamel Husain, Shreya Shankar, Eugene Yan, Chip Huyen, Simon Willison, and Anthropic's candidate-AI guidance.
- **Model-agnostic** — Anthropic / OpenAI / Google Gemini supported via thin adapters (no `litellm`, no LangChain). `--model` picks the provider; provider defaults are Sonnet, GPT-4.1, Gemini 2.0 Flash.

Full methodology: [`evidence/methodology.md`](evidence/methodology.md). **Start with the ["What this tool does NOT measure"](evidence/methodology.md#what-this-tool-does-not-measure) section — the tool cannot distinguish code that is actually good from code that merely looks good, and that's important before citing any score.** Calibration state per component: [`evidence/calibration_state.md`](evidence/calibration_state.md). Calibration trials (Phase 1): [`calibration/README.md`](calibration/README.md). Research sources: [`evidence/research_sources.md`](evidence/research_sources.md). Design decisions traced to research: [`evidence/design_decisions.md`](evidence/design_decisions.md). Roadmap: [`ROADMAP.md`](ROADMAP.md).

## Customize

**Bring your own rubric** — pass `--rubric /path/to/your.yaml` to `prose` or `code`. See [`src/portfolio_judge/rubrics/`](src/portfolio_judge/rubrics/) for the shipped defaults as templates.

**Bring your own persona** — drop a new markdown file into `src/portfolio_judge/personas/` and list it in the orchestrator's persona registry. Each persona is self-contained.

**Run subset of personas** — `--personas recruiter,applied_ai_hm` skips the others.

## Contributing

**Most valuable contribution: disagreement on verdicts.** Run this on your own portfolio and tell me where the tool got it wrong. That feedback is the human-review layer the methodology lacks.

Open an issue with:

- The portfolio you reviewed (GitHub URL)
- What the tool said
- What you disagreed with, and why

Also welcome: new personas, rubric improvements, support for non-Python languages, additional LLM provider adapters, structural scanner checks.

## Known limits

- **Prose rubric is optimized for long-form analytical technical writing.** Pure-install READMEs will score low on criteria like `counterargument_handling` and `integrative_reasoning` — use the structural scanner alone, or swap rubrics.
- **Python-only code judge in v1.** The rubric is language-specific; adding TypeScript/Go/Rust is a port of `code_default.yaml`.
- **Context-length ceilings.** Top 5 docs + top 5 Python files by size, 40KB per file. Large codebases get a representative sample, not a complete read.
- **Self-review bias in the dogfood.** The Explodable full-review example scored 90–95th percentile. The tool's builder also built Explodable. That N=1 run is a dogfood, not a validation. See `evidence/calibration_state.md`.

## Cost

A full portfolio review on Sonnet runs ~12 LLM calls and costs roughly $0.05–$0.20. Opus is about 3–5× that. Haiku is cheaper and faster but the synthesis quality drops noticeably.

The structural scanner costs $0 and doesn't require an API key. Running it first is the fastest way to find the structural gaps hiring managers spot in the first 30 seconds.

## License

MIT. See [LICENSE](LICENSE).
