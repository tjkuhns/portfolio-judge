"""Code judge — rubric-driven LLM-as-judge for Python code quality.

Thin wrapper over core.scorer. The default rubric (rubrics/code_default.yaml)
covers six subjective dimensions linters can't catch: naming, readability,
architectural fit, documentation, error handling, testability. Grounded in
Clean Code (Martin), A Philosophy of Software Design (Ousterhout),
PEP 8/257, Google Python Style Guide.

The code judge methodology was transferred in an afternoon from the
calibrated essay judge (ρ = 0.841 against a 7-model editorial panel) as
an ablation demonstration. It has NOT been independently calibrated
against human reviewers — community feedback is the calibration
mechanism this release is soliciting.

Proposed upstream to Braintrust autoevals as Issue #185:
https://github.com/braintrustdata/autoevals/issues/185
"""

from __future__ import annotations

from importlib import resources
from pathlib import Path

from portfolio_judge.core.llm import Provider
from portfolio_judge.core.rubric import DraftScore, Rubric, load_rubric
from portfolio_judge.core.scorer import score_artifact


CODE_INSTRUCTIONS = """You are grading Python source code. Grade the code \
itself — readability, structure, documentation, error handling, testability — \
not the problem it solves. Do not penalize the code for being short (a clean \
50-line module can score 5 on every criterion) or for being domain-specific. \
Cite specific line numbers or identifiers when reasoning."""


def default_rubric_path() -> Path:
    """Path to the shipped default code rubric."""
    from_pkg = _try_package_rubric("code_default.yaml")
    if from_pkg is not None:
        return from_pkg
    here = Path(__file__).resolve()
    repo_root = here.parents[3]
    return repo_root / "rubrics" / "code_default.yaml"


def _try_package_rubric(filename: str) -> Path | None:
    try:
        ref = resources.files("portfolio_judge.rubrics").joinpath(filename)
        with resources.as_file(ref) as p:
            if p.exists():
                return p
    except (ModuleNotFoundError, FileNotFoundError):
        return None
    return None


async def review_code(
    source_code: str,
    source: str,
    rubric: Rubric | Path | str | None = None,
    model: str | None = None,
    provider: Provider | None = None,
) -> DraftScore:
    """Score a Python source file.

    Args:
        source_code: the full text of the .py file.
        source: identifier for reporting (usually the file path).
        rubric: pre-loaded Rubric, path to YAML, or None (uses default).
        model: model shortcut or ID; defaults to whichever provider has a key.
        provider: pre-built Provider (overrides model-string resolution).

    Returns a DraftScore.
    """
    resolved_rubric = _resolve_rubric(rubric)
    return await score_artifact(
        artifact_text=source_code,
        rubric=resolved_rubric,
        source=source,
        artifact_label="code",
        custom_instructions=CODE_INSTRUCTIONS,
        model=model,
        provider=provider,
    )


def _resolve_rubric(rubric: Rubric | Path | str | None) -> Rubric:
    if isinstance(rubric, Rubric):
        return rubric
    if rubric is None:
        return load_rubric(default_rubric_path())
    return load_rubric(rubric)
