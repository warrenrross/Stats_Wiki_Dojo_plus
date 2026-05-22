"""Backend registry, orchestration, retries, and handwritten extraction."""

from __future__ import annotations

import logging
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from tenacity import (
    RetryError,
    Retrying,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from notes_pipeline.config import AppConfig, OCRBackendName
from notes_pipeline.ocr.base import OCRBackend, OCRResult
from notes_pipeline.ocr.claude import ClaudeOCRBackend
from notes_pipeline.ocr.ollama_backend import llama_backend, olmocr_backend

log = logging.getLogger(__name__)


_HANDWRITTEN_RE = re.compile(r"<handwritten>(.*?)</handwritten>", re.DOTALL | re.IGNORECASE)


def extract_handwritten_content(ocr_text: str) -> str:
    """Pull only the <handwritten>...</handwritten> tagged sections."""
    matches = _HANDWRITTEN_RE.findall(ocr_text)
    return "\n\n".join(m.strip() for m in matches if m.strip())


def build_backend(name: OCRBackendName, cfg: AppConfig) -> OCRBackend:
    if name == "claude":
        return ClaudeOCRBackend(cfg.ocr.claude)
    if name == "olmocr":
        return olmocr_backend(cfg.ocr.ollama)
    if name == "llama":
        return llama_backend(cfg.ocr.ollama)
    raise ValueError(f"Unknown backend: {name!r}")


def _ocr_one_with_retry(
    backend: OCRBackend,
    img: Path,
    max_retries: int,
    base_delay: float,
) -> str:
    try:
        for attempt in Retrying(
            stop=stop_after_attempt(max_retries),
            wait=wait_exponential(multiplier=base_delay, min=base_delay, max=30),
            retry=retry_if_exception_type(Exception),
            reraise=True,
        ):
            with attempt:
                return backend.ocr_page(img)
    except RetryError as e:  # pragma: no cover
        raise e.last_attempt.exception() from e
    raise RuntimeError("unreachable")


def run_ocr(
    backend: OCRBackend,
    page_images: list[Path],
    *,
    max_concurrency: int = 1,
    max_retries: int = 3,
    retry_base_delay_seconds: float = 2.0,
    progress_cb=None,
) -> OCRResult:
    """Run an OCR backend across all pages with retries and optional concurrency.

    progress_cb: optional callable(page_index, total, backend_name) called after each page.
    """
    total = len(page_images)
    log.info("[%s] OCR starting on %d pages (concurrency=%d)",
             backend.name, total, max_concurrency)
    start = time.perf_counter()
    page_texts: list[str | None] = [None] * total
    first_error: Exception | None = None

    def _do(i: int, img: Path):
        return i, _ocr_one_with_retry(
            backend, img, max_retries=max_retries, base_delay=retry_base_delay_seconds
        )

    if max_concurrency <= 1:
        for i, img in enumerate(page_images):
            try:
                _, text = _do(i, img)
                page_texts[i] = text
            except Exception as e:
                first_error = first_error or e
                log.error("[%s] page %d/%d failed: %s", backend.name, i + 1, total, e)
            if progress_cb:
                progress_cb(i + 1, total, backend.name)
    else:
        with ThreadPoolExecutor(max_workers=max_concurrency) as ex:
            futures = {ex.submit(_do, i, img): i for i, img in enumerate(page_images)}
            done = 0
            for fut in as_completed(futures):
                i = futures[fut]
                try:
                    _, text = fut.result()
                    page_texts[i] = text
                except Exception as e:
                    first_error = first_error or e
                    log.error("[%s] page %d/%d failed: %s", backend.name, i + 1, total, e)
                done += 1
                if progress_cb:
                    progress_cb(done, total, backend.name)

    elapsed = time.perf_counter() - start

    if first_error is not None and all(t is None for t in page_texts):
        return OCRResult(
            backend=backend.name,
            raw_text="",
            handwritten_text="",
            elapsed_seconds=elapsed,
            page_count=total,
            page_texts=[],
            error=str(first_error),
        )

    filled = [t or "" for t in page_texts]
    full_text = "\n\n---PAGE BREAK---\n\n".join(filled)
    handwritten = extract_handwritten_content(full_text)
    log.info(
        "[%s] Done in %.1fs | %d handwritten chars extracted",
        backend.name, elapsed, len(handwritten),
    )
    return OCRResult(
        backend=backend.name,
        raw_text=full_text,
        handwritten_text=handwritten,
        elapsed_seconds=elapsed,
        page_count=total,
        page_texts=filled,
        error=str(first_error) if first_error else None,
    )
