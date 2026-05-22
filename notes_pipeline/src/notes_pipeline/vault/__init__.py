"""Vault matching, merging, frontmatter, MOC link updates."""
from notes_pipeline.vault.frontmatter import extract_tags_from_frontmatter
from notes_pipeline.vault.matching import find_source_note
from notes_pipeline.vault.merge import merge_annotations_into_vault
from notes_pipeline.vault.mocs import update_moc_links

__all__ = [
    "extract_tags_from_frontmatter",
    "find_source_note",
    "merge_annotations_into_vault",
    "update_moc_links",
]
