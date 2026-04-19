# Portfolio review: https://github.com/eugeneyan/applied-ml

**Role:** Applied AI Engineer / Agentic Engineering
**Model:** claude-sonnet-4-20250514

---

## Synthesis

## Convergent verdict
**UNANIMOUS REJECT** — All four reviewers identified this as a curated resource list, not an engineering portfolio demonstrating Applied AI capability.

## Convergent strengths
- **Professional technical register**: All reviewers noted clean, technical writing without marketing fluff (recruiter: "register_alignment: 5/5", applied_ai_hm: "register_alignment: 5/5", fde_solutions_hm: "register_alignment: 5/5")
- **Domain knowledge breadth**: Multiple reviewers acknowledged comprehensive ML domain coverage (recruiter: "spans relevant production ML domains", applied_ai_hm: "extensive domain knowledge", devrel_hm: "domain awareness")
- **Organizational capability**: Three reviewers praised systematic categorization (recruiter: "clear taxonomy", fde_solutions_hm: "systematic categorization suggests they can structure information clearly", devrel_hm: "organizational skills")

## Convergent gaps
- **Zero engineering artifacts**: All four reviewers flagged complete absence of code, tests, CI, or production systems (recruiter: "no code, no systems, no implementations", applied_ai_hm: "zero engineering artifacts", fde_solutions_hm: "no tests, no CI, no package manifest", devrel_hm: "no tests, no CI, no package manifest")
- **Fundamental role mismatch**: Every reviewer noted the candidate misunderstood what Applied AI Engineering requires (recruiter: "fundamentally misunderstands what Applied AI Engineer roles require", applied_ai_hm: "misunderstanding of what the role requires", fde_solutions_hm: "mismatch between role requirements and demonstrated capability")
- **No problem-solving demonstration**: Multiple reviewers cited inability to frame or solve technical problems (applied_ai_hm: "no problem-solving demonstration", fde_solutions_hm: "no evidence of building anything", devrel_hm: "not evidence of teaching ability, technical depth")

## Role-fit ranking
**Bad fit across all evaluated roles** — Recruiter, Applied AI HM, and FDE HM all rated as bad fit; DevRel HM rejected due to genre mismatch. No reviewer found a suitable role match.

## Probability estimate
**Bottom 5th percentile** — Applied AI HM and recruiter both placed this in "bottom 5%" of inbound for engineering roles, with recruiter noting it would be "immediately archived in any engineering pipeline."

## Top 3 actionable next steps
1. **Build and ship a complete AI system** — Create an end-to-end implementation with evals, error analysis, and production deployment artifacts. Include tests, CI, and clear installation instructions.

2. **Document your engineering process** — Write about debugging decisions, architectural tradeoffs, and measurement methodology from building actual systems. Show problem-solving, not just problem awareness.

3. **Pick one domain and go deep** — Instead of surveying all ML areas, demonstrate expertise in a specific application (e.g., recommendation systems) with multiple implementations, comparative analysis, and novel insights.

---

## Per-reviewer verdicts


### Reviewer: recruiter

## 60-second first-pass verdict
**ARCHIVE** — This is a curated resource list, not a portfolio demonstrating applied AI engineering capability.

## What I saw in the first minute
Pattern-matched immediately to "awesome list" or bibliography, not an engineering portfolio. The README is 6,642 words of curated links to other people's work, organized by ML domain (classification, recommendation, etc.). No evidence of the candidate building, shipping, or evaluating AI systems. The title "applied-ml" and description as "curated papers, articles, and blogs" made it clear this is content curation, not engineering work.

## Second-pass findings
### Signal
- **Domain knowledge breadth**: The curation spans relevant production ML domains and includes reputable sources (Uber, Netflix, etc.)
- **Professional register**: Technical language without marketing fluff (register_alignment: 5/5)
- **Comprehensive organization**: Clear taxonomy across 11+ ML application areas

