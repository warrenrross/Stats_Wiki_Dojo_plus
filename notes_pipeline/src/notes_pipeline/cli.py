"""Typer-based CLI."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console

from notes_pipeline import __version__
from notes_pipeline.benchmark import (
    benchmark_pdf,
    print_benchmark_table,
    save_benchmark_report,
)
from notes_pipeline.config import AppConfig, OCRBackendName  # noqa: F401
from notes_pipeline.logging_setup import setup_logging
from notes_pipeline.pdf import render_markdown_to_pdf
from notes_pipeline.pipeline import process_annotated_pdf
from notes_pipeline.watcher import run_watch

# Backends shown in --help
ALL_BACKENDS: list[str] = ["claude", "olmocr", "llama"]

app = typer.Typer(
    add_completion=False,
    help="Annotated-PDF → Obsidian vault pipeline.",
    no_args_is_help=True,
)
console = Console()


def _load_cfg(config: Optional[Path], verbose: bool) -> AppConfig:
    setup_logging(verbose=verbose)
    cfg = AppConfig.load(config)
    cfg.paths.ensure()
    logging.getLogger("notes_pipeline").debug("Loaded config: %s", cfg.model_dump())
    return cfg


def _version_callback(value: bool):
    if value:
        typer.echo(f"notes-pipeline {__version__}")
        raise typer.Exit(0)


@app.callback()
def _root(
    version: bool = typer.Option(False, "--version", callback=_version_callback, is_eager=True),
):
    """notes-pipeline CLI."""


# ── watch ─────────────────────────────────────────────────────────────────────


@app.command()
def watch(
    ocr: str = typer.Option(None, "--ocr", help=f"OCR backend ({', '.join(ALL_BACKENDS)})"),
    config: Optional[Path] = typer.Option(None, "--config", help="Path to TOML config"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
):
    """Watch the inbox folder continuously."""
    cfg = _load_cfg(config, verbose)
    backend = (ocr or cfg.ocr.backend).lower()
    if backend not in ALL_BACKENDS:
        typer.echo(f"Unknown backend: {backend!r}. Choose from {ALL_BACKENDS}", err=True)
        raise typer.Exit(2)
    run_watch(cfg, backend)  # type: ignore[arg-type]


# ── process ───────────────────────────────────────────────────────────────────


@app.command()
def process(
    filename: str = typer.Argument(..., help="PDF inside inbox/, or an absolute path"),
    ocr: str = typer.Option(None, "--ocr", help=f"OCR backend ({', '.join(ALL_BACKENDS)})"),
    skip_merge: bool = typer.Option(False, "--skip-merge", help="Run OCR only; don't touch vault"),
    dry_run: bool = typer.Option(False, "--dry-run", help="OCR only; don't move PDF or write vault"),
    force: bool = typer.Option(False, "--force", help="Reprocess even if previously processed"),
    config: Optional[Path] = typer.Option(None, "--config"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
):
    """Process a single annotated PDF end-to-end."""
    cfg = _load_cfg(config, verbose)
    backend = (ocr or cfg.ocr.backend).lower()
    if backend not in ALL_BACKENDS:
        typer.echo(f"Unknown backend: {backend!r}", err=True)
        raise typer.Exit(2)

    pdf_path = _resolve_pdf(filename, cfg)
    result = process_annotated_pdf(
        pdf_path,
        cfg,
        backend_name=backend,  # type: ignore[arg-type]
        skip_merge=skip_merge,
        dry_run=dry_run,
        force=force,
    )
    if not result.ok and result.error != "already_processed":
        typer.echo(f"Pipeline finished with errors: {result.error}", err=True)
        raise typer.Exit(1)


# ── benchmark ─────────────────────────────────────────────────────────────────


@app.command()
def benchmark(
    filename: str = typer.Argument(..., help="PDF inside inbox/, or an absolute path"),
    backends: list[str] = typer.Option(
        ALL_BACKENDS, "--backends", "-b",
        help="Backends to benchmark; default: all three",
    ),
    config: Optional[Path] = typer.Option(None, "--config"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
):
    """Run multiple OCR backends on one PDF and save a side-by-side comparison."""
    cfg = _load_cfg(config, verbose)
    for b in backends:
        if b not in ALL_BACKENDS:
            typer.echo(f"Unknown backend: {b!r}", err=True)
            raise typer.Exit(2)
    pdf_path = _resolve_pdf(filename, cfg)
    report = benchmark_pdf(pdf_path, backends, cfg)  # type: ignore[arg-type]
    print_benchmark_table(report, console=console)
    saved = save_benchmark_report(report, cfg.paths.benchmarks)  # type: ignore[arg-type]
    console.print(f"\n[bold]Full report saved:[/bold] {saved}")


# ── render ────────────────────────────────────────────────────────────────────


@app.command()
def render(
    filename: str = typer.Argument(..., help="Markdown filename in vault/"),
    config: Optional[Path] = typer.Option(None, "--config"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
):
    """Render a vault markdown note to PDF (for sending to iPad)."""
    cfg = _load_cfg(config, verbose)
    md_path = cfg.paths.vault / filename  # type: ignore[operator]
    if not md_path.exists() and Path(filename).is_file():
        md_path = Path(filename)
    if not md_path.exists():
        typer.echo(f"Not found: {md_path}", err=True)
        raise typer.Exit(1)
    out = render_markdown_to_pdf(md_path, cfg.paths.rendered, cfg.render)  # type: ignore[arg-type]
    console.print(f"[bold]PDF ready:[/bold] {out}")


# ── doctor ────────────────────────────────────────────────────────────────────


@app.command()
def doctor(
    config: Optional[Path] = typer.Option(None, "--config"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
):
    """Verify environment: directories, pandoc, poppler, Ollama, Anthropic key."""
    cfg = _load_cfg(config, verbose)
    import shutil as _sh

    ok = True

    console.print(f"[bold]Config root:[/bold] {cfg.paths.root}")
    for label, path in [
        ("vault", cfg.paths.vault), ("inbox", cfg.paths.inbox),
        ("rendered", cfg.paths.rendered), ("processed", cfg.paths.processed),
        ("benchmarks", cfg.paths.benchmarks), ("state", cfg.paths.state),
    ]:
        exists = path.exists()  # type: ignore[union-attr]
        console.print(f"  {'✓' if exists else '✗'} {label}: {path}")
        ok = ok and exists

    console.print("\n[bold]External tools:[/bold]")
    for tool in ["pandoc", "pdftoppm"]:
        path = _sh.which(tool)
        console.print(f"  {'✓' if path else '✗'} {tool}: {path or 'NOT FOUND'}")
        ok = ok and bool(path)

    console.print("\n[bold]Anthropic API:[/bold]")
    import os
    key = cfg.ocr.claude.api_key or os.environ.get("ANTHROPIC_API_KEY")
    console.print(f"  {'✓' if key else '✗'} ANTHROPIC_API_KEY {'set' if key else 'NOT set'}")

    console.print("\n[bold]Ollama:[/bold]")
    try:
        import ollama as _ollama
        host = os.environ.get("OLLAMA_HOST", cfg.ocr.ollama.host)
        client = _ollama.Client(host=host)
        tags = client.list()
        names = [m.get("model") or m.get("name") for m in tags.get("models", [])]
        console.print(f"  ✓ reachable at {host}")
        for needed in (cfg.ocr.ollama.olmocr_model, cfg.ocr.ollama.llama_model):
            present = any(n == needed for n in names if n)
            console.print(f"  {'✓' if present else '✗'} {needed} {'present' if present else 'NOT pulled'}")
            ok = ok and present
    except Exception as e:
        console.print(f"  ✗ Ollama unreachable: {e}")
        ok = False

    raise typer.Exit(0 if ok else 1)


# ── helpers ───────────────────────────────────────────────────────────────────


def _resolve_pdf(filename: str, cfg: AppConfig) -> Path:
    p = Path(filename)
    if p.is_absolute() and p.exists():
        return p
    candidate = cfg.paths.inbox / filename  # type: ignore[operator]
    if candidate.exists():
        return candidate
    if p.exists():
        return p.resolve()
    typer.echo(f"Not found: {filename}", err=True)
    raise typer.Exit(1)


if __name__ == "__main__":
    app()
