# Portfolio review: https://github.com/simonw/datasette

**Role:** Applied AI Engineer / Agentic Engineering
**Model:** claude-sonnet-4-20250514

---

## Synthesis

## Convergent verdict
All four reviewers rejected due to complete domain mismatch — this is a high-quality data tooling portfolio (Datasette) with zero AI/ML components for an Applied AI Engineer role.

## Convergent strengths
**Exceptional engineering fundamentals** — All reviewers praised the code quality (applied_ai_hm: 8/10, fde_solutions_hm: 8/10 implementation discipline, devrel_hm: 8/10 runnable artifacts). The multipart parser specifically impressed both applied_ai_hm (28/30) and recruiter as "sophisticated architecture."

**Production-grade discipline** — Three reviewers (recruiter, applied_ai_hm, fde_solutions_hm) highlighted the comprehensive test suite (56 files), robust CI (14 workflows), and proper packaging structure as evidence of senior-level shipping discipline.

**Technical documentation competence** — Both applied_ai_hm and fde_solutions_hm noted the upgrade guides show systematic approach to breaking changes with clear migration paths and specific code examples.

## Convergent gaps
**Complete AI/ML absence** — All four reviewers flagged zero AI components: no LLMs, agents, evals, RAG systems, or model integration anywhere in the codebase (recruiter: "No AI artifacts," applied_ai_hm: "Wrong domain entirely," fde_solutions_hm: "Complete domain mismatch").

**Role targeting error** — Three reviewers (recruiter, applied_ai_hm, fde_solutions_hm) explicitly called this a fundamental application mistake — applying for AI engineering with a data publishing tool portfolio.

**Missing AI methodology** — Applied_ai_hm noted absence of eval methodology, systematic error analysis, and LLM-as-judge patterns specifically called out in role requirements.

## Role-fit ranking
**Bad fit** — Unanimous across all reviewers. Recruiter: "0th percentile for AI engineering," applied_ai_hm: "Hard pass," fde_solutions_hm: "Reject," devrel_hm: "Not a DevRel candidate."

## Probability estimate
0th percentile for Applied AI Engineer role. Multiple reviewers noted this would be 85th+ percentile for backend/data infrastructure roles, but complete mismatch for AI positions.

## Top 3 actionable next steps

1. **Build AI portfolio immediately** — Create 2-3 projects demonstrating LLM integration, eval methodology, and agentic workflows. Applied_ai_hm suggested: "LLM-powered natural language querying with eval methodology for measuring query understanding accuracy."

2. **Target correct role category** — Apply for Senior Backend Engineer or Data Infrastructure roles where this portfolio would be competitive (recruiter noted "top 5%" fit for those domains).

3. **Bridge the gap explicitly** — If pursuing AI roles, create cover materials explaining: "I know this portfolio shows data tooling, but here's my AI work: [specific AI projects]" as recruiter recommended.

---

## Per-reviewer verdicts


### Reviewer: recruiter

## 60-second first-pass verdict
**ARCHIVE** — This is a mature open-source tool (Datasette), not an AI engineering portfolio.

## What I saw in the first minute
The README immediately signals this is Simon Willison's Datasette project - a data exploration and publishing tool, not AI/ML work. The badges, branding, and description ("multi-tool for exploring and publishing data") clearly position this as infrastructure tooling for data journalists and researchers. No mention of LLMs, agents, embeddings, or AI workflows anywhere in the opening.

## Second-pass findings
### Signal
- **Production-grade engineering**: 56 test files, 14 CI workflows, comprehensive error handling with custom exceptions, proper async patterns
- **Documentation discipline**: Detailed upgrade guides, API documentation, clear architectural decisions around permission systems
- **Code quality**: Excellent naming conventions, proper separation of concerns, sophisticated multipart parsing implementation

### Concerns
- **Wrong domain entirely**: This is data tooling, not AI engineering. No evidence of LLM integration, RAG systems, agents, or AI workflows
- **Role mismatch**: Candidate applied for "Applied AI Engineer / Agentic Engineering" but portfolio shows database/web tooling expertise
- **No AI artifacts**: No evals, no model integration, no prompt engineering, no AI-specific architecture decisions

## Overclaim audit
- Claim I clicked through on: "Applied AI Engineer" application vs. actual portfolio content
- Result: Complete mismatch - this is a data publishing tool with zero AI components

## Role fit ranking
1. **Bad fit**: Applied AI Engineer — No AI/ML work visible anywhere in codebase
2. **Bad fit**: Forward Deployed Engineer — Wrong technical domain (data tools vs. AI systems)  
3. **Bad fit**: AI Solutions Engineer — No AI solutions demonstrated

## Comparable bench
This would be top 5% for a **backend/data infrastructure** role, but 0th percentile for AI engineering roles. It's like reviewing a brilliant chef's portfolio for a mechanical engineering position.

## Would I forward to the hiring manager?
**No** — This is a fundamental role-targeting error. The candidate has submitted a portfolio for the wrong job category entirely. While the engineering quality is exceptional (production-ready codebase, excellent documentation, sophisticated architecture), there's zero overlap with AI engineering requirements. No LLMs, no agents, no evals, no AI-specific challenges solved.

The structural scan shows strong engineering discipline (tests, CI, documentation), and the code quality is genuinely impressive - particularly the multipart parser and permission system architecture. But this is like receiving a world-class violin performance audition for a software engineering role.

