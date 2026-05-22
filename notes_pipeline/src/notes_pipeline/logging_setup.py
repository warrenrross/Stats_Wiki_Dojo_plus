"""Structured logging with rich formatting."""

from __future__ import annotations

import logging

from rich.logging import RichHandler


def setup_logging(verbose: bool = False) -> logging.Logger:
    level = logging.DEBUG if verbose else logging.INFO
    handler = RichHandler(
        rich_tracebacks=True,
        markup=True,
        show_time=True,
        show_level=True,
        show_path=False,
    )
    logging.basicConfig(
        level=level,
        format="%(message)s",
        datefmt="[%H:%M:%S]",
        handlers=[handler],
        force=True,
    )
    # Silence noisy third-party loggers
    for name in ("httpx", "httpcore", "urllib3", "anthropic", "watchdog"):
        logging.getLogger(name).setLevel(logging.WARNING)
    return logging.getLogger("notes_pipeline")
