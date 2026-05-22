"""OCR backends."""
from notes_pipeline.ocr.base import OCRBackend, OCRResult
from notes_pipeline.ocr.registry import build_backend, extract_handwritten_content

__all__ = ["OCRBackend", "OCRResult", "build_backend", "extract_handwritten_content"]
