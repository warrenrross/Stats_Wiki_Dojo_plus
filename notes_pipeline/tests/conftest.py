"""Shared pytest fixtures."""

from __future__ import annotations

from pathlib import Path

import pytest

from notes_pipeline.config import AppConfig


@pytest.fixture
def tmp_cfg(tmp_path: Path) -> AppConfig:
    """A minimal AppConfig pointing at a temp directory."""
    cfg = AppConfig()
    cfg.paths.root = tmp_path
    cfg.paths = cfg.paths.resolved()
    cfg.paths.ensure()
    return cfg
