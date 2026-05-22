"""Top-level pipeline: process one annotated PDF end-to-end."""

from __future__ import annotations

import json
import logging
import shutil
from dataclasses import asdict
from datetime import datetime
from pathlib import Path

import anthropic

from notes_pipeline.config import AppConfig, OCRBackendName
from notes_pipeline.ocr import build_backend
from notes_pipeline.ocr.base import OCRResult
from notes_pipeline.ocr.registry import run_ocr
from notes_pipeline.pdf import cleanup_page_images, file_fingerprint, pdf_to_images
from notes_pipeline.vault import (
    extract_tags_from_frontmatter,
    find_source_note,
    merge_annotations_into_vault,
    update_moc_links,
)

log = logging.getLogger(__name__)


def _state_file(cfg: AppConfig, pdf_path: Path) -> Path:
    fp = file_fingerprint(pdf_path)
    return cfg.paths.state / f"{pdf_path.stem}.{fp}.json"  # type: ignore[operator]


def already_processed(cfg: AppConfig, pdf_path: Path) -> bool:
    return _state_file(cfg, pdf_path).exists()


def mark_processed(cfg: AppConfig, pdf_path: Path, result: OCRResult, *,
                   note: Path | None) -> None:
    payload = {
        "pdf": str(pdf_path),
        "fingerprint": file_fingerprint(pdf_path),
        "processed_at": datetime.utcnow().isoformat() + "Z",
        "backend": result.backend,
        "elapsed_seconds": result.elapsed_seconds,
        "page_count": result.page_count,
        "handwritten_chars": len(result.handwritten_text),
        "source_note": str(note) if note else None,
        "error": result.error,
    }
    state_path = _state_file(cfg, pdf_path)
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def process_annotated_pdf(
    pdf_path: Path,
    cfg: AppConfig,
    *,
    backend_name: OCRBackendName | None = None,
    skip_merge: bool = False,
    dry_run: bool = False,
    force: bool = False,
    progress_cb=None,
) -> OCRResult:
    """Full pipeline for a single annotated PDF."""
    backend_name = backend_name or cfg.ocr.backend
    log.info("Processing [%s]: %s", backend_name, pdf_path.name)

    if not force and already_processed(cfg, pdf_path):
        log.info("Already processed (same fingerprint): %s — use --force to redo", pdf_path.name)
        return OCRResult(
            backend=backend_name, raw_text="", handwritten_text="",
            elapsed_seconds=0.0, page_count=0, error="already_processed",
        )

    backend = build_backend(backend_name, cfg)
    page_images = pdf_to_images(pdf_path, dpi=cfg.ocr.dpi)

    try:
        result = run_ocr(
            backend,
            page_images,
            max_concurrency=cfg.ocr.max_concurrency,
            max_retries=cfg.ocr.max_retries,
            retry_base_delay_seconds=cfg.ocr.retry_base_delay_seconds,
            progress_cb=progress_cb,
        )

        source_note: Path | None = None

        if not result.ok:
            log.error("OCR backend reported error: %s", result.error)
            return result

        if dry_run:
            log.info("[dry-run] OCR complete. Skipping vault merge and file move.")
            log.info("[dry-run] Handwritten preview:\n%s", result.handwritten_text[:500])
            return result

        if skip_merge:
            log.info("Skipping vault merge (--skip-merge). PDF will not be moved.")
            return result

        if not result.handwritten_text.strip():
            log.warning("No handwritten content detected — skipping vault merge.")
        else:
            source_note = find_source_note(pdf_path.stem, cfg.paths.vault)  # type: ignore[arg-type]
            if source_note is None:
                source_note = _create_new_vault_note(cfg, pdf_path)
                log.info("Created new vault note: %s", source_note.name)
            else:
                log.info("Matched vault note: %s", source_note.name)

            client = anthropic.Anthropic(
                **({"api_key": cfg.ocr.claude.api_key} if cfg.ocr.claude.api_key else {})
            )
            updated = merge_annotations_into_vault(
                source_note,
                result.handwritten_text,
                result.raw_text,
                merge_cfg=cfg.merge,
                claude_cfg=cfg.ocr.claude,
                client=client,
            )
            source_note.write_text(updated, encoding="utf-8")
            log.info("Updated vault note: %s", source_note.name)

            tags = extract_tags_from_frontmatter(updated)
            if tags:
                update_moc_links(cfg.paths.vault, source_note, tags)  # type: ignore[arg-type]

        # Move PDF to processed/
        dest = cfg.paths.processed / pdf_path.name  # type: ignore[operator]
        if dest.exists():
            stem, suffix = dest.stem, dest.suffix
            ts = datetime.now().strftime("%Y%m%d-%H%M%S")
            dest = dest.with_name(f"{stem}.{ts}{suffix}")
        shutil.move(str(pdf_path), str(dest))
        log.info("Moved to processed/: %s", dest.name)

        mark_processed(cfg, dest, result, note=source_note)
        return result

    finally:
        cleanup_page_images(pdf_path)


def _create_new_vault_note(cfg: AppConfig, pdf_path: Path) -> Path:
    new_note_path = cfg.paths.vault / (pdf_path.stem + ".md")  # type: ignore[operator]
    ts = datetime.now().strftime("%Y-%m-%d")
    new_note_path.write_text(
        f"---\ntitle: {pdf_path.stem}\ndate: {ts}\ntags: []\n---\n\n",
        encoding="utf-8",
    )
    return new_note_path


def result_to_dict(r: OCRResult) -> dict:
    return asdict(r)
