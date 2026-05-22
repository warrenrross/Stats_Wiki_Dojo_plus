# notes-pipeline

Annotated-PDF → Obsidian vault pipeline with pluggable OCR backends.

This is the refactored v0.2 package. The original single-file script
(`notes_pipeline.py`) has been split into a small Python package with a typed
config, structured logging, retries, concurrency, resumable processing,
a `doctor` health-check command, and a pytest suite for pure functions.

## Quick start (MacBook, Apple Silicon)

```bash
# Install uv (Python toolchain manager)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install pixi (system package manager via conda-forge)
curl -fsSL https://pixi.sh/install.sh | sh

# System deps via pixi
pixi global install poppler pandoc

# LaTeX support for notes render (optional, large download — skip if unneeded)
pixi global install texlive-core

# Ollama — use the official installer (not available on conda-forge)
curl -fsSL https://ollama.com/install.sh | sh

# Python package
git clone <this repo> notes-pipeline
cd notes-pipeline
uv venv && source .venv/bin/activate
uv pip install -e ".[dev]"

# Pull local OCR models
ollama serve &
ollama pull richardyoung/olmocr2:7b-q8
ollama pull llama3.2-vision:11b

# Config (optional — defaults Just Work)
mkdir -p ~/.config/notes_pipeline
cp config.example.toml ~/.config/notes_pipeline/config.toml

# Set your Claude key (for the merge step, or the claude backend)
export ANTHROPIC_API_KEY=sk-ant-...

# Verify environment
notes doctor

# Run the watcher
notes watch --ocr olmocr
```

## Commands

| Command | Purpose |
|---|---|
| `notes watch --ocr {claude,olmocr,llama}` | Watch the inbox and process new PDFs |
| `notes process FILE.pdf [--ocr ...] [--dry-run] [--force]` | One-shot |
| `notes benchmark FILE.pdf [-b olmocr -b claude]` | Side-by-side OCR comparison |
| `notes render note.md` | Render a vault note to PDF for the iPad |
| `notes doctor` | Verify all dependencies are present and reachable |

See **CLAUDE_CODE_SPEC.md** for the full setup spec for Claude Code.
