# Portfolio review: https://github.com/hamelsmu/evals-skills

**Role:** Applied AI Engineer / Agentic Engineering
**Model:** claude-sonnet-4-20250514

---

## Synthesis

## Convergent verdict
Strong LLM evaluation methodology expertise undermined by complete absence of engineering execution artifacts — no tests, no CI, no runnable code.

## Convergent strengths
- **Deep evaluation methodology expertise**: All four reviewers praised the sophisticated understanding of LLM evaluation challenges, with recruiter noting "TPR/TNR calibration, Rogan-Gladen correction, bootstrap confidence intervals" and applied_ai_hm scoring methodology rigor 8/10
- **Pedagogical clarity and systematic thinking**: Recruiter highlighted "pedagogical clarity" and "systematic failure mode knowledge," while fde_solutions_hm gave pedagogical instinct 9/10 and devrel_hm noted "solid pedagogical instinct with transferable techniques"
- **Technical honesty and disclosure**: Applied_ai_hm scored disclosure 9/10 for "honest engagement with failure modes," fde_solutions_hm gave 8/10 for "genuine technical honesty," and devrel_hm praised avoiding "marketing hype"
- **Practitioner-level specificity**: Recruiter noted "concrete numbers throughout" and "named tools," while applied_ai_hm appreciated "specific metrics" and "concrete failure patterns"

## Convergent gaps
- **Zero engineering artifacts**: All four reviewers flagged the complete absence of tests, CI, package structure, and runnable code. Applied_ai_hm called this "the core problem," fde_solutions_hm noted "no production discipline signals," and devrel_hm cited "broken installation instructions"
- **Documentation-only portfolio**: Applied_ai_hm noted "all artifacts are SKILL.md files," fde_solutions_hm observed "collection of documentation artifacts rather than shipped software," and devrel_hm highlighted the lack of "runnable examples that work out of the box"
- **Missing production readiness signals**: Fde_solutions_hm scored implementation discipline 3/10, applied_ai_hm couldn't assess "code quality" or "architectural judgment," and recruiter noted "no quantitative validation"

## Role-fit ranking
**Bad fit for Applied AI Engineer** — While recruiter suggested "stretch" fit, applied_ai_hm and fde_solutions_hm both rejected for lacking engineering execution. Devrel_hm noted this would be "highly valued" in Applied AI roles but the consensus shows the engineering gaps are disqualifying.

**Better fit for AI Solutions/Consulting** — Recruiter ranked this as "best fit" for AI Solutions Engineer, noting the evaluation expertise maps to "customer-facing technical roles" and "ability to guide non-experts."

## Probability estimate
**15th-30th percentile** for Applied AI Engineer roles based on reviewer consensus (applied_ai_hm: 15th percentile, recruiter: top 30%, others noted strong domain knowledge but execution gaps).

## Top 3 actionable next steps
1. **Ship a runnable evaluation tool with tests and CI** — Build a Python package that implements the eval-audit methodology with proper test coverage, GitHub Actions, and pip installation. This directly addresses the unanimous "no engineering artifacts" concern.

2. **Create end-to-end evaluation pipeline examples** — Build 2-3 complete evaluation workflows (RAG system audit, judge validation, error analysis) that work out-of-the-box with popular tools like LangChain/LlamaIndex. Include Docker setup and clear reproduction steps.

3. **Document quantitative validation of methodologies** — Provide case studies with metrics showing how these evaluation approaches improved system performance for real clients. Applied_ai_hm specifically noted "no data on whether these skills actually improve eval outcomes when deployed."

---

## Per-reviewer verdicts


### Reviewer: recruiter

## 60-second first-pass verdict
**ADVANCE** — This is a skills plugin for AI coding agents focused on LLM evaluation methodology, with detailed technical documentation that demonstrates deep practitioner knowledge.

## What I saw in the first minute
Strong pattern-match on the "50+ companies" credibility signal and the specific focus on LLM evaluation methodology. The README immediately positions this as practical tooling rather than research or demo work. Installation instructions are concrete and the skill-based architecture suggests systematic thinking about evaluation problems. However, I noticed this isn't a traditional codebase — it's documentation for AI agent skills, which is unusual for Applied AI Engineer roles.

## Second-pass findings
### Signal
- **Deep evaluation methodology expertise**: The skill documents show sophisticated understanding of LLM evaluation challenges — TPR/TNR calibration, Rogan-Gladen correction, bootstrap confidence intervals, systematic error analysis taxonomies
- **Practitioner-level specificity**: Concrete numbers throughout (100 traces for saturation, 50 Pass/Fail examples), named tools (Phoenix, Braintrust, LangSmith), specific statistical methods with code snippets
- **Systematic failure mode knowledge**: The error-analysis skill demonstrates insider knowledge of how LLM pipelines actually break in production, with specific examples like "SQL missed budget constraint" and "made up property features"
- **Anti-pattern documentation**: Each skill includes explicit warnings about common mistakes, showing awareness of how evaluation work goes wrong in practice
- **Pedagogical clarity**: All skills are structured as transferable methodologies that practitioners can apply to their own problems