## What I'd want to see in a cover note
If this person contacted me for an AI engineering role, I'd need them to explain: "I know this portfolio shows data tooling, but here's my AI work: [link to RAG system/agent framework/LLM application]." Without that bridge, this is an immediate archive regardless of code quality.

### Reviewer: applied_ai_hm

## Decision
REJECT

## One-line rationale
This is a mature open-source tool (Datasette), not an Applied AI Engineer portfolio demonstrating eval methodology, LLM integration, or production AI system design.

## Technical depth assessment
### What impressed me
- **Code quality is genuinely strong**: The multipart parser (28/30) shows excellent architectural design with proper state machine implementation, comprehensive error handling, and clean separation of concerns. This is production-grade systems code.
- **Engineering discipline evident**: 56 test files, 14 CI workflows, proper package structure with pyproject.toml. The structural hygiene is solid.
- **Documentation methodology**: The upgrade guides (30/50, 38/50) show systematic approach to breaking changes with specific before/after code examples and clear migration paths.

### What concerned me
- **Wrong domain entirely**: This is a data publishing/exploration tool with zero AI/ML/LLM components. No evals, no model integration, no retrieval systems, no agents.
- **No Applied AI artifacts**: Scanning 5 code files reveals database abstraction layers, CLI tooling, multipart parsing, and SQL generation. Nothing that demonstrates AI engineering competency.
- **Mismatch with role requirements**: The grounding explicitly calls out "systematic error analysis on real traces," "calibrated LLM-as-judge," "context engineering over model chasing" — none present here.

### What I'd probe in interview
This wouldn't reach interview stage, but if it did: "Walk me through how you'd add LLM-powered natural language querying to Datasette, including your eval methodology for measuring query understanding accuracy."

## Methodology rigor score: N/A
No AI methodology present to evaluate. This is a data tooling project.

## Code quality score: 8/10
Genuinely impressive systems programming. The multipart parser and database abstraction show senior-level architectural thinking.

## Architectural judgment score: N/A
Strong general software architecture, but no AI-specific architectural decisions to assess.

## Disclosure / honesty score: N/A
No AI claims made, so no opportunity for overclaiming or underdisclosure.

## Role-seniority band
Senior — based on code quality alone. But wrong specialization entirely.

## Comparable bench
0th percentile for Applied AI Engineer role (domain mismatch), but would be ~85th percentile for a Senior Backend Engineer role.

## Recommendation to head of engineering
Hard pass. This candidate has strong general engineering skills — the code quality is genuinely impressive, particularly the multipart parser and database abstraction layers. They clearly understand production systems, testing, and architectural design. However, they're applying for Applied AI Engineer and have submitted a portfolio with zero AI components. No evals, no LLM integration, no retrieval systems, no model orchestration. It's like a brilliant frontend engineer applying for a kernel developer role with React components. The skills don't transfer to what we need: someone who can build and measure AI systems in production. If we had a data infrastructure role open, I'd advance them immediately. For Applied AI? Not a fit.

### Reviewer: fde_solutions_hm

## Decision
REJECT

## Role-fit verdict
Bad fit — this is a mature open-source tool maintainer's portfolio, not an Applied AI Engineer candidate. No AI/ML work visible anywhere.

## Technical writing quality
Score 6/10. The upgrade guides show solid technical documentation skills with specific examples and clear migration paths. However, the writing is purely descriptive documentation rather than analytical technical communication that teaches broader principles. The README excerpt is functional but lacks the problem-framing and pedagogical instinct needed for customer-facing roles.

## Pedagogical instinct
Score 4/10. The upgrade guides teach specific migration techniques that are transferable (plugin API changes, async patterns), but most content is reference documentation. Missing the "why" behind decisions and broader patterns that would help readers understand underlying principles.

## Implementation discipline
Score 8/10. Excellent evidence of shipping discipline — comprehensive test suite (56 test files), robust CI (14 workflows), proper packaging, clean error handling, and production-ready code architecture. The database.py and multipart.py files show sophisticated async patterns and resource management.

## Customer-facing clarity
Score 3/10. The writing assumes deep technical context and doesn't translate complexity for non-technical stakeholders. A VP reading the upgrade guides would understand *what* changed but not *why it matters* for their business objectives.

## Honesty / disclosure quality
Score 7/10. The upgrade documentation honestly discloses breaking changes and migration complexity. However, no measurement claims or performance assertions are made that would test deeper disclosure practices around limitations and tradeoffs.

## What would surprise me in a customer call
**Impress:** Deep systems knowledge, production reliability focus, clear documentation of breaking changes. This person clearly ships robust software and communicates changes responsibly.

**Trip them up:** Complete absence of AI/ML context. No evidence they've worked with LLMs, evals, retrieval systems, or any applied AI patterns. They'd be lost discussing RAG architectures, judge calibration, or agentic workflows.

## Strongest evidence of FDE potential
The upgrade documentation in docs/upgrade-1.0a20.md (38/50 prose score) shows strong technical communication with clear before/after code examples and strategic guidance like "Target the new APIs exclusively." This demonstrates ability to guide technical users through complex migrations.