### Concerns
- **Zero engineering artifacts**: No code, no systems, no implementations
- **Missing all production signals**: No tests, no CI, no package manifest, no install instructions
- **Not a git repo**: Can't assess commit history or development process
- **Curation ≠ capability**: Knowing about ML papers doesn't demonstrate ability to build ML systems
- **No methodology disclosure**: Even for curation, no explanation of selection criteria or quality filters

## Overclaim audit
- Claim I clicked through on: "applied ML" in title vs. content being a reading list
- Result: Misleading. "Applied" suggests implementation/engineering work, but this is purely bibliographic

## Role fit ranking
1. **Bad fit: Applied AI Engineer** — Zero evidence of building, evaluating, or shipping AI systems
2. **Bad fit: Forward Deployed Engineer** — No customer-facing engineering work shown
3. **Stretch: DevRel** — Could indicate domain knowledge for content creation, but lacks the writing/tutorial creation that DevRel requires

## Comparable bench
Bottom 5% of inbound for Applied AI roles. This would be immediately archived in any engineering pipeline. For DevRel roles, maybe bottom 25% — shows domain awareness but no content creation or technical communication skills.

## Would I forward to the hiring manager?
**No.** This portfolio fundamentally misunderstands what Applied AI Engineer roles require. The grounding document is explicit: we need "end-to-end production shape, not notebook" and "direct evidence of ability over credentials." A curated reading list provides neither. The structural scan confirms zero engineering discipline markers (no tests, CI, package management, recent commits). The prose judge gave it 22/50, noting it "doesn't frame a problem" and has "no thesis to challenge."

For an Applied AI Engineer role, I need to see evals, error analysis, production deployment artifacts, and systematic methodology. This candidate has demonstrated research skills and domain awareness, but hasn't shown they can build, debug, or ship AI systems.

## What I'd want to see in a cover note
If this person contacted me, I'd need them to explain: "I know this looks like just a reading list, but here's the AI system I actually built: [link]. The applied-ml repo demonstrates my research process for understanding production ML patterns before implementing [specific system] with [specific results]." Without that bridge to actual engineering work, this is a non-starter for technical roles.

### Reviewer: applied_ai_hm

## Decision
**REJECT**

## One-line rationale
This is a curated resource list, not a portfolio demonstrating Applied AI Engineering capability — no code, no evals, no production systems built.

## Technical depth assessment
### What impressed me
- Extensive domain knowledge evidenced by comprehensive resource curation across ML production domains
- Professional technical register without marketing fluff (register_alignment: 5/5)
- Substantial effort investment (6642-word README shows commitment to the space)

### What concerned me
- **Zero engineering artifacts**: No code, tests, CI, or package manifest. This is documentation, not engineering work
- **No measurement methodology**: README judge scored 3/5 on methodology_disclosure only because "no measurement claims to evaluate" — that's the problem
- **Missing all production signals**: No tests/ directory, no CI config, no .gitignore, no recent git activity
- **Thesis clarity failure**: README judge scored 1/5 — "no specific, defensible claim" beyond being a resource collection
- **No problem-solving demonstration**: README judge scored 1/5 on problem_framing — "doesn't frame a problem at all"

### What I'd probe in interview
This wouldn't reach interview. If it did: "Walk me through a production ML system you've built, measured, and debugged."

## Methodology rigor score: 1/10
No methodology present. This is a bibliography, not empirical work with measurement claims.

## Code quality score: 1/10
No code artifacts to evaluate. Cannot assess engineering competence from a curated list.

## Architectural judgment score: 1/10
No architecture decisions demonstrated. Resource organization ≠ system design judgment.

## Disclosure / honesty score: 8/10
No overclaiming detected — the candidate accurately presents this as a resource collection, not original engineering work. However, submitting this for an Applied AI Engineer role suggests misunderstanding of what the role requires.

