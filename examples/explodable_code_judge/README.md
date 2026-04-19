# Code judge — Explodable's `judge.py`

```bash
portfolio-judge code /home/thoma/explodable/src/content_pipeline/eval/judge.py --model sonnet
```

Rubric: `code_default` v0.1.0 — the 6-criterion Python code quality rubric shipped with the tool.

**Date:** 2026-04-19

**Headline:** 30/30 unweighted. All criteria scored 5/5 — naming, readability/structure, architectural fit, documentation, error handling, testability.

**Honest caveat:** this is the judge scoring the *source module it was ported from*. Self-review effects likely apply. The point of committing this example is to demonstrate what the code-judge output *looks like*, not to claim the rubric is validated. Calibration status disclosed in [`../../evidence/calibration_state.md`](../../evidence/calibration_state.md).

See [`review.md`](review.md) for per-criterion reasoning with line-specific references.
