# Methodology

`portfolio-judge` is four evaluators bundled under one methodology: a rubric-driven LLM-as-judge for prose, the same pattern for code, a deterministic structural scanner for everything linters can't catch, and a multi-persona orchestrator that reads all three and produces a role-calibrated review.

This document explains *how* it works and *what* it inherits. For honest per-component calibration state, see [`calibration_state.md`](calibration_state.md). For the grounding research the personas are tuned against, see [`research_sources.md`](research_sources.md).

## Where the methodology comes from

The methodology originates in the calibrated LLM-as-judge harness built for [Explodable](https://github.com/tjkuhns/explodable) — an AI content engine whose production quality gate is an LLM judge calibrated against a 7-model editorial panel. That judge achieved Spearman ρ = 0.841 (Opus) / ρ = 0.782 (Sonnet) against a 5-model tight cluster derived from the 7-model panel (with a pre-registration flaw disclosed upfront in the [Explodable methodology writeup](https://github.com/tjkuhns/explodable/blob/main/docs/eval-methodology.md)).

Three design choices carried over from that calibration work:

1. **G-Eval–style prompts** (Liu et al., *G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment*, EMNLP 2023). Chain-of-thought reasoning is required *before* committing a score per criterion. Reviewers cite specific evidence from the artifact; "I rate this a 4 because it seems well-written" is not an acceptable output shape.

2. **Flat parallel-primitive tool schema.** Every criterion gets two top-level fields: `{id}__reasoning` (string) and `{id}__score` (integer 1–5). The alternative — a nested array of `{criterion_id, reasoning, score}` objects — failed in practice during Explodable's calibration: Anthropic Opus occasionally serialized nested arrays as JSON strings with unescaped inner quotes, breaking tool-use parsing. Flat primitive schemas don't trigger that mode.

3. **Deterministic temperature.** Every judge call uses `temperature=0`. The judge must be rank-stable across runs, which matters for calibration: if the same artifact yields different scores on repeat calls, ρ against any reference collapses.

## Three evaluator layers

### Layer 1: Component evaluators

**Prose judge** (`judges/prose.py`) grades long-form analytical technical writing against a 10-criterion rubric (`rubrics/prose_default.yaml`) — thesis clarity, problem framing, evidence specificity, pedagogical instinct, methodology disclosure, integrative reasoning, counterargument, structural coherence, register alignment (no marketing voice), conclusion advances. Weights on `thesis_clarity`, `methodology_disclosure`, and `register_alignment` (1.5×) reflect the three signals hiring managers in this genre call out most often.

**Code judge** (`judges/code.py`) grades Python source against a 6-criterion rubric (`rubrics/code_default.yaml`) — naming, readability, architectural fit, documentation, error handling, testability. Grounded in *Clean Code* (Martin), *A Philosophy of Software Design* (Ousterhout), PEP 8/257, Google Python Style Guide. Explicitly complements linters: the rubric covers only what automated tools can't assess.

**Structural scanner** (`judges/structure.py`) runs 12 deterministic checks — tests present, CI present, license present, README sections, ADR directory, recent commit activity, package manifest, examples directory, gitignore. No LLM, no calibration, no ambiguity. Each finding has a severity (critical / moderate / cosmetic) so persona agents weight them appropriately.

### Layer 2: Persona orchestration

Four reviewer personas, each defined as a standalone markdown prompt (`personas/*.md`), operating fresh-context from the same grounding document (`grounding.md`):

- `recruiter.md` — 60-second first-pass + 5-minute second-pass triage by a technical sourcer at an AI-native mid-tier company.
- `applied_ai_hm.md` — 15-minute deep review by an Applied AI / Agentic Engineering hiring manager.
- `fde_solutions_hm.md` — 15-minute review by an FDE or Solutions Engineer hiring manager emphasizing writing + customer-facing clarity.
- `devrel_hm.md` — 15-minute review by a DevRel hiring manager in the Husain/Shankar/Willison tradition (teaching quality, runnable artifacts, public posture).

Each persona reads the component-judge outputs (not the raw portfolio — that's a deliberate design choice: personas evaluate whether the portfolio's *measured signals* support their role's hiring bar, rather than re-deriving the signals themselves).

### Layer 3: Synthesis

A single LLM call reads all four persona outputs and produces a synthesis: convergent verdict, convergent strengths (with reviewer attribution), convergent gaps, role-fit ranking, percentile estimate, and top-3 actionable next steps.

## What we changed from Explodable

The essay-judge calibration was for a specific register (consulting-quality B2B buyer psychology essays). Three generalizations for portfolio-judge:

1. **Rubric generalization.** The Explodable rubric bakes in "fractional CMO forwarding to CEO" as a calibration criterion. Portfolio-judge's prose rubric replaces that with `methodology_disclosure` and `register_alignment` — criteria that apply to any analytical technical writing, not just consulting essays.

2. **Multi-provider support.** Explodable's judge only used Anthropic. Portfolio-judge ships thin adapters for Anthropic, OpenAI, and Google, selectable via `--model`. This is both user-accessible (not everyone has an Anthropic key) and a hedge against single-provider failure modes in community reviews.

3. **Structural + multi-persona composition.** Explodable's judge scored single artifacts. Portfolio-judge orchestrates multiple component judges over a repo's file set, then layers persona-based role-calibrated review on top. The composition is new; the underlying scorer is not.

## What we did NOT change

- G-Eval prompt structure (CoT-before-score).
- Flat tool schema for structured output.
- Temperature = 0 for scorers.
- Disclosed-limits-in-line register (the Husain/Shankar genre convention — see the calibration-state doc for the disclosures this release ships with).

## What this tool does NOT measure

This is the most important section in this document. Read it before citing any score the tool produces.

**The tool cannot distinguish code that is actually good from code that merely looks good.** The code judge reads the source; it does not execute it, does not import it, does not run its tests, does not check if the algorithm is correct, does not know if an abstraction is load-bearing or gratuitous, does not know whether the code interfaces correctly with the rest of the system. The judge pattern-matches on the surface features of good code — clear docstrings, type hints, consistent naming, modular structure, thoughtful-looking error handling, tests that exist. All of those signals can be present while the code solves the wrong problem, uses the wrong algorithm, or silently fails at runtime.

Shankar et al. (*[Who Validates the Validators?](https://arxiv.org/abs/2404.12272)*, NAACL 2025) names the general version of this failure mode "vanity dashboards" — LLM judges that track surface rubric signals while missing ground-truth quality. For subjective code quality specifically, there is less calibration data than for prose — making the code judge's scores weaker evidence than the prose judge's scores, not stronger.

**The circular-flattery risk for AI-generated code.** If you use an LLM to write code and a different LLM to judge it, the judge is evaluating whether the code has the surface features that the generator was trained to produce. The generator is reliably good at producing those features. The judge is reliably good at recognizing them. The resulting high score is not evidence that the code works — it is evidence that the two LLMs agree on what good code looks like, which they often do, because they were trained on overlapping data. The example scores in this repo (`judge.py` at 30/30, `rubric.py` at 29/30) should be read through this lens: they are consistent with either "the code is excellent" or "the code has the surface signals and the judge recognized them." Without execution or human review, this ambiguity is not resolvable.

**The structural scanner counts; it does not verify.** `tests_present` passes if the `tests/` directory contains at least one `test_*.py` file. It does not run the tests. It does not verify the tests cover anything meaningful. A repo with 100 trivially-passing assertions will pass `tests_present` identically to a repo with 100 well-targeted tests against the risky modules. The checks are useful as signal that shipping discipline exists; they are not evidence that the discipline is load-bearing.

**Verdicts track the rubric, not ground truth.** The persona reviewers are grounded in hiring-heuristic research (Husain, Shankar, Yan, Huyen). Their output predicts what a hiring manager *should* say given the rubric; it does not measure what a hiring manager *would actually* say, because there is no hiring-outcome calibration data. A portfolio can score well and still fail in interview; a portfolio can score weak and succeed through connections, demeanor, or factors the tool cannot see.

**Prior-knowledge bias in persona design.** The four reviewer personas were not designed from a blank slate — they were designed by a builder who had his own portfolio (Explodable) in view while writing the persona prompts. When the tool runs on Explodable, the personas naturally tune toward signals that portfolio exhibits, which is why [Phase 1 calibration](../calibration/README.md#the-self-referential-calibration-problem--disclosed-openly) returns a 90–95th percentile score for the builder's own repo. That score is *not* independent evidence the tool works. Phase 2 calibration across portfolio-shaped peers is the next step; third-party cohort data from bootcamps is the calibration this release is actively soliciting.

**What closes these gaps, for the reader who wants to use the tool honestly:**

- For code quality verification: run the code. Run the tests. Type-check with Pyright or mypy. Lint with Ruff. These catch execution-adjacent failures the LLM judge does not. (See [`ROADMAP.md`](../ROADMAP.md) — deterministic execution-adjacent checks are v0.2.0 scope.)
- For hiring-outcome calibration: take the verdict as one input, not as a certificate. Pair it with human review from someone whose judgment you trust.
- For the AI-generated-code case specifically: the tool's job is to check whether the code has the surface signals a skeptical reader expects. It is not a substitute for the reader themselves; it is a pre-filter that catches surface failures so the human reader can focus on the substantive dimensions the tool cannot see.

**Framing this release honestly: this is "here is what LLMs think is good code." The open-source release invites skeptics to say "no, it isn't."** That exchange is the substance of the methodology. Build-in-public is not a vibe — it is the mechanism by which the tool's blind spots get surfaced.

## Other failure modes (known)

**Domain mismatch for pure-README rubric application.** The prose rubric is tuned for long-form analytical writing. Short install-focused READMEs will score low on criteria like `counterargument_handling` and `integrative_reasoning` even when the README is well-written for its genre. This is known; the intent is for users to either swap in a README-specific rubric via `--rubric` or interpret those scores as N/A.

**Context-length ceilings.** Orchestrator samples the top 5 docs + top 5 Python files by size, capped at 40KB per file. Very large codebases get a representative sample, not a complete read.

**Single-judge-model verdict inflation.** Explodable's calibration against a 7-model panel showed that any single judge model's verdict carries systematic bias (stylistic preferences, different severity floors). Portfolio-judge's v1 ships with a single-model mode. A future enhancement is multi-model-panel scoring with agreement reporting; v1 does not do this.

**No hiring-outcome calibration.** The persona reviewers are grounded in hiring-heuristic research, not in actual hiring outcomes (did the portfolio land a role?). That calibration requires N >> 1 and a time series the tool's builder doesn't have. See `calibration_state.md`.
