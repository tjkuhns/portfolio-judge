"""Prose judge — rubric-driven LLM-as-judge for analytical technical writing.

Thin wrapper over core.scorer. The default rubric (rubrics/prose_default.yaml)
is generalized from Explodable's consulting-essay rubric, which calibrated
ρ = 0.841 against a 7-model editorial panel at the panel's own ceiling
(disclosed post-hoc outlier-drop limit — see
github.com/tjkuhns/explodable/blob/main/docs/eval-methodology.md).

The methodology is inherited. The generalized rubric has NOT been
independently re-calibrated; community dogfooding on specific verdicts
is the calibration mechanism this release is soliciting.
"""

from __future__ import annotations

from importlib import resources
from pathlib import Path

from portfolio_judge.core.llm import Provider
from portfolio_judge.core.rubric import DraftScore, Rubric, load_rubric
from portfolio_judge.core.scorer import score_artifact


PROSE_INSTRUCTIONS = """You are grading analytical technical writing — a blog \
post, architecture doc, or methodology writeup — produced as part of an AI \
engineering portfolio. Grade the prose itself, not the underlying technical \
work it describes. If the piece has no measurement claims, score \
methodology_disclosure as 3 (neutral) rather than penalizing its absence."""


def default_rubric_path() -> Path:
    """Path to the shipped default prose rubric."""
    # rubrics/ lives at the repo root (not inside the installable package).
    # For an installed package we need to ship the YAML via package-data;
    # for a src-checkout, resolve relative to the repo root.
    from_pkg = _try_package_rubric("prose_default.yaml")
    if from_pkg is not None:
        return from_pkg
    here = Path(__file__).resolve()
    # src/portfolio_judge/judges/prose.py → repo root is three parents up.
    repo_root = here.parents[3]
    return repo_root / "rubrics" / "prose_default.yaml"


def _try_package_rubric(filename: str) -> Path | None:
    try:
        ref = resources.files("portfolio_judge.rubrics").joinpath(filename)
        # resources.files returns a Traversable; cast to path for Rubric.load.
        with resources.as_file(ref) as p:
            if p.exists():
                return p
    except (ModuleNotFoundError, FileNotFoundError):
        return None
    return None


async def review_prose(
    text: str,
    source: str,
    rubric: Rubric | Path | str | None = None,
    model: str | None = None,
    provider: Provider | None = None,
) -> DraftScore:
    """Score a piece of analytical technical writing.

    Args:
        text: the full prose being evaluated.
        source: identifier for reporting (path, URL, or descriptive label).
        rubric: a pre-loaded Rubric, a path to a YAML file, or None (uses default).
        model: model shortcut or ID; defaults to whichever provider has a key set.
        provider: pre-built Provider (overrides model-string resolution).

    Returns a DraftScore with per-criterion scores and reasoning.
    """
    resolved_rubric = _resolve_rubric(rubric)
    return await score_artifact(
        artifact_text=text,
        rubric=resolved_rubric,
        source=source,
        artifact_label="writing",
        custom_instructions=PROSE_INSTRUCTIONS,
        model=model,
        provider=provider,
    )


def _resolve_rubric(rubric: Rubric | Path | str | None) -> Rubric:
    if isinstance(rubric, Rubric):
        return rubric
    if rubric is None:
        return load_rubric(default_rubric_path())
    return load_rubric(rubric)
