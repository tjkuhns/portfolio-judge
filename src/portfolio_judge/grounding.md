# Grounding: 2025–26 AI Engineering Hiring Heuristics

All reviewer personas in this package are informed by this grounding document. It captures what hiring managers and recruiters at AI-native mid-tier companies actually evaluate when screening candidates for Applied AI Engineer / Forward Deployed Engineer / AI Solutions Engineer / DevRel roles in 2025–26.

Use this context when generating any review. Cite specific heuristics when your verdict turns on them.

## Signal patterns that advance candidates

**Systematic error analysis on real traces.** Hamel Husain, *Your AI Product Needs Evals* and *LLM Evals FAQ*. A portfolio that shows labeled failure traces, discovered failure modes, and evals built *after* looking at data is doing the 60–80% of the work that real applied AI looks like. Without this, the candidate is demo-driving.

**Calibrated LLM-as-judge with disclosed limits.** Shreya Shankar et al., *Who Validates the Validators?* (NAACL 2025 oral); Eugene Yan, *Evaluating the Effectiveness of LLM-Evaluators*. A judge with a correlation number to a reference (human or panel) and a disclosed ceiling is past "vanity dashboards."

**End-to-end production shape, not notebook.** Chip Huyen, *AI Engineering* (O'Reilly 2025). FastAPI/Celery/queue, config-as-code, CI, deploy surface, tests against the risky modules. Notebook-only work doesn't clear the "shipping reliable, maintainable AI products" threshold.

**Context engineering over model chasing.** RAG design decisions documented with tradeoffs (latency/cost/relevance); agentic-vs-workflow choice justified by measured result. The candidate optimizes the layer they control.

**Writing that documents the learning curve in public.** Simon Willison's canonical pattern: TIL-style posts, negative results, annotated experiments, runnable demos. Directly hireable into DevRel and Solutions roles.

**Direct evidence of ability over credentials.** Anthropic careers policy (widely quoted 2025): "roughly half technical staff from non-ML backgrounds." GitHub project, blog, OSS contributions weighted over degree. The repo itself is the interview.

## Red flags that kill candidates

**"API call in a trench coat."** Thin wrapper over Chat Completions, no retrieval layer, no eval, no domain. Candidate has not done the hard part.

**Vibes-driven evaluation.** "We tested it and it worked well" / screenshots instead of numbers; no error analysis; no calibration. Hamel Husain: "you can't vibe-check your way to understanding what's going on."

**Passing 100% of evals.** "If you're passing 100% of your evals, you're likely not challenging your system enough" (Hamel Husain, *Evals FAQ*). Evals were built to pass, not to find bugs.

**Framework religiosity.** LangChain/LangGraph used everywhere with no justification; "agent" where a plain function call would do. Candidate picks tools by brand, not fit.

**Overclaiming architecture/model novelty.** "Novel," "first-of-its-kind," "invented" on what is actually integration work. Trust problem — the biggest one in FDE/Applied contexts. Anthropic's candidate-AI guidance: misrepresentation disqualifies, not AI use itself.

**Unfinished / undocumented / stale repos.** README stops at "installation," no deploy, commits trail off. Proxy for production readiness.

**Buzzword density without ablations.** RAG, agents, MCP, fine-tuning all mentioned; no ablation showing which moved the metric. Surface fluency, no mechanism thinking.

## 30-second recruiter checklist

- Pinned repo with a clear one-line value prop in the README header.
- Runnable demo link (Streamlit / HF Space / deployed URL).
- A number in the first screen — eval score, correlation, latency, hit rate — not adjectives.
- Commit history within last ~60 days; not a graveyard.
- LinkedIn headline matches repo claims (no "AI architect" over a wrapper demo).
- At least one piece of long-form writing linked.
- Tests visible in repo root; CI badge green.
- No "coming soon" sections as placeholder for core claims.

## Hiring manager deep-dive checklist

- Error analysis artifact exists: labeled traces, taxonomy of failures.
- Eval methodology disclosed with limits, not just scores.
- ADRs or equivalent — *why* this retrieval strategy, *why* this agent boundary.
- Ablations: at least one comparison run where a component was removed and the delta measured.
- Tests target the risky layer (judge, retrieval, gating), not just utility glue.
- Separation of concerns: config from code, prompts from code, data from code.
- Handles failure cases: timeouts, malformed outputs, judge disagreement.
- Honest writing: negative results, things that didn't work, "what I'd do differently."
- Clean boundary between third-party framework and candidate's own code.
- Commit hygiene: small, labeled commits showing the debugging trail.

## Role-specific lenses

**Applied AI Engineer.** Eval harness sophistication is the differentiator. Judge correlation to a reference, ablations, documented failure modes. Taste for picking the metric that matches the product, not the one that's easy.

**Forward Deployed Engineer.** Customer-empathy signals in writing: problem framing before tech, tradeoffs named, scaffolding a non-expert could pick up. Debugging narratives beat feature narratives.

**AI Solutions Engineer.** Narrative clarity on tradeoffs for non-technical stakeholders. Can the candidate write one paragraph that makes a VP understand *why* the chunking choice matters?

**DevRel.** Public writing cadence + runnable examples. Niche depth beats breadth. Simon Willison's blog + Datasette is the canonical shape.

## Genre exemplars

- [Hamel Husain — Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/)
- [Hamel Husain — LLM Evals FAQ](https://hamel.dev/blog/posts/evals-faq/)
- [Eugene Yan — How to Interview and Hire ML/AI Engineers](https://eugeneyan.com/writing/how-to-interview/)
- [Eugene Yan — An LLM-as-Judge Won't Save The Product](https://eugeneyan.com/writing/eval-process/)
- [Shreya Shankar — Who Validates the Validators? (NAACL 2025)](https://www.sh-reya.com/)
- [Simon Willison's Weblog](https://simonwillison.net/)
- [Chip Huyen — AI Engineering (O'Reilly 2025)](https://github.com/chiphuyen/aie-book)
