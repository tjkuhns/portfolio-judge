# portfolio-judge

> Role-calibrated LLM-as-judge for AI engineering portfolios. Prose judge, code judge, structural scanner, and multi-persona synthesis — bundled under one methodology.

**Status:** alpha. Methodology dogfooded at N=1; community feedback on verdicts is the calibration mechanism this release is soliciting. See [`evidence/calibration_state.md`](evidence/calibration_state.md) for honest per-component status.

## Why this exists

I've been building evaluated AI systems while hunting for an Applied AI Engineering role. To validate my own portfolio I built this, using the same LLM-as-judge methodology I'd calibrated for analytical writing (ρ = 0.841 against a 7-model editorial panel at the panel's own ceiling — disclosed limits and all).

Open-sourcing because the honest gap in this methodology is the lack of human-review calibration — and running it on your own portfolio and telling me where the verdicts are wrong is the fastest way to close that gap.

## What it does

Four runnable entry points:

```bash
portfolio-judge review --github <url> --role applied-ai    # full multi-persona review
portfolio-judge prose <path-or-url>                        # prose quality (README, docs, blog)
portfolio-judge code <path>                                # Python code quality
portfolio-judge structure <path-or-url>                    # deterministic portfolio checks
```

The full `review` command orchestrates all three component judges, then runs four role-specific reviewer personas (recruiter, Applied AI hiring manager, FDE / Solutions hiring manager, DevRel hiring manager) over the component outputs, then synthesizes.

## Quickstart

```bash
pip install portfolio-judge

# Set at least one provider key
export ANTHROPIC_API_KEY=sk-...    # or OPENAI_API_KEY / GOOGLE_API_KEY

# Optional: GitHub token lifts rate limit from 60 → 5000 req/hr
export GITHUB_TOKEN=ghp_...

portfolio-judge review --github https://github.com/yourname/yourrepo --role applied-ai
```

## Example output

See [`examples/`](examples/) for verbatim dogfood runs against [Explodable](https://github.com/tjkuhns/explodable), including the full four-persona portfolio review.

## Methodology

- [`evidence/methodology.md`](evidence/methodology.md) — how it works and what it inherits
- [`evidence/calibration_state.md`](evidence/calibration_state.md) — honest state per component
- [`evidence/research_sources.md`](evidence/research_sources.md) — grounding research (Hamel Husain, Shreya Shankar, Eugene Yan, Chip Huyen)

## Contributing

Especially welcome: running this on your own portfolio and telling me where the verdicts are wrong. That's the human-review layer the methodology is missing. Open an issue with:

- The portfolio you reviewed
- What the tool said
- What you disagree with, and why

Also welcome: new reviewer personas, rubric improvements, support for non-Python languages, provider adapters.

## License

MIT. See [LICENSE](LICENSE).
