# Portfolio review: [phase2 sample 02 — URL anonymized]

**Role:** Applied AI Engineer / Agentic Engineering
**Model:** claude-sonnet-4-20250514

---

## Synthesis

## Convergent verdict
Strong technical depth in agentic RAG with measured evaluation, but critical gaps in testing discipline and customer communication prevent advancement.

## Convergent strengths
**Technical architecture sophistication**: All four reviewers praised the LangGraph state machine implementation with proper separation of concerns (recruiter: "genuine agentic behavior beyond API wrapper," applied_ai_hm: "real understanding of agentic patterns," fde_solutions_hm: "solid technical execution," devrel_hm: "strong technical implementation").

**Measured evaluation methodology**: Three reviewers specifically highlighted the RAGAs evaluation with concrete metrics (recruiter: "measured eval results...not vibes-driven," applied_ai_hm: "actual RAGAs evaluation harness," fde_solutions_hm: "actual evaluation metrics rather than vibes-based claims").

**Production-shaped API design**: Multiple reviewers noted the FastAPI implementation quality (recruiter: "proper error handling," applied_ai_hm: "excellent FastAPI implementation," fde_solutions_hm: "28/30 code score").

**Hybrid retrieval sophistication**: Applied_ai_hm and recruiter both called out the BM25+FAISS fusion with RRF as showing "depth beyond basic vector search" and "production-grade retrieval thinking."

## Convergent gaps
**Complete absence of tests**: All four reviewers flagged this as a major concern (recruiter: "major red flag," applied_ai_hm: "concerning gaps in testing," fde_solutions_hm: "no tests directory found," devrel_hm: "missing tests...hurt discoverability").

**Customer communication deficits**: Three reviewers noted poor problem framing and business value articulation (recruiter: "missing customer-facing documentation," fde_solutions_hm: "fails the customer communication test," devrel_hm: "reads like project documentation rather than teaching material").

**Limited evaluation rigor**: Three reviewers questioned the 5-question test set size and lack of confidence intervals (recruiter: "quite small for confidence," applied_ai_hm: "could be more robust," fde_solutions_hm: "lacks confidence intervals").

**Missing basic hygiene**: Three reviewers noted the absent LICENSE file (recruiter, applied_ai_hm, fde_solutions_hm all flagged this).

## Role-fit ranking
1. **Best fit: Applied AI Engineer** — All reviewers agreed this shows the technical depth needed, despite testing gaps
2. **Bad fit: Forward Deployed Engineer** — fde_solutions_hm gave definitive reject due to customer communication failures
3. **Bad fit: DevRel** — devrel_hm rejected due to complete absence of public teaching and community engagement

## Probability estimate
**75th percentile** for Applied AI Engineer roles (consensus between recruiter and applied_ai_hm), but would be much lower percentile for customer-facing roles due to communication gaps.

## Top 3 actionable next steps
1. **Add comprehensive test suite** — Write unit tests for the LangGraph state machine, integration tests for the hybrid retrieval pipeline, and end-to-end API tests. This was the #1 gap flagged by all reviewers and blocks "production-grade" credibility.

2. **Expand evaluation dataset and add confidence intervals** — Scale beyond 5 questions, include statistical significance testing, and document what would invalidate the results. This addresses the methodology rigor concerns raised by three reviewers.

3. **Rewrite README with problem-first framing** — Start with customer pain points that basic RAG fails to solve, then explain why agentic approaches matter, before diving into technical implementation. This addresses the customer communication gap that killed the FDE fit.

---

## Per-reviewer verdicts


### Reviewer: recruiter

## 60-second first-pass verdict
**ADVANCE** — Strong technical depth with measured eval results and production-grade architecture, though missing some foundational elements.

## What I saw in the first minute
Pattern-matched immediately on "agentic decision loop using LangGraph" with specific version numbers (0.4), RAGAs evaluation scores (Faithfulness 0.91, Answer Relevancy 0.88), and production signals (FastAPI, Docker, CI). The README leads with concrete technical claims rather than marketing fluff. Confused by the missing LICENSE and tests directory despite "production-grade" claims. Would Google "LangGraph agentic RAG" to verify if this is genuinely differentiated or just framework following.

