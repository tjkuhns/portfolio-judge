# Full portfolio review — Explodable

```bash
portfolio-judge review --path /home/thoma/explodable --role applied-ai --model sonnet
```

This is the headline artifact — all four personas (recruiter, Applied AI hiring manager, FDE/Solutions hiring manager, DevRel hiring manager) reading the component-judge outputs and producing role-calibrated reviews, followed by a synthesis call.

**Date:** 2026-04-19
**Runtime:** 2m 32s
**LLM calls:** ~12 (structural is free; prose × 6 files; code × 5 files; 4 personas; 1 synthesis)

**Headline synthesis verdict:** ADVANCE TO PHONE SCREEN. 90–95th percentile for Applied AI Engineer roles. Unanimous praise for eval methodology rigor (ρ = 0.841 calibration) and production-grade architecture. Convergent gaps: testability issues, error-handling inconsistencies, no public OSS presence (the last is why DevRel is ranked a bad fit).

**Top 3 actionable next steps the synthesis surfaced:**
1. Fix testability gaps before phone screen (refactor pipeline nodes to separate pure computation from I/O)
2. Prepare eval methodology deep-dive (walk through oracle routing ablation, confidence intervals, how judge disagreement was handled)
3. Frame the AI pair programming disclosure strategically — lead with measurement, not the pair-programming framing

**Context:** this review is self-review (the builder also built Explodable). N=1 dogfood. The whole point of the open-source release is for the community to run this on *their* portfolios and tell the builder where the verdicts diverge — that feedback is the calibration mechanism this release is soliciting.

See [`review.md`](review.md) for the full 339-line output including all four per-reviewer verdicts and the component scores (6 prose scores, 5 code scores, 12 structural findings).
