"""Typed configuration with TOML + environment variable support.

Resolution order (later wins):
1. Defaults defined on the model
2. ~/.config/notes_pipeline/config.toml  (or path from $NOTES_PIPELINE_CONFIG)
3. Environment variables (NOTES_* with __ as nested delimiter)
"""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

if sys.version_info >= (3, 11):
    import tomllib
else:  # pragma: no cover
    import tomli as tomllib


OCRBackendName = Literal["claude", "olmocr", "llama"]


def _expand(p: str | Path) -> Path:
    return Path(os.path.expandvars(str(p))).expanduser().resolve()


# ── Sub-models ────────────────────────────────────────────────────────────────


class PathsConfig(BaseModel):
    root: Path = Path("~/notes")
    vault: Path | None = None
    inbox: Path | None = None
    rendered: Path | None = None
    processed: Path | None = None
    benchmarks: Path | None = None
    state: Path | None = None

    @field_validator("root", "vault", "inbox", "rendered", "processed", "benchmarks", "state",
                     mode="before")
    @classmethod
    def _expand_paths(cls, v):
        if v is None:
            return None
        return _expand(v)

    def resolved(self) -> "PathsConfig":
        """Fill in any unset folders relative to root."""
        root = _expand(self.root)
        return PathsConfig(
            root=root,
            vault=self.vault or root / "vault",
            inbox=self.inbox or root / "inbox",
            rendered=self.rendered or root / "rendered",
            processed=self.processed or root / "processed",
            benchmarks=self.benchmarks or root / "benchmarks",
            state=self.state or root / ".state",
        )

    def ensure(self) -> None:
        for p in (self.vault, self.inbox, self.rendered, self.processed,
                  self.benchmarks, self.state):
            assert p is not None
            p.mkdir(parents=True, exist_ok=True)


class ClaudeOCRConfig(BaseModel):
    model: str = "claude-sonnet-4-5"
    max_tokens: int = 4096
    api_key: str | None = None  # falls back to ANTHROPIC_API_KEY


class OllamaOCRConfig(BaseModel):
    host: str = "http://localhost:11434"
    olmocr_model: str = "richardyoung/olmocr2:7b-q8"
    llama_model: str = "llama3.2-vision:11b"
    keep_alive: str = "30m"
    request_timeout: int = 300


class OCRConfig(BaseModel):
    backend: OCRBackendName = "olmocr"
    dpi: int = 200
    max_concurrency: int = 2
    max_retries: int = 3
    retry_base_delay_seconds: float = 2.0
    claude: ClaudeOCRConfig = Field(default_factory=ClaudeOCRConfig)
    ollama: OllamaOCRConfig = Field(default_factory=OllamaOCRConfig)


class MergeConfig(BaseModel):
    model: str = "claude-sonnet-4-5"
    max_tokens: int = 8000
    ocr_context_chars: int = 6000


class WatchConfig(BaseModel):
    settle_seconds: int = 5
    recursive: bool = False


class RenderConfig(BaseModel):
    pdf_engine: str = "xelatex"
    geometry: str = "margin=1in"
    fontsize: str = "12pt"


# ── Root settings ─────────────────────────────────────────────────────────────


class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="NOTES_",
        env_nested_delimiter="__",
        extra="ignore",
    )

    paths: PathsConfig = Field(default_factory=PathsConfig)
    ocr: OCRConfig = Field(default_factory=OCRConfig)
    merge: MergeConfig = Field(default_factory=MergeConfig)
    watch: WatchConfig = Field(default_factory=WatchConfig)
    render: RenderConfig = Field(default_factory=RenderConfig)

    @classmethod
    def load(cls, config_path: Path | None = None) -> "AppConfig":
        """Load configuration, merging defaults with optional TOML file."""
        if config_path is None:
            env_path = os.environ.get("NOTES_PIPELINE_CONFIG")
            if env_path:
                config_path = Path(env_path).expanduser()
            else:
                default = Path("~/.config/notes_pipeline/config.toml").expanduser()
                if default.exists():
                    config_path = default

        data: dict = {}
        if config_path and config_path.exists():
            with open(config_path, "rb") as fh:
                data = tomllib.load(fh)

        cfg = cls(**data)
        cfg.paths = cfg.paths.resolved()
        return cfg


__all__ = [
    "AppConfig",
    "OCRBackendName",
    "PathsConfig",
    "OCRConfig",
    "ClaudeOCRConfig",
    "OllamaOCRConfig",
    "MergeConfig",
    "WatchConfig",
    "RenderConfig",
]