### Concerns
- **No traditional codebase**: This is documentation for AI agent skills, not a runnable system I can evaluate for production readiness
- **Missing structural elements**: No tests, CI, package manifest, or recent git activity (not a git repo)
- **Unclear deployment model**: How would this person's evaluation expertise translate to building production AI systems vs. consulting/training?
- **No quantitative validation**: While the methodology is sophisticated, there's no evidence of these approaches being validated on real systems with measured outcomes

## Overclaim audit
- Claim I clicked through on: "50+ companies" — Can't verify this directly, but the depth of failure mode knowledge and specific anti-patterns suggests genuine consulting experience
- Claim I clicked through on: Statistical methodology (Rogan-Gladen correction, bootstrap CIs) — The technical details check out and show proper understanding of evaluator validation

## Role fit ranking
1. **Best fit: AI Solutions Engineer** — The deep evaluation methodology knowledge and ability to systematically diagnose AI system failures maps perfectly to customer-facing technical roles. The pedagogical instinct and anti-pattern documentation suggest strong ability to guide non-experts through evaluation challenges.

2. **Stretch: Applied AI Engineer** — The evaluation expertise is clearly there, but this portfolio doesn't demonstrate ability to build production AI systems. Would need evidence of implementing these methodologies in code, not just documenting them as agent skills.

3. **Bad fit: Forward Deployed Engineer** — While the evaluation knowledge is valuable, FDE roles typically require full-stack implementation skills and customer deployment experience that isn't demonstrated here.

## Comparable bench
Approximately **top 15%** of inbound I see for AI Solutions roles, **top 30%** for Applied AI roles. The evaluation methodology depth is exceptional — most candidates can't articulate TPR/TNR tradeoffs or systematic error analysis. However, the lack of traditional engineering artifacts (code, tests, deployments) limits the signal for hands-on implementation roles.

## Would I forward to the hiring manager?
**Yes, with reservations** — This candidate demonstrates exceptional depth in LLM evaluation methodology, which is a critical skill gap I see across most AI teams. The systematic thinking about failure modes and the ability to teach complex evaluation concepts clearly suggests they could add significant value to customer-facing technical roles. However, I'd flag that this portfolio doesn't demonstrate traditional software engineering skills or production system building experience. The hiring manager should assess whether the role requires hands-on implementation or if deep evaluation expertise with teaching ability is the primary need.

## What I'd want to see in a cover note
"I've helped 50+ companies debug their LLM evaluation pipelines and consistently see the same failure patterns. I've systematized this knowledge into methodologies that catch 80% of evaluation problems before they reach production. Here's how I'd apply this to [specific company challenge] and the first three diagnostic questions I'd ask about your current eval setup."

### Reviewer: applied_ai_hm

## Decision
**REJECT**

## One-line rationale
Strong eval methodology content but zero evidence of engineering execution — no tests, no CI, no package structure, no runnable code, just documentation.

## Technical depth assessment
### What impressed me
- **Methodological sophistication**: The eval-audit skill shows deep practitioner knowledge with specific metrics (TPR/TNR, ~100 traces for saturation), named tools (Phoenix, Braintrust), and concrete failure patterns I recognize from production systems.
- **Honest disclosure of limits**: The validate-evaluator skill properly discusses confidence intervals, sample size requirements, and when the Rogan-Gladen correction breaks down — this is the kind of statistical rigor that separates real practitioners from demo builders.
- **Pedagogical clarity**: The error-analysis skill provides a transferable 7-step process with concrete sampling strategies and decision frameworks that I could hand to a junior engineer.

### What concerned me
- **Zero engineering artifacts**: No tests, no CI, no package manifest, no runnable code. This reads like a consulting deliverable, not a software engineering portfolio.
- **Documentation-only evidence**: All artifacts are SKILL.md files. I can't assess code quality, architectural judgment, or production readiness because there's no code to review.
- **No measurement of the methodology itself**: Claims about "50+ companies" and course teaching, but no data on whether these skills actually improve eval outcomes when deployed.

### What I'd probe in interview
- "Show me the code that implements the eval-audit diagnostic checks — how do you actually detect missing error analysis in a codebase?"
- "Walk me through how you'd deploy the validate-evaluator workflow in a production CI pipeline."
- "What's your experience shipping these methodologies as actual software vs. consulting guidance?"

## Methodology rigor score: 8/10
The eval methodology is sophisticated and honest about limits. The validate-evaluator skill properly handles statistical validation with confidence intervals and bias correction. The error-analysis approach shows deep understanding of LLM failure modes.

## Code quality score: N/A
No code artifacts to assess. This is the core problem.

## Architectural judgment score: N/A
No architectural decisions visible. The skills are presented as documentation templates rather than implemented systems.

## Disclosure / honesty score: 9/10
Excellent disclosure of statistical limits, sample size requirements, and methodology boundaries. The "anti-patterns" sections show honest engagement with failure modes.

