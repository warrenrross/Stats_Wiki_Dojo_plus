"""Maps-of-Content updater."""

from __future__ import annotations

import logging
from pathlib import Path

log = logging.getLogger(__name__)


def update_moc_links(vault_dir: Path, updated_note: Path, tags: list[str]) -> list[Path]:
    """Append a wiki-link to ``MOC - <tag>.md`` for each tag, if the link isn't already there.

    Returns the list of MOCs that were modified.
    """
    modified: list[Path] = []
    for tag in tags:
        moc_path = vault_dir / f"MOC - {tag}.md"
        if not moc_path.exists():
            continue
        content = moc_path.read_text(encoding="utf-8")
        link = f"- [[{updated_note.stem}]]"
        if updated_note.stem in content:
            continue
        sep = "" if content.endswith("\n") else "\n"
        moc_path.write_text(content + sep + link + "\n", encoding="utf-8")
        modified.append(moc_path)
        log.info("Updated MOC: %s", moc_path.name)
    return modified
