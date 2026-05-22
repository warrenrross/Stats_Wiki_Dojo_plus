"""PDF rasterization and pandoc rendering."""

from __future__ import annotations

import hashlib
import logging
import shutil
import subprocess
from pathlib import Path

from pdf2image import convert_from_path

from notes_pipeline.config import RenderConfig

log = logging.getLogger(__name__)


def file_fingerprint(path: Path) -> str:
    """Stable hash of file contents for caching/state."""
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()[:16]


def pdf_to_images(pdf_path: Path, dpi: int = 200, out_dir: Path | None = None) -> list[Path]:
    """Rasterize each PDF page to PNG.

    Returns list of image paths in page order.
    """
    out_dir = out_dir or (pdf_path.parent / f"{pdf_path.stem}_pages")
    out_dir.mkdir(parents=True, exist_ok=True)

    pages = convert_from_path(str(pdf_path), dpi=dpi)
    paths: list[Path] = []
    for i, page in enumerate(pages):
        p = out_dir / f"page_{i + 1:03d}.png"
        page.save(str(p), "PNG")
        paths.append(p)
    log.info("Rasterized %s → %d pages @ %ddpi", pdf_path.name, len(paths), dpi)
    return paths


def cleanup_page_images(pdf_path: Path, out_dir: Path | None = None) -> None:
    target = out_dir or (pdf_path.parent / f"{pdf_path.stem}_pages")
    if target.exists():
        shutil.rmtree(target, ignore_errors=True)


def render_markdown_to_pdf(md_path: Path, dest_dir: Path, cfg: RenderConfig) -> Path:
    """Convert a markdown file to PDF using pandoc."""
    if shutil.which("pandoc") is None:
        raise RuntimeError("pandoc not found on PATH. Install with `brew install pandoc basictex`.")
    out_pdf = dest_dir / (md_path.stem + ".pdf")
    cmd = [
        "pandoc", str(md_path),
        "-o", str(out_pdf),
        f"--pdf-engine={cfg.pdf_engine}",
        "-V", f"geometry:{cfg.geometry}",
        "-V", f"fontsize={cfg.fontsize}",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(f"Pandoc failed (code {result.returncode}):\n{result.stderr}")
    log.info("Rendered %s → %s", md_path.name, out_pdf.name)
    return out_pdf
