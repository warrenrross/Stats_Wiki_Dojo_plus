"""Ollama-based vision OCR backends (olmOCR2 and llama3.2-vision)."""

from __future__ import annotations

import logging
import os
from pathlib import Path

import ollama

from notes_pipeline.config import OllamaOCRConfig
from notes_pipeline.ocr.prompts import OCR_PROMPT

log = logging.getLogger(__name__)


class OllamaOCRBackend:
    """Generic Ollama vision backend; pick model at construction."""

    def __init__(self, cfg: OllamaOCRConfig, model: str, name: str):
        self.cfg = cfg
        self.model = model
        self.name = name
        # Honor OLLAMA_HOST env var if set (e.g. for remote EVO-X2 server),
        # otherwise use the configured host.
        host = os.environ.get("OLLAMA_HOST", cfg.host)
        self.client = ollama.Client(host=host, timeout=cfg.request_timeout)

    def ocr_page(self, image_path: Path) -> str:
        with open(image_path, "rb") as f:
            image_bytes = f.read()

        response = self.client.chat(
            model=self.model,
            messages=[{
                "role": "user",
                "content": OCR_PROMPT,
                "images": [image_bytes],
            }],
            keep_alive=self.cfg.keep_alive,
            options={"temperature": 0.0},
        )
        text = response["message"]["content"]
        if not isinstance(text, str):
            raise RuntimeError(f"Unexpected Ollama response shape: {response!r}")
        return text


def olmocr_backend(cfg: OllamaOCRConfig) -> OllamaOCRBackend:
    return OllamaOCRBackend(cfg, model=cfg.olmocr_model, name="olmocr")


def llama_backend(cfg: OllamaOCRConfig) -> OllamaOCRBackend:
    return OllamaOCRBackend(cfg, model=cfg.llama_model, name="llama")
