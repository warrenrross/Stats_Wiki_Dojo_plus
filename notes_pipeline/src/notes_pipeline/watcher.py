"""Watchdog-based inbox watcher with debounced settle and resumable state."""

from __future__ import annotations

import logging
import threading
import time
from pathlib import Path

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from notes_pipeline.config import AppConfig, OCRBackendName
from notes_pipeline.pipeline import process_annotated_pdf

log = logging.getLogger(__name__)


class InboxHandler(FileSystemEventHandler):
    def __init__(self, cfg: AppConfig, backend: OCRBackendName):
        super().__init__()
        self.cfg = cfg
        self.backend = backend
        self._lock = threading.Lock()
        self._in_flight: set[str] = set()

    def _is_pdf(self, p: Path) -> bool:
        return p.suffix.lower() == ".pdf" and not p.name.startswith(".")

    def _claim(self, p: Path) -> bool:
        with self._lock:
            key = str(p)
            if key in self._in_flight:
                return False
            self._in_flight.add(key)
            return True

    def _release(self, p: Path) -> None:
        with self._lock:
            self._in_flight.discard(str(p))

    def _wait_until_stable(self, p: Path, settle: int) -> bool:
        """Wait until the file has stopped growing for `settle` seconds."""
        last_size = -1
        deadline = time.time() + 600  # 10 min absolute cap
        while time.time() < deadline:
            if not p.exists():
                return False
            try:
                size = p.stat().st_size
            except OSError:
                return False
            if size == last_size and size > 0:
                return True
            last_size = size
            time.sleep(settle)
        return False

    def _handle(self, p: Path) -> None:
        if not self._claim(p):
            return
        try:
            log.info("New PDF detected: %s — waiting for it to settle...", p.name)
            if not self._wait_until_stable(p, self.cfg.watch.settle_seconds):
                log.warning("File never stabilized or disappeared: %s", p)
                return
            if not p.exists():
                return
            try:
                process_annotated_pdf(p, self.cfg, backend_name=self.backend)
            except Exception:
                log.exception("Pipeline failed for %s", p.name)
        finally:
            self._release(p)

    def on_created(self, event):
        if event.is_directory:
            return
        p = Path(event.src_path)
        if self._is_pdf(p):
            threading.Thread(target=self._handle, args=(p,), daemon=True).start()

    def on_moved(self, event):
        if event.is_directory:
            return
        dest = Path(event.dest_path)
        if self._is_pdf(dest):
            threading.Thread(target=self._handle, args=(dest,), daemon=True).start()


def run_watch(cfg: AppConfig, backend: OCRBackendName) -> None:
    inbox = cfg.paths.inbox
    log.info("Watching %s with backend %s", inbox, backend)

    # Drain any pre-existing PDFs first
    handler = InboxHandler(cfg, backend)
    for existing in sorted(inbox.glob("*.pdf")):  # type: ignore[union-attr]
        log.info("Found pre-existing PDF in inbox: %s", existing.name)
        threading.Thread(target=handler._handle, args=(existing,), daemon=True).start()

    observer = Observer()
    observer.schedule(handler, str(inbox), recursive=cfg.watch.recursive)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        log.info("Stopping watcher...")
        observer.stop()
    observer.join()
