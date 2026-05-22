import os
from pathlib import Path

from notes_pipeline.config import AppConfig


def test_defaults_load():
    cfg = AppConfig()
    assert cfg.ocr.backend in ("claude", "olmocr", "llama")
    assert cfg.ocr.dpi == 200


def test_path_resolution(tmp_path: Path):
    cfg = AppConfig()
    cfg.paths.root = tmp_path
    cfg.paths = cfg.paths.resolved()
    assert cfg.paths.vault == tmp_path / "vault"
    assert cfg.paths.inbox == tmp_path / "inbox"


def test_load_from_toml(tmp_path: Path):
    cfg_file = tmp_path / "config.toml"
    cfg_file.write_text(
        "[paths]\n"
        f"root = \"{tmp_path}\"\n\n"
        "[ocr]\n"
        "backend = \"llama\"\n"
        "dpi = 300\n"
    )
    cfg = AppConfig.load(cfg_file)
    assert cfg.ocr.backend == "llama"
    assert cfg.ocr.dpi == 300
    assert cfg.paths.vault == tmp_path / "vault"


def test_env_override(tmp_path: Path, monkeypatch):
    monkeypatch.setenv("NOTES_OCR__BACKEND", "claude")
    monkeypatch.setenv("NOTES_OCR__DPI", "250")
    cfg = AppConfig.load()
    assert cfg.ocr.backend == "claude"
    assert cfg.ocr.dpi == 250
