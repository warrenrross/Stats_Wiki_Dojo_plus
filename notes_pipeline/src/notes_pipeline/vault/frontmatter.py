"""YAML frontmatter helpers."""

from __future__ import annotations

import frontmatter


def extract_tags_from_frontmatter(markdown: str) -> list[str]:
    """Read the ``tags`` field from YAML frontmatter; return a flat list of strings."""
    try:
        post = frontmatter.loads(markdown)
    except Exception:
        return []
    tags = post.get("tags", [])
    if tags is None:
        return []
    if isinstance(tags, list):
        return [str(t) for t in tags if t]
    return [str(tags)]
