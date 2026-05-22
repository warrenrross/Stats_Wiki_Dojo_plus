from notes_pipeline.ocr.registry import extract_handwritten_content


def test_extracts_single_block():
    text = "intro <handwritten>this is\nmy note</handwritten> outro"
    assert extract_handwritten_content(text) == "this is\nmy note"


def test_extracts_multiple_blocks():
    text = (
        "before <handwritten>one</handwritten> middle "
        "<handwritten>two</handwritten> end"
    )
    assert extract_handwritten_content(text) == "one\n\ntwo"


def test_handles_no_blocks():
    assert extract_handwritten_content("just printed text") == ""


def test_strips_whitespace_only_blocks():
    text = "<handwritten>   \n\n   </handwritten><handwritten>real</handwritten>"
    assert extract_handwritten_content(text) == "real"


def test_dotall_handles_newlines():
    text = "<handwritten>line1\nline2\nline3</handwritten>"
    assert "line1\nline2\nline3" in extract_handwritten_content(text)


def test_case_insensitive_tags():
    text = "<Handwritten>case test</Handwritten>"
    assert extract_handwritten_content(text) == "case test"
