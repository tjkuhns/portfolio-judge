"""Tests for core.calibration — Spearman + Kendall."""

from __future__ import annotations

import pytest

from portfolio_judge.core.calibration import kendall_tau, spearman


def test_spearman_perfect_positive() -> None:
    assert spearman([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == pytest.approx(1.0)


def test_spearman_perfect_negative() -> None:
    assert spearman([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) == pytest.approx(-1.0)


def test_spearman_handles_ties() -> None:
    # Two items tied in both rankings — rho should still be +1 (perfect monotonic)
    rho = spearman([1.0, 2.0, 2.0, 3.0], [10.0, 20.0, 20.0, 30.0])
    assert rho == pytest.approx(1.0)


def test_spearman_rejects_length_mismatch() -> None:
    with pytest.raises(ValueError):
        spearman([1, 2], [1, 2, 3])


def test_spearman_rejects_tiny_input() -> None:
    with pytest.raises(ValueError):
        spearman([1], [1])


def test_kendall_perfect_positive() -> None:
    assert kendall_tau([1, 2, 3, 4, 5], [10, 20, 30, 40, 50]) == pytest.approx(1.0)


def test_kendall_perfect_negative() -> None:
    assert kendall_tau([1, 2, 3, 4, 5], [50, 40, 30, 20, 10]) == pytest.approx(-1.0)


def test_kendall_partial_agreement() -> None:
    # 6 pairs on [1,2,3,4] vs [1,3,2,4]:
    # only (2,3) vs (3,2) is discordant → 5 concordant, 1 discordant
    # tau = (5-1)/6 = 2/3
    tau = kendall_tau([1, 2, 3, 4], [1, 3, 2, 4])
    assert tau == pytest.approx(2 / 3, abs=0.01)
