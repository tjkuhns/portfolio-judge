# Examples

Verbatim outputs from dogfooding `portfolio-judge` against [Explodable](https://github.com/tjkuhns/explodable) — an AI content engine built by the same author. Committed here so skeptics can read what the tool actually produces before installing it.

**All runs used Claude Sonnet 4 (`claude-sonnet-4-20250514`) at `temperature=0` for the component judges and `temperature=0.3` for persona reviews + synthesis.**

| Example | What it demonstrates | Cost |
|---|---|---|
| [`explodable_structure/`](explodable_structure/) | Deterministic structural scan (no LLM) | $0.00 |
| [`explodable_prose_readme/`](explodable_prose_readme/) | Prose judge on a real README | ~$0.01 |
| [`explodable_code_judge/`](explodable_code_judge/) | Code judge on a single Python file | ~$0.02 |
| [`explodable_full_review/`](explodable_full_review/) | Full four-persona review with synthesis | ~$0.15 |

**On why Explodable is the target:** portfolio-judge's builder also built Explodable, so this is self-review. The N=1 dogfood is explicit in [`../evidence/calibration_state.md`](../evidence/calibration_state.md) — community runs on independent portfolios are the calibration mechanism this release is soliciting.