## Role-seniority band
**Not applicable** — This portfolio provides no evidence of hands-on engineering capability at any level. A junior engineer needs to show code; a senior engineer needs to show systems and measurement.

## Comparable bench
**Bottom 5th percentile** among inbound for Applied AI Engineer roles. Most rejected candidates at least attempt to show code or a demo.

## Recommendation to head of engineering
Hard pass. This candidate has domain knowledge and curation skills, but submitted a reading list for an engineering role. Per our grounding heuristics, this hits multiple red flags: "API call in a trench coat" (actually worse — no API calls at all), "unfinished/undocumented repos" (no repo engineering artifacts), and fundamentally misunderstands what Applied AI Engineering entails. 

The structural scan found zero engineering discipline markers: no tests, no CI, no package manifest, no recent commits. The README judge confirmed this isn't even attempting to solve a technical problem (1/5 on problem_framing and thesis_clarity).

This might be a strong DevRel candidate if they had accompanying technical work, but for Applied AI Engineer, they need to reapply with actual systems they've built and measured.

### Reviewer: fde_solutions_hm

## Decision
**REJECT**

## Role-fit verdict
**Bad fit — this is a curated resource list, not evidence of applied AI engineering capability**

## Technical writing quality
Score **3/10**. While the writing is clear and professional (register_alignment: 5/5), it demonstrates no technical depth or original thinking. The README is essentially a well-organized bibliography with no thesis, problem-framing, or pedagogical instinct (scores of 1/5 each). For an FDE role requiring customer-facing technical communication, this shows organization skills but zero evidence of explaining complex systems or translating technical decisions for stakeholders.

## Pedagogical instinct
Score **2/10**. The structural scan reveals this is purely a resource aggregation with no teaching capability. The prose judge noted it "points to other resources that do [the teaching]" rather than teaching concepts directly. An FDE needs to explain AI systems to customers, not just curate links.

## Implementation discipline
Score **1/10**. Catastrophic gaps across all production signals: no tests, no CI, no package manifest, no recent commits (not even a git repo), no examples/demo directory, no .gitignore. The structural findings show this person has never shipped production code. This is disqualifying for any engineering role.

## Customer-facing clarity
Score **2/10**. The writing is organized but shows no evidence of translating technical concepts for business stakeholders. A curated list doesn't demonstrate the ability to sit with a VP and explain why a particular ML approach matters for their use case.

## Honesty / disclosure quality
Score **3/10** (neutral). No measurement claims to evaluate, but the framing as "applied ML" when it's actually just link curation borders on misrepresentation. The title suggests hands-on engineering experience that isn't evidenced.

## What would surprise me in a customer call
**Impress**: Potentially broad knowledge of ML landscape from curation work.
**Trip them up**: Complete inability to discuss implementation details, debugging approaches, or production tradeoffs. No evidence they've built anything themselves.

## Strongest evidence of FDE potential
The only positive signal is organizational capability and professional writing register. The systematic categorization suggests they can structure information clearly, which is table stakes for customer communication.

## Biggest gap
**Zero evidence of building anything**. This portfolio shows research/curation skills but no engineering, no production experience, no customer-facing work, no debugging narratives, no technical decision-making. The structural scan reveals someone who has never shipped code to production.

## Recommendation
**Strong reject**. This candidate applied for "Applied AI Engineer / Agentic Engineering" but submitted a curated reading list. There's no evidence they can code, debug, deploy, or explain technical systems to customers. The complete absence of tests, CI, examples, or even basic git hygiene suggests they've never worked on production systems. 

For FDE roles requiring customer empathy and implementation discipline, this portfolio demonstrates neither. A customer would quickly discover this person can recommend papers but can't build, deploy, or troubleshoot AI systems. The mismatch between role requirements and demonstrated capability is too large to bridge in a hiring process.

### Reviewer: devrel_hm

## Decision
REJECT

## Role-fit verdict
Not a DevRel candidate — This is a resource curation project, not evidence of teaching ability, technical depth, or public engagement that DevRel requires.

