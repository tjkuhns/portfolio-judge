# Code review: judge.py
**Source:** /home/thoma/explodable/src/content_pipeline/eval/judge.py
**Rubric:** code_default v0.1.0
**Total (unweighted):** 30/30

### naming_clarity: 5/5
The code demonstrates excellent naming clarity throughout. Function names like `load_rubric`, `build_judge_prompt`, `spearman_rank_correlation`, and `calibrate` clearly communicate their purpose. Class names like `CriterionScore` and `DraftScore` are descriptive and domain-appropriate. Variable names are consistently meaningful (`draft_text`, `word_count`, `criterion_scores`) with appropriate length scaling - short names like `c` and `cid` are used only in tight loops or comprehensions where context is clear.

### readability_structure: 5/5
The module is exceptionally well-structured with clear logical sections marked by comments (Types, Rubric loading, Prompt builder, etc.). Functions maintain consistent abstraction levels - for example, `score_draft` orchestrates high-level operations while helper functions like `_extract_tool_use_scores` handle specific implementation details. Control flow is straightforward with minimal nesting, and the file reads top-to-bottom naturally. The module docstring provides excellent context and design rationale upfront.

### architectural_fit: 5/5
The code exhibits strong architectural design with clear module boundaries and single responsibilities. The separation between data classes (CriterionScore, DraftScore), utility functions (rubric loading), and core logic (scoring, calibration) creates clean interfaces. Dependencies flow in one direction, and each component can be understood independently. The design follows deep module principles - complex prompt building and Claude API interaction are hidden behind simple interfaces like `score_draft()`.

### documentation_quality: 5/5
The module has comprehensive documentation starting with an excellent docstring that explains the purpose, design choices, and calibration targets. All public functions have clear docstrings explaining contracts, parameters, and return values. Type hints are complete and accurate throughout. Comments explain design decisions (like the flat schema choice in `build_judge_tool_schema`) rather than restating code, focusing appropriately on the WHY.

### error_handling: 5/5
Error handling is thorough and explicit throughout the code. The `load_rubric` function validates required keys and raises specific ValueError with context. The `_extract_tool_use_scores` function handles missing tool_use blocks with descriptive error messages. Input validation occurs at system boundaries (checking for missing criteria in line 234-238). The `spearman_rank_correlation` function validates input lengths and handles edge cases explicitly. Exceptions are specific and carry meaningful context.

### testability: 5/5
The code is highly testable with excellent separation of concerns. Pure functions like `spearman_rank_correlation` and `rubric_weights` have no side effects. Dependencies are injected (rubric_path, model parameters) rather than hardcoded. The Claude client is lazily initialized in `_claude_client()` making it easy to mock. Side effects are isolated in boundary functions like `score_draft` which clearly handles I/O, while core logic functions remain pure. The public API is minimal and well-defined.
