"""CLI entry point for portfolio-judge.

Four subcommands matching the four layers of the tool:

    portfolio-judge review     --github <url> --role applied-ai     # full multi-persona
    portfolio-judge prose      <path>                               # single-artifact prose
    portfolio-judge code       <path>                               # single-file code
    portfolio-judge structure  <path>                               # deterministic only
"""

from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path

import click
from dotenv import load_dotenv
from rich.console import Console

from portfolio_judge import __version__
from portfolio_judge.core.llm import MissingAPIKey
from portfolio_judge.judges import code as code_judge
from portfolio_judge.judges import prose as prose_judge
from portfolio_judge.judges.structure import scan_directory
from portfolio_judge.orchestrator import (
    ALL_PERSONAS,
    ROLE_DESCRIPTIONS,
    render_review_markdown,
    review_portfolio,
)

console = Console(stderr=True, highlight=False)


def _write_output(text: str, output: Path | None) -> None:
    if output is None:
        sys.stdout.write(text)
        if not text.endswith("\n"):
            sys.stdout.write("\n")
    else:
        output.write_text(text, encoding="utf-8")
        console.print(f"[green]Wrote[/green] {output}")


def _render_score_markdown(score_dict: dict, title: str) -> str:
    lines = [f"# {title}"]
    lines.append(f"**Source:** {score_dict['source']}")
    lines.append(f"**Rubric:** {score_dict['rubric_id']} v{score_dict['rubric_version']}")
    total = score_dict["total_unweighted"]
    max_score = 5 * len(score_dict["criterion_scores"])
    lines.append(f"**Total (unweighted):** {total}/{max_score}")
    if score_dict["vetoed_criteria"]:
        lines.append(f"**Vetoed:** {', '.join(score_dict['vetoed_criteria'])}")
    lines.append("")
    for c in score_dict["criterion_scores"]:
        lines.append(f"### {c['criterion_id']}: {c['score']}/5")
        lines.append(c["reasoning"].strip())
        lines.append("")
    return "\n".join(lines)


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(__version__, "-V", "--version")
def cli() -> None:
    """Role-calibrated LLM-as-judge for AI engineering portfolios.

    See https://github.com/tjkuhns/portfolio-judge for the full methodology.
    """
    load_dotenv()


@cli.command()
@click.option(
    "--github",
    "github_url",
    type=str,
    default=None,
    help="GitHub repo URL (https://github.com/owner/repo).",
)
@click.option(
    "--path",
    "local_path",
    type=click.Path(exists=True, file_okay=False, path_type=Path),
    default=None,
    help="Local directory path (alternative to --github).",
)
@click.option(
    "--role",
    type=click.Choice(list(ROLE_DESCRIPTIONS.keys())),
    default="applied-ai",
    show_default=True,
    help="Target role the candidate is applying for.",
)
@click.option(
    "--personas",
    default=",".join(ALL_PERSONAS),
    show_default=True,
    help="Comma-separated persona names to run.",
)
@click.option(
    "--model",
    default=None,
    help="Model shortcut (sonnet/opus/haiku/gpt-4.1/gemini/...) or full ID. Defaults to whichever provider has a key set.",
)
@click.option(
    "--output",
    "-o",
    type=click.Path(path_type=Path),
    default=None,
    help="Write the report to a file. Default: stdout.",
)
@click.option("--json", "as_json", is_flag=True, help="Output as JSON instead of markdown.")
def review(
    github_url: str | None,
    local_path: Path | None,
    role: str,
    personas: str,
    model: str | None,
    output: Path | None,
    as_json: bool,
) -> None:
    """Full portfolio review: prose + code + structural + four personas + synthesis."""
    if github_url and local_path:
        raise click.UsageError("Provide either --github or --path, not both.")
    if not github_url and not local_path:
        raise click.UsageError("Provide either --github or --path.")
    source = github_url or str(local_path)
    persona_list = [p.strip() for p in personas.split(",") if p.strip()]

    try:
        review_result = asyncio.run(
            review_portfolio(
                source=source,
                role=role,
                personas=persona_list,
                model=model,
            )
        )
    except MissingAPIKey as e:
        console.print(f"[red]API key missing:[/red] {e}")
        console.print(
            "Set ANTHROPIC_API_KEY, OPENAI_API_KEY, or GOOGLE_API_KEY — "
            "or copy .env.example to .env."
        )
        raise SystemExit(2) from e

    if as_json:
        _write_output(json.dumps(review_result.to_dict(), indent=2), output)
    else:
        _write_output(render_review_markdown(review_result), output)


