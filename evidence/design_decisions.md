# Design decisions — traced to research

Every major design decision in `portfolio-judge` has a specific research source that informed it. This document maps decisions to sources so a reader can check the reasoning, critique it, or propose a change with equivalent evidence.

If you disagree with a decision below, the issue tracker is the right place — reference the decision number and the counter-evidence.

## D1: Bundle three evaluators in one repo under one methodology

**Decision.** Ship prose judge + code judge + structural scanner + multi-persona orchestrator as a single `portfolio-judge` package, not three separate libraries.

**Sources considered:**
- [`braintrustdata/autoevals`](https://github.com/braintrustdata/autoevals) — multiple LLM-judge scorers bundled under one package
- [`langchain-ai/openevals`](https://github.com/langchain-ai/openevals) — LLM-judge + deterministic code evaluators in one package
- [`explodinggradients/ragas`](https://github.com/vibrantlabsai/ragas) — multiple metrics under one name
- [`langchain-ai/agentevals`](https://github.com/langchain-ai/agentevals) — counter-example, split from openevals *because agent trajectories are a structurally different evaluation shape*

**Reasoning.** Every successful multi-evaluator eval tool in this space bundles. The single clean counter-example (agentevals from openevals) split only because evaluation *shape* differed (ordered tool-call sequences vs. single-shot scoring). Portfolio-judge's three evaluators share the same shape — rubric → LLM/deterministic scoring → structured output. Composition is the right default; split later only if a shape difference forces it.

## D2: Role-calibrated reviewer personas grounded in named practitioner heuristics

**Decision.** Orchestrate four persona agents (recruiter, Applied AI HM, FDE/Solutions HM, DevRel HM) reading component outputs, each operating fresh-context from a shared grounding document.

**Sources considered:**
- Hamel Husain — [*Your AI Product Needs Evals*](https://hamel.dev/blog/posts/evals/), [*LLM Evals FAQ*](https://hamel.dev/blog/posts/evals-faq/)
- Shreya Shankar — [*Who Validates the Validators?*](https://arxiv.org/abs/2404.12272) (NAACL 2025)
- Eugene Yan — [*How to Interview and Hire ML/AI Engineers*](https://eugeneyan.com/writing/how-to-interview/), [*Evaluating the Effectiveness of LLM-Evaluators*](https://eugeneyan.com/writing/eval-process/)
- Chip Huyen — [*AI Engineering*](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) (O'Reilly, 2025)
- Simon Willison — [his weblog](https://simonwillison.net/) (canonical "document in public" pattern)
- Anthropic — [*Candidate AI Guidance*](https://www.anthropic.com/candidate-ai-guidance)

**Reasoning.** Hiring signal patterns in AI-native companies 2024–26 converge on named published heuristics (error analysis, disclosed methodology limits, production shape, context engineering over model chasing). Encoding those heuristics as explicit role-specific prompts makes the tool's decision layer inspectable. A single-prompt generic "review this portfolio" call would bury the role-specific weighting that is the tool's actual value. See [`grounding.md`](../src/portfolio_judge/grounding.md) for the full rubric.

## D3: G-Eval-style prompts with forced CoT before each score

**Decision.** Every criterion gets 2–4 sentences of reasoning citing specific evidence *before* the score is committed. Temperature = 0 for scorers.

**Sources considered:**
- Liu et al. — [*G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment*](https://arxiv.org/pdf/2303.16634) (EMNLP 2023)
- Shankar et al. — *Who Validates the Validators* (already cited)

**Reasoning.** G-Eval on SummEval achieved ρ = 0.514 against human reference — the strongest published LLM-judge correlation for a comparable task. The CoT-before-score structure is the single highest-leverage design choice from that work, because it constrains the model to generate evidence-backed reasoning rather than surface-pattern vibes. Temperature = 0 ensures rank stability across reruns, which matters for any calibration claim.

## D4: Flat parallel-primitive tool schema for structured output

**Decision.** Each criterion gets two top-level primitive fields (`{id}__reasoning` string + `{id}__score` integer), not a nested array of `{criterion_id, reasoning, score}` objects.

**Source.** Failure mode observed during Explodable's calibration work: Anthropic Opus occasionally serialized nested-object arrays as JSON strings with unescaped inner quotes in the reasoning text, breaking tool-use parsing. Flat primitive schemas avoid that specific mode. Design choice annotated in [`src/content_pipeline/eval/judge.py:191-236`](https://github.com/tjkuhns/explodable/blob/main/src/content_pipeline/eval/judge.py#L191-L236) of the source-of-origin repo.

**Reasoning.** Portable across providers (Anthropic tool_use, OpenAI response_format, Google response_schema); avoids a known failure mode; validated over ~200 calls during Explodable calibration with zero parse failures.

## D5: Multi-provider support via thin hand-rolled adapters, not litellm/LangChain

**Decision.** Three provider classes (`AnthropicProvider`, `OpenAIProvider`, `GoogleProvider`) with a unified async interface, totaling ~300 lines of code.

**Sources considered:**
- `litellm` — popular single-interface-to-100-providers library, heavy dep surface
- LangChain LLM abstractions — very heavy, large API surface
- Rolling thin adapters — explicit, per-provider patches (e.g. OpenAI's `additionalProperties: false` strict-mode requirement)

**Reasoning.** OSS adoption rewards small dependency trees. Any practitioner running `pip install portfolio-judge` who doesn't already use `litellm` in their stack would be pulling in ~50MB of transitive deps for three API calls. Hand-rolled wins on install weight, surface area, and explicit failure-mode control. Cost: ~3 hours of engineering work to write + test. Defensible tradeoff.

## D6: Publish verbatim calibration outputs in a `calibration/` directory

**Decision.** Ship trial outputs as runnable-by-anyone artifacts under `calibration/NNNN_target/` with metadata.yaml per trial, modeled on [SWE-bench `experiments/`](https://github.com/SWE-bench/experiments).

**Sources considered:**
- Commercial eval libraries (autoevals, ragas, deepeval, openevals, promptfoo, TruLens, Inspect AI) — none commit verbatim scoring outputs; most only ship evaluators + datasets
- Academic benchmark repos (SWE-bench experiments, G-Eval `results/`) — do publish prediction + trajectory dumps as reproducibility artifacts

**Reasoning.** Portfolio-judge has no human-labeled ground truth and no hiring-outcome calibration data. Visible artifacts are the credibility substitute. A reader can check not just "what the tool claims" but "what the tool actually said against this named repo at this SHA on this date." Rare for an eval library, standard for eval benchmarks. The tool's positioning falls between those categories; committing the outputs matches the benchmark convention because the tool is ultimately a scored-verdict system, not a utility scorer.

## D7: Anonymize low-tier calibration targets

**Decision.** Phase 1 low-tier trials (low_08 / low_09 / low_10) are run on named public repos but displayed anonymously in committed outputs; the sampling query + date are recorded for reproducibility.

**Reasoning.** The analytical value comes from tier differentiation, not from naming specific hobbyist repos as "weak." Naming them publicly rates strangers' personal work without adding analytical value and could punch down. Anonymizing keeps the experiment reproducible (same query + date + selection rule = same sample) while avoiding the "punches down" failure mode.

## D8: Reject "litellm-style" product positioning; hold "portfolio review tool for career switchers" instead

**Decision.** The tool is explicitly scoped to *explicit portfolio repos* built by career switchers / bootcamp grads / capstone students, NOT generic "AI engineer portfolio review." See [`README.md`](../README.md#who-this-is-for).

**Source.** Phase 1 calibration finding: every "community-canonical exemplar" (Willison datasette, Willison llm, Yan applied-ml, Huyen aie-book) scored 0th to 15th percentile as Applied-AI-Engineer portfolios. Not because the tool is broken — because those repos are tools/books/curations, not portfolio-shaped. Established practitioners don't have portfolio repos; their portfolios are their accumulated work.

**Reasoning.** Scope discipline over scope creep. The tool works well on a specific niche. Pretending it works for "all AI engineer portfolios" would require broadening the scope to review GitHub profiles + blogs + LinkedIn + project repos, which is a v0.3.0+ engineering effort and dilutes the v0.1.0 value. See [`../ROADMAP.md`](../ROADMAP.md).

## D9: Outreach register for community feedback — short, one-ask, no "hop on a call"

**Decision.** Cold outreach to individual practitioners is ~100 words, one specific ask, explicit opt-out, no call-to-action for a meeting. Organizational outreach is slightly longer, numbered questions for internal forwarding legibility, with explicit "no pitch, no partnership" disclaimer.

**Sources considered:**
- Patrick McKenzie (patio11) — [*Standing Invitation*](https://www.kalzumeus.com/standing-invitation/), [*You Should Probably Send More Email*](https://www.kalzumeus.com/2012/05/31/can-i-get-your-email/)
- Eugene Yan — [*How I Can Help*](https://eugeneyan.com/how-i-can-help/)
- Simon Willison — [*South Park Commons interview*](https://blog.southparkcommons.com/p/simon-willison-my-career-in-side-projects-and-open-source)
- Cal Newport — [*Write Your Own E-mail Protocols*](https://calnewport.com/deep-habits-write-your-own-e-mail-protocols/)
- Julia Evans — [*Ask for specific feedback*](https://wizardzines.com/comics/ask-for-specific-feedback/)
- Swyx — [*Learn In Public*](https://www.swyx.io/learn-in-public)

**Reasoning.** One-paragraph emails with a single decision ask get responses; multi-ask corporate-speak emails get deleted. The "I honestly don't know if this is useful" move is calibrated humility specifically, not groveling — it makes the uncertainty *the reason for the ask*, not an apology for it.

## D10: Soft-launch in practitioner communities before bulk-pitching bootcamps

**Decision.** Sequence is r/LocalLLaMA / r/LLMDevs / r/AI_Agents / MLOps Community Slack / LinkedIn *first*, then individual practitioner outreach (Willison's Calendly office hours, Husain/Shankar/Yan/Huyen emails), then organizational outreach to bootcamps last.

**Sources considered:** earlier session research on channel selection (cited in internal session logs; not a published source). Grounded in the premise that initial GitHub stars + community signal create the warm-context that makes individual emails land better, which in turn creates the validation that makes organizational pitches credible.

**Reasoning.** Each tier requires the previous tier as warm-up. Launching to bootcamps without any community signal reads as product pitch; launching to community after individual signal reads as bulk promotion. Staggered reads as iterative dogfooding; simultaneous reads as a PR push.
