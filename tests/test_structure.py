"""Tests for judges.structure — deterministic portfolio checks."""

from __future__ import annotations

from pathlib import Path

from portfolio_judge.judges.structure import (
    SEVERITY_COSMETIC,
    SEVERITY_CRITICAL,
    SEVERITY_MODERATE,
    scan_directory,
)


def _make_repo(
    tmp_path: Path,
    *,
    readme: str | None = (
        "# Project\n\n## Installation\n\n`pip install it`\n\n## Usage\n\n"
        "Run it. This is a test fixture with enough filler words to clear the 100-word "
        "non-trivial-length check. " * 10
    ),
    license_file: bool = True,
    with_tests: bool = True,
    with_ci: bool = True,
    with_pyproject: bool = True,
    with_adrs: bool = False,
    with_examples: bool = False,
    with_gitignore: bool = True,
) -> Path:
    root = tmp_path / "repo"
    root.mkdir()
    if readme is not None:
        (root / "README.md").write_text(readme)
    if license_file:
        (root / "LICENSE").write_text("MIT\n")
    if with_pyproject:
        (root / "pyproject.toml").write_text("[project]\nname='x'\nversion='0.1'\n")
    if with_gitignore:
        (root / ".gitignore").write_text("*.pyc\n")
    if with_tests:
        tests = root / "tests"
        tests.mkdir()
        (tests / "test_thing.py").write_text("def test_x(): assert True\n")
    if with_ci:
        wf = root / ".github" / "workflows"
        wf.mkdir(parents=True)
        (wf / "test.yml").write_text("name: test\n")
    if with_adrs:
        adr = root / "docs" / "decisions"
        adr.mkdir(parents=True)
        (adr / "0001-thing.md").write_text("# ADR 0001\n")
    if with_examples:
        ex = root / "examples"
        ex.mkdir()
        (ex / "hello.py").write_text("print('hi')\n")
    return root


def test_scan_full_repo_all_checks_pass(tmp_path: Path) -> None:
    root = _make_repo(tmp_path, with_adrs=True, with_examples=True)
    report = scan_directory(root)
    failed = report.failed()
    # recent_activity is expected to fail — tmp_path is not a git repo
    non_git_failures = [f for f in failed if f.check != "recent_activity"]
    assert non_git_failures == [], f"Unexpected failures: {non_git_failures}"


def test_scan_missing_readme_is_critical(tmp_path: Path) -> None:
    root = _make_repo(tmp_path, readme=None)
    report = scan_directory(root)
    readme = [f for f in report.findings if f.check == "readme_present"][0]
    assert not readme.passed
    assert readme.severity == SEVERITY_CRITICAL


def test_scan_missing_license_is_moderate(tmp_path: Path) -> None:
    root = _make_repo(tmp_path, license_file=False)
    report = scan_directory(root)
    lic = [f for f in report.findings if f.check == "license_present"][0]
    assert not lic.passed
    assert lic.severity == SEVERITY_MODERATE


def test_empty_tests_directory_fails(tmp_path: Path) -> None:
    root = _make_repo(tmp_path, with_tests=False)
    # Create an empty tests dir
    (root / "tests").mkdir()
    report = scan_directory(root)
    tests = [f for f in report.findings if f.check == "tests_present"][0]
    assert not tests.passed
    assert "contains no test_" in tests.evidence


def test_empty_ci_directory_fails(tmp_path: Path) -> None:
    root = _make_repo(tmp_path, with_ci=False)
    (root / ".github" / "workflows").mkdir(parents=True)  # empty
    report = scan_directory(root)
    ci = [f for f in report.findings if f.check == "ci_present"][0]
    assert not ci.passed


def test_adr_cosmetic_severity_when_missing(tmp_path: Path) -> None:
    root = _make_repo(tmp_path, with_adrs=False)
    report = scan_directory(root)
    adr = [f for f in report.findings if f.check == "adr_present"][0]
    assert not adr.passed
    assert adr.severity == SEVERITY_COSMETIC


def test_readme_usage_section_detected(tmp_path: Path) -> None:
    root = _make_repo(tmp_path, readme="# Project\n\n## Quickstart\n\nRun the thing.\n" * 20)
    report = scan_directory(root)
    # Both install-keyword (quickstart) and usage-keyword (quickstart) match
    usage = [f for f in report.findings if f.check == "readme_has_usage"][0]
    assert usage.passed


def test_summary_aggregates_by_severity(tmp_path: Path) -> None:
    root = _make_repo(tmp_path, with_ci=False, with_tests=False, with_adrs=False)
    summary = scan_directory(root).to_dict()["summary"]
    assert summary["total_checks"] >= 10
    # tests + ci missing → 2 moderate failures; adr missing → 1 cosmetic; git non-repo → 1 cosmetic
    assert summary["moderate_failures"] >= 2
    assert summary["cosmetic_failures"] >= 1
