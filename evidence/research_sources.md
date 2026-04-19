# Research sources

The grounding document (`src/portfolio_judge/grounding.md`) and the four persona prompts draw from a specific set of 2024–26 practitioner writings on how AI-native companies actually hire for Applied AI / FDE / Solutions / DevRel roles. Each source below is linked to the heuristics it informed.

## Eval methodology + disclosed-limits register

- **Hamel Husain — *Your AI Product Needs Evals***. [hamel.dev/blog/posts/evals/](https://hamel.dev/blog/posts/evals/)
  *Cited for:* "error analysis on real traces" signal; "you can't vibe-check your way to understanding what's going on" red flag; LLM-as-judge methodology transfer.

- **Hamel Husain — *LLM Evals FAQ***. [hamel.dev/blog/posts/evals-faq/](https://hamel.dev/blog/posts/evals-faq/)
  *Cited for:* "If you're passing 100% of your evals, you're likely not challenging your system enough" red flag; disclosed-limits-as-credibility-multiplier framing.

- **Shreya Shankar et al. — *Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences*** (NAACL 2025 oral). [sh-reya.com](https://www.sh-reya.com/)
  *Cited for:* "calibrated LLM-as-judge with disclosed limits" signal; recommendation to report both Spearman ρ and Kendall τ.

- **Eugene Yan — *Evaluating the Effectiveness of LLM-Evaluators***. [eugeneyan.com/writing/eval-process/](https://eugeneyan.com/writing/eval-process/)
  *Cited for:* judge correlation to a reference; ceiling analysis.

- **Eugene Yan — *Patterns for Building LLM-based Systems & Products***. [eugeneyan.com/writing/llm-patterns/](https://eugeneyan.com/writing/llm-patterns/)
  *Cited for:* production-system signals on hiring manager deep-dive checklist.

- **Eugene Yan — *How to Interview and Hire ML/AI Engineers***. [eugeneyan.com/writing/how-to-interview/](https://eugeneyan.com/writing/how-to-interview/)
  *Cited for:* "overstating role without acknowledging team contributions" red flag.

## Production shape + engineering discipline

- **Chip Huyen — *AI Engineering: Building Applications with Foundation Models* (O'Reilly, 2025)**. [github.com/chiphuyen/aie-book](https://github.com/chiphuyen/aie-book)
  *Cited for:* "end-to-end production shape, not notebook" signal; context-engineering framing; "graduated from writing experiments or demos to shipping reliable, maintainable AI products" threshold.

- **Anthropic — *Building Effective Agents***. [anthropic.com](https://www.anthropic.com/engineering/building-effective-agents) (2024)
  *Cited for:* workflow-vs-agent choice justification; architectural decision record signal.

- **Anthropic — *Candidate AI Guidance***. [anthropic.com/candidate-ai-guidance](https://www.anthropic.com/candidate-ai-guidance)
  *Cited for:* "overclaiming architecture/model novelty" red flag ("misrepresentation is the disqualifier, not AI use itself").

## Public-writing + DevRel register

- **Simon Willison's Weblog**. [simonwillison.net](https://simonwillison.net/)
  *Cited for:* the canonical "document-in-public" AI engineer pattern; TIL / negative-results / runnable examples genre.

- **Swyx — *The Rise of the AI Engineer***. [latent.space/p/ai-engineer](https://www.latent.space/p/ai-engineer)
  *Cited for:* role definition + genre conventions for the broader AI Engineering category.

- **Draft.dev — *Developer Relations Career Guide 2025***. [draft.dev/learn/developer-relations-career-insights-from-7-industry-leaders](https://draft.dev/learn/developer-relations-career-insights-from-7-industry-leaders)
  *Cited for:* "what you've done in public over what's on your resume" DevRel evaluation framing.

## Role-specific

- **Interview Query — *Why OpenAI Is Hiring Forward-Deployed AI Engineers Like Palantir***. [interviewquery.com](https://www.interviewquery.com/p/openai-palantir-forward-deployed-ai-engineers)
  *Cited for:* FDE persona scope + interview emphasis on decomposition and explanation.

- **Fonzi AI / Sammi Cox — *Forward-Deployed Engineers: the 800% Growth Role***. [medium.com/fonzi-ai](https://medium.com/fonzi-ai/forward-deployed-engineers-the-800-growth-role-redefining-ai-hiring-69e19d800047)
  *Cited for:* FDE role growth + hiring-bar framing in 2025.

## Genre exemplars (not heuristics sources, but the "what good looks like" standards)

- **Thorsten Ball — *Writing An Interpreter In Go***. [interpreterbook.com](https://interpreterbook.com/)
  *Cited for:* "book-as-credential" deep technical writing exemplar.

- **Hamel Husain & Shreya Shankar — *AI Evals for Engineers & PMs* (Maven cohort course)**. [maven.com/parlance-labs/evals](https://maven.com/parlance-labs/evals)
  *Cited for:* canonical venue where the eval practitioner community forms.

## Survey + field-scan references

- **alexeygrigorev — *ai-engineering-field-guide* (Q4 2025 / Q1 2026)**. [github.com/alexeygrigorev/ai-engineering-field-guide](https://github.com/alexeygrigorev/ai-engineering-field-guide)
  *Cited for:* "framework religiosity" and "API call in a trench coat" red-flag synthesis.

---

## How to cite this tool in your own work

If `portfolio-judge` was useful, please link the repo and the calibration state doc so readers can see the same disclosed limits the tool ships with.

If you ran the tool on your own portfolio and disagreed with a verdict, that disagreement is the single most valuable contribution — please open an issue describing what it got wrong. The aggregate of such reports is the community calibration mechanism this release is designed around.