@cli.command()
@click.argument("path", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.option("--rubric", type=click.Path(exists=True, dir_okay=False, path_type=Path), default=None)
@click.option("--model", default=None)
@click.option("--output", "-o", type=click.Path(path_type=Path), default=None)
@click.option("--json", "as_json", is_flag=True)
def prose(
    path: Path,
    rubric: Path | None,
    model: str | None,
    output: Path | None,
    as_json: bool,
) -> None:
    """Score a prose artifact (blog post, README, docs)."""
    text = path.read_text(encoding="utf-8")
    try:
        score = asyncio.run(
            prose_judge.review_prose(
                text=text,
                source=str(path),
                rubric=rubric,
                model=model,
            )
        )
    except MissingAPIKey as e:
        console.print(f"[red]API key missing:[/red] {e}")
        raise SystemExit(2) from e

    if as_json:
        _write_output(json.dumps(score.to_dict(), indent=2), output)
    else:
        _write_output(_render_score_markdown(score.to_dict(), f"Prose review: {path.name}"), output)


@cli.command()
@click.argument("path", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.option("--rubric", type=click.Path(exists=True, dir_okay=False, path_type=Path), default=None)
@click.option("--model", default=None)
@click.option("--output", "-o", type=click.Path(path_type=Path), default=None)
@click.option("--json", "as_json", is_flag=True)
def code(
    path: Path,
    rubric: Path | None,
    model: str | None,
    output: Path | None,
    as_json: bool,
) -> None:
    """Score a Python source file."""
    source_code = path.read_text(encoding="utf-8")
    try:
        score = asyncio.run(
            code_judge.review_code(
                source_code=source_code,
                source=str(path),
                rubric=rubric,
                model=model,
            )
        )
    except MissingAPIKey as e:
        console.print(f"[red]API key missing:[/red] {e}")
        raise SystemExit(2) from e

    if as_json:
        _write_output(json.dumps(score.to_dict(), indent=2), output)
    else:
        _write_output(_render_score_markdown(score.to_dict(), f"Code review: {path.name}"), output)


@cli.command()
@click.argument("path", type=click.Path(exists=True, file_okay=False, path_type=Path))
@click.option("--output", "-o", type=click.Path(path_type=Path), default=None)
@click.option("--json", "as_json", is_flag=True)
def structure(path: Path, output: Path | None, as_json: bool) -> None:
    """Deterministic structural checks on a local repo directory."""
    report = scan_directory(path)
    if as_json:
        _write_output(json.dumps(report.to_dict(), indent=2), output)
    else:
        lines = [f"# Structural scan: {report.source}\n"]
        summary = report.to_dict()["summary"]
        lines.append(
            f"{summary['passed']}/{summary['total_checks']} checks passed · "
            f"critical failures: {summary['critical_failures']} · "
            f"moderate: {summary['moderate_failures']} · "
            f"cosmetic: {summary['cosmetic_failures']}\n"
        )
        for f in report.findings:
            mark = "✅" if f.passed else "❌"
            lines.append(f"- {mark} **{f.check}** ({f.severity}): {f.evidence}")
        _write_output("\n".join(lines), output)


def main() -> None:
    cli()


if __name__ == "__main__":
    main()