## Biggest gap
**Complete domain mismatch.** This portfolio shows zero AI/ML work — no LLM integration, no retrieval systems, no evals, no agentic patterns. For an "Applied AI Engineer / Agentic Engineering" role, this is disqualifying. The candidate appears to be a data publishing tool maintainer, not an AI practitioner.

## Recommendation
**Reject.** While this candidate demonstrates excellent software engineering discipline and technical documentation skills, they're applying for the wrong role entirely. This is a traditional web application/data tool developer with no visible AI/ML experience. The structural scan confirms this is Datasette (Simon Willison's data publishing tool) — impressive software, but completely orthogonal to applied AI engineering. The candidate should be applying for backend engineering or developer tools roles, not AI positions.

The technical quality is high, but domain relevance is zero. No amount of good engineering practices compensates for complete absence of AI/ML context in an AI engineering role.

### Reviewer: devrel_hm

## Decision
REJECT

## Role-fit verdict
Not a DevRel candidate — This is a mature, well-engineered open source project (Datasette) but lacks the specific DevRel signals I need to see. The candidate appears to be a strong systems engineer but hasn't demonstrated the teaching, community engagement, and public learning patterns that define effective DevRel work.

## Teaching quality score: 3/10
The writing samples are pure documentation rather than teaching artifacts. The upgrade guides (scoring 30/50 and 38/50) are competent technical documentation but don't transfer techniques practitioners can steal and apply elsewhere. The README excerpt shows tool introduction rather than pedagogical instinct. Missing entirely: blog posts, tutorials that teach transferable patterns, or "learning exhaust" that shows the candidate figuring things out in public. This is maintenance documentation, not DevRel-quality teaching.

## Runnable artifact quality: 8/10
Excellent on the engineering fundamentals. The structural scan shows ✅ on all critical markers: README with install/usage, tests (56 files), CI (14 workflows), proper packaging. The code quality is strong across all samples (20-28/30 scores), with particularly excellent work in multipart.py (28/30). However, no examples/ or demo/ directory found, which is a gap for DevRel — practitioners need runnable examples, not just installable tools.

