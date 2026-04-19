"""Rubric loading and validation.

A rubric is a YAML file defining a named set of 1–5 scored criteria with
anchor descriptions at 1 / 3 / 5 and optional weights. Every judge in this
package runs against a rubric — the judge code is rubric-agnostic.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field, field_validator


class Criterion(BaseModel):
    """A single scored criterion in a rubric."""

    id: str
    name: str
    what_it_measures: str
    scale: dict[int, str]
    weight: float | None = None

    @field_validator("scale")
    @classmethod
    def scale_must_have_anchors(cls, scale: dict[int, str]) -> dict[int, str]:
        missing = {1, 3, 5} - set(scale.keys())
        if missing:
            raise ValueError(f"scale must have anchor descriptions at 1, 3, 5; missing {missing}")
        return scale


class Rubric(BaseModel):
    """A complete rubric loaded from YAML."""

    id: str
    version: str = "unknown"
    description: str = ""
    criteria: list[Criterion] = Field(min_length=1)
    scoring_guidance: dict[str, Any] = Field(default_factory=dict)

    @property
    def criterion_ids(self) -> list[str]:
        return [c.id for c in self.criteria]

    @property
    def weights(self) -> dict[str, float]:
        """Per-criterion weight multipliers. Unlisted criteria default to 1.0."""
        weighted = self.scoring_guidance.get("weighted_criteria") or {}
        explicit_weights = {c.id: c.weight for c in self.criteria if c.weight is not None}
        # Explicit `weight` on a criterion wins over scoring_guidance map.
        return {**weighted, **explicit_weights}

    def max_unweighted(self) -> int:
        return 5 * len(self.criteria)

    def max_weighted(self) -> float:
        return sum(5 * self.weights.get(c.id, 1.0) for c in self.criteria)


def load_rubric(path: Path | str) -> Rubric:
    """Load and validate a rubric from YAML."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Rubric not found: {path}")
    with open(path) as f:
        data = yaml.safe_load(f)
    return Rubric.model_validate(data)


@dataclass
class CriterionScore:
    """A single criterion score with the judge's reasoning."""

    criterion_id: str
    score: int
    reasoning: str

    def is_veto(self) -> bool:
        return self.score <= 1


@dataclass
class DraftScore:
    """Full rubric scoring for a single artifact."""

    source: str  # file path, URL, or identifier
    criterion_scores: list[CriterionScore]
    rubric_id: str
    rubric_version: str

    def total_unweighted(self) -> int:
        return sum(c.score for c in self.criterion_scores)

    def total_weighted(self, weights: dict[str, float]) -> float:
        return sum(c.score * weights.get(c.criterion_id, 1.0) for c in self.criterion_scores)

    def vetoed_criteria(self) -> list[str]:
        return [c.criterion_id for c in self.criterion_scores if c.is_veto()]

    def to_dict(self) -> dict:
        return {
            "source": self.source,
            "rubric_id": self.rubric_id,
            "rubric_version": self.rubric_version,
            "total_unweighted": self.total_unweighted(),
            "vetoed_criteria": self.vetoed_criteria(),
            "criterion_scores": [
                {"criterion_id": c.criterion_id, "score": c.score, "reasoning": c.reasoning}
                for c in self.criterion_scores
            ],
        }