## Teaching quality score: 2/10
The README scores 22/50 on prose quality with particularly weak thesis clarity (1/5) and pedagogical instinct (2/5). This is a curated bibliography, not a teaching artifact. The candidate points to other people's work rather than transferring techniques themselves. A DevRel hire needs to *create* educational content, not just organize existing content. The grounding emphasizes "learning exhaust" and runnable artifacts — this provides neither.

## Runnable artifact quality: 1/10
Critical failure: README missing installation instructions entirely (readme_has_install: ❌). No tests, no CI, no package manifest, no examples directory. This isn't a runnable tool — it's a static list. A developer couldn't "clone this and have it working in 5 min" because there's nothing to run. DevRel candidates must ship tools practitioners can actually use.

## Public posture score: 3/10
While the candidate has organized a substantial collection (6642-word README), there's no evidence of substantive public engagement. No visible commit history (not a git repo per structural scan), no community interaction patterns, no evidence of filing issues or contributing to other projects. The grounding specifically calls out "operating in the open" — this feels more like passive curation than active community participation.

## Genre fluency score: 5/10
The register alignment scores well (5/5) — technical terminology, no marketing fluff. However, the overall approach misses the DevRel genre entirely. Compare to Simon Willison's pattern: he builds tools, documents his learning process, and teaches transferable techniques. This candidate organizes other people's work without adding their own analytical layer or runnable demonstrations.

## Niche depth score: 2/10
Breadth-over-depth red flag from the grounding. The table of contents spans 11+ ML domains from data quality to NLP. No evidence of deep ownership in any specific area. DevRel careers reward "niche depth over breadth" — this is the opposite pattern.

## One piece of their work I'd embed in our docs
None. This is a link collection, not original educational content. Our docs need tutorials that teach techniques, not bibliographies that point elsewhere.

## Biggest gap for DevRel specifically
Fundamental genre mismatch. The candidate needs to demonstrate:
1. **Original teaching content** — write tutorials that transfer techniques, not just organize links
2. **Runnable artifacts** — build tools practitioners can clone and use immediately  
3. **Public learning process** — document their own debugging, experimentation, and discovery
4. **Niche expertise** — pick one domain and go deep rather than surveying everything

The grounding cites Hamel Husain's eval work and Simon Willison's tool-building as exemplars. This portfolio shows neither pattern.

## Recommendation
Pass. While the candidate demonstrates organizational skills and domain awareness, they haven't produced the core artifacts DevRel requires: original educational content and runnable tools. The structural scan reveals missing production basics (no tests, CI, install instructions), and the prose analysis shows this functions as a bibliography rather than teaching material. For DevRel, we need candidates who create educational experiences, not just curate existing ones. The candidate would need to build and document their own ML tools, write tutorials that teach transferable techniques, and demonstrate active community engagement before becoming a viable DevRel candidate.

---

## Structural findings

- ✅ **readme_present** (critical): Found README.md at repo root.
- ❌ **readme_has_install** (moderate): README missing section for ['install', 'installation', 'getting started', 'quickstart', 'quick start']; a README should tell the reader how to install / run the project.
- ✅ **readme_has_usage** (moderate): README contains one of ['usage', 'example', 'how to use', 'how it works', 'quickstart'].
- ✅ **readme_non_trivial_length** (cosmetic): README is 6642 words.
- ✅ **license_present** (moderate): Found LICENSE at repo root.
- ❌ **tests_present** (moderate): No tests/ directory or test_*.py files found. Production readiness is hard to read without tests.
- ❌ **ci_present** (moderate): No CI config found (.github/workflows, .gitlab-ci.yml, .circleci, tox, etc.).
- ❌ **package_manifest_present** (moderate): No package manifest (pyproject.toml, package.json, Cargo.toml, etc.).
- ❌ **adr_present** (cosmetic): No docs/decisions or adr/ directory. ADRs are a signal of senior engineering discipline.
- ❌ **examples_or_demo_present** (cosmetic): No examples/ or demo/ directory found.
- ❌ **gitignore_present** (cosmetic): No .gitignore — secrets / artifacts may be exposed.
- ❌ **recent_activity** (cosmetic): Target is not a git repo; cannot check commit recency.

