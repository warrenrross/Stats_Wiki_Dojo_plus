from pathlib import Path

from notes_pipeline.vault.mocs import update_moc_links


def test_appends_link_when_moc_exists(tmp_path: Path):
    (tmp_path / "MOC - math.md").write_text("# Math MOC\n- [[older]]\n")
    note = tmp_path / "lecture_03.md"
    note.write_text("x")

    modified = update_moc_links(tmp_path, note, ["math"])
    assert modified == [tmp_path / "MOC - math.md"]
    content = (tmp_path / "MOC - math.md").read_text()
    assert "- [[lecture_03]]" in content


def test_skips_when_link_already_present(tmp_path: Path):
    (tmp_path / "MOC - math.md").write_text("- [[lecture_03]]\n")
    note = tmp_path / "lecture_03.md"
    note.write_text("x")
    modified = update_moc_links(tmp_path, note, ["math"])
    assert modified == []


def test_no_moc_file_is_noop(tmp_path: Path):
    note = tmp_path / "lecture_03.md"
    note.write_text("x")
    assert update_moc_links(tmp_path, note, ["math"]) == []
