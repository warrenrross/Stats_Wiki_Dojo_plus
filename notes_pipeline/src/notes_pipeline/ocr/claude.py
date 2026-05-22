"""Claude vision OCR backend."""

from __future__ import annotations

import base64
import logging
from pathlib import Path

import anthropic

from notes_pipeline.config import ClaudeOCRConfig
from notes_pipeline.ocr.prompts import OCR_PROMPT

log = logging.getLogger(__name__)


class ClaudeOCRBackend:
    name = "claude"

    def __init__(self, cfg: ClaudeOCRConfig, client: anthropic.Anthropic | None = None):
        self.cfg = cfg
        if client is None:
            kwargs = {"api_key": cfg.api_key} if cfg.api_key else {}
            client = anthropic.Anthropic(**kwargs)
        self.client = client

    def ocr_page(self, image_path: Path) -> str:
        with open(image_path, "rb") as f:
            image_data = base64.standard_b64encode(f.read()).decode("utf-8")

        message = self.client.messages.create(
            model=self.cfg.model,
            max_tokens=self.cfg.max_tokens,
            messages=[{
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/png",
                            "data": image_data,
                        },
                    },
                    {"type": "text", "text": OCR_PROMPT},
                ],
            }],
        )
        # Concatenate any text blocks defensively
        parts = [b.text for b in message.content if getattr(b, "type", None) == "text"]
        if not parts:
            raise RuntimeError("Claude returned no text blocks")
        return "\n".join(parts)
