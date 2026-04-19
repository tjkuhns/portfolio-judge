"""Rank correlation utilities for calibrating a judge against a reference.

Exported for consumers who want to run their own calibration: score a set
of artifacts with the judge, collect reference rankings (human or panel),
compute ρ.

Portable from `src/content_pipeline/eval/judge.py` in the Explodable repo
where ρ = 0.841 (Opus) / ρ = 0.782 (Sonnet) was measured against a
7-model editorial panel (5-cluster after post-hoc outlier drop). Full
methodology: github.com/tjkuhns/explodable/blob/main/docs/eval-methodology.md
"""

from __future__ import annotations

from math import sqrt


def _rank(values: list[float]) -> list[float]:
    """Return average-rank assignments (handles ties)."""
    n = len(values)
    sorted_indices = sorted(range(n), key=lambda i: values[i])
    ranks = [0.0] * n
    i = 0
    while i < n:
        j = i
        while j + 1 < n and values[sorted_indices[j + 1]] == values[sorted_indices[i]]:
            j += 1
        avg_rank = (i + j) / 2 + 1
        for k in range(i, j + 1):
            ranks[sorted_indices[k]] = avg_rank
        i = j + 1
    return ranks


def spearman(a: list[float], b: list[float]) -> float:
    """Spearman's rank correlation coefficient.

    a[i] and b[i] are scores (or ranks) for the same item. Returns ρ in [-1, 1].
    """
    if len(a) != len(b):
        raise ValueError("sequences must have equal length")
    if len(a) < 2:
        raise ValueError("need at least 2 items to compute rank correlation")

    ra = _rank(a)
    rb = _rank(b)
    n = len(ra)
    mean_a = sum(ra) / n
    mean_b = sum(rb) / n
    num = sum((ra[i] - mean_a) * (rb[i] - mean_b) for i in range(n))
    den = sqrt(
        sum((ra[i] - mean_a) ** 2 for i in range(n))
        * sum((rb[i] - mean_b) ** 2 for i in range(n))
    )
    if den == 0:
        return 0.0
    return num / den


def kendall_tau(a: list[float], b: list[float]) -> float:
    """Kendall τ (τ-b; tie-adjusted). Returns τ in [-1, 1].

    More conservative than Spearman on ranked data — reports less reliability
    when ranks are noisy. Reporting both is the Shankar *Who Validates the
    Validators?* (NAACL 2025) recommendation.
    """
    if len(a) != len(b):
        raise ValueError("sequences must have equal length")
    n = len(a)
    if n < 2:
        raise ValueError("need at least 2 items")

    concordant = 0
    discordant = 0
    ties_a = 0
    ties_b = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            da = a[i] - a[j]
            db = b[i] - b[j]
            if da == 0 and db == 0:
                continue
            if da == 0:
                ties_a += 1
                continue
            if db == 0:
                ties_b += 1
                continue
            if (da > 0) == (db > 0):
                concordant += 1
            else:
                discordant += 1
    denom = sqrt((concordant + discordant + ties_a) * (concordant + discordant + ties_b))
    if denom == 0:
        return 0.0
    return (concordant - discordant) / denom