## Second-pass findings
### Signal
- **Measured evaluation methodology**: RAGAs scores with specific thresholds (faithfulness > 0.70) and CI integration, not vibes-driven assessment
- **Architectural sophistication**: LangGraph state machine with clear decision nodes (route_query, grade_documents, rewrite_query) showing genuine agentic behavior beyond API wrapper
- **Production-shaped code**: FastAPI with proper error handling (HTTPExceptions), structured logging, health endpoints, and Docker deployment
- **Hybrid retrieval implementation**: BM25+FAISS with RRF fusion and cross-encoder reranking shows depth beyond basic vector search
- **Clean separation of concerns**: API layer delegates to domain modules (app.agent, vectorstore.store), not monolithic notebook code

### Concerns
- **Missing tests**: No test files despite "production-grade" claims — major red flag for reliability assessment
- **No LICENSE**: Blocks OSS adoption, basic oversight for public repo
- **Limited eval dataset**: 5-question test set is quite small for confidence in the metrics
- **Hardcoded dependencies**: File paths and constants scattered through modules reduce configurability

## Overclaim audit
- Claim I clicked through on: "Production-grade" — **Partial support**. Has FastAPI, Docker, CI, proper error handling, but missing tests and license undermines the claim
- Claim I clicked through on: "Full agentic decision loop" — **Strong support**. The LangGraph state machine with routing, grading, and rewriting shows genuine decision-making beyond simple RAG
- Claim I clicked through on: RAGAs scores — **Verified**. Actual evaluation code present with specific metrics and CI integration

## Role fit ranking
1. **Best fit: Applied AI Engineer** — Strong eval methodology, architectural depth with LangGraph, measured results with disclosed limits. The agentic RAG implementation shows the systematic approach to complex AI systems that this role requires.
2. **Stretch: Forward Deployed Engineer** — Has production deployment pieces but limited customer-facing documentation. Would need stronger narrative around business value and tradeoff communication.
3. **Bad fit: DevRel** — No public writing, limited pedagogical content in README, missing the community engagement signals essential for developer relations.

## Comparable bench
Approximately **75th percentile** of inbound I see for these roles. The combination of measured evaluation, architectural sophistication, and production deployment puts this well above typical "LLM wrapper" submissions, but missing tests and limited eval dataset prevent top-tier placement.

## Would I forward to the hiring manager?
**Yes with reservations** — This candidate demonstrates genuine technical depth in agentic AI systems with proper evaluation methodology, which is rare in our pipeline. The LangGraph implementation shows understanding of complex state machines beyond basic RAG, and the RAGAs integration with CI shows production thinking. However, I'd flag the missing tests as a significant concern for a "production-grade" claim and note the small evaluation dataset. The code quality is strong enough (API design, error handling, architectural boundaries) that a hiring manager should see this, but they'll need to probe on testing practices and evaluation rigor in the interview.

## What I'd want to see in a cover note
If this person contacted me cold, I'd want them to lead with: "Built an agentic RAG system with LangGraph that achieved 0.91 faithfulness on RAGAs evaluation, with hybrid retrieval and corrective query rewriting." Then explain one specific technical decision (like why RRF fusion over simple concatenation) and mention they have CI-integrated evaluation. Skip the "production-grade" marketing language and focus on the measured results and architectural choices that differentiate this from basic RAG implementations.

### Reviewer: applied_ai_hm

## Decision
**ADVANCE TO PHONE SCREEN**

## One-line rationale
Strong architectural judgment with LangGraph state machine, hybrid retrieval with RRF fusion, and RAGAs evaluation pipeline — but concerning gaps in testing and error handling need probing.

## Technical depth assessment
### What impressed me
- **app/agent.py** — Clean LangGraph state machine implementation with proper separation of concerns. The ASCII art flow diagram and node-based architecture shows real understanding of agentic patterns beyond simple API wrappers.
- **vectorstore/store.py** — Sophisticated hybrid retrieval with BM25+FAISS fusion using Reciprocal Rank Fusion. The two-stage retrieve-then-rerank pattern with cross-encoder shows production-grade retrieval thinking.
- **evaluation/evaluate.py** — Actual RAGAs evaluation harness with specific metrics (Faithfulness 0.91, Answer Relevancy 0.88). Uses proper evaluation dataset structure and measures what matters for RAG quality.
- **app/api.py** — Excellent FastAPI implementation with proper error handling, clean separation between HTTP and domain logic, comprehensive docstrings.

