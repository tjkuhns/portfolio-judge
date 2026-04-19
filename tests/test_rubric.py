"""Tests for core.rubric — loading, validation, score math."""

from __future__ import annotations

import textwrap
from pathlib import Path

import pytest
from pydantic import ValidationError

from portfolio_judge.core.rubric import (
    Criterion,
    CriterionScore,
    DraftScore,
    Rubric,
    load_rubric,
)


@pytest.fixture
def minimal_rubric_yaml() -> str:
    return textwrap.dedent(
        """
        id: test_rubric
        version: "0.1"
        description: Test rubric for unit tests.
        criteria:
          - id: a
            name: Criterion A
            what_it_measures: Tests thing A.
            scale:
              1: bad A
              3: ok A
              5: great A
          - id: b
            name: Criterion B
            what_it_measures: Tests thing B.
            weight: 1.5
            scale:
              1: bad B
              3: ok B
              5: great B
        scoring_guidance:
          weighted_criteria:
            a: 2.0  # explicit scoring_guidance entry
        """
    ).strip()


def test_rubric_loads_and_validates(tmp_path: Path, minimal_rubric_yaml: str) -> None:
    p = tmp_path / "r.yaml"
    p.write_text(minimal_rubric_yaml)
    r = load_rubric(p)
    assert r.id == "test_rubric"
    assert r.version == "0.1"
    assert len(r.criteria) == 2
    assert r.criterion_ids == ["a", "b"]


def test_criterion_weights_prefer_explicit_on_criterion(tmp_path: Path, minimal_rubric_yaml: str) -> None:
    """When a criterion defines its own weight, it wins over scoring_guidance."""
    p = tmp_path / "r.yaml"
    p.write_text(minimal_rubric_yaml)
    r = load_rubric(p)
    # b has explicit weight=1.5 on the criterion
    # a has weight=2.0 via scoring_guidance.weighted_criteria
    assert r.weights == {"a": 2.0, "b": 1.5}


def test_rubric_rejects_missing_scale_anchors() -> None:
    with pytest.raises(ValidationError):
        Criterion(
            id="x",
            name="x",
            what_it_measures="x",
            scale={1: "bad", 5: "good"},  # missing 3
        )


def test_rubric_rejects_missing_criteria() -> None:
    with pytest.raises(ValidationError):
        Rubric(id="x", criteria=[])


def test_draft_score_unweighted() -> None:
    ds = DraftScore(
        source="a.md",
        rubric_id="r",
        rubric_version="0.1",
        criterion_scores=[
            CriterionScore("a", 3, "ok"),
            CriterionScore("b", 5, "great"),
        ],
    )
    assert ds.total_unweighted() == 8


def test_draft_score_weighted() -> None:
    ds = DraftScore(
        source="a.md",
        rubric_id="r",
        rubric_version="0.1",
        criterion_scores=[
            CriterionScore("a", 3, "ok"),
            CriterionScore("b", 5, "great"),
        ],
    )
    weights = {"a": 1.0, "b": 1.5}
    # 3*1.0 + 5*1.5 = 3 + 7.5 = 10.5
    assert ds.total_weighted(weights) == pytest.approx(10.5)


def test_draft_score_veto() -> None:
    ds = DraftScore(
        source="a.md",
        rubric_id="r",
        rubric_version="0.1",
        criterion_scores=[
            CriterionScore("a", 1, "fail"),
            CriterionScore("b", 4, "good"),
        ],
    )
    assert ds.vetoed_criteria() == ["a"]


def test_load_rubric_missing_file(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        load_rubric(tmp_path / "nope.yaml")


def test_shipped_default_rubrics_load() -> None:
    """The shipped default prose + code rubrics must be valid."""
    from portfolio_judge.judges.code import default_rubric_path as code_rp
    from portfolio_judge.judges.prose import default_rubric_path as prose_rp

    prose = load_rubric(prose_rp())
    code = load_rubric(code_rp())

    assert len(prose.criteria) == 10
    assert len(code.criteria) == 6
    # Both define weights
    assert "thesis_clarity" in prose.weights
    assert "naming_clarity" in code.weights