## Role-seniority band
**Senior** — based on methodology sophistication alone. The eval frameworks demonstrate deep practitioner knowledge and the kind of statistical rigor I'd expect from someone who's debugged production LLM systems. However, this assessment is based purely on domain knowledge, not engineering execution.

## Comparable bench
Approximately **15th percentile** among inbound for this role type.

## Recommendation to head of engineering
Don't interview. This candidate has strong eval methodology knowledge — the kind of domain expertise we'd want on the team — but has provided zero evidence they can ship software. The portfolio reads like a consultant's methodology deck rather than an engineer's work product. For an Applied AI Engineer role, I need to see tests, CI, runnable code, and architectural decisions under measurement pressure. The eval knowledge is valuable, but without engineering execution evidence, this is a consulting hire masquerading as an engineering candidate. If we're hiring for a Staff AI Researcher or Eval Methodology role, this would be different — but for Applied AI Engineer, the missing engineering discipline is disqualifying.

The irony is that someone with this level of eval sophistication should understand that claims need measurement and validation — yet they're asking us to evaluate their engineering ability with no engineering artifacts. That's a red flag about judgment under technical pressure.

### Reviewer: fde_solutions_hm

## Decision
**REJECT**

## Role-fit verdict
**Bad fit — lacks customer-facing implementation discipline and production readiness signals**

## Technical writing quality
Score **8/10**. The prose consistently demonstrates strong pedagogical instinct and technical precision. The eval-audit skill (36/50) and RAG evaluation skill (42/50) show genuine teaching ability with concrete, transferable techniques. However, the writing is optimized for AI agents as users rather than human customers — a fundamental mismatch for FDE work where you're explaining systems to skeptical VPs, not feeding instructions to Claude.

## Pedagogical instinct
Score **9/10**. Exceptional teaching throughout — the error analysis skill provides a complete 7-step methodology, the judge validation skill teaches statistical calibration with specific formulas, and the RAG evaluation skill maps failure patterns to diagnostic approaches. This person clearly knows how to break down complex technical work into learnable components.

## Implementation discipline
Score **3/10**. Critical gaps: no tests, no CI, no package manifest, no recent commits (not a git repo). The structural scan reveals this is a collection of documentation artifacts rather than shipped software. For an FDE role where you're debugging live customer systems, the absence of any production discipline signals is disqualifying.

## Customer-facing clarity
Score **4/10**. The writing is technically excellent but assumes the reader is already technical. Phrases like "TPR/TNR calibration" and "Rogan-Gladen correction" would lose a business stakeholder immediately. No evidence this person can translate between "here's the eval rigor" and "here's why the customer should trust this system."

## Honesty / disclosure quality
Score **8/10**. Strong disclosure of methodological limits throughout — the judge validation skill extensively covers confidence intervals and sample size requirements, the error analysis acknowledges when approaches don't scale. This is genuine technical honesty, not CYA disclaimers.

## What would surprise me in a customer call
**Impress**: Deep evaluation expertise — this person genuinely understands the hard parts of LLM evaluation and can diagnose failure modes systematically. **Trip them up**: Translating technical concepts to business value. They'd likely dive into statistical details when the customer needs to understand "will this catch the failures that matter to our users?"

## Strongest evidence of FDE potential
The eval-audit skill (skills/eval-audit/SKILL.md, 36/50) shows systematic diagnostic thinking — six specific areas to check, concrete sampling strategies, and a structured report format. This is exactly the kind of methodical troubleshooting approach FDEs need when inheriting customer systems.

## Biggest gap
Complete absence of production implementation signals. No tests, CI, or shipping evidence means I can't assess whether this person can actually build the systems they're teaching about. The grounding heuristics are clear: "End-to-end production shape, not notebook" and "Unfinished / undocumented / stale repos" as red flags. This portfolio hits both.

## Recommendation
**Reject for FDE/Solutions roles**. While the evaluation expertise is genuinely impressive, this candidate optimizes for AI agent consumption rather than human customer communication. The complete lack of production discipline signals (tests, CI, shipping evidence) suggests they're more suited for research or consulting than customer-facing engineering. They might be a strong fit for a pure ML evaluation role, but not for the customer empathy and implementation discipline that FDE work requires.

The technical writing quality is high, but it's the wrong register for customer-facing work. An FDE needs to move fluidly between "here's the statistical validation" and "here's why your CEO should trust this system" — this portfolio only demonstrates the former.

### Reviewer: devrel_hm

## Decision
REJECT

## Role-fit verdict
Not a DevRel candidate — This portfolio shows strong technical depth in LLM evaluation methodology but lacks the core DevRel artifacts: public teaching cadence, community engagement, and narrative-driven content that transfers knowledge to practitioners.

## Teaching quality score: 7/10
The skills documentation demonstrates solid pedagogical instinct with transferable techniques and specific examples. The eval-audit methodology (36/50) and RAG evaluation framework (42/50) provide actionable frameworks practitioners can steal. However, these read like internal documentation rather than public teaching — they're comprehensive but lack the narrative flow and contextual motivation that characterizes strong DevRel content. Compare to Simon Willison's blog posts which tell a story of discovery alongside the technical content.

