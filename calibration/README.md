# Calibration trials — Phase 1

Verbatim outputs from running `portfolio-judge review` against 10 externally-sourced repositories across three quality tiers. Modeled on [SWE-bench `experiments/`](https://github.com/SWE-bench/experiments) — the only pattern I could find for publishing eval outputs in-repo. Do not treat this as human-validated calibration; treat it as a published first pass whose weird results the community is invited to critique.

**Phase 1 status:** N=10 target repos, 1 run each, Claude Sonnet 4 judge (`claude-sonnet-4-20250514`), temperature=0 for component scoring and 0.3 for persona + synthesis. All runs from 2026-04-19. Total cost ≈ $1.80.

## The methodology question this set out to answer

Can `portfolio-judge` distinguish code that is actually good from code that merely *looks* good? That is an unanswered question at the level of ground truth — see [`../evidence/methodology.md#what-this-tool-does-not-measure`](../evidence/methodology.md#what-this-tool-does-not-measure). What this trial *can* answer, more narrowly: do the tool's verdicts vary meaningfully across an externally-sourced sample, or does it rubber-stamp everything it reviews?

## Sampling

External criteria only — no author intuition. See [`../evidence/research_sources.md`](../evidence/research_sources.md) for the full framework.

- **Top tier (4)**: community-canonical AI-engineering exemplars — repos practitioners cite as "what good looks like."
- **Middle tier (3)**: mature, popular, AI-adjacent OSS projects with mixed signals — known-critiqued architectures, smaller teams, or author-exemplar repos outside their canonical flagship.
- **Low tier (3)**: first three repos (no cherry-picking) matching GitHub search `"ai portfolio" language:Python stars:<20`, filtered for "self-labeled AI portfolio project." Low-tier repos are anonymized in the committed outputs to avoid publicly rating individual hobbyist work; the search query + date are recorded so the sample is reproducible.

## Summary — all 10 verdicts

| Tier | Repo | Convergent verdict | Percentile estimate |
|---|---|---|---|
| Top | [simonw/datasette](top_01_datasette/) | REJECT — domain mismatch (data tooling, no AI/ML) | 0th for AI; 85th+ for data infra |
| Top | [simonw/llm](top_02_llm/) | REJECT — strong software, wrong role fit | 15th for AI; "top 5%" for tooling |
| Top | [eugeneyan/applied-ml](top_03_applied_ml/) | REJECT — curated resource list, not engineering portfolio | Bottom 5th |
| Top | [chiphuyen/aie-book](top_04_aie_book/) | REJECT — book promotion, zero runnable code | Bottom 5th |
| Mid | [langchain-ai/langchain](mid_05_langchain/) | REJECT — category error, framework ≠ portfolio | 0th |
| Mid | [explodinggradients/ragas](mid_06_ragas/) | REJECT — established OSS as individual portfolio | 0th |
| Mid | [hamelsmu/evals-skills](mid_07_evals_skills/) | Partial — strong methodology, execution gaps | 15-30th |
| Low | [low_08](low_08/) | REJECT — "API call in a trench coat" anti-pattern | Bottom 15-25th |
| Low | [low_09](low_09/) | REJECT — beginner Python learning, no AI content | Bottom 5th |
| Low | [low_10](low_10/) | REJECT — 9-word README, no production hygiene | Bottom 15th |

For comparison, the [Explodable dogfood review](../examples/explodable_full_review/) — the builder's own AI portfolio repo — scored **90–95th percentile for Applied AI Engineer**.

## The self-referential calibration problem — disclosed openly

**My portfolio (Explodable) scored 90–95th percentile. The tool was built by someone (me) who was reviewing that same portfolio while designing the personas. That is a real problem and it needs to be named directly, not hidden in a caveats footer.**

The four reviewer personas in this tool were not designed from a blank slate. They were designed partly by observing what a good Applied AI portfolio *appears* to need, and the portfolio I had closest at hand was mine. When I then ran the tool on Explodable and it scored 90–95th percentile, that is not independent evidence the tool works. It is partial evidence that the personas learned what Explodable looks like and then rewarded a portfolio shaped exactly that way.

The Phase 1 calibration in this directory shows the tool discriminates at extremes — it rejects frameworks, paper curations, and low-effort hobbyist attempts. What it does *not* establish is whether the tool differentiates meaningfully *within* the portfolio-shaped category, because Explodable is currently the only portfolio-shaped target in the sample. Every other repo in Phase 1 was wrong-shape in some way (tool, library, book promo, curated list, beginner scratchpad).

**What would close this gap:**

- **Phase 2 calibration** — 10 repos sampled from `topic:ai-portfolio` or similar, all portfolio-shaped, across an effort spectrum. If Explodable still scores meaningfully higher than portfolio-shaped peers, that's either real differentiation or a deeper design-time bias Phase 2 doesn't reach. Planned.
- **Third-party cohort calibration** — a bootcamp running this on a cohort of portfolios against their own instructor reviews + placement outcomes. This is the only source of actually-external calibration the tool can acquire, and why the soft-launch is in part a request for collaborators.

**What not to read into the 90–95 number:** not that the builder's portfolio is in the top 5–10% of AI engineering portfolios globally. Read it as: the tool's personas, when applied to the portfolio whose shape partly informed them, return a high score. That's a weaker statement than "Explodable is a top portfolio," and it is the only statement Phase 1 data supports.

---

## The surprising finding

**The tool rejects every "top tier" exemplar as a portfolio for Applied AI Engineer roles.** This is not a calibration failure. It is evidence the tool discriminates more narrowly than expected:

- `simonw/datasette` is excellent software. It is not a personal portfolio demonstrating Applied AI engineering, because it has no AI/ML components.
- `simonw/llm` is excellent AI tooling. It is not a personal-narrative portfolio, because it's a CLI framework.
- `eugeneyan/applied-ml` is a curated paper list that thousands of engineers cite. It is not an engineering artifact — it is a reading list.
- `chiphuyen/aie-book` is a book companion repo. It's not runnable code.
- `langchain-ai/langchain` is the LangChain framework. A candidate submitting it as "their portfolio" would be making a category error; the tool calls that out.

The tool is calibrated toward "individual AI engineering portfolio for employment" specifically, not "good AI engineering work in general." That is a meaningful thing to know, and it is directly consistent with how the persona prompts are written: each persona is evaluating a candidate's individual application portfolio, not a generic repo.

**What this also means:** Explodable's 90–95th percentile score is less surprising than it first looked. Explodable is a personal-portfolio-framed project by construction. The top-tier exemplars in this sample are not. The comparison therefore isn't apples-to-apples — and the tool correctly identified the mismatch.

## What this trial does NOT establish

- **That the tool correctly identifies actually-good code** — see [`../evidence/methodology.md#what-this-tool-does-not-measure`](../evidence/methodology.md#what-this-tool-does-not-measure). Every score here is surface-pattern-matching.
- **That the percentile estimates are calibrated** — they are what the personas predict a hiring manager would say, not what a hiring manager *actually* would say. No hiring-outcome validation.
- **That N=1-per-repo is stable** — a single Sonnet run with temperature > 0 on the personas could produce different verdicts on a different run. Multi-run stability is not tested.
- **That the verdicts generalize to non-GitHub portfolios** (LinkedIn-text, resume-based, closed-source work).

## What the community can do with this

1. **Run the tool on your own portfolio and file a disagreement issue** if the verdict is wrong. Multiple disagreements on the same axis = a calibration signal. See [`../CONTRIBUTING.md`](../CONTRIBUTING.md).
2. **Run the tool on a known-outcome portfolio** (e.g., one that got hired at a named company for a named role, or one that got rejected after a take-home). File the outcome + the verdict — that is the closest thing to hiring-outcome calibration this release can collect from community input.
3. **Propose rubric changes** if a specific criterion seems miscalibrated across multiple repos. The more portfolios a pattern shows up across, the stronger the case for changing the rubric.

## Per-trial directories

Each subdirectory contains:

- `review.md` — verbatim output from `portfolio-judge review` (the full synthesis + all four persona verdicts + component scores)
- `metadata.yaml` — repo URL (or anonymized note for low tier), commit SHA at time of review, trial date, rubric version, model, approximate cost, runtime

## Reproducing the sample

```bash
# Top + mid tier: named directly
portfolio-judge review --github https://github.com/simonw/datasette --role applied-ai --model sonnet
# ... etc for each URL in the table above

# Low tier sample query (recorded for reproducibility; individual repos anonymized):
gh search repos "ai portfolio" --language python --stars "<20" --limit 30
# Take the first 3 that match: self-labeled AI portfolio, no CI, no tests, README-only
# Queried: 2026-04-19
```
