"""Tests for ingest — local directory collection (GitHub path is integration-only)."""

from __future__ import annotations

from pathlib import Path

import pytest

from portfolio_judge.ingest import fetch_local


def _write_repo(tmp_path: Path) -> Path:
    root = tmp_path / "repo"
    root.mkdir()
    (root / "README.md").write_text("# Project\n\n" + "Words here. " * 100)
    (root / "pyproject.toml").write_text("[project]\nname='x'\n")
    docs = root / "docs"
    docs.mkdir()
    (docs / "methodology.md").write_text("# Methodology\n\n" + "Content. " * 200)
    src = root / "src" / "pkg"
    src.mkdir(parents=True)
    (src / "__init__.py").write_text("")
    (src / "main.py").write_text("def main():\n    " + "pass\n    " * 200)
    tests = root / "tests"
    tests.mkdir()
    (tests / "test_main.py").write_text("def test_foo(): assert True\n")
    return root


def test_fetch_local_finds_readme(tmp_path: Path) -> None:
    root = _write_repo(tmp_path)
    artifacts = fetch_local(root)
    assert artifacts.readme_text is not None
    assert "# Project" in artifacts.readme_text


def test_fetch_local_collects_docs_from_docs_dir(tmp_path: Path) -> None:
    root = _write_repo(tmp_path)
    artifacts = fetch_local(root)
    assert any("methodology.md" in name for name, _ in artifacts.docs)


def test_fetch_local_excludes_tests_and_init_from_code(tmp_path: Path) -> None:
    root = _write_repo(tmp_path)
    artifacts = fetch_local(root)
    for name, _ in artifacts.code_files:
        assert "__init__.py" not in name
        assert "tests/" not in name


def test_fetch_local_excludes_package_internal_markdown(tmp_path: Path) -> None:
    """A .md file inside a python package (has __init__.py sibling) should not show as docs."""
    root = _write_repo(tmp_path)
    pkg_md = root / "src" / "pkg" / "notes.md"
    pkg_md.write_text("# Internal\n\n" + "Words. " * 100)
    artifacts = fetch_local(root)
    for name, _ in artifacts.docs:
        assert "notes.md" not in name


def test_fetch_local_rejects_missing_dir(tmp_path: Path) -> None:
    with pytest.raises(NotADirectoryError):
        fetch_local(tmp_path / "does_not_exist")