## Runnable artifact quality: 4/10
Major red flags here. The structural scan shows no tests, no CI, no package manifest, and crucially — this isn't even a git repo so we can't assess commit recency. The README promises Claude Code plugin installation but provides no fallback for developers not using that specific tool. The "npx skills" installation section is incomplete ("install from this repo w"). This fails the "5-minute setup" test completely.

## Public posture score: 2/10
Zero evidence of operating in the open. No blog posts, no OSS contributions visible, no community engagement, no conference talks. The portfolio mentions "helping 50+ companies" and teaching a Maven course, but these are private consulting engagements, not public knowledge sharing. DevRel requires consistent public presence — this candidate operates entirely in private channels.

## Genre fluency score: 8/10
The writing maintains excellent technical register throughout, avoiding marketing hype and providing specific, load-bearing details. The methodology disclosure varies by artifact (2-5/50 range) but the overall tone matches the Husain/Shankar tradition of measured, evidence-based technical writing. However, it lacks the "learning exhaust" narrative style that makes DevRel content compelling.

## Niche depth score: 9/10
Clear ownership of LLM evaluation methodology. The candidate demonstrates deep expertise in error analysis, judge validation, and RAG evaluation with specific techniques like TPR/TNR calibration, bootstrap confidence intervals, and systematic failure categorization. This is exactly the kind of niche depth DevRel careers reward — but it needs to be shared publicly to be valuable for DevRel.

## One piece of their work I'd embed in our docs
The RAG evaluation skill (42/50) — specifically the diagnostic table mapping metric patterns to failure modes. This provides immediately actionable guidance for practitioners debugging their RAG pipelines. However, I'd need to rewrite it with better narrative flow and setup instructions that actually work.

## Biggest gap for DevRel specifically
Complete absence of public teaching artifacts. This candidate has built excellent internal methodology but hasn't demonstrated the ability to teach in public. DevRel requires: (1) consistent blog posting cadence showing learning in public, (2) runnable examples that work out of the box, (3) community engagement through issues/PRs/discussions, (4) conference talks or similar public speaking. This portfolio shows zero evidence of any of these.

## Recommendation
Reject for DevRel. This candidate has strong technical depth in LLM evaluation methodology — exactly what we'd want in an Applied AI Engineer role. But DevRel requires public teaching ability, community engagement, and polished artifacts that work immediately. The broken installation instructions, missing tests/CI, and complete absence of public writing disqualify them for DevRel specifically. They should apply for Applied AI Engineer roles where this evaluation expertise would be highly valued, then build public teaching artifacts over 6-12 months if they want to transition to DevRel later.

The technical content quality (especially the RAG evaluation framework) suggests they could become a strong DevRel candidate with coaching, but they need to demonstrate public teaching ability first. I'd recommend they start a technical blog, contribute to OSS evaluation tools, and build runnable examples before reapplying for DevRel roles.

---

## Structural findings

- ✅ **readme_present** (critical): Found README.md at repo root.
- ✅ **readme_has_install** (moderate): README contains one of ['install', 'installation', 'getting started', 'quickstart', 'quick start'].
- ❌ **readme_has_usage** (moderate): README missing section for ['usage', 'example', 'how to use', 'how it works', 'quickstart']; a README should show the reader what the project does, not just what it is.
- ✅ **readme_non_trivial_length** (cosmetic): README is 433 words.
- ✅ **license_present** (moderate): Found LICENSE at repo root.
- ❌ **tests_present** (moderate): No tests/ directory or test_*.py files found. Production readiness is hard to read without tests.
- ❌ **ci_present** (moderate): No CI config found (.github/workflows, .gitlab-ci.yml, .circleci, tox, etc.).
- ❌ **package_manifest_present** (moderate): No package manifest (pyproject.toml, package.json, Cargo.toml, etc.).
- ❌ **adr_present** (cosmetic): No docs/decisions or adr/ directory. ADRs are a signal of senior engineering discipline.
- ❌ **examples_or_demo_present** (cosmetic): No examples/ or demo/ directory found.
- ✅ **gitignore_present** (cosmetic): Found .gitignore.
- ❌ **recent_activity** (cosmetic): Target is not a git repo; cannot check commit recency.

---

## Prose judge scores


