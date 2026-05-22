from pathlib import Path

from notes_pipeline.vault.matching import find_source_note


def _write(p: Path, content: str = "x") -> Path:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content)
    return p


def test_exact_match(tmp_path: Path):
    note = _write(tmp_path / "lecture_03.md")
    assert find_source_note("lecture_03", tmp_path) == note


def test_strips_annotated_suffix(tmp_path: Path):
    note = _write(tmp_path / "lecture_03.md")
    assert find_source_note("lecture_03-annotated", tmp_path) == note
    assert find_source_note("lecture_03_annotated", tmp_path) == note


def test_recursive_case_insensitive(tmp_path: Path):
    note = _write(tmp_path / "subdir" / "Lecture_03.md")
    assert find_source_note("lecture_03", tmp_path) == note


def test_strips_timestamp_suffix(tmp_path: Path):
    note = _write(tmp_path / "lecture_03.md")
    assert find_source_note("lecture_03-annotated_2025-05-12", tmp_path) == note


def test_no_match_returns_none(tmp_path: Path):
    _write(tmp_path / "other.md")
    assert find_source_note("missing", tmp_path) is None
