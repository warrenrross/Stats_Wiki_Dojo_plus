"""Benchmark multiple OCR backends on a single PDF."""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

from rich.console import Console
from rich.table import Table

from notes_pipeline.config import AppConfig, OCRBackendName
from notes_pipeline.ocr import build_backend
from notes_pipeline.ocr.base import OCRResult
from notes_pipeline.ocr.registry import run_ocr
from notes_pipeline.pdf import cleanup_page_images, pdf_to_images

log = logging.getLogger(__name__)


@dataclass
class BenchmarkReport:
    pdf_name: str
    timestamp: str
    results: list[OCRResult] = field(default_factory=list)


def benchmark_pdf(
    pdf_path: Path,
    backends: list[OCRBackendName],
    cfg: AppConfig,
    *,
    progress_cb=None,
) -> BenchmarkReport:
    """Run each backend on the same rasterized pages. No vault merge."""
    log.info("Benchmarking %d backends on %s", len(backends), pdf_path.name)
    page_images = pdf_to_images(pdf_path, dpi=cfg.ocr.dpi)

    report = BenchmarkReport(
        pdf_name=pdf_path.name,
        timestamp=datetime.now().strftime("%Y-%m-%d_%H-%M-%S"),
    )

    try:
        for name in backends:
            backend = build_backend(name, cfg)
            result = run_ocr(
                backend,
                page_images,
                max_concurrency=cfg.ocr.max_concurrency,
                max_retries=cfg.ocr.max_retries,
                retry_base_delay_seconds=cfg.ocr.retry_base_delay_seconds,
                progress_cb=progress_cb,
            )
            report.results.append(result)
    finally:
        cleanup_page_images(pdf_path)

    return report


def print_benchmark_table(report: BenchmarkReport, console: Console | None = None) -> None:
    console = console or Console()
    table = Table(title=f"OCR Benchmark — {report.pdf_name}", show_lines=True)
    table.add_column("Backend", style="bold cyan")
    table.add_column("Status")
    table.add_column("Pages", justify="right")
    table.add_column("Total time", justify="right")
    table.add_column("Time/page", justify="right")
    table.add_column("HW chars", justify="right")

    for r in report.results:
        status = "[red]ERROR[/red]" if r.error else "[green]OK[/green]"
        tpp = f"{r.elapsed_seconds / r.page_count:.1f}s" if r.page_count else "—"
        table.add_row(
            r.backend, status, str(r.page_count),
            f"{r.elapsed_seconds:.1f}s", tpp, str(len(r.handwritten_text)),
        )
    console.print(table)


def save_benchmark_report(report: BenchmarkReport, dest_dir: Path) -> Path:
    """Persist a markdown benchmark report. Returns the path."""
    slug = re.sub(r"[^\w]", "_", report.pdf_name)
    out_path = dest_dir / f"benchmark_{slug}_{report.timestamp}.md"
    lines: list[str] = [
        "# OCR Benchmark Report",
        "",
        f"**File:** `{report.pdf_name}`  ",
        f"**Date:** {report.timestamp}  ",
        f"**Backends tested:** {', '.join(r.backend for r in report.results)}",
        "",
        "---",
        "",
    ]

    for r in report.results:
        tpp = f"{r.elapsed_seconds / r.page_count:.2f}s" if r.page_count else "—"
        lines += [
            f"## Backend: `{r.backend}`",
            "",
            "| Metric | Value |",
            "|--------|-------|",
            f"| Status | {'ERROR' if r.error else 'OK'} |",
            f"| Pages | {r.page_count} |",
            f"| Total time | {r.elapsed_seconds:.2f}s |",
            f"| Time per page | {tpp} |",
            f"| Handwritten chars | {len(r.handwritten_text)} |",
            "",
        ]
        if r.error:
            lines += [f"**Error:** `{r.error}`", "", "---", ""]
        else:
            hw_preview = r.handwritten_text[:2000]
            if len(r.handwritten_text) > 2000:
                hw_preview += "\n... [truncated]"
            raw_preview = r.raw_text[:2000]
            if len(r.raw_text) > 2000:
                raw_preview += "\n... [truncated]"
            lines += [
                "### Extracted handwritten content",
                "",
                "```",
                hw_preview,
                "```",
                "",
                "### Full OCR output (first 2000 chars)",
                "",
                "```",
                raw_preview,
                "```",
                "",
                "---",
                "",
            ]

    dest_dir.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")
    log.info("Benchmark report saved: %s", out_path)
    return out_path