### README.md — 33/50
- **thesis_clarity**: 5/5 — The opening line "Skills that guide AI coding agents to help you build LLM evaluations" is a clear, specific claim that frames the entire piece. This is immediately followed by a concrete value proposition about guarding against common mistakes seen across 50+ companies. The thesis is defensible and specific rather than generic throat-clearing.
- **problem_framing**: 2/5 — The piece mentions "common mistakes I've seen helping 50+ companies" but doesn't articulate what's specifically hard about building LLM evaluations or why naive approaches fail. It jumps fairly quickly to the solution (the skills plugin) without deeply motivating the problem space or explaining what makes eval work challenging.
- **specific_evidence**: 4/5 — The piece provides concrete specifics: "50+ companies," named tools like "Claude Code," specific installation commands, and direct GitHub URLs. The skills table provides concrete functionality descriptions, and there are specific course links with promo codes. However, it lacks quantitative performance data or specific failure examples that would signal deeper insider knowledge.
- **pedagogical_instinct**: 4/5 — The piece teaches multiple transferable techniques: how to install and use the plugin system, specific command patterns for different CLI tools, and a concrete workflow for using the eval-audit skill with subagents. The installation instructions and skill invocation patterns are directly applicable to readers' own work. The meta-skill reference and course pointer provide additional learning pathways.
- **methodology_disclosure**: 3/5 — The piece makes no measurement claims about the effectiveness of the skills, performance improvements, or quantitative results. Since there are no measurement claims to evaluate, this criterion should be scored as neutral per the instructions.
- **integrative_reasoning**: 2/5 — The piece acknowledges that "these skills are a starting point" and "skills grounded in your stack, your domain, and your data will outperform them," showing awareness of the tension between generalized vs. customized solutions. However, it doesn't deeply explore this tension or synthesize a resolution - it simply states both sides exist without integrative analysis.
- **counterargument_handling**: 2/5 — The piece briefly acknowledges limitations by stating the skills "only encode common mistakes that generalize across projects" and that "much of the process doesn't" generalize. However, it doesn't steelman potential objections like "why use these instead of building custom solutions from scratch" or address skepticism about the effectiveness of generalized eval skills.
- **structural_coherence**: 2/5 — The headings are mostly topic labels like "Installation," "Available Skills," and "Write Your Own Skills" rather than argumentative assertions. While "New to Evals? Start Here" is more directive, the overall structure uses container headings that describe content areas rather than making specific claims that advance an argument.
- **register_alignment**: 5/5 — The piece maintains a technical register throughout, using precise terminology like "TPR/TNR," "dimension-based tuple generation," and "CI/CD integration." It avoids marketing hype and superlatives, presenting the skills as practical tools rather than revolutionary solutions. The tone is measured and professional without overclaiming.
- **conclusion_advances**: 4/5 — The conclusion section "Beyond These Skills" advances beyond summary by reframing the skills as handling only the generalizable parts of eval work, while pointing toward the broader ecosystem of production monitoring, CI/CD integration, and domain-specific work. This provides a novel perspective on where these tools fit in the larger evaluation landscape that couldn't have been stated at the outset.

### skills/eval-audit/SKILL.md — 36/50
- **thesis_clarity**: 5/5 — The piece opens with a clear, specific claim in the first sentence: "Inspect an LLM eval pipeline and produce a prioritized list of problems with concrete next steps." This immediately establishes what the piece will do and frames the entire methodology. The opening avoids throat-clearing or background setup, diving directly into the core purpose.
- **problem_framing**: 3/5 — The piece articulates the problem clearly - inheriting or auditing eval systems where trustworthiness is uncertain. However, it doesn't deeply explore what makes this problem hard or why naive approaches fail. It mentions some failure modes (missing error analysis, unvalidated judges) but doesn't frame why these are particularly challenging problems to solve systematically.
- **specific_evidence**: 5/5 — The piece consistently deploys specific, named tools and concrete examples throughout. It references specific observability platforms (Phoenix, Braintrust, LangSmith, Truesight), cites specific articles with direct links, mentions concrete metrics (TPR/TNR, ~100 traces for saturation, ~50 Pass/Fail examples), and provides specific technical details like file formats (CSVs, JSON). This level of specificity signals deep practitioner knowledge.
- **pedagogical_instinct**: 5/5 — The piece teaches multiple transferable techniques: six diagnostic areas with specific checks, concrete sampling strategies (random, clustering, data analysis, classification, feedback), a structured report format, and specific anti-patterns to avoid. Each technique is framed so practitioners can apply it to their own eval audits. The diagnostic framework is particularly stealable as a systematic approach.
- **methodology_disclosure**: 2/5 — The piece makes specific measurement claims (100 traces for saturation, 50 Pass/Fail examples for validation) but doesn't provide confidence intervals, calibration states, or detailed methodology for how these numbers were derived. While it mentions these are "rough targets," it doesn't disclose the limits or what would invalidate these recommendations.
- **integrative_reasoning**: 2/5 — The piece acknowledges some tensions (like when to use code-based checks vs LLM judges, or different sampling strategies) but doesn't deeply explore opposing models in genuine tension. It tends to present clear preferences (binary over Likert scales, specific over generic categories) rather than synthesizing competing approaches or holding contradictory models in productive tension.
- **counterargument_handling**: 3/5 — The piece includes an "Anti-Patterns" section that addresses potential objections like running audits as checklists or recommending evaluators before error analysis. However, these feel more like warnings than steelmanned counterarguments. It doesn't deeply engage with the strongest objection a skeptical reader might have about the methodology's effectiveness or completeness.
- **structural_coherence**: 4/5 — The headings function well as a standalone argument structure. Reading just "Overview," "Diagnostic Checks," "Error Analysis," "Evaluator Design," "Judge Validation," etc. reconstructs the core methodology. However, some headings like "Prerequisites" and "Connecting to Eval Infrastructure" are more procedural than argumentative, and the numbered diagnostic areas could be more assertion-based.
- **register_alignment**: 5/5 — The piece maintains a consistently technical register throughout, avoiding marketing language and hype. Claims are measured and specific (e.g., "~100 traces is the rough target" rather than "many traces"). The language is precise and practitioner-focused without overclaiming or using superlatives like "revolutionary" or "cutting-edge."
- **conclusion_advances**: 2/5 — The piece doesn't have a traditional conclusion section. The "Anti-Patterns" section at the end provides some novel framing about what not to do, and the "No Eval Infrastructure" section offers actionable next steps for a specific scenario. However, there's no synthesis that advances beyond what was covered in the diagnostic sections or reframes the overall approach in a new light.