### What concerned me
- **No tests directory found** — Production claims with zero visible test coverage. The structural scan shows no test files whatsoever, which is a major red flag for "production-grade" claims.
- **Error handling gaps** — While api.py handles errors well, core modules like agent.py and store.py have minimal error handling. No validation of LLM responses, FAISS operations, or external service failures.
- **Missing license** — OSS adoption claims without explicit licensing. Basic hygiene issue.
- **Hardcoded dependencies** — Global variables in agent.py, hardcoded paths in store.py reduce modularity and testability.

### What I'd probe in interview
- Walk me through how you'd test the LangGraph state machine — what would you mock, what would you integration test?
- Your RAGAs eval shows 5-question test set. How did you validate this was representative? What failure modes did you discover?
- The hybrid retrieval uses RRF fusion — did you ablate this against simpler approaches? What was the measured improvement?

## Methodology rigor score: 7/10
RAGAs evaluation with specific metrics and thresholds shows real measurement discipline. However, 5-question test set is quite small, and no confidence intervals or ablation studies are disclosed. The evaluation methodology is present but could be more robust.

## Code quality score: 6/10
API layer and core algorithms are well-structured with good naming and documentation. However, the complete absence of tests, minimal error handling in core modules, and some architectural coupling (global variables, hardcoded paths) prevent a higher score.

## Architectural judgment score: 8/10
Excellent separation of concerns with LangGraph for orchestration, hybrid retrieval strategy, and clean API boundaries. The choice to use state machines for agentic behavior shows sophisticated thinking beyond simple RAG. Minor deductions for some coupling issues.

## Disclosure / honesty score: 8/10
Claims are generally backed by code — the "agentic decision loop" is actually implemented, hybrid retrieval is real, RAGAs scores are measured. The "production-grade" claim is somewhat overstated given the testing gaps, but core technical claims hold up.

## Role-seniority band
**Mid-level** — Shows strong architectural thinking and can implement sophisticated RAG patterns, but gaps in testing discipline and production hardening suggest not quite senior-level engineering maturity.

## Comparable bench
Approximately **75th percentile** among inbound for this role type.

## Recommendation to head of engineering
This candidate demonstrates real depth in modern RAG architecture — they understand LangGraph state machines, hybrid retrieval patterns, and evaluation methodology. The code quality in core modules is solid with good separation of concerns. However, the complete absence of tests for a "production-grade" system is concerning, and error handling needs work. I'd advance to phone screen to probe their testing philosophy and production experience, but they show the technical depth we need for complex RAG systems. The architectural judgment alone puts them in the top quartile of candidates.

### Reviewer: fde_solutions_hm

## Decision
**REJECT**

## Role-fit verdict
**Bad fit — lacks customer-facing communication skills and production discipline**

## Technical writing quality
Score **4/10**. The README shows technical competence but fails the customer communication test. The opening is marketing fluff ("Production-grade," "state-of-the-art") rather than clear problem framing. Most critically, it jumps straight into solution details without explaining what's insufficient about basic RAG or why customers would care about agentic approaches. A customer reading this would get lost in the technical jargon without understanding the business value.

## Pedagogical instinct
Score **5/10**. Mixed signals here. The architecture diagram and specific implementation details (hybrid retrieval, RRF fusion, 2-stage reranking) show some teaching instinct. However, the prose judge flagged that techniques are "presented more as implementation details than as generalizable patterns with clear applicability guidance." The writing performs expertise rather than genuinely teaching transferable concepts.

## Implementation discipline
Score **6/10**. Solid technical execution with proper FastAPI structure, comprehensive error handling in the API layer (28/30 code score), and RAGAs evaluation pipeline. However, critical gaps: no tests directory found, no license, minimal error handling in core components like vectorstore (20/30), and heavy coupling to global variables that would make debugging difficult in production.

## Customer-facing clarity
Score **3/10**. This is the biggest red flag for FDE work. The README methodology disclosure scored only 3/5 — evaluation claims lack confidence intervals, sample size beyond "5-question test set," and don't explain what would invalidate results. A customer asking "how do I know this will work for my data?" wouldn't get a satisfying answer. The writing assumes technical sophistication that most customers don't have.

## Honesty / disclosure quality
Score **4/10**. The candidate provides specific RAGAs scores (Faithfulness 0.91, Answer Relevancy 0.88) but with minimal context about limitations. The prose judge noted "lacks confidence intervals, sample size details beyond '5-question test set,' and doesn't disclose what would invalidate these results." This reads more like marketing metrics than genuine technical disclosure.

