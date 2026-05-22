from notes_pipeline.ocr.prompts import MERGE_SYSTEM_PROMPT, OCR_PROMPT


def test_ocr_prompt_mentions_handwritten_tag():
    assert "<handwritten>" in OCR_PROMPT
    assert "</handwritten>" in OCR_PROMPT


def test_ocr_prompt_mentions_latex():
    assert "LaTeX" in OCR_PROMPT


def test_merge_prompt_preserves_existing():
    assert "Preserve all existing content" in MERGE_SYSTEM_PROMPT
    assert "WikiLinks" in MERGE_SYSTEM_PROMPT