### skills/validate-evaluator/SKILL.md — 38/50
- **thesis_clarity**: 5/5 — The piece opens with a clear, specific claim: "Calibrate an LLM judge against human judgment." This is immediately followed by a concrete overview that frames the entire methodology. The opening doesn't waste time with background or throat-clearing, instead directly stating what the piece will teach and why it matters.
- **problem_framing**: 4/5 — The piece clearly articulates the problem: LLM judges need validation against human labels before they can be trusted. It explains what's hard about this - judges may "consistently miss failures or flag passing traces" and raw scores are biased. The anti-patterns section reinforces why naive approaches (assuming judges "just work") fail.
- **specific_evidence**: 5/5 — The piece is rich with specific technical details: exact code snippets using sklearn, specific formulas like the Rogan-Gladen correction, concrete numbers (TPR > 90%, ~100 traces, 50 Pass/50 Fail), and named tools like the `judgy` library. It provides specific model version examples ("gpt-4o-2024-05-13") and exact statistical methods (Cohen's Kappa, bootstrap confidence intervals).
- **pedagogical_instinct**: 5/5 — The piece teaches multiple concrete, transferable techniques: data splitting methodology, TPR/TNR measurement, bias correction formulas, bootstrap confidence intervals, and systematic disagreement analysis. Each technique is presented with enough detail that a practitioner could implement it on their own evaluation problem. The step-by-step structure and code examples make the techniques immediately actionable.
- **methodology_disclosure**: 5/5 — The piece extensively discloses methodological limits and assumptions. It specifies sample size requirements (~100 labeled examples), warns about confidence interval width with small samples, discusses when the correction formula becomes invalid (TPR + TNR - 1 near 0), and emphasizes the need for bootstrap confidence intervals rather than point estimates alone.
- **integrative_reasoning**: 2/5 — The piece doesn't present opposing models in tension or synthesize competing frameworks. It presents a single methodology without exploring alternative approaches or acknowledging trade-offs between different validation strategies. The content is comprehensive but doesn't engage with conflicting perspectives on evaluator validation.
- **counterargument_handling**: 3/5 — The piece anticipates several strong objections through its "Anti-Patterns" section, addressing concerns like "assuming judges just work," using raw accuracy instead of TPR/TNR, and reporting point estimates without confidence intervals. However, it doesn't deeply steelman these objections or provide extensive evidence against them - it mostly states why they're wrong rather than engaging with their underlying logic.
- **structural_coherence**: 2/5 — The headings are mostly topic labels ("Overview," "Prerequisites," "Core Instructions") rather than argument-bearing assertions. While the step-by-step structure is clear, reading only the headings doesn't reconstruct the core argument about why this validation methodology is necessary or superior to alternatives.
- **register_alignment**: 5/5 — The piece maintains a consistently technical register throughout, using precise statistical terminology (TPR, TNR, Rogan-Gladen correction) and avoiding marketing language. Claims are measured and specific rather than hyperbolic. The tone is instructional and professional without any "revolutionary" or "cutting-edge" language.
- **conclusion_advances**: 2/5 — The piece doesn't have a traditional conclusion section - it ends with practical guidance and anti-patterns. The final sections provide actionable next steps and reframe common mistakes, but don't synthesize a novel implication that couldn't have been stated at the outset. The ending feels more like completion of instructions rather than advancement of the argument.

### skills/error-analysis/SKILL.md — 39/50
- **thesis_clarity**: 5/5 — The piece opens with a clear, specific claim: "Guide the user through reading LLM pipeline traces and building a catalog of how the system fails." This immediately establishes the purpose and frames the entire methodology. The opening doesn't waste time with background or throat-clearing, instead directly stating what the piece will accomplish.
- **problem_framing**: 3/5 — The piece articulates the problem clearly in the overview: systematically identifying failure modes in LLM pipelines. However, it doesn't deeply explore what makes this problem hard or why naive approaches fail. While it mentions that "errors cascade" and explains why to focus on "the first thing that went wrong," it could better motivate why systematic error analysis is challenging.
- **specific_evidence**: 5/5 — The piece provides concrete, specific guidance throughout: "~100 traces," specific sampling strategies with named methods (K-means clustering), code snippets for failure rate computation, and detailed templates. It includes specific examples like "SQL missed the budget constraint" and "Made up property features (solar panels)" that demonstrate insider knowledge of LLM failure modes.
- **pedagogical_instinct**: 5/5 — The piece is highly transferable, providing multiple concrete techniques practitioners can steal: the 7-step process, trace sampling strategies, failure categorization methods, and specific heuristics for when to split vs. group failures. The templates, code snippets, and decision frameworks are all directly applicable to other LLM pipeline analysis projects.
- **methodology_disclosure**: 2/5 — The piece makes specific measurement claims (like "~100 traces" and stopping criteria) but doesn't provide confidence intervals, calibration states, or detailed limitations. While it mentions that "the exact number depends on system complexity," it doesn't disclose what would invalidate the approach or provide statistical backing for the recommended sample sizes.
- **integrative_reasoning**: 3/5 — The piece acknowledges tensions between different approaches (real vs. synthetic data, code-based vs. LLM judges, fixing vs. evaluating) but generally provides clear guidance on when to use each rather than synthesizing opposing models. It doesn't deeply explore fundamental tensions in the methodology or provide integrative resolutions to competing frameworks.
- **counterargument_handling**: 3/5 — The piece anticipates several strong objections through its "Anti-Patterns" section, addressing concerns like "why not brainstorm categories first?" and "why not build evaluators immediately?" However, these are presented as warnings rather than steelmanned objections with evidence-based responses. The piece could better address the strongest objection: whether this manual process scales.
- **structural_coherence**: 5/5 — The headings function well as a standalone argument: "Collect Traces" → "Read Traces and Take Notes" → "Group Failures into Categories" → "Label Every Trace" → "Compute Failure Rates" → "Decide What to Do About Each Failure" → "Iterate." Reading only the headings reconstructs the core methodology and logical flow of the error analysis process.
- **register_alignment**: 5/5 — The piece maintains a consistently technical register throughout, avoiding marketing language and hype. Terms like "LLM pipeline traces," "embedding clustering," and "binary labels" signal technical expertise. The language is precise and measured, with claims appropriately qualified (e.g., "roughly where new traces stop revealing new kinds of failures").
- **conclusion_advances**: 3/5 — The piece doesn't have a traditional conclusion section, ending instead with "Anti-Patterns" that provide novel warnings about common mistakes. While this adds value beyond summary, it doesn't deliver a reframing or implication that couldn't have been stated at the outset. The anti-patterns are more of a checklist than a synthesis of the methodology's deeper insights.

### skills/write-judge-prompt/SKILL.md — 40/50
- **thesis_clarity**: 5/5 — The opening immediately states a specific, defensible claim: "Design a binary Pass/Fail LLM-as-Judge evaluator for one specific failure mode. Each judge checks exactly one thing." This frames the entire piece around a particular approach to evaluation design. The claim is concrete and actionable, setting clear expectations for what follows.
- **problem_framing**: 5/5 — The piece clearly articulates what's hard about the problem in the Prerequisites section, explaining that "many failure modes that seem subjective reduce to keyword checks, regex, or API calls when you understand the domain." It provides a concrete example of how detecting "general" interview questions seems to require semantic understanding but can actually be solved with keyword checks. This motivates why LLM judges are needed only after exhausting simpler approaches.
- **specific_evidence**: 5/5 — The piece consistently deploys specific examples throughout, including concrete email templates, JSON schemas, and detailed failure mode examples. It references specific tools and providers (OpenAI's response_format, Anthropic tool definitions, Instructor, Outlines) and includes precise implementation details like "2-4 examples is typical" and "Performance plateaus after 4-8." The evidence is concrete enough to signal practitioner knowledge.
- **pedagogical_instinct**: 5/5 — The piece provides multiple transferable techniques: the four-component structure for judge prompts, specific rules for selecting examples, structured output formatting, and a decision table for what to pass to judges. Each technique is framed so practitioners can apply it to their own evaluation problems. The anti-patterns section explicitly teaches what to avoid, making the guidance immediately actionable.
- **methodology_disclosure**: 3/5 — The piece makes no measurement claims about performance, accuracy, or effectiveness of the proposed approach. It mentions "Performance plateaus after 4-8" examples but doesn't provide supporting data. Since there are no measurement claims requiring disclosure of methodology limits, this criterion should be scored as neutral.
- **integrative_reasoning**: 2/5 — The piece acknowledges the tension between using code-based evaluators versus LLM judges, but it resolves this by advocating for exhausting code-based options first rather than synthesizing both approaches. While it mentions this trade-off, it doesn't hold the models in genuine tension or provide a nuanced synthesis that incorporates elements of both approaches.
- **counterargument_handling**: 4/5 — The piece anticipates several strong objections through its anti-patterns section, addressing concerns about vague criteria, holistic judges, and Likert scales. It steelmans the objection to binary scoring by explaining why "Likert scales produce scores that sound precise but can't be calibrated" and provides specific evidence about annotator disagreement. However, it doesn't address the strongest potential objection about when LLM judges might be unreliable or biased.
- **structural_coherence**: 2/5 — The headings function as topic labels rather than standalone arguments. Headings like "The Four Components," "Choosing What to Pass to the Judge," and "Anti-Patterns" describe content categories but don't convey the specific argument being made. Reading only the headings doesn't reconstruct the core argument about how to design effective LLM judges.
- **register_alignment**: 5/5 — The piece maintains a consistently technical register throughout, avoiding marketing language and hype. Claims are measured and specific, such as "Performance plateaus after 4-8" rather than "dramatically improves." The language is precise and practitioner-focused without overclaiming or using superlatives like "revolutionary" or "cutting-edge."
- **conclusion_advances**: 4/5 — The conclusion section is actually the "Anti-Patterns" section, which goes beyond summary to provide actionable guidance about what to avoid. It delivers novel implications like "Binary forces you to define a clear decision boundary upfront" and reframes the validation requirement as essential rather than optional. This advances beyond what was established in the main body.

### skills/evaluate-rag/SKILL.md — 42/50
- **thesis_clarity**: 5/5 — The piece opens with a numbered overview that immediately presents its core claim: "Do error analysis on end-to-end traces first. Determine whether failures come from retrieval, generation, or both." This is a specific, defensible methodology claim that frames the entire evaluation approach. The opening doesn't waste time with background or throat-clearing but jumps directly to the main argument about prioritizing error analysis before metrics.
- **problem_framing**: 5/5 — The piece clearly articulates what's hard about RAG evaluation: the challenge of separating retrieval failures from generation failures, and the common mistake of using end-to-end metrics without component-level diagnosis. It explicitly states "Complete error analysis on RAG pipeline traces before selecting metrics" and explains why naive approaches fail (jumping to metrics without understanding failure modes). The Prerequisites section specifically motivates why error analysis must come first.
- **specific_evidence**: 5/5 — The piece consistently deploys specific technical details: named metrics (Recall@k, NDCG@k, MRR), concrete formulas, specific example configurations in grid search tables, and detailed prompt templates. It provides exact JSON formats, specific token counts (128, 256, 512), and numerical examples in tables. The synthetic QA generation section includes a complete prompt template and concrete examples with specific companies and dates.
- **pedagogical_instinct**: 5/5 — The piece teaches multiple transferable techniques: synthetic QA generation with specific prompts, adversarial question generation methodology, grid search optimization for chunking, and diagnostic patterns for failure analysis. Each technique is presented with enough detail that a practitioner could implement it directly. The diagnostic table mapping metric patterns to failure modes is particularly actionable, allowing readers to classify their own pipeline failures.
- **methodology_disclosure**: 3/5 — The piece makes no specific measurement claims about performance numbers or experimental results. The grid search table appears to be illustrative rather than reporting actual experimental results. Since no measurement claims are made, this should be scored as neutral rather than penalized for absence of methodology disclosure.
- **integrative_reasoning**: 4/5 — The piece acknowledges the tension between recall and precision in retrieval (wanting comprehensive coverage vs. ranked quality) and synthesizes this by recommending different metrics for different stages: Recall@k for first-pass retrieval, Precision@k for reranking. It also balances the trade-off between synthetic (scalable) and manual (high quality) evaluation datasets, providing guidance on when to use each approach rather than declaring one superior.
- **counterargument_handling**: 4/5 — The piece anticipates several strong objections: the caveat that "optimal ranking of weakly relevant documents can outscore a highly relevant document ranked lower" for NDCG, the warning about "overfitting to synthetic evaluation data," and the limitation that "even correct facts from the LLM's own knowledge count as hallucinations" in RAG contexts. These objections are addressed with specific evidence and mitigation strategies rather than dismissed.
- **structural_coherence**: 2/5 — The headings are mostly descriptive topic labels rather than argumentative assertions: "Evaluate Retrieval and Generation Separately," "Building a Retrieval Evaluation Dataset," "Retrieval Metrics." While these headings organize the content logically, they don't function as a standalone argument that could be read independently to reconstruct the core thesis. They describe what will be covered rather than making specific claims.
- **register_alignment**: 5/5 — The piece maintains a consistently technical register throughout, using precise terminology like "Recall@k," "NDCG," and "two-hop queries" without marketing language. There are no hype adjectives or overclaims about being "revolutionary" or "cutting-edge." The tone is measured and instructional, appropriate for a technical audience, with claims that are specific and load-bearing rather than promotional.
- **conclusion_advances**: 4/5 — The piece ends with an "Anti-Patterns" section that provides novel synthesis by identifying common failure modes that weren't explicitly stated earlier: the danger of single end-to-end metrics, the trap of similarity metrics for generation evaluation, and the risk of overfitting to synthetic data. This reframes the entire methodology by showing what NOT to do, which couldn't have been stated at the outset without first establishing the positive framework.