"""Portfolio ingestion — fetch the artifacts a review needs.

Two modes: GitHub URL (via the REST API) or local filesystem path.
Fetches the README, a small set of docs, and the top-N Python files
by size. The structural scanner requires a local directory; for
GitHub URLs we download a tarball to a temp dir.
"""

from __future__ import annotations

import io
import os
import re
import tarfile
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

import httpx

MAX_DOC_FILES = 5
MAX_CODE_FILES = 5
MAX_PER_FILE_BYTES = 40_000  # ~10k lines of code or ~6k words of prose


_GITHUB_URL_RE = re.compile(
    r"^https?://github\.com/(?P<owner>[^/]+)/(?P<repo>[^/]+?)(?:\.git)?/?$"
)


@dataclass
class PortfolioArtifacts:
    """The subset of a portfolio we feed to the review pipeline."""

    source: str
    local_path: Path  # always populated; may be a temp dir for GitHub-sourced repos
    readme_text: str | None = None
    docs: list[tuple[str, str]] = field(default_factory=list)  # (relative_path, text)
    code_files: list[tuple[str, str]] = field(default_factory=list)
    # Cleanup hook: caller should invoke this when done (for GitHub fetches)
    _cleanup: object | None = None

    def cleanup(self) -> None:
        if self._cleanup is not None:
            self._cleanup.cleanup()
            self._cleanup = None

    def __enter__(self) -> PortfolioArtifacts:
        return self

    def __exit__(self, *_exc) -> None:
        self.cleanup()


# ── Public entry points ──


def fetch_local(path: Path | str) -> PortfolioArtifacts:
    """Collect artifacts from a local directory (no cleanup needed)."""
    root = Path(path).resolve()
    if not root.is_dir():
        raise NotADirectoryError(f"{root} is not a directory")
    return _collect(source=str(root), root=root, cleanup=None)


def fetch_github(url: str, token: str | None = None) -> PortfolioArtifacts:
    """Download a public GitHub repo as a tarball and collect artifacts.

    The returned PortfolioArtifacts holds a TemporaryDirectory handle under
    `_cleanup` — use it as a context manager or call `.cleanup()` explicitly.
    """
    m = _GITHUB_URL_RE.match(url.strip())
    if not m:
        raise ValueError(f"Not a GitHub repo URL: {url}")
    owner, repo = m["owner"], m["repo"]
    token = token or os.environ.get("GITHUB_TOKEN")

    tarball_url = f"https://api.github.com/repos/{owner}/{repo}/tarball"
    headers = {"Accept": "application/vnd.github.v3.raw"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    with httpx.Client(timeout=60, follow_redirects=True) as client:
        resp = client.get(tarball_url, headers=headers)
        resp.raise_for_status()
        tarball_bytes = resp.content

    tmp = tempfile.TemporaryDirectory(prefix="portfolio-judge-")
    with tarfile.open(fileobj=io.BytesIO(tarball_bytes), mode="r:gz") as tar:
        tar.extractall(tmp.name, filter="data")

    # GitHub tarballs extract to a single nested dir like `owner-repo-HASH/`.
    children = [p for p in Path(tmp.name).iterdir() if p.is_dir()]
    if len(children) != 1:
        tmp.cleanup()
        raise RuntimeError(f"Unexpected tarball structure at {tmp.name}: {children}")
    root = children[0]

    return _collect(source=url, root=root, cleanup=tmp)


# ── Internal collection ──


def _collect(source: str, root: Path, cleanup: object | None) -> PortfolioArtifacts:
    readme = _find_readme(root)
    readme_text = _read_text(readme) if readme else None
    docs = _collect_docs(root)
    code_files = _collect_code(root)
    return PortfolioArtifacts(
        source=source,
        local_path=root,
        readme_text=readme_text,
        docs=docs,
        code_files=code_files,
        _cleanup=cleanup,
    )


def _find_readme(root: Path) -> Path | None:
    for name in ("README.md", "README.rst", "README.txt", "README"):
        p = root / name
        if p.exists():
            return p
    return None


def _collect_docs(root: Path) -> list[tuple[str, str]]:
    """Find up to MAX_DOC_FILES markdown docs worth reviewing as prose.

    Excludes the README (already captured), CHANGELOGs, CONTRIBUTING, and
    any file under a `vendor/`, `node_modules/`, or similar dependency dir.
    """
    docs_candidates: list[tuple[Path, int]] = []
    skip_dir_names = {
        "node_modules",
        "vendor",
        "venv",
        ".venv",
        "dist",
        "build",
        "__pycache__",
        # Python package internals live under src/ in the standard src-layout
        # convention; those are tool internals (personas, grounding, etc.), not
        # portfolio prose. Skip entirely.
        "src",
    }
    skip_file_names = {
        "README.md",
        "README.rst",
        "CHANGELOG.md",
        "CONTRIBUTING.md",
        "CODE_OF_CONDUCT.md",
        "SECURITY.md",
    }
    for p in root.rglob("*.md"):
        if any(part in skip_dir_names for part in p.parts):
            continue
        if p.name in skip_file_names:
            continue
        if not p.is_file():
            continue
        # Also skip any .md file whose parent dir contains an __init__.py
        # (package-internal docs like the ones shipped alongside Python modules).
        if (p.parent / "__init__.py").exists():
            continue
        size = p.stat().st_size
        if size > MAX_PER_FILE_BYTES or size < 500:
            continue
        docs_candidates.append((p, size))

    # Prefer `docs/` and `blog/` trees, then size-descending
    def _priority(item: tuple[Path, int]) -> tuple[int, int]:
        p, size = item
        parts = set(p.parts)
        if "docs" in parts or "doc" in parts:
            priority = 0
        elif "blog" in parts or "posts" in parts:
            priority = 1
        else:
            priority = 2
        return (priority, -size)

    docs_candidates.sort(key=_priority)
    return [
        (str(p.relative_to(root)), _read_text(p))
        for p, _ in docs_candidates[:MAX_DOC_FILES]
    ]


def _collect_code(root: Path) -> list[tuple[str, str]]:
    """Top-N representative Python files by size, excluding tests and __init__."""
    skip_dir_names = {"node_modules", "vendor", "venv", ".venv", "dist", "build", "__pycache__", "tests", "test"}
    candidates: list[tuple[Path, int]] = []
    for p in root.rglob("*.py"):
        if any(part in skip_dir_names for part in p.parts):
            continue
        if p.name in ("__init__.py", "setup.py", "conftest.py"):
            continue
        if p.name.startswith("test_") or p.name.endswith("_test.py"):
            continue
        if not p.is_file():
            continue
        size = p.stat().st_size
        if size > MAX_PER_FILE_BYTES or size < 300:
            continue
        candidates.append((p, size))

    candidates.sort(key=lambda t: -t[1])  # largest first
    return [
        (str(p.relative_to(root)), _read_text(p))
        for p, _ in candidates[:MAX_CODE_FILES]
    ]


def _read_text(path: Path, max_bytes: int = MAX_PER_FILE_BYTES) -> str:
    """Read a file, capping at max_bytes to keep prompts bounded."""
    with open(path, "rb") as f:
        raw = f.read(max_bytes + 1)
    text = raw.decode("utf-8", errors="replace")
    if len(raw) > max_bytes:
        text = text[:max_bytes] + "\n\n[... truncated ...]"
    return text
