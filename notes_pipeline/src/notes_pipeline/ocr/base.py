"""OCR backend protocol and result types."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Protocol


@dataclass
class OCRResult:
    backend: str
    raw_text: str
    handwritten_text: str
    elapsed_seconds: float
    page_count: int
    page_texts: list[str] = field(default_factory=list)
    error: str | None = None

    @property
    def ok(self) -> bool:
        return self.error is None


class OCRBackend(Protocol):
    """Each backend implements per-page OCR. Orchestration handles multi-page + retries."""

    name: str

    def ocr_page(self, image_path: Path) -> str:
        ...
