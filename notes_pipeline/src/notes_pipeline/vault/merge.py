"""Claude-driven vault merge step."""

from __future__ import annotations

import logging
from pathlib import Path

import anthropic

from notes_pipeline.config import ClaudeOCRConfig, MergeConfig
from notes_pipeline.ocr.prompts import MERGE_SYSTEM_PROMPT

log = logging.getLogger(__name__)


def merge_annotations_into_vault(
    source_note: Path,
    handwritten_text: str,
    full_ocr_text: str,
    *,
    merge_cfg: MergeConfig,
    claude_cfg: ClaudeOCRConfig,
    client: anthropic.Anthropic | None = None,
) -> str:
    """Use Claude to merge handwritten annotations into an existing vault note."""
    if client is None:
        kwargs = {"api_key": claude_cfg.api_key} if claude_cfg.api_key else {}
        client = anthropic.Anthropic(**kwargs)

    existing_content = source_note.read_text(encoding="utf-8")
    truncated_ocr = full_ocr_text[: merge_cfg.ocr_context_chars]

    user_prompt = (
        "Here is the existing vault note:\n\n"
        f"<existing_note>\n{existing_content}\n</existing_note>\n\n"
        "Here is the handwritten content extracted from the annotated PDF:\n\n"
        f"<handwritten_annotations>\n{handwritten_text}\n</handwritten_annotations>\n\n"
        "For additional context, here is the full OCR of all pages (truncated):\n\n"
        f"<full_ocr>\n{truncated_ocr}\n</full_ocr>\n\n"
        "Merge the handwritten annotations into the existing note following the rules above. "
        "Return the complete updated markdown."
    )

    message = client.messages.create(
        model=merge_cfg.model,
        max_tokens=merge_cfg.max_tokens,
        messages=[{"role": "user", "content": user_prompt}],
        system=MERGE_SYSTEM_PROMPT,
    )
    parts = [b.text for b in message.content if getattr(b, "type", None) == "text"]
    if not parts:
        raise RuntimeError("Claude merge returned no text content")
    return "\n".join(parts)