---

## Prose judge scores


### README.md — 22/50
- **thesis_clarity**: 1/5 — The piece opens with a title and tagline describing it as "Curated papers, articles, and blogs on data science & machine learning in production" followed by badges and a brief description of what readers can learn. There is no specific, defensible claim in the opening - instead it's a repository description that explains what the collection contains and how it's organized. The opening reads more like documentation or a table of contents than an analytical argument with a clear thesis.
- **problem_framing**: 1/5 — This piece doesn't frame a problem at all - it's a curated list/repository of resources rather than an analytical piece that identifies and solves a problem. The brief description mentions "Figuring out how to implement your ML project?" but this is framed as a question the collection helps answer, not a problem the author is analyzing or solving. There's no articulation of what's hard about ML implementation or why existing approaches fail.
- **specific_evidence**: 5/5 — The piece provides extensive specific evidence in the form of named companies, specific years, direct links to papers and blog posts, and concrete examples across dozens of ML applications. Each entry includes the company name, publication year, and often links to both blog posts and academic papers. For example, entries like "Monitoring Data Quality at Scale with Statistical Modeling" from Uber 2017 with direct links demonstrate insider knowledge of the field and provide actionable resources.
- **pedagogical_instinct**: 2/5 — While the piece provides extensive resources that practitioners could use, it functions more as a curated bibliography than a teaching document. The brief introductory text mentions learning "how the problem is framed," "what techniques worked," and "why it works," but the piece itself doesn't teach these concepts - it points to other resources that do. A practitioner would need to read the linked materials to extract transferable techniques, rather than learning them directly from this piece.
- **methodology_disclosure**: 3/5 — This piece makes no measurement claims, experimental results, or quantitative assertions that would require methodology disclosure. It's a curated list of resources rather than a research or analysis piece with empirical findings. Since there are no measurement claims to evaluate, this should be scored as neutral per the rubric instructions.
- **integrative_reasoning**: 1/5 — The piece doesn't engage in analytical reasoning or hold opposing models in tension. It's organized as a categorized list of resources across different ML domains (classification, recommendation, search, etc.) without synthesizing different approaches or identifying tensions between competing methodologies. Each section simply lists relevant papers and blog posts without comparative analysis or integration of different perspectives.
- **counterargument_handling**: 1/5 — As a curated resource list, this piece doesn't present arguments that would generate objections or counterarguments. There's no thesis to challenge or methodology to critique. The piece doesn't acknowledge potential limitations of the curation approach, alternative ways to organize ML resources, or address why someone might prefer a different type of resource collection.
- **structural_coherence**: 2/5 — The headings are clear topic labels that organize the content effectively (Data Quality, Data Engineering, Classification, etc.) but they don't function as a standalone argument. Reading just the headings tells you what domains are covered but doesn't reconstruct any analytical argument or thesis. The structure serves as a taxonomy for organizing resources rather than building a coherent argument.
- **register_alignment**: 5/5 — The piece maintains a technical register throughout, using domain-specific terminology and focusing on practical ML applications without marketing language. The tone is straightforward and professional, with phrases like "machine learning in production" and technical domain names. There are no hype adjectives, overclaiming, or marketing voice - it reads like a professional resource compilation for practitioners.
- **conclusion_advances**: 1/5 — The piece has no conclusion section and doesn't advance beyond its initial premise. It ends with the last category (Fails) and final resource entry without synthesis, implications, or next steps. Since it's structured as a resource list rather than an analytical argument, there's no argumentative progression that would culminate in novel insights or actionable recommendations.