"""Match an annotated PDF to its source vault note."""

from __future__ import annotations

import re
from pathlib import Path

_ANNOTATED_SUFFIX = re.compile(r"[_\-\s]annotated$", re.IGNORECASE)
_TS_SUFFIX = re.compile(r"[_\-]\d{4}-\d{2}-\d{2}([_\-T]\d{2}[-:_]\d{2}([-:_]\d{2})?)?$")


def _candidates(stem: str) -> list[str]:
    """Return progressively-stripped stems to try when matching.

    Strips, in order: trailing timestamp, ``-annotated`` suffix, and any
    combination thereof. Returns unique candidates preserving order.
    """
    s = stem.strip()
    out: list[str] = [s]

    def _push(x: str) -> None:
        if x and x not in out:
            out.append(x)

    # Strip timestamp then annotated
    ts_first = _TS_SUFFIX.sub("", s)
    _push(ts_first)
    _push(_ANNOTATED_SUFFIX.sub("", ts_first))

    # Strip annotated then timestamp (alternate order, in case file is named
    # "lecture_03_2025-05-12-annotated")
    ann_first = _ANNOTATED_SUFFIX.sub("", s)
    _push(ann_first)
    _push(_TS_SUFFIX.sub("", ann_first))

    return out


def find_source_note(pdf_stem: str, vault_dir: Path) -> Path | None:
    """Find the vault markdown file corresponding to an annotated PDF stem.

    Search strategy:
    1. Exact match: vault/<stem>.md
    2. Strip common ``-annotated`` / ``_annotated`` suffix
    3. Strip trailing iPad timestamp suffix
    4. Case-insensitive recursive search
    """
    for cand in _candidates(pdf_stem):
        p = vault_dir / f"{cand}.md"
        if p.exists():
            return p

    lower_candidates = {c.lower() for c in _candidates(pdf_stem)}
    for note in vault_dir.rglob("*.md"):
        if note.stem.lower() in lower_candidates:
            return note
    return None