## What would surprise me in a customer call
**Impress:** Deep technical knowledge of RAG architectures, specific experience with hybrid retrieval and reranking, actual evaluation metrics rather than vibes-based claims.

**Trip them up:** Explaining why a customer should care about "agentic" vs. basic RAG, handling questions about cost implications of multiple LLM calls, debugging live system failures (no evidence they've dealt with production issues), translating technical architecture into business value.

## Strongest evidence of FDE potential
The FastAPI implementation (app/api.py, 28/30) shows excellent architectural boundaries and comprehensive error handling. The candidate can build production-grade APIs with proper separation of concerns. The RAGAs evaluation pipeline demonstrates measurement discipline beyond "it works well."

## Biggest gap
**Customer empathy and communication clarity.** The prose judge scored problem framing at only 2/5 — "jumps directly into describing the solution without articulating what's hard about the problem or why naive approaches fail." For FDE work, you need to start with customer pain, not technical architecture. The writing style would alienate non-technical stakeholders who need to understand and trust the system.

## Recommendation
**Reject for FDE/Solutions roles.** This candidate has solid technical chops but lacks the customer-facing communication skills essential for Forward Deployed work. The writing performs technical expertise rather than explaining value to business stakeholders. Consider for a backend Applied AI Engineer role instead, where the technical depth would be better utilized and the customer communication gaps less critical. The implementation discipline is there, but the translation capability between technical and business contexts is missing.

### Reviewer: devrel_hm

## Decision
REJECT

## Role-fit verdict
Not a DevRel candidate — This is a solid Applied AI Engineer portfolio with strong technical implementation, but it lacks the core DevRel competencies: public teaching, community engagement, and learning-in-public artifacts.

## Teaching quality score: 3/10
The README is technically competent but reads like project documentation rather than teaching material. The prose judge scored it 28/50, noting it "jumps directly into describing the solution without articulating what's hard about the problem or why naive approaches fail." A DevRel candidate would frame this as "Here's what I learned building agentic RAG" with failure modes, debugging narratives, and transferable insights. Instead, this presents a finished system without the learning journey.

## Runnable artifact quality: 7/10
Strong technical execution with proper FastAPI backend (28/30 code score), Docker deployment, and CI pipeline. The structural scan shows comprehensive setup with requirements.txt and workflows. However, missing tests and examples directories hurt discoverability for practitioners wanting to learn from the code.

## Public posture score: 2/10
Zero evidence of operating in the open. No blog posts, OSS contributions, community engagement, or learning-in-public artifacts. The structural scan shows "Target is not a git repo; cannot check commit recency" — suggesting this might be a snapshot rather than an active public project. DevRel requires consistent public presence.

## Genre fluency score: 4/10
The writing contains marketing language flagged by the prose judge: "Production-grade," "state-of-the-art multilingual embeddings," and promotional badge displays. This sounds like vendor documentation rather than the Husain/Shankar/Willison tradition of honest technical writing with disclosed limits and negative results.

## Niche depth score: 6/10
Shows solid depth in agentic RAG architecture with LangGraph, hybrid retrieval, and RAGAs evaluation. The technical implementation demonstrates real expertise. However, there's no evidence of thought leadership or unique perspective that would make this person a go-to voice in the space.

## One piece of their work I'd embed in our docs
The `app/agent.py` state machine implementation (22/30 code score) with its clear ASCII art diagram and well-structured LangGraph nodes. This is the most pedagogically valuable artifact, showing how to structure complex agentic workflows.

## Biggest gap for DevRel specifically
Complete absence of teaching artifacts and public engagement. This candidate needs to start writing about their learning process, filing issues on tools they use, contributing to OSS projects, and building a public presence around their agentic RAG expertise. The technical foundation is solid, but DevRel is about community and teaching, not just building.

## Recommendation
Pass. This is a strong Applied AI Engineer candidate with solid technical chops in agentic RAG systems, proper evaluation methodology (RAGAs scores: Faithfulness 0.91, Answer Relevancy 0.88), and production-ready architecture. However, they lack the core DevRel competencies: no public writing, no community engagement, no learning-in-public artifacts, and documentation that reads like project specs rather than teaching material. The grounding heuristics are clear: DevRel requires "writing that documents the learning curve in public" and "evidence of operating in the open." This portfolio shows neither. Recommend they build a blog, start contributing to OSS, and reframe their technical work as teaching narratives before considering DevRel roles.

---

## Structural findings

- ✅ **readme_present** (critical): Found README.md at repo root.
- ✅ **readme_has_install** (moderate): README contains one of ['install', 'installation', 'getting started', 'quickstart', 'quick start'].
- ✅ **readme_has_usage** (moderate): README contains one of ['usage', 'example', 'how to use', 'how it works', 'quickstart'].
- ✅ **readme_non_trivial_length** (cosmetic): README is 1157 words.
- ❌ **license_present** (moderate): No LICENSE / LICENSE.md / COPYING at repo root. OSS adoption requires an explicit license.
- ❌ **tests_present** (moderate): No tests/ directory or test_*.py files found. Production readiness is hard to read without tests.
- ✅ **ci_present** (moderate): Found .github/workflows/ with 1 workflow file(s).
- ✅ **package_manifest_present** (moderate): Found requirements.txt.
- ❌ **adr_present** (cosmetic): No docs/decisions or adr/ directory. ADRs are a signal of senior engineering discipline.
- ❌ **examples_or_demo_present** (cosmetic): No examples/ or demo/ directory found.
- ✅ **gitignore_present** (cosmetic): Found .gitignore.
- ❌ **recent_activity** (cosmetic): Target is not a git repo; cannot check commit recency.

---

## Prose judge scores


### README.md — 28/50
- **thesis_clarity**: 4/5 — The opening immediately presents a specific, defensible claim: "This project goes beyond a basic RAG chatbot. It implements a **full agentic decision loop** using LangGraph — the system reasons about what to do with each query rather than blindly retrieving and generating." This frames the entire piece around the distinction between basic RAG and agentic RAG with decision-making capabilities. The claim is specific and defensible, appearing in the first substantive paragraph after the brief overview.
- **problem_framing**: 2/5 — The piece jumps directly into describing the solution (agentic RAG system) without articulating what's hard about the problem or why naive approaches fail. While it mentions going "beyond a basic RAG chatbot," it doesn't explain what's insufficient about basic RAG or what specific challenges motivated the agentic approach. The reader has to infer that basic RAG systems have limitations around query handling and retrieval quality.
- **specific_evidence**: 5/5 — The piece consistently deploys named tools (LangGraph 0.4, BAAI/bge-m3, FAISS, BM25, ms-marco-MiniLM), specific numbers (RAGAs scores: Faithfulness 0.91, Answer Relevancy 0.88), and concrete implementation details (retrieve top-20 candidates, rerank to top-5, up to 2 retries). The tech stack table and evaluation results provide specific version numbers and quantified metrics that signal insider knowledge without over-explaining.
- **pedagogical_instinct**: 4/5 — The piece teaches multiple transferable techniques: hybrid retrieval with RRF fusion, 2-stage retrieval with cross-encoder reranking, Corrective RAG with query rewriting, and web search fallback patterns. The architecture diagram and detailed tech stack provide concrete patterns a practitioner could apply to their own RAG systems. However, the techniques are presented more as implementation details than as generalizable patterns with clear applicability guidance.
- **methodology_disclosure**: 3/5 — The piece makes specific measurement claims (RAGAs scores) and provides the evaluation context: "Evaluated on a 5-question test set using RAGAs metrics" with a CI quality gate threshold of "faithfulness drops below 0.70." However, it lacks confidence intervals, sample size details beyond "5-question test set," and doesn't disclose what would invalidate these results or what wasn't measured in the evaluation.
- **integrative_reasoning**: 2/5 — The piece presents a single-perspective analysis focused on the agentic RAG approach without acknowledging alternative models or trade-offs. It doesn't identify competing approaches (e.g., fine-tuning vs. RAG, simple vs. complex retrieval) or synthesize tensions between different design choices. The analysis treats the chosen architecture as straightforwardly superior without exploring genuine trade-offs.
- **counterargument_handling**: 1/5 — The piece doesn't anticipate or address potential objections to the agentic approach, such as increased complexity, latency concerns, or cost implications of multiple LLM calls. It presents the system's capabilities without acknowledging limitations or addressing why someone might prefer simpler alternatives. No alternative views or potential criticisms are acknowledged.
- **structural_coherence**: 2/5 — The headings are mostly topic labels ("Overview," "Architecture," "Tech Stack," "Getting Started") rather than argument-bearing assertions. While some headings like "RAGAs Evaluation Results" hint at content, reading only the headings doesn't reconstruct the core argument about why agentic RAG is superior to basic RAG. The structure describes containers rather than making specific claims.
- **register_alignment**: 3/5 — The piece maintains a technical register with specific tool names, version numbers, and implementation details. However, it contains marketing language like "Production-grade," "state-of-the-art multilingual embeddings," and promotional phrases in the badges and descriptions. The opening tagline uses marketing superlatives that detract from the otherwise technical presentation.
- **conclusion_advances**: 2/5 — The piece ends with a roadmap section that lists future enhancements but doesn't provide a conclusion that advances beyond the content presented. There's no novel synthesis, actionable next steps for readers, or reframing that couldn't have been stated at the outset. The roadmap is essentially a feature wishlist rather than analytical advancement.

---

## Code judge scores


### app/agent.py — 22/30
- **naming_clarity**: 5/5 — The code demonstrates excellent naming clarity throughout. Function names like `route_query`, `grade_documents`, `rewrite_query`, and `web_search` clearly describe their purpose and contract. Variable names are descriptive (`rewrite_count`, `web_results`, `relevant`) and domain-specific vocabulary is consistent (using RAG terminology like "retrieve", "grade", "generate"). The only minor weakness is the use of single-letter variables in comprehensions (like `c` and `r`), but these are in tight scopes where the context is clear.
- **readability_structure**: 5/5 — The file has excellent top-to-bottom readability with clear logical sections separated by ASCII art comments. Each function operates at a consistent abstraction level - node functions handle state transformations, routing functions make decisions, and the main `ask` function provides a clean public interface. Control flow is straightforward with minimal nesting (mostly 1-2 levels), and functions are appropriately sized with single responsibilities. The state machine flow is clearly documented at the top, making the overall architecture immediately comprehensible.
- **architectural_fit**: 4/5 — The code exhibits strong architectural boundaries with the LangGraph state machine pattern providing clear separation of concerns. Each node function has a single responsibility and operates on well-defined state, with dependencies flowing unidirectionally through the graph. The public interface is minimal (just the `ask` function) while hiding the complex state machine implementation. However, there's some coupling through shared global variables like `llm` and `web_search_tool`, and the `hybrid_search` import suggests external dependencies that could be better abstracted.
- **documentation_quality**: 3/5 — The module has excellent high-level documentation with a comprehensive ASCII art diagram explaining the state machine flow and decision points. The module docstring clearly explains the architecture and routing logic. However, individual functions lack docstrings explaining their contracts, parameters, and return values. Type hints are present and comprehensive using TypedDict for state management. Comments explain the WHY (like "prevent infinite loops") rather than restating code.
- **error_handling**: 2/5 — Error handling is minimal throughout the code. The routing logic has basic fallback behavior (defaulting to "llm_only" if "documents" not found), and there's a MAX_REWRITES constant to prevent infinite loops. However, there's no validation of environment variables, no handling of LLM API failures, no validation of the hybrid_search results, and no specific exception handling around external service calls. The code would likely fail silently or with generic exceptions if external dependencies fail.
- **testability**: 3/5 — The code has mixed testability characteristics. While most node functions are pure state transformations that would be easy to test, they depend on global variables (`llm`, `web_search_tool`) that would require mocking. The `hybrid_search` import is a hidden dependency that complicates testing. However, the state-based architecture makes it possible to test individual nodes by providing mock state objects. The public `ask` function has a clean interface but would require extensive mocking of the entire graph execution.

### vectorstore/store.py — 20/30
- **naming_clarity**: 5/5 — The code demonstrates excellent naming clarity throughout. Function names like `build_index`, `hybrid_search`, and `_load_index` clearly communicate their purpose. Variable names are descriptive and domain-appropriate: `dense_ids`, `sparse_ids`, `candidate_chunks`, `fused_ids`, and constants like `TOP_K_FETCH`, `RRF_K` are self-documenting. The consistent use of snake_case and meaningful abbreviations (RRF for Reciprocal Rank Fusion) makes the code highly readable without requiring implementation details.
- **readability_structure**: 5/5 — The file has excellent top-to-bottom flow with clear logical sections marked by comments (Build/persist, Load, Hybrid search). Functions are appropriately sized and focused on single responsibilities - `build_index` handles index creation, `_load_index` handles loading, and `hybrid_search` orchestrates the retrieval process. The hybrid search function follows a clear step-by-step structure with descriptive section comments, making the complex algorithm easy to follow. Control flow is linear with minimal nesting.
- **architectural_fit**: 3/5 — The module exhibits good separation of concerns with distinct functions for building, loading, and searching indexes. The private `_load_index` function properly encapsulates the complexity of loading multiple index components. However, there are some architectural concerns: the module has hardcoded paths and constants at the module level, and the `hybrid_search` function mixes high-level orchestration with detailed implementation steps. The tight coupling to specific file paths and the embeddings module reduces modularity.
- **documentation_quality**: 3/5 — The module has a comprehensive docstring explaining the hybrid retrieval approach and its benefits. The `build_index` function has a clear docstring explaining parameters and purpose. However, the critical `hybrid_search` function lacks a proper docstring despite its complexity, and the `_load_index` function has no documentation. Type hints are present and accurate throughout. Comments effectively explain the algorithm steps but some functions would benefit from more complete docstrings.
- **error_handling**: 2/5 — The code shows minimal error handling. The `_load_index` function properly raises `FileNotFoundError` with a descriptive message when the FAISS index is missing. However, there's no validation of input parameters (e.g., empty chunks list, invalid top_k values), no handling of potential failures in embedding operations, FAISS operations, or pickle loading/saving. The code assumes all operations will succeed and doesn't handle edge cases like empty search results or malformed metadata.
- **testability**: 2/5 — The code has significant testability issues due to tight coupling with external dependencies and file system operations. Functions like `build_index` and `hybrid_search` directly call external embedding functions and perform file I/O, making unit testing difficult without extensive mocking. The hardcoded paths and constants at module level further reduce testability. While the logic within `hybrid_search` could potentially be extracted into more testable components, the current design mixes pure computation with side effects throughout.

### app/main.py — 16/30
- **naming_clarity**: 2/5 — Variable names like `uploaded`, `resp`, `data`, `msg`, `m`, `s`, `k`, `v` are generic and don't reveal intent clearly. The `API_BASE` constant is well-named, and `st.session_state.messages` follows Streamlit conventions appropriately. Function-level names are absent since this is primarily a script, but the overall naming lacks the precision expected for higher scores.
- **readability_structure**: 3/5 — The code is well-organized with clear visual sections separated by comments (sidebar, chat history, input). The linear flow from top to bottom is easy to follow, with logical groupings of related functionality. However, the main input handling block (lines 67-102) is quite long and mixes multiple concerns including API calls, UI updates, and state management, preventing it from reaching the highest scores.
- **architectural_fit**: 3/5 — This is a UI script that appropriately separates concerns by calling a separate FastAPI backend rather than mixing business logic with presentation. The module has a single clear responsibility as a Streamlit frontend. However, the tight coupling to the specific API structure and the mixing of HTTP client logic with UI rendering within the same functions prevents clean separation of concerns.
- **documentation_quality**: 3/5 — The module has a comprehensive docstring explaining its purpose, how to run it, and dependencies. Inline comments effectively separate logical sections (sidebar, chat history, input). However, there are no function docstrings since this is primarily a script, and no type hints are present throughout the code, limiting the documentation quality.
- **error_handling**: 3/5 — The code handles HTTP connection errors specifically with `httpx.ConnectError` and provides user-friendly error messages. API errors are caught and displayed using `resp.status_code` checks and `resp.json().get("detail", resp.text)` for fallback error messages. However, there's no validation of uploaded file types beyond Streamlit's built-in filtering, and some potential edge cases like malformed JSON responses aren't explicitly handled.
- **testability**: 2/5 — The code is heavily dependent on Streamlit's global state (`st.session_state`) and UI components, making unit testing extremely difficult without extensive mocking. The `API_BASE` configuration is properly externalized via environment variables, which is good for testability. However, all logic is intertwined with Streamlit UI calls and HTTP requests, with no separation of pure computation from side effects.

### app/api.py — 28/30
- **naming_clarity**: 5/5 — The code demonstrates excellent naming clarity throughout. Function names like `health()`, `ingest()`, `query()`, and `metrics()` clearly communicate their purpose. Class names like `QueryRequest`, `SourceItem`, and `QueryResponse` follow consistent domain vocabulary. Constants like `DATA_DIR` and `METRICS_FILE` are descriptive, and variable names like `dest`, `chunks`, `metas`, and `latency` appropriately communicate their intent within their scopes.
- **readability_structure**: 5/5 — The file is exceptionally well-structured with clear visual separation using comment dividers (lines 32, 49, 66). Each function operates at a consistent abstraction level - route handlers focus on HTTP concerns while delegating domain logic to imported modules. Control flow is straightforward with early returns for error cases (lines 78-79, 105-109) and minimal nesting. The top-to-bottom organization flows logically from setup to schemas to routes.
- **architectural_fit**: 5/5 — The module exhibits excellent architectural boundaries by acting as a thin API layer that delegates to specialized modules (`app.agent`, `ingestion.ingest`, `vectorstore.store`). Each route handler has a single responsibility and the interfaces are clean - the API doesn't expose implementation details of the underlying RAG system. Dependencies flow in one direction from the API layer to domain modules, and the separation between HTTP concerns and business logic is well-maintained.
- **documentation_quality**: 4/5 — The module header provides comprehensive documentation explaining all endpoints and usage. Each route function has clear docstrings explaining its purpose and behavior (lines 69, 75, 95, 130). The Pydantic models serve as self-documenting schemas with clear field names. However, type hints could be more complete - some parameters like `req` in the query function could benefit from explicit typing, and the module lacks detailed parameter documentation in some docstrings.
- **error_handling**: 5/5 — Error handling is comprehensive and specific throughout the code. The ingest function validates file types (line 78) and catches exceptions with context (lines 87-88). The query function handles specific cases like missing index (lines 105-109) and general exceptions with logging (lines 110-113). All error cases raise appropriate HTTPExceptions with descriptive messages rather than silently failing. The code fails fast and provides clear feedback to API consumers.
- **testability**: 4/5 — The code demonstrates good testability principles with dependencies injected through imports rather than hardcoded. Route handlers are thin wrappers that delegate to pure functions in other modules, making the core logic easily testable. However, some global state exists (DATA_DIR, METRICS_FILE as module-level constants) and file I/O operations are mixed with business logic in the ingest function. The API design is clean and minimal, but testing would require some setup for file system interactions.

### evaluation/evaluate.py — 23/30
- **naming_clarity**: 5/5 — The code demonstrates excellent naming clarity throughout. Function names like `run_evaluation()` clearly describe their purpose, and variables like `questions`, `answers`, `contexts`, and `ground_truths` are descriptive and domain-appropriate. Constants like `EVAL_DATASET`, `SCORES_FILE`, and `RAGAS_LLM` use clear, consistent naming conventions. Even temporary variables like `q`, `gt`, and `ctx_texts` are appropriately abbreviated given their tight scope within the loop.
- **readability_structure**: 5/5 — The file has excellent top-to-bottom readability with clear logical sections separated by comments (lines 30-34, 38-39, 49-50). The main function `run_evaluation()` follows a linear flow without deep nesting, using straightforward loops and list comprehensions. The module-level setup (lines 30-40) is cleanly separated from the evaluation dataset (lines 49-65) and the main logic. Each section serves a single purpose and can be understood independently.
- **architectural_fit**: 4/5 — The module exhibits good separation of concerns with clear boundaries between configuration, data setup, and evaluation logic. Dependencies are properly imported and configured at the module level (lines 30-40), while the evaluation logic is contained in a single focused function. The code appropriately delegates to external libraries (RAGAs, datasets) rather than reimplementing evaluation logic. However, there's some coupling to the `app.agent.ask` function and file system paths that could be more configurable.
- **documentation_quality**: 4/5 — The module has excellent documentation with a comprehensive docstring explaining purpose, usage, and what each metric measures (lines 1-16). Inline comments effectively explain non-obvious decisions like why the LLM wrapper is needed (lines 30-32) and provide clear section headers. The code includes helpful guidance for users about extending the evaluation dataset (line 41). However, the main function lacks a docstring explaining its return value and behavior.
- **error_handling**: 2/5 — The code has minimal explicit error handling and relies heavily on external libraries to handle failures. There's no validation of the evaluation dataset structure, no handling of potential failures from the `ask()` function, and no error handling around file I/O operations (line 95). The code assumes that `result["sources"]` will always exist and be iterable (line 77), which could lead to runtime errors. While the code may work in the happy path, it doesn't fail gracefully on edge cases.
- **testability**: 3/5 — The code has mixed testability characteristics. The main evaluation logic is contained in a single function that could be tested, but it has several dependencies that would require mocking: the `ask()` function, file I/O operations, and the RAGAs evaluation framework. The evaluation dataset is hardcoded as a module-level constant, making it difficult to test with different inputs. However, the core logic is relatively straightforward and the function returns a clear result that could be asserted against.