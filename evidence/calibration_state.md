# Calibration state

Honest per-component status. The tool's credibility depends on knowing what's calibrated, what's inherited, and what isn't yet — in the [Husain](https://hamel.dev/blog/posts/evals-faq/) / [Shankar](https://www.sh-reya.com/) convention of disclosed limits as a credibility multiplier, not a weakness.

## Prose judge

**Inherited calibration.** The rubric design and scoring methodology originate in the Explodable content engine's analytical essay judge, which was calibrated against a 7-model editorial panel on 12 ranked drafts:

| Model | Spearman ρ | vs. |
|---|---|---|
| Claude Opus (target) | **0.841** | 5-model tight cluster |
| Claude Sonnet (ops judge) | **0.782** | 5-model tight cluster |
| 5-model internal agreement | ~0.83 | — (panel ceiling) |

The full panel was Gemini 2.5 Pro, Grok 4, DeepSeek V3, Mistral Large, GPT-5, Claude Deep Research, Qwen3. Two outliers (Claude Deep Research, Qwen) were dropped post-hoc to form the 5-model cluster. The judge sits at the panel's own internal-agreement ceiling; further tightening would require more independent ground truth, not better modeling.

**Full methodology + disclosed limits:** [github.com/tjkuhns/explodable/blob/main/docs/eval-methodology.md](https://github.com/tjkuhns/explodable/blob/main/docs/eval-methodology.md)

**Key disclosed limit:** the 2-model outlier drop was decided *after* seeing the agreement structure. A pre-registered protocol would have specified the drop criteria in advance. The ρ = 0.841 number is real but inflated by post-hoc selection.

**What's NOT transferred.** The portfolio-judge prose rubric is *generalized* from the Explodable rubric — three criteria were rewritten for portfolio context (methodology disclosure, register alignment, pedagogical instinct replaced Explodable's consulting-specific forwarding/CMO criteria). The generalized rubric has **NOT** been independently calibrated against a panel. It inherits methodology, not correlation numbers.

**What community feedback would close.** Running this judge on portfolios where you disagree with its verdict — and filing an issue explaining what was wrong — is the calibration mechanism this release is soliciting. Enough such reports would enable a post-hoc panel-agreement analysis on the generalized rubric.

## Code judge

**Inherited methodology, no independent calibration.** The rubric was transferred in an afternoon from the calibrated prose-judge harness to Python code quality, grounded in *Clean Code* (Martin), *A Philosophy of Software Design* (Ousterhout), PEP 8/257, Google Python Style Guide.

Applied to the Explodable codebase, the judge produced this differentiation (Gemini Flash as judge, a different model family from the generator to reduce same-model self-scoring bias):

| File | Score |
|---|---|
| `eval/judge.py` | 35.0 / 35 |
| `adversarial_critic.py` | 34.0 / 35 |
| `graph_expander.py` | 30.5 / 35 |
| `thesis_outline.py` | 30.5 / 35 |
| `revision_gate.py` | 26.5 / 35 |
| `topic_router.py` | 25.5 / 35 |

The ranking matched the builder's subjective assessment of which files received the most design care. **This is a sanity check, not a calibration.** Proper calibration would require human reviewer ground truth (N>>1) that the tool's builder does not have.

**What community feedback would close.** Running this judge on your own codebase and telling the builder where the verdicts diverge from your judgment is the calibration mechanism this release is soliciting.

**Upstream contribution.** The code judge rubric is also proposed as a feature addition to Braintrust's `autoevals` library as [Issue #185](https://github.com/braintrustdata/autoevals/issues/185), following the research's recommended OSS protocol (issue-first, not cold PR).

## Structural scanner

**Deterministic; no calibration needed.** The 12 checks are boolean observations — file exists, directory contains N items, commit date is within N days. No LLM, no ambiguity. The *severity weighting* (critical / moderate / cosmetic) is a design choice grounded in reviewer-research signal weighting (README absence is critical; ADR absence is cosmetic).

## Persona orchestration + synthesis

**N=1 dogfood, not calibrated against hiring outcomes.** The four reviewer personas were run fresh-context against the Explodable repo on 2026-04-19. All three distinct persona runs (recruiter, Applied AI HM, FDE / Solutions HM) advanced the portfolio with specific evidence citations. The three verdicts converged on percentile estimates of top 5–15% for Applied AI / DevRel roles at evals-adjacent AI-native mid-tier companies.

**Three structural limits on this signal:**

1. **Portfolio-of-origin bias.** The personas were designed *after* seeing the Explodable portfolio. Their prompts naturally tune toward signals that portfolio exhibits.
2. **No hiring-outcome calibration.** "Advanced to phone screen" is the persona's predicted hiring manager behavior, not an actual hiring outcome. The prediction is grounded in published hiring heuristics, not in outcome data.
3. **N=1.** One portfolio doesn't validate a methodology.

**What community feedback would close.** Running this orchestrator on portfolios whose authors have actual hiring outcome data (got interviewed / got rejected / got hired for role X at company Y) and comparing the orchestrator's verdict to the outcome. At N >> 10 with outcome data, this becomes a calibration signal rather than a dogfood. Contributions welcomed.

## Summary

| Component | Calibration state |
|---|---|
| Prose judge (methodology) | Inherited ρ = 0.841 / ρ = 0.782 from Explodable (post-hoc outlier drop disclosed) |
| Prose judge (generalized rubric) | **Not independently calibrated** — community feedback solicited |
| Code judge | **Not calibrated** — sanity-check on Explodable only, community feedback solicited |
| Structural scanner | Deterministic; no calibration needed |
| Persona orchestration | **N=1 dogfood**, no hiring-outcome calibration — community feedback solicited |
| Synthesis | Inherits limitations of the four personas |

**Disclosed limits are credibility multipliers, not weaknesses.** Anything this tool claims is either linked to a calibration artifact or flagged above as a known gap. If a verdict it produces on your portfolio feels wrong, that disagreement is exactly the signal this release is designed to capture — please file an issue.
