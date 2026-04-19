# Contributing

**The most valuable contribution to `portfolio-judge` is disagreement on verdicts.**

The methodology is N=1 dogfooded and has no hiring-outcome calibration (see [`evidence/calibration_state.md`](evidence/calibration_state.md)). Community runs on independent portfolios — and *disagreement with the tool's output* — are how the methodology gets calibrated.

## If you ran this on your own portfolio and disagreed

Open an issue titled `Disagreement: <role>` with:

- The portfolio URL (or a portion pasted inline if private)
- Which entry point you ran (`review` / `prose` / `code`)
- What the tool said (score, verdict, or quoted reasoning)
- What you disagree with, specifically
- Your reasoning — ideally: *this criterion is miscalibrated because X* or *this persona is overweighting Y*

Multiple disagreements on the same axis = a calibration signal. That's the data this release is designed to capture.

## Other contributions welcome

### New reviewer personas

Drop a markdown file into `src/portfolio_judge/personas/` following the format of the existing four (see [`src/portfolio_judge/personas/recruiter.md`](src/portfolio_judge/personas/recruiter.md) as a template). Add the persona name to `ALL_PERSONAS` in [`orchestrator.py`](src/portfolio_judge/orchestrator.py).

Personas should:

- Operate fresh-context from the shared `grounding.md`
- Target a specific, named role type
- Output a structured format the synthesizer can parse
- Cite grounding heuristics when their verdicts turn on them

### Rubric improvements

Open a PR updating one of the rubric YAMLs, or propose a new default rubric. For rubric changes, include reasoning for the delta from the current version — the rubrics ship with disclosed methodology inheritance and any change updates that story.

### Language support

The code judge defaults to Python. To add TypeScript / Go / Rust / etc.:

1. Add a new rubric YAML in `src/portfolio_judge/rubrics/`
2. Extend the code-judge file-extension filter in `orchestrator.py`
3. Update README's "Known limits"
4. Add a worked example in `examples/`

### Provider adapters

Anthropic / OpenAI / Google are in. For additional providers (Mistral, Cohere, local via Ollama, etc.), add a thin adapter in `src/portfolio_judge/core/llm.py` following the existing pattern. No `litellm` or LangChain — the point is zero heavy-dep surface.

### Structural scanner checks

New checks should be:

- Fully deterministic (no LLM)
- Boolean or cheap-count (not subjective)
- Severity-tagged (critical / moderate / cosmetic)

Examples worth adding: Dockerfile presence, pre-commit config, security policy, changelog format.

## Development

```bash
git clone https://github.com/tjkuhns/portfolio-judge.git
cd portfolio-judge
pip install -e ".[dev]"
pytest -q
ruff check src/ tests/
```

CI runs on Python 3.10 / 3.11 / 3.12 via GitHub Actions.

No live LLM calls in CI — scorer tests use a mocked `Provider`. If you want to smoke-test end-to-end, set an API key locally and run:

```bash
portfolio-judge review --path . --role applied-ai --model sonnet
```

## Release

Releases are gated on a git tag + GitHub Release. The `publish.yml` workflow verifies the tag version matches `pyproject.toml`, then publishes to PyPI via trusted publishing.

## License

All contributions are under MIT (matching the project license).
