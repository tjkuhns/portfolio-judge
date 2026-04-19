"""Structural scanner — deterministic portfolio checks.

Signal that hiring managers read in <60 seconds: does the repo have
tests, CI, a license, meaningful docs, an ADR/decisions trail, recent
commit activity. These are boolean-ish observations — no LLM needed,
no calibration needed, no ambiguity.

The scanner is rubric-agnostic: it emits a fixed set of findings per
check, each with severity (critical / moderate / cosmetic). The
orchestrator's persona agents consume findings as part of their
context when producing the portfolio review.

Ported from the checks the three fresh-context reviewer agents ran
against the Explodable repo on 2026-04-19 (see
github.com/tjkuhns/explodable/blob/main/.internal/reviews/ for the
source reviews — .internal/ is gitignored; those are local to the
builder's machine).
"""

from __future__ import annotations

import subprocess
from dataclasses import asdict, dataclass, field
from pathlib import Path


SEVERITY_CRITICAL = "critical"
SEVERITY_MODERATE = "moderate"
SEVERITY_COSMETIC = "cosmetic"


@dataclass
class Finding:
    """A single deterministic observation about a repo."""

    check: str
    passed: bool
    severity: str
    evidence: str

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class StructuralReport:
    """Complete scan output."""

    source: str
    findings: list[Finding] = field(default_factory=list)

    def passed(self, severity: str | None = None) -> list[Finding]:
        return [f for f in self.findings if f.passed and (severity is None or f.severity == severity)]

    def failed(self, severity: str | None = None) -> list[Finding]:
        return [f for f in self.findings if not f.passed and (severity is None or f.severity == severity)]

    def to_dict(self) -> dict:
        return {
            "source": self.source,
            "summary": {
                "total_checks": len(self.findings),
                "passed": len(self.passed()),
                "critical_failures": len(self.failed(SEVERITY_CRITICAL)),
                "moderate_failures": len(self.failed(SEVERITY_MODERATE)),
                "cosmetic_failures": len(self.failed(SEVERITY_COSMETIC)),
            },
            "findings": [f.to_dict() for f in self.findings],
        }


# ── Individual checks ──


def _check_license(root: Path) -> Finding:
    candidates = ["LICENSE", "LICENSE.md", "LICENSE.txt", "COPYING", "COPYING.md"]
    for name in candidates:
        if (root / name).exists():
            return Finding(
                check="license_present",
                passed=True,
                severity=SEVERITY_MODERATE,
                evidence=f"Found {name} at repo root.",
            )
    return Finding(
        check="license_present",
        passed=False,
        severity=SEVERITY_MODERATE,
        evidence="No LICENSE / LICENSE.md / COPYING at repo root. OSS adoption requires an explicit license.",
    )


def _check_readme(root: Path) -> tuple[Finding, Path | None]:
    for name in ("README.md", "README.rst", "README.txt", "README"):
        p = root / name
        if p.exists():
            return Finding(
                check="readme_present",
                passed=True,
                severity=SEVERITY_CRITICAL,
                evidence=f"Found {name} at repo root.",
            ), p
    return Finding(
        check="readme_present",
        passed=False,
        severity=SEVERITY_CRITICAL,
        evidence="No README.md / README.rst at repo root. This is the single most critical missing artifact.",
    ), None


def _check_readme_sections(readme: Path | None) -> list[Finding]:
    if readme is None:
        return []
    text = readme.read_text(encoding="utf-8", errors="replace").lower()
    findings: list[Finding] = []
    section_markers = {
        "readme_has_install": (
            ["install", "installation", "getting started", "quickstart", "quick start"],
            SEVERITY_MODERATE,
            "a README should tell the reader how to install / run the project",
        ),
        "readme_has_usage": (
            ["usage", "example", "how to use", "how it works", "quickstart"],
            SEVERITY_MODERATE,
            "a README should show the reader what the project does, not just what it is",
        ),
    }
    for check, (keywords, severity, why) in section_markers.items():
        hit = any(k in text for k in keywords)
        findings.append(
            Finding(
                check=check,
                passed=hit,
                severity=severity,
                evidence=f"README contains one of {keywords!r}." if hit else f"README missing section for {keywords!r}; {why}.",
            )
        )
    word_count = len(text.split())
    findings.append(
        Finding(
            check="readme_non_trivial_length",
            passed=word_count >= 100,
            severity=SEVERITY_COSMETIC,
            evidence=f"README is {word_count} words.",
        )
    )
    return findings


def _check_tests(root: Path) -> Finding:
    candidates = ["tests", "test", "spec", "__tests__"]
    for name in candidates:
        if (root / name).is_dir():
            n = sum(1 for _ in (root / name).rglob("test_*.py")) + sum(
                1 for _ in (root / name).rglob("*_test.py")
            )
            if n > 0:
                return Finding(
                    check="tests_present",
                    passed=True,
                    severity=SEVERITY_MODERATE,
                    evidence=f"Found {name}/ directory with {n} test file(s).",
                )
            # Directory exists but empty — intermediate signal (scaffolded but not used)
            return Finding(
                check="tests_present",
                passed=False,
                severity=SEVERITY_MODERATE,
                evidence=f"Found {name}/ directory but it contains no test_*.py / *_test.py files.",
            )
    # Also check for test_*.py files at root
    root_tests = list(root.glob("test_*.py")) + list(root.glob("*_test.py"))
    if root_tests:
        return Finding(
            check="tests_present",
            passed=True,
            severity=SEVERITY_MODERATE,
            evidence=f"Found {len(root_tests)} test files at repo root.",
        )
    return Finding(
        check="tests_present",
        passed=False,
        severity=SEVERITY_MODERATE,
        evidence="No tests/ directory or test_*.py files found. Production readiness is hard to read without tests.",
    )


