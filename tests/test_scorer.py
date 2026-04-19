"""Tests for core.scorer — prompt building, schema, score extraction.

No live LLM calls; the Provider is mocked.
"""

from __future__ import annotations

from typing import Any

import pytest

from portfolio_judge.core.llm import Provider
from portfolio_judge.core.rubric import Rubric
from portfolio_judge.core.scorer import (
    build_judge_prompt,
    build_judge_tool_schema,
    score_artifact,
)


def _minimal_rubric() -> Rubric:
    return Rubric(
        id="t",
        version="0.1",
        criteria=[
            {
                "id": "a",
                "name": "A",
                "what_it_measures": "tests a",
                "scale": {1: "bad", 3: "ok", 5: "good"},
            },
            {
                "id": "b",
                "name": "B",
                "what_it_measures": "tests b",
                "scale": {1: "bad", 3: "ok", 5: "good"},
            },
        ],
    )


def test_tool_schema_has_flat_parallel_primitive_fields() -> None:
    schema = build_judge_tool_schema(_minimal_rubric())
    assert schema["type"] == "object"
    # Flat: one reasoning + one score per criterion, all at top level
    props = schema["properties"]
    assert set(props.keys()) == {
        "a__reasoning",
        "a__score",
        "b__reasoning",
        "b__score",
    }
    assert props["a__score"]["type"] == "integer"
    assert props["a__score"]["minimum"] == 1
    assert props["a__score"]["maximum"] == 5
    assert props["a__reasoning"]["type"] == "string"
    # All fields required
    assert set(schema["required"]) == set(props.keys())


def test_prompt_contains_criteria_and_instruction() -> None:
    system, user = build_judge_prompt("Some artifact text.", _minimal_rubric(), artifact_label="draft")
    assert "editorial judge" in system.lower()
    assert "draft" in user.lower()
    assert "Some artifact text" in user
    # Both criteria should appear in the rendered rubric
    assert "Criterion A" in user or "### a" in user
    assert "Criterion B" in user or "### b" in user


def test_prompt_appends_custom_instructions() -> None:
    system, _user = build_judge_prompt(
        "x", _minimal_rubric(), custom_instructions="Grade Python code, not prose."
    )
    assert "Grade Python code" in system


class _MockProvider(Provider):
    name = "mock"
    default_model = "mock-1"

    def __init__(self, payload: dict[str, Any]):
        self._payload = payload

    async def generate_structured(
        self, system, user, schema, schema_name, model=None, max_tokens=4096, temperature=0.0
    ):
        return self._payload

    async def generate_text(self, system, user, model=None, max_tokens=4096, temperature=0.0):
        return "mock-text"


@pytest.mark.asyncio
async def test_score_artifact_with_mocked_provider() -> None:
    payload = {
        "a__reasoning": "A is ok.",
        "a__score": 3,
        "b__reasoning": "B is great.",
        "b__score": 5,
    }
    provider = _MockProvider(payload)
    ds = await score_artifact(
        artifact_text="x",
        rubric=_minimal_rubric(),
        source="test.md",
        provider=provider,
    )
    assert ds.source == "test.md"
    assert len(ds.criterion_scores) == 2
    assert ds.total_unweighted() == 8
    scores_by_id = {c.criterion_id: c for c in ds.criterion_scores}
    assert scores_by_id["a"].score == 3
    assert scores_by_id["b"].reasoning == "B is great."


@pytest.mark.asyncio
async def test_score_artifact_raises_on_missing_criterion() -> None:
    # Provider returns only one criterion's fields
    provider = _MockProvider({"a__reasoning": "ok", "a__score": 3})
    with pytest.raises(ValueError, match="missing criteria"):
        await score_artifact(
            artifact_text="x",
            rubric=_minimal_rubric(),
            source="test.md",
            provider=provider,
        )