## Public posture score: 2/10
This is the biggest gap. I see no evidence of operating in the open beyond maintaining the codebase. No blog posts, no conference talks, no community engagement artifacts, no issues filed on other projects, no learning-in-public pattern. The candidate may be Simon Willison himself (Datasette's creator), but the portfolio as presented shows maintenance work, not DevRel community engagement.

## Genre fluency score: 4/10
The writing is technically competent but reads like engineering documentation, not DevRel content. Missing the Willison/Husain/Shankar register of "here's what I learned, here's what didn't work, here's the tradeoff I discovered." The upgrade guides are functional but don't have the narrative quality or disclosed learning process that characterizes strong DevRel writing.

## Niche depth score: 7/10
Clear ownership of the data exploration/publishing niche through Datasette. The code shows deep SQLite expertise, sophisticated permission systems, and thoughtful API design. However, this reads more like product engineering than DevRel niche development — I need to see the candidate teaching others in this niche, not just building in it.

## One piece of their work I'd embed in our docs
The upgrade-1.0a20.md guide (38/50 score) for its clear before/after code examples and specific migration patterns. The structural coherence is strong with argument-driven headings, and it provides actionable guidance practitioners could follow. However, it's still documentation rather than teaching — it tells you how to upgrade but doesn't teach you the underlying patterns.

## Biggest gap for DevRel specifically
Complete absence of public teaching and community engagement. This candidate needs to demonstrate: (1) regular blog posts that teach transferable techniques, (2) evidence of helping practitioners in public forums, (3) conference talks or similar community presence, (4) runnable examples that teach concepts beyond just tool usage. The engineering quality is there, but DevRel requires being a public teacher and community member, not just a maintainer.

## Recommendation
Pass. While this is clearly a skilled engineer working on an important open source project, they haven't demonstrated the core DevRel competencies I need. The portfolio shows maintenance and documentation work rather than teaching, learning in public, or community engagement. For a DevRel role, I need evidence that the candidate can take complex technical concepts and make them accessible to practitioners through teaching-quality content and public engagement. The engineering foundation is solid, but the DevRel-specific skills are missing entirely.

The candidate would need to build a substantial portfolio of teaching content, demonstrate community engagement patterns, and show evidence of helping practitioners learn — not just maintaining excellent code.

---

## Structural findings

- ✅ **readme_present** (critical): Found README.md at repo root.
- ✅ **readme_has_install** (moderate): README contains one of ['install', 'installation', 'getting started', 'quickstart', 'quick start'].
- ✅ **readme_has_usage** (moderate): README contains one of ['usage', 'example', 'how to use', 'how it works', 'quickstart'].
- ✅ **readme_non_trivial_length** (cosmetic): README is 489 words.
- ✅ **license_present** (moderate): Found LICENSE at repo root.
- ✅ **tests_present** (moderate): Found tests/ directory with 56 test file(s).
- ✅ **ci_present** (moderate): Found .github/workflows/ with 14 workflow file(s).
- ✅ **package_manifest_present** (moderate): Found pyproject.toml.
- ❌ **adr_present** (cosmetic): No docs/decisions or adr/ directory. ADRs are a signal of senior engineering discipline.
- ❌ **examples_or_demo_present** (cosmetic): No examples/ or demo/ directory found.
- ✅ **gitignore_present** (cosmetic): Found .gitignore.
- ❌ **recent_activity** (cosmetic): Target is not a git repo; cannot check commit recency.

---

## Prose judge scores


### README.md — 28/50
- **thesis_clarity**: 4/5 — The opening immediately states "Datasette is a tool for exploring and publishing data" followed by a specific claim about what it helps people do - "take data of any shape or size and publish that as an interactive, explorable website and accompanying API." This is a clear, defensible thesis that frames the entire piece as a tool introduction. However, it's preceded by badges and branding elements, and the core claim comes in the second sentence rather than the very first.
- **problem_framing**: 1/5 — The piece jumps directly into describing what Datasette is and does without articulating the underlying problem it solves. While it mentions target users (data journalists, museum curators, etc.), it doesn't explain what's hard about data exploration and publishing that necessitates this tool. The reader must infer that existing solutions are inadequate for making data interactive and explorable.
- **specific_evidence**: 5/5 — The piece provides concrete examples throughout: specific installation commands ("brew install datasette"), exact file paths ("~/Library/Application\ Support/Google/Chrome/Default/History"), specific port numbers (8001), and real URLs (datasette.io, latest.datasette.io). It includes actual code snippets, JSON examples, and deployment commands for named platforms (Heroku, Google Cloud Run). This demonstrates insider knowledge with actionable specificity.
- **pedagogical_instinct**: 5/5 — The piece teaches multiple transferable techniques: how to serve databases locally, how to add metadata via JSON files, how to deploy to cloud platforms, and how to access browser history data. Each technique includes specific commands and examples that practitioners can directly apply to their own data projects. The Chrome history example is particularly instructive, showing a concrete use case with exact file paths.
- **methodology_disclosure**: 3/5 — This piece makes no measurement claims, performance benchmarks, or quantitative assertions that would require disclosure of methodology limits. It's a tool introduction and usage guide rather than an analytical piece with empirical claims. Following the rubric guidance, this should be scored as neutral.
- **integrative_reasoning**: 1/5 — The piece presents Datasette as a straightforward solution without acknowledging competing approaches or trade-offs. It doesn't identify tensions between different data publishing models or synthesize opposing viewpoints. The analysis is single-perspective, focusing only on Datasette's capabilities without considering alternative tools or approaches.
- **counterargument_handling**: 1/5 — The piece doesn't anticipate or address potential objections to using Datasette. It doesn't discuss limitations, performance concerns, security considerations, or scenarios where other tools might be preferable. The presentation is entirely positive without acknowledging counterarguments or edge cases where the tool might not be suitable.
- **structural_coherence**: 1/5 — The piece uses topic-label headings like "Installation," "Basic usage," "metadata.json," and "datasette publish" rather than argument-driven headings. These headings describe functional categories rather than making specific assertions. Reading only the headings gives a sense of topics covered but doesn't reconstruct any argument about why or when to use Datasette.
- **register_alignment**: 5/5 — The writing maintains a technical register throughout, focusing on specific commands, file formats, and implementation details. The language is measured and factual without marketing hyperbole - it describes Datasette as "a tool" rather than using superlatives like "revolutionary" or "cutting-edge." The tone is instructional and practical, appropriate for a technical audience.
- **conclusion_advances**: 2/5 — The piece ends with a brief mention of Datasette Lite, which introduces WebAssembly packaging as a browser-only option. However, this feels more like an additional feature mention rather than a novel synthesis or implication that advances beyond the main content. It doesn't reframe the overall argument or provide actionable next steps that couldn't have been stated earlier.

### docs/upgrade_guide.md — 30/50
- **thesis_clarity**: 2/5 — The piece opens with "This section reviews breaking changes Datasette 1.0 has when upgrading from a 0.XX version" - this is a clear statement of purpose but reads more like documentation scope than a defensible analytical claim. The opening is functional and direct but lacks the kind of specific, arguable thesis that would frame an analytical piece. It's more of a reference guide introduction than an opening that stakes out intellectual territory.
- **problem_framing**: 2/5 — The piece jumps directly into cataloging breaking changes without articulating why these changes were necessary or what problems they solve. While it mentions that metadata "became a kitchen sink" in one section, it doesn't establish upfront what was hard about the previous approach or why users should care about these changes beyond compliance. The reader has to infer the underlying problems from the solutions presented.
- **specific_evidence**: 5/5 — The piece provides extensive specific evidence including exact URL patterns ("/databasename?sql=select+1"), specific version numbers ("1.0a14", "1.0a25"), concrete code examples, and precise command-line syntax. It names specific tools like "datasette-upgrade plugin" and provides direct links to external resources. The level of technical specificity consistently signals insider knowledge throughout.
- **pedagogical_instinct**: 4/5 — The piece teaches multiple transferable techniques: how to split configuration files, how to use the datasette-upgrade plugin, how to migrate from old to new API patterns, and how to handle CSRF protection changes. Each section provides concrete steps and code examples that practitioners can directly apply. The upgrade patterns and migration strategies are generalizable beyond just Datasette.
- **methodology_disclosure**: 3/5 — This piece makes no measurement claims, performance comparisons, or quantitative assertions that would require methodology disclosure. It's purely a technical migration guide documenting API changes and upgrade procedures. Since no measurements are presented, this criterion should be scored as neutral.
- **integrative_reasoning**: 2/5 — The piece presents changes in a binary fashion - old way versus new way - without exploring tensions between different approaches or synthesizing competing models. While it mentions that some changes "aren't breaking changes" due to redirects, it doesn't engage with deeper tensions between backward compatibility and clean architecture, or between different security models.
- **counterargument_handling**: 3/5 — The piece acknowledges some potential objections, particularly around backward compatibility (noting that SQL query URL changes "isn't a breaking change" due to redirects), and explains the rationale behind CSRF changes. However, it doesn't deeply engage with the strongest objections users might have to these changes, such as migration complexity or the removal of familiar patterns.
- **structural_coherence**: 2/5 — The headings are mostly topic labels like "Metadata changes," "New URL for SQL queries," and "CSRF protection is now header-based." While these are more specific than generic labels like "Background," they describe what changed rather than making argumentative assertions. Reading the headings alone gives a sense of what topics are covered but doesn't reconstruct a coherent argument about why these changes matter.
- **register_alignment**: 5/5 — The piece maintains a consistently technical register throughout, using precise terminology, code examples, and technical specifications without marketing language. There are no hype adjectives, revolutionary claims, or overclaiming. The tone is measured and documentation-focused, appropriate for a technical upgrade guide.
- **conclusion_advances**: 2/5 — The piece ends with technical details about security properties and SameSite cookies, which provides additional context but doesn't advance beyond the information already presented in the body. There's no novel synthesis, broader implications, or actionable next steps that couldn't have been stated earlier. It reads more like completing the technical specification than offering new insights.

### docs/upgrade-1.0a20.md — 38/50
- **thesis_clarity**: 5/5 — The opening immediately states "Datasette 1.0a20 makes some breaking changes to Datasette's permission system. Plugins need to be updated if they use any of the following:" followed by a specific bulleted list. This is a clear, specific claim that frames the entire piece as an upgrade guide. The thesis is defensible and actionable, telling readers exactly what they need to know upfront.
- **problem_framing**: 2/5 — The piece jumps directly into the solution (how to upgrade plugins) without articulating what's hard about the upgrade process or why the breaking changes were necessary. While it names that there are "breaking changes," it doesn't explain what makes this upgrade challenging or why a naive approach might fail. The reader has to infer the complexity from the detailed examples.
- **specific_evidence**: 5/5 — The piece consistently provides concrete code examples, specific method names like "register_permissions()", "datasette.allowed()", and exact API patterns. It includes direct links to documentation and shows before/after code comparisons with specific parameter names and class imports. The evidence is detailed enough to signal deep practitioner knowledge of the Datasette ecosystem.
- **pedagogical_instinct**: 5/5 — The piece teaches multiple transferable techniques: how to migrate from old to new permission systems, how to update test patterns, and how to handle async function conversions. Each section provides concrete before/after code examples that practitioners can directly apply to their own plugins. The patterns shown (like the httpx.AsyncClient migration) are generalizable beyond just Datasette.
- **methodology_disclosure**: 3/5 — This piece makes no measurement claims, performance comparisons, or quantitative assertions that would require methodology disclosure. It's purely a technical migration guide focused on API changes and code patterns. Since no measurements are presented, this criterion should be scored as neutral.
- **integrative_reasoning**: 2/5 — The piece presents a single perspective: how to upgrade from old APIs to new ones. It doesn't identify competing approaches or hold different models in tension. While it shows the contrast between old and new patterns, it doesn't synthesize or resolve any genuine conceptual tensions - it simply advocates for the new approach.
- **counterargument_handling**: 2/5 — The piece doesn't anticipate or address potential objections to the upgrade process. It doesn't acknowledge scenarios where developers might want to maintain backward compatibility, discuss the costs of migration, or address concerns about breaking existing workflows. The final section briefly mentions avoiding "brittle workarounds" but doesn't steelman the case for maintaining compatibility.
- **structural_coherence**: 5/5 — The headings function as clear assertions that reconstruct the argument: "Permissions are now actions," "permission_allowed() hook is replaced by permission_resources_sql()," "Root user checks are no longer necessary." Reading only the headings tells the complete story of what needs to be changed. Each heading makes a specific claim about the migration process rather than just labeling topics.
- **register_alignment**: 5/5 — The piece maintains a consistently technical register throughout, using precise API terminology and avoiding marketing language. There are no hype adjectives or overclaims - it simply states what has changed and how to adapt. The tone is matter-of-fact and focused on practical implementation details rather than selling the benefits of the new system.
- **conclusion_advances**: 4/5 — The conclusion section "Target the new APIs exclusively" provides a novel strategic recommendation that couldn't have been stated at the outset: avoid trying to maintain compatibility with both old and new systems. This is an actionable insight that emerges from understanding all the migration details presented in the body. It advances beyond mere summary to offer strategic guidance.

### docs/events.md — 20/50
- **thesis_clarity**: 2/5 — The opening immediately states "Datasette includes a mechanism for tracking events that occur while the software is running" which is a clear, specific claim about what the piece will document. However, this reads more like documentation than analytical writing - it's describing a feature rather than making a defensible analytical claim that frames an argument.
- **problem_framing**: 1/5 — The piece jumps directly into describing the events mechanism without articulating what problem this solves or why event tracking is needed. There's no discussion of what's hard about the problem or why a naive approach would fail - it simply documents the existing solution.
- **specific_evidence**: 4/5 — The piece provides specific technical details like the plugin hook name "plugin_hook_track_event" and references to specific classes and modules. It includes concrete code references and links to related documentation, demonstrating insider knowledge of the Datasette system.
- **pedagogical_instinct**: 1/5 — This is pure documentation that describes what exists rather than teaching transferable techniques. A reader learns about Datasette's event system but gains no extractable patterns or techniques they could apply to other systems or problems.
- **methodology_disclosure**: 3/5 — The piece makes no measurement claims, performance assertions, or quantitative statements that would require methodology disclosure. It's purely descriptive documentation of an existing feature.
- **integrative_reasoning**: 1/5 — The piece presents a single perspective on how Datasette's event system works without acknowledging alternative approaches or holding competing models in tension. It's straightforward documentation without analytical complexity.
- **counterargument_handling**: 1/5 — There's no acknowledgment of limitations, alternative approaches, or potential objections to the event system design. The piece presents the feature as-is without addressing why someone might question this approach.
- **structural_coherence**: 1/5 — The piece has only one heading "Events" which is a topic label rather than an argument. Reading the heading alone provides no insight into the argument or claims being made - it simply identifies the subject matter.
- **register_alignment**: 5/5 — The writing maintains a technical, documentation-style register throughout. There are no marketing adjectives, hype language, or overclaims - it simply describes the technical functionality in measured terms appropriate for developer documentation.
- **conclusion_advances**: 1/5 — The piece has no conclusion section and ends abruptly with a code reference. There's no synthesis, implications, or next steps - it simply stops after describing the technical details.

---

## Code judge scores


### datasette/database.py — 23/30
- **naming_clarity**: 5/5 — The code demonstrates excellent naming clarity throughout. Class names like `Database`, `WriteTask`, `QueryInterrupted`, and `DatasetteClosedError` clearly communicate their purpose. Method names are descriptive verbs that reveal intent: `execute_write`, `table_exists`, `foreign_keys_for_table`, `_cleanup_temp_file`. Instance variables like `is_mutable`, `is_memory`, `cached_table_counts` use clear, domain-appropriate vocabulary. Even internal variables like `_write_thread`, `_all_file_connections` follow consistent naming patterns that make their purpose obvious.
- **readability_structure**: 4/5 — The code structure is well-organized with clear separation of concerns. The Database class is substantial but each method has a single, clear responsibility. Methods like `connect()`, `execute()`, and `close()` follow a logical flow that's easy to follow. However, some methods are quite long (e.g., `_execute_writes` at ~50 lines, `hidden_table_names` with complex SQL queries) and mix abstraction levels. The `__init__` method handles multiple initialization patterns which adds some complexity, but overall the file maintains good readability.
- **architectural_fit**: 4/5 — The code shows good architectural design with clear separation between read and write operations, proper resource management, and well-defined interfaces. The Database class encapsulates SQLite connection management effectively, hiding complex threading and connection pooling behind simple async methods. The use of composition (WriteTask, Results classes) and proper dependency injection (ds parameter) demonstrates good modular design. However, the Database class is quite large and handles multiple concerns (connection management, query execution, metadata inspection), which slightly violates single responsibility principle.
- **documentation_quality**: 2/5 — The code has minimal documentation. The `close()` method has a good docstring explaining its behavior and idempotent nature, and `DatasetteClosedError` has a clear docstring. However, most methods lack docstrings entirely, including complex async methods like `execute_write_fn` and `_send_to_write_thread`. There are no type hints throughout the codebase. Comments are sparse and mostly explain implementation details rather than the why behind decisions. For a complex database abstraction layer, this level of documentation is insufficient.
- **error_handling**: 5/5 — The code demonstrates excellent error handling practices. It uses specific exception types like `DatasetteClosedError` and `QueryInterrupted` rather than generic exceptions. The `_check_not_closed()` method ensures operations fail fast when called on closed databases. Exception handling in `_execute_writes()` properly catches and propagates errors while logging them. The code handles SQLite-specific errors like "interrupted" queries and converts them to domain-specific exceptions. Connection cleanup is handled robustly with try/except blocks that don't silently swallow errors.
- **testability**: 3/5 — The code shows mixed testability characteristics. Dependencies are injected (the `ds` parameter), and many methods are pure functions that would be easy to test. The separation of read and write operations, and the use of connection factories make testing feasible. However, the heavy use of threading, global state (`connections` thread-local), and complex async patterns would require significant mocking for comprehensive testing. Methods like `_execute_writes()` mix I/O with business logic, making them harder to test in isolation. The public API is well-defined but some internal complexity leaks through.

### datasette/cli.py — 24/30
- **naming_clarity**: 5/5 — The code demonstrates excellent naming clarity throughout. Function names like `run_sync`, `check_databases`, `sqlite_extensions`, and `create_token` clearly communicate their purpose. Variable names are descriptive and domain-appropriate (e.g., `inspect_data`, `metadata_data`, `sqlite_extensions`, `uvicorn_kwargs`). The CLI command structure uses clear, action-oriented names that match the domain vocabulary of a data publishing tool.
- **readability_structure**: 4/5 — The file is well-structured with clear separation between utility functions, CLI command definitions, and helper functions. Each CLI command function has a single responsibility and maintains consistent abstraction levels. The code flows logically from imports to utility functions to command definitions. However, the `serve` function is quite long (around 100+ lines) and handles multiple concerns, which slightly impacts readability despite being well-organized internally.
- **architectural_fit**: 4/5 — The code exhibits good architectural boundaries with clear separation of concerns. CLI commands are properly separated from business logic, with the actual Datasette functionality imported from other modules. The use of Click decorators creates clean interfaces for command-line interaction. Dependencies are properly injected through function parameters rather than hardcoded. The module serves as a clean interface layer between the CLI and the core Datasette functionality.
- **documentation_quality**: 3/5 — The code has comprehensive docstrings for all CLI commands that clearly explain their purpose and usage, including examples for complex commands like `create_token`. The main CLI group has a helpful description with links to documentation. However, utility functions like `run_sync` and `check_databases` lack docstrings, and there are no type hints throughout the code, which limits the documentation quality.
- **error_handling**: 5/5 — The code demonstrates excellent error handling with specific exception types and meaningful error messages. It catches specific exceptions like `SpatialiteNotFound`, `StartupError`, and `ConnectionProblem` and converts them to appropriate `ClickException`s with helpful messages. The code validates inputs (e.g., checking for Docker installation, validating file paths) and provides clear guidance when errors occur, such as suggesting the `--load-extension=spatialite` option for SpatiaLite issues.
- **testability**: 3/5 — The code shows mixed testability characteristics. While dependencies are generally injected through function parameters and the CLI commands are well-separated, there are several challenges for testing. Many functions have side effects like file I/O, subprocess calls, and web browser opening. The `serve` function has a `return_instance` parameter specifically for testing, which is a good design choice. However, functions like `package` directly call external processes and `serve` has many environmental dependencies that would require extensive mocking.

### datasette/utils/multipart.py — 28/30
- **naming_clarity**: 5/5 — The code demonstrates excellent naming clarity throughout. Class names like `MultipartParser`, `UploadedFile`, and `FormData` clearly communicate their purpose. Method names are descriptive verbs that reveal intent: `parse_content_disposition`, `_ensure_disk_space`, `_process_preamble`. Constants follow clear naming patterns with `DEFAULT_` prefixes and descriptive suffixes like `MAX_FILE_SIZE`, `MAX_MEMORY_FILE_SIZE`. Variable names are consistently meaningful: `boundary`, `content_type`, `current_part_size`, avoiding generic names like `data` or `temp`.
- **readability_structure**: 5/5 — The code exhibits excellent structure with clear separation of concerns. The `MultipartParser` class uses a state machine pattern with well-defined states (`STATE_PREAMBLE`, `STATE_HEADER`, `STATE_BODY`) and corresponding processing methods. Functions are appropriately sized and focused on single responsibilities - `_process_preamble()`, `_process_header()`, `_process_body()` each handle one parsing phase. The main `parse_form_data()` function clearly branches between URL-encoded and multipart handling. Control flow uses early returns and avoids deep nesting, making the logic easy to follow top-to-bottom.
- **architectural_fit**: 5/5 — The module demonstrates strong architectural design with clear separation of concerns. The `UploadedFile`, `FormData`, and `MultipartParser` classes each have distinct, well-defined responsibilities. The parser implements a deep module pattern - complex multipart parsing logic is hidden behind a simple `parse_form_data()` interface. Dependencies flow in one direction, and the streaming parser design allows processing large requests without loading everything into memory. The module boundary is clean with a focused public API centered around the main `parse_form_data()` function.
- **documentation_quality**: 4/5 — The code has comprehensive documentation with detailed module-level docstring explaining capabilities and a well-documented `UploadedFile` class with clear attribute descriptions. The main `parse_form_data()` function has excellent documentation covering all parameters, return values, and supported formats. However, many internal methods like `_process_preamble()`, `_process_header()`, and `_process_body()` lack docstrings explaining their specific roles in the state machine. Type hints are complete and accurate throughout, enhancing the documentation quality.
- **error_handling**: 5/5 — The code demonstrates excellent error handling with specific exceptions and comprehensive validation. It defines a custom `MultipartParseError` exception and uses it consistently for various failure modes like "Request body too large", "Too many parts", "Missing boundary in Content-Type". Input validation occurs at system boundaries with checks for file sizes, field counts, disk space, and malformed headers. The code fails fast with descriptive error messages and includes defensive programming like the `__del__` method in `UploadedFile` with exception handling for cleanup failures.
- **testability**: 4/5 — The code exhibits strong testability with dependency injection and isolated side effects. The `MultipartParser` constructor accepts all configuration parameters, making it easy to test with different limits. The main `parse_form_data()` function takes a `receive` callable as a parameter, enabling easy mocking of ASGI input. File I/O is isolated to specific methods like `_ensure_disk_space()` and uses `tempfile` for predictable behavior. However, some methods like `_write_body_data()` mix parsing logic with I/O operations, and the parser maintains significant internal state that could complicate testing of individual methods.

### datasette/facets.py — 21/30
- **naming_clarity**: 5/5 — The code demonstrates excellent naming clarity throughout. Function names like `load_facet_configs`, `register_facet_classes`, and `facet_results` clearly communicate their purpose. Class names like `ColumnFacet`, `ArrayFacet`, and `DateFacet` follow a consistent pattern and reveal their domain purpose. Variable names are descriptive (`facet_configs`, `suggested_facets`, `facet_results_values`) and the code uses domain-specific vocabulary consistently (facet, config, toggle_url).
- **readability_structure**: 3/5 — The code is well-structured with clear separation between the utility function, hook implementation, and class hierarchy. Each method has a single clear responsibility, and the inheritance structure is logical with the base `Facet` class defining the interface. However, some methods like `facet_results` in the concrete classes are quite long (50+ lines) and mix multiple concerns like SQL generation, execution, and result formatting. The nesting levels are generally manageable, though some conditional blocks could be flattened.
- **architectural_fit**: 4/5 — The code exhibits good architectural design with a clear base class `Facet` that defines the interface and concrete implementations for different facet types. The separation of concerns is evident with `load_facet_configs` as a standalone utility function and the hook implementation separate from the core classes. Dependencies are properly injected through the constructor (ds, request, database, etc.), and each facet type encapsulates its specific logic while sharing common functionality through inheritance.
- **documentation_quality**: 2/5 — The code has minimal documentation with only one substantial comment block in `load_facet_configs` explaining the return format. Most methods lack docstrings entirely, making it difficult to understand their contracts without reading the implementation. There are no type hints present, and the few comments that exist (like "TODO" comments) are more about implementation notes than explaining the why behind decisions. The comment in `load_facet_configs` is helpful but insufficient for the entire module.
- **error_handling**: 4/5 — The code demonstrates good error handling practices with specific exception catching (`QueryInterrupted`, `sqlite3.OperationalError`, `ValueError`). Rather than failing silently, the code continues gracefully when queries time out or fail, adding items to `facets_timed_out` lists or using `continue` statements in suggestion loops. Input validation is present with assertions like `assert table or sql` and type checking in `_is_json_array_of_strings`. The code avoids bare except clauses and handles edge cases like invalid JSON or missing configurations appropriately.
- **testability**: 3/5 — The code is reasonably testable with dependencies injected through the constructor rather than hardcoded. The `Facet` base class accepts all necessary dependencies (ds, request, database) as parameters, making it possible to mock these for testing. However, the concrete implementations mix database I/O with business logic extensively, making unit testing challenging without database setup. Methods like `suggest` and `facet_results` perform complex SQL operations that would be difficult to test in isolation. The `load_facet_configs` utility function is more testable as it primarily processes data structures.

### datasette/utils/actions_sql.py — 20/30
- **naming_clarity**: 4/5 — Function names like `build_allowed_resources_sql`, `check_permission_for_resource`, and `build_permission_rules_sql` clearly communicate their purpose and return types. Variable names are descriptive and domain-specific: `permission_sqls`, `restriction_sqls`, `anon_is_allowed`, `any_deny`, `any_allow`. The consistent use of snake_case and meaningful prefixes like `anon_` for anonymous-related variables shows good naming conventions. However, some abbreviations like `ar`, `cl`, `pl`, `gl` in SQL aliases could be more descriptive, though they're used in limited SQL scope.
- **readability_structure**: 2/5 — The module has clear top-to-bottom flow with comprehensive docstring explaining the overall pattern, followed by well-structured functions. The main function `build_allowed_resources_sql` handles the complex case of combining actions, while `_build_single_action_sql` contains the core logic in a readable helper. However, `_build_single_action_sql` is quite long (200+ lines) and mixes multiple concerns like building CTEs, handling anonymous permissions, and constructing the final query. The deeply nested conditional logic for cascading permissions and the large query construction make it challenging to follow without backtracking.
- **architectural_fit**: 4/5 — The module demonstrates good separation of concerns with distinct functions for different aspects: building allowed resources, building permission rules, and checking individual resources. The interface is clean with well-defined parameters and return types. Dependencies are properly injected (datasette instance) rather than accessed globally. The module follows single responsibility at the top level - it's focused solely on SQL query building for hierarchical permissions. The helper function `_build_single_action_sql` appropriately hides complex implementation details behind a simple interface.
- **documentation_quality**: 5/5 — The module-level docstring excellently explains the overall pattern, core concepts, and cascading logic with concrete examples. Function docstrings are comprehensive, explaining parameters, return values, and providing usage examples like in `build_allowed_resources_sql`. Type hints are complete and accurate throughout, using proper typing constructs like `dict | None` and `TYPE_CHECKING` imports. Comments within the complex SQL building logic explain the WHY behind cascading permission decisions and priority ordering, not just the WHAT.
- **error_handling**: 3/5 — The code includes explicit validation with specific error messages like `raise ValueError(f"Unknown action: {action}")` when actions don't exist. It handles edge cases like empty permission rules by returning appropriate empty results rather than failing silently. The code properly handles the `SKIP_PERMISSION_CHECKS` sentinel value and gracefully deals with missing or None values throughout. However, there's limited input validation on parameters like `parent` and `child`, and some database operations could potentially fail without explicit handling.
- **testability**: 2/5 — Functions accept dependencies as parameters (datasette instance) rather than accessing globals, making them testable. The separation between `build_allowed_resources_sql` and `_build_single_action_sql` allows testing the core logic independently. However, the functions are heavily dependent on the datasette instance and database operations, requiring significant mocking to test effectively. The complex SQL generation logic is intertwined with I/O operations, making it difficult to test the query building logic in isolation from database execution.