def _check_ci(root: Path) -> Finding:
    ci_paths = [
        ".github/workflows",
        ".gitlab-ci.yml",
        ".circleci",
        "azure-pipelines.yml",
        "tox.ini",
        ".travis.yml",
    ]
    for p in ci_paths:
        target = root / p
        if target.exists():
            if target.is_dir():
                n = len(list(target.glob("*.yml"))) + len(list(target.glob("*.yaml")))
                if n > 0:
                    return Finding(
                        check="ci_present",
                        passed=True,
                        severity=SEVERITY_MODERATE,
                        evidence=f"Found {p}/ with {n} workflow file(s).",
                    )
                continue  # empty CI dir — keep searching for another CI indicator
            return Finding(
                check="ci_present",
                passed=True,
                severity=SEVERITY_MODERATE,
                evidence=f"Found {p}.",
            )
    return Finding(
        check="ci_present",
        passed=False,
        severity=SEVERITY_MODERATE,
        evidence="No CI config found (.github/workflows, .gitlab-ci.yml, .circleci, tox, etc.).",
    )


def _check_package_manifest(root: Path) -> Finding:
    manifests = [
        "pyproject.toml",
        "setup.py",
        "setup.cfg",
        "requirements.txt",
        "Pipfile",
        "poetry.lock",
        "package.json",
        "Cargo.toml",
        "go.mod",
    ]
    for m in manifests:
        if (root / m).exists():
            return Finding(
                check="package_manifest_present",
                passed=True,
                severity=SEVERITY_MODERATE,
                evidence=f"Found {m}.",
            )
    return Finding(
        check="package_manifest_present",
        passed=False,
        severity=SEVERITY_MODERATE,
        evidence="No package manifest (pyproject.toml, package.json, Cargo.toml, etc.).",
    )


def _check_adrs(root: Path) -> Finding:
    candidates = ["docs/decisions", "docs/adr", "adr", "decisions", "doc/decisions"]
    for c in candidates:
        p = root / c
        if p.is_dir():
            n = len(list(p.glob("*.md")))
            if n > 0:
                return Finding(
                    check="adr_present",
                    passed=True,
                    severity=SEVERITY_COSMETIC,
                    evidence=f"Found {c}/ with {n} ADR(s).",
                )
    return Finding(
        check="adr_present",
        passed=False,
        severity=SEVERITY_COSMETIC,
        evidence="No docs/decisions or adr/ directory. ADRs are a signal of senior engineering discipline.",
    )


def _check_examples_or_demo(root: Path) -> Finding:
    for c in ("examples", "demo", "docs/examples", "example"):
        if (root / c).is_dir():
            return Finding(
                check="examples_or_demo_present",
                passed=True,
                severity=SEVERITY_COSMETIC,
                evidence=f"Found {c}/.",
            )
    return Finding(
        check="examples_or_demo_present",
        passed=False,
        severity=SEVERITY_COSMETIC,
        evidence="No examples/ or demo/ directory found.",
    )


def _check_gitignore(root: Path) -> Finding:
    exists = (root / ".gitignore").exists()
    return Finding(
        check="gitignore_present",
        passed=exists,
        severity=SEVERITY_COSMETIC,
        evidence="Found .gitignore." if exists else "No .gitignore — secrets / artifacts may be exposed.",
    )


def _check_recent_activity(root: Path) -> Finding:
    """Check the last commit date via git (requires the target path to be a git repo)."""
    if not (root / ".git").exists():
        return Finding(
            check="recent_activity",
            passed=False,
            severity=SEVERITY_COSMETIC,
            evidence="Target is not a git repo; cannot check commit recency.",
        )
    try:
        result = subprocess.run(
            ["git", "-C", str(root), "log", "-1", "--format=%ct"],
            capture_output=True,
            text=True,
            check=True,
            timeout=5,
        )
        import time

        last_commit_ts = int(result.stdout.strip())
        days_since = (time.time() - last_commit_ts) / 86400
        passed = days_since <= 90
        return Finding(
            check="recent_activity",
            passed=passed,
            severity=SEVERITY_COSMETIC,
            evidence=(
                f"Last commit {days_since:.0f} days ago."
                + ("" if passed else " Repo may read as stale or abandoned.")
            ),
        )
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, ValueError) as e:
        return Finding(
            check="recent_activity",
            passed=False,
            severity=SEVERITY_COSMETIC,
            evidence=f"Could not read git log: {e}",
        )


# ── Public API ──


def scan_directory(path: Path | str) -> StructuralReport:
    """Run every deterministic check against a local directory.

    If `path` is a git working tree the commit-recency check runs; otherwise
    it's skipped with an evidence note.
    """
    root = Path(path).resolve()
    if not root.is_dir():
        raise NotADirectoryError(f"{root} is not a directory")

    report = StructuralReport(source=str(root))

    # README is the gateway check — several follow-ups depend on it.
    readme_finding, readme_path = _check_readme(root)
    report.findings.append(readme_finding)
    report.findings.extend(_check_readme_sections(readme_path))

    report.findings.extend(
        [
            _check_license(root),
            _check_tests(root),
            _check_ci(root),
            _check_package_manifest(root),
            _check_adrs(root),
            _check_examples_or_demo(root),
            _check_gitignore(root),
            _check_recent_activity(root),
        ]
    )
    return report
