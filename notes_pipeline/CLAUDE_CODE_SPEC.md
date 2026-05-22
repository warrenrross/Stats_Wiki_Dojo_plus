# Claude Code Working Spec — Ollama + `notes-pipeline` on macOS

**Owner:** Warren Ross
**Target machine:** MacBook (Apple Silicon, M1 or newer)
**Goal:** Stand up a local OCR + Obsidian-merge pipeline that watches `~/notes/inbox/` for annotated PDFs from the iPad, extracts handwritten content with a local vision model (or Claude API), and merges the result into the user's Obsidian vault using Claude.

This document is the **single source of truth** for Claude Code. Read it top to bottom and execute the phases in order. Stop and report status at every checkpoint marked with **STOP**.

---

## 0. Operating rules for Claude Code

1. **Do not invent commands.** Every shell command you run must be either listed in this spec or a direct, documented follow-up to one that is.
2. **Never run `rm -rf` outside `~/notes` or the project repo.** Treat `~/notes/vault/` as user data — never delete vault files.
3. **One phase at a time.** After each phase, run its verification step. If verification fails, stop and report.
4. **Idempotency.** Every phase must be safely re-runnable. Detect existing state before doing work.
5. **No silent fallbacks.** If a model or tool is unavailable, fail loudly with the exact error and suggested fix.
6. **Use the project virtualenv** (`./.venv`) for all Python work. Never `pip install` into the system Python.
7. **macOS only.** Skip any Linux/ROCm/EVO-X2 instructions in the original setup guide — they are out of scope.

---

## 1. Deliverables (definition of done)

When you are done, the following must all be true:

- [ ] `uv` installed (Python toolchain), `pixi` installed (system packages via conda-forge), and `poppler`, `pandoc`, `texlive-core`, `ollama` are present.
- [ ] Ollama is running locally at `http://localhost:11434` and is set to launch at login.
- [ ] Both vision models are pulled: `richardyoung/olmocr2:7b-q8` and `llama3.2-vision:11b`.
- [ ] `OLLAMA_KEEP_ALIVE=30m` is exported in `~/.zshrc`.
- [ ] `ANTHROPIC_API_KEY` is exported (you will prompt the user for it once, do **not** persist it to git).
- [ ] The repo `notes_pipeline/` is checked out under `~/code/notes-pipeline` (or wherever the user prefers).
- [ ] A Python 3.11+ virtualenv lives at `./.venv` with the package installed editable (`pip install -e ".[dev]"`).
- [ ] `notes doctor` reports **all green** ticks.
- [ ] `pytest -q` is **all green** (27 tests).
- [ ] A test annotated PDF runs through `notes process` end-to-end and the user's vault is updated (only attempt if the user provides a test PDF).
- [ ] A LaunchAgent (`com.warren.notes-pipeline.watch.plist`) is installed and loaded so `notes watch` starts at login.

---

## 2. Inventory — what's in this repo

```
notes_pipeline/
├── pyproject.toml                  # package definition; entry point: `notes`
├── README.md
├── CLAUDE_CODE_SPEC.md             # this file
├── config.example.toml             # TOML configuration template
├── src/notes_pipeline/
│   ├── __init__.py
│   ├── __main__.py                 # `python -m notes_pipeline`
│   ├── cli.py                      # Typer CLI: watch / process / benchmark / render / doctor
│   ├── config.py                   # Pydantic config + TOML loader + env overrides
│   ├── logging_setup.py            # Rich-formatted structured logging
│   ├── pdf.py                      # pdf2image rasterization + pandoc render + fingerprint
│   ├── pipeline.py                 # process_annotated_pdf — full pipeline + resumable state
│   ├── benchmark.py                # multi-backend comparison reports
│   ├── watcher.py                  # watchdog-based inbox watcher (debounced, threaded)
│   ├── ocr/
│   │   ├── base.py                 # OCRBackend protocol, OCRResult dataclass
│   │   ├── prompts.py              # OCR_PROMPT, MERGE_SYSTEM_PROMPT
│   │   ├── claude.py               # Anthropic vision OCR
│   │   ├── ollama_backend.py       # olmOCR2 + llama3.2-vision via ollama
│   │   └── registry.py             # build_backend, run_ocr (retries + concurrency)
│   └── vault/
│       ├── matching.py             # find_source_note (handles -annotated, timestamps, recursion)
│       ├── frontmatter.py
│       ├── mocs.py                 # Maps-of-Content updater
│       └── merge.py                # Claude-driven vault merge
└── tests/                          # 27 pytest unit tests covering pure functions
```

### Key improvements over the original script

| Area | Before | After |
|---|---|---|
| Structure | Single 659-line file | Small package, single-responsibility modules |
| Config | Hard-coded module constants | Pydantic + TOML + `NOTES_*` env vars |
| OCR backends | If/elif chain, no retries | `OCRBackend` protocol, tenacity retries, optional concurrency |
| Watcher | `set()` of seen paths, fixed sleep | Debounced "wait until file stops growing" + threaded worker per file |
| Resumability | None — re-processing duplicates work | SHA-256 fingerprint state in `~/notes/.state/` |
| Logging | `logging.basicConfig` | Rich-formatted logs, third-party noise silenced |
| Health check | None | `notes doctor` verifies dirs + pandoc + poppler + Anthropic key + Ollama models |
| Test coverage | None | 27 pytest tests for pure functions |
| CLI | argparse | Typer with `--dry-run`, `--force`, `--skip-merge`, `--verbose` |
| Claude model | `claude-sonnet-4-20250514` (stale alias) | `claude-sonnet-4-5` (configurable) |
| Defensive parsing | `message.content[0].text` (fails on tool blocks) | Filters to `type == "text"` blocks |
| Vault matching | 3 hard-coded strategies | Strips `-annotated`, ISO timestamps, recurses case-insensitively |
| File move on duplicate | Would overwrite in `processed/` | Suffixes with timestamp |

---

## 3. Phase A — System prerequisites (macOS)

### A.1 Confirm Apple Silicon and macOS version

```bash
system_profiler SPHardwareDataType | grep -E "Chip|System Version|macOS"
sw_vers
```

Expected: chip starts with `Apple M` and macOS ≥ 12 (Monterey). If Intel Mac, **STOP** and report — Ollama will not GPU-accelerate.

### A.2 Install uv and pixi if missing

`uv` manages Python environments; `pixi` (via conda-forge) manages system-level binaries.

```bash
# uv — Python toolchain manager
curl -LsSf https://astral.sh/uv/install.sh | sh

# pixi — system package manager (conda-forge)
curl -fsSL https://pixi.sh/install.sh | sh

# Reload shell env (or open a new terminal)
source ~/.zshrc
uv --version && pixi --version    # both expect 0.4 or newer
```

### A.3 Install system dependencies

```bash
pixi global install poppler pandoc
pixi global install texlive-core   # only if pandoc PDF render is desired; harmless to skip if user declines

# Ollama is not available on conda-forge — use the official installer
curl -fsSL https://ollama.com/install.sh | sh
```

**Note:** `basictex` is large (~100MB). If the user doesn't plan to use `notes render`, you may skip it and document the omission. Mark this as a question in your status report rather than auto-deciding.

### A.4 Start Ollama and set it to launch at login

The official installer places a menu-bar app on your Mac. Launch it and enable **Launch at Login** in its preferences, or start the daemon from the terminal:

```bash
ollama serve &

# Verify
curl -fsS http://localhost:11434/api/tags >/dev/null && echo "Ollama OK"
```

**STOP — Checkpoint A.** Report: macOS version, chip, uv version, pixi version, ollama version, whether `curl :11434` succeeded.

---

## 4. Phase B — Pull OCR models

```bash
ollama pull richardyoung/olmocr2:7b-q8     # ~8.9 GB, primary
ollama pull llama3.2-vision:11b            # ~7.9 GB, benchmark fallback
ollama list
```

Expected output of `ollama list` contains both names. If a pull fails halfway, just re-run it — Ollama resumes.

### B.1 Configure keep-alive

```bash
# Persist for new shells
grep -q "OLLAMA_KEEP_ALIVE" ~/.zshrc || echo 'export OLLAMA_KEEP_ALIVE="30m"' >> ~/.zshrc

# Apply immediately: export for launchd, then restart the daemon
launchctl setenv OLLAMA_KEEP_ALIVE "30m"
pkill ollama 2>/dev/null; sleep 1; ollama serve &
```

**STOP — Checkpoint B.** Report `ollama list` output and the line you appended to `.zshrc`.

---

## 5. Phase C — Get the project on disk

### C.1 Choose a location

Default: `~/code/notes-pipeline`. If the user has a preferred location, use it. Ask if uncertain.

### C.2 Place the files

The user has handed you the contents of this package. Either:

- **(A)** They cloned a git repo containing this tree — just `cd` into it; or
- **(B)** They handed you a zip — extract it into the chosen location and `cd` in.

Confirm the layout matches **Section 2**. If anything is missing, stop and report rather than guessing.

### C.3 Create the virtualenv and install editable

```bash
uv --version    # require 0.4+; uv manages Python 3.11+ automatically
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"
```

### C.4 Run the unit tests

```bash
pytest -q
```

Expected: `27 passed`. If any test fails, **STOP** and report the failure verbatim. Do **not** "fix" tests — they're the contract.

**STOP — Checkpoint C.** Report Python version, virtualenv path, and pytest summary.

---

## 6. Phase D — Configuration

### D.1 Create the config directory and copy the example

```bash
mkdir -p ~/.config/notes_pipeline
[ -f ~/.config/notes_pipeline/config.toml ] || cp config.example.toml ~/.config/notes_pipeline/config.toml
```

Open the config and make these decisions with the user:

- `paths.root` — confirm `~/notes` or pick another location.
- `ocr.backend` — recommend `olmocr` as the default for local handwriting; `claude` if accuracy matters more than cost.
- `ocr.dpi` — `200` is good; bump to `300` only if handwriting is small/dense.
- `ocr.max_concurrency` — leave at `2` on Apple Silicon for olmocr/llama; set to `4` only for `claude` on a fast network.
- `merge.model` — leave at `claude-sonnet-4-5`.

**Do not** put the API key in this file unless the user specifically asks to. Prefer the environment variable.

### D.2 Set the Anthropic API key

```bash
# Add to ~/.zshrc (you must ask the user for the key — never invent one)
grep -q "ANTHROPIC_API_KEY" ~/.zshrc || echo 'export ANTHROPIC_API_KEY="<paste user's key>"' >> ~/.zshrc
```

If the user does not want to use Claude at all, skip this and choose `olmocr` as the default backend. The merge step still requires Claude — flag this clearly.

### D.3 Create the folder layout

The `doctor` command will do this automatically, but to be explicit:

```bash
mkdir -p ~/notes/{vault,inbox,rendered,processed,benchmarks,.state}
```

### D.4 (Optional) Hook the inbox to iCloud Drive

If the user wants iPad → inbox via iCloud:

```bash
# Replace the local inbox with a symlink to the iCloud-synced folder
ICLOUD="$HOME/Library/Mobile Documents/com~apple~CloudDocs/notes-inbox"
mkdir -p "$ICLOUD"
[ -L ~/notes/inbox ] || { rm -rf ~/notes/inbox && ln -s "$ICLOUD" ~/notes/inbox; }
```

Ask the user before doing this — they may want the inbox elsewhere (Dropbox, plain folder, etc.).

**STOP — Checkpoint D.** Show `notes doctor` output (it will fail until Phase E).

---

## 7. Phase E — Run `notes doctor` and resolve issues

```bash
source .venv/bin/activate
notes doctor
```

Every tick must be green. Resolution table:

| Failure | Fix |
|---|---|
| `pandoc: NOT FOUND` | `pixi global install pandoc` |
| `pdftoppm: NOT FOUND` | `pixi global install poppler` |
| `ANTHROPIC_API_KEY NOT set` | export in `~/.zshrc`, then `source ~/.zshrc` |
| `Ollama unreachable` | Launch the Ollama app or run `ollama serve &` |
| `richardyoung/olmocr2:7b-q8 NOT pulled` | `ollama pull richardyoung/olmocr2:7b-q8` |
| `llama3.2-vision:11b NOT pulled` | `ollama pull llama3.2-vision:11b` |

Re-run `notes doctor` until everything is green. **STOP — Checkpoint E.** Paste the doctor output.

---

## 8. Phase F — Smoke test

### F.1 Sanity-check Ollama directly

```bash
ollama run richardyoung/olmocr2:7b-q8 "Reply with the single word: ready" --verbose
```

Expect a one-word response and GPU stats in stderr.

### F.2 If the user provides a test annotated PDF

Place it at `~/notes/inbox/smoketest.pdf` and run a **dry run** (no vault writes, no file moves):

```bash
notes process smoketest.pdf --ocr olmocr --dry-run -v
```

Expected log lines:

- `Rasterized smoketest.pdf → N pages @ 200dpi`
- `[olmocr] OCR starting on N pages`
- `[olmocr] Done in T.Ts | M handwritten chars extracted`
- `[dry-run] Handwritten preview: ...`

If the dry run looks good, run a **real** process on a non-critical file:

```bash
notes process smoketest.pdf --ocr olmocr -v
```

Verify:

1. `~/notes/processed/smoketest.pdf` exists.
2. A vault note was created/updated under `~/notes/vault/`.
3. A state file exists in `~/notes/.state/smoketest.<fingerprint>.json`.

### F.3 (Optional) Benchmark all three backends

Only run this if the user is curious **and** has set `ANTHROPIC_API_KEY` (this costs Claude tokens):

```bash
cp ~/notes/processed/smoketest.pdf ~/notes/inbox/bench.pdf
notes benchmark bench.pdf
```

A side-by-side table is printed; the full report lands in `~/notes/benchmarks/`.

**STOP — Checkpoint F.** Report the test outcome. Do **not** proceed to the LaunchAgent step until the user confirms the smoke test produced sensible output.

---

## 9. Phase G — Always-on watcher via LaunchAgent

This phase makes `notes watch` start automatically at login and restart on crash.

### G.1 Generate the plist

Use these values verbatim, substituting `<USER>` with the output of `whoami` and `<REPO>` with the absolute path to the repo:

```bash
USER_NAME="$(whoami)"
REPO_PATH="$(pwd)"
PLIST_PATH="$HOME/Library/LaunchAgents/com.${USER_NAME}.notes-pipeline.watch.plist"

cat > "$PLIST_PATH" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.${USER_NAME}.notes-pipeline.watch</string>

  <key>ProgramArguments</key>
  <array>
    <string>${REPO_PATH}/.venv/bin/notes</string>
    <string>watch</string>
    <string>--ocr</string>
    <string>olmocr</string>
  </array>

  <key>WorkingDirectory</key>
  <string>${REPO_PATH}</string>

  <key>EnvironmentVariables</key>
  <dict>
    <key>PATH</key>
    <string>${HOME}/.pixi/bin:/usr/local/bin:/usr/bin:/bin</string>
    <key>OLLAMA_KEEP_ALIVE</key>
    <string>30m</string>
  </dict>

  <key>RunAtLoad</key>
  <true/>
  <key>KeepAlive</key>
  <true/>

  <key>StandardOutPath</key>
  <string>${HOME}/notes/.state/watcher.out.log</string>
  <key>StandardErrorPath</key>
  <string>${HOME}/notes/.state/watcher.err.log</string>
</dict>
</plist>
EOF
```

**Critical:** Do **not** put `ANTHROPIC_API_KEY` in this plist. The merge step will fail at runtime if the key isn't in the user's shell. To make it available to the agent, write it into the plist's `EnvironmentVariables` block **only if the user explicitly approves** — otherwise document that the user must run `launchctl setenv ANTHROPIC_API_KEY "..."` once per boot (or use a keychain wrapper).

### G.2 Load and start

```bash
launchctl unload "$PLIST_PATH" 2>/dev/null || true
launchctl load -w "$PLIST_PATH"
launchctl list | grep notes-pipeline
```

### G.3 Verify

Watch the logs for ~30 seconds:

```bash
tail -f ~/notes/.state/watcher.err.log
# (Ctrl-C after you see "Watching /Users/.../notes/inbox with backend olmocr")
```

Drop a tiny test PDF into `~/notes/inbox/` — within ~15 seconds you should see processing begin in the log.

**STOP — Checkpoint G.** Report `launchctl list | grep notes` and a tail of `watcher.err.log`.

---

## 10. Phase H — Final report

Write a short summary to the user containing:

1. **Versions:** macOS, Python, Ollama, package version (`notes --version`).
2. **Config locations:** repo path, virtualenv path, config TOML path, vault path.
3. **Service status:** Ollama (`curl -s http://localhost:11434/api/tags >/dev/null && echo running` or check the menu-bar icon), watcher (`launchctl list | grep notes`).
4. **Models pulled:** verbatim `ollama list` output.
5. **Test pass count:** `pytest -q` summary.
6. **Smoke test outcome:** name of the vault note that was created/updated, or a note that no test PDF was provided.
7. **Anything skipped:** e.g. `basictex` if they declined, iCloud symlink if they declined.
8. **Day-2 commands** (paste these into the report so the user can copy-paste):

   ```bash
   # Tail the watcher
   tail -f ~/notes/.state/watcher.err.log

   # Stop / start the watcher
   launchctl unload ~/Library/LaunchAgents/com.<USER>.notes-pipeline.watch.plist
   launchctl load -w ~/Library/LaunchAgents/com.<USER>.notes-pipeline.watch.plist

   # Switch the default OCR backend
   #   edit ~/.config/notes_pipeline/config.toml → [ocr] backend = "claude"
   #   then bounce the watcher

   # Process a specific file manually
   source ~/code/notes-pipeline/.venv/bin/activate
   notes process some.pdf --ocr olmocr -v

   # Force-reprocess a file already in processed/
   notes process some.pdf --force

   # Compare backends head-to-head
   notes benchmark some.pdf

   # Render a vault note to PDF for the iPad
   notes render my-note.md
   ```

---

## 11. Troubleshooting reference

| Symptom | Cause / Fix |
|---|---|
| `ollama: command not found` | Re-run the official installer: `curl -fsSL https://ollama.com/install.sh \| sh` |
| `curl :11434` fails | Launch the Ollama app or run `pkill ollama; ollama serve &`; check Console.app for crash logs |
| `notes doctor` shows Anthropic key missing under LaunchAgent but it's set in shell | LaunchAgents don't inherit your shell env. Either run `launchctl setenv ANTHROPIC_API_KEY "..."` (must repeat after reboot) or add to the plist `EnvironmentVariables`. |
| Watcher process keeps restarting in a loop | Tail `~/notes/.state/watcher.err.log`. Most common: missing Anthropic key for merge step. |
| Out-of-memory pulling olmocr | Free disk; check `df -h ~`. Each model is 8–9 GB. |
| Pages save but vault note isn't updated | Check that `<handwritten>...</handwritten>` tags appeared in the OCR output. Some pages are 100% printed — pipeline correctly logs `No handwritten content detected — skipping vault merge.` |
| OCR very slow on first run | First call after a long idle period reloads the model. With `OLLAMA_KEEP_ALIVE=30m` subsequent runs are fast. |
| `pandoc: xelatex: command not found` when running `notes render` | `pixi global install texlive-core` then restart shell. |
| Same PDF keeps being reprocessed | The fingerprint state lives in `~/notes/.state/`. Check that this directory is writable. |

---

## 12. Architecture notes (for future maintenance)

- **OCR backend swap.** To add a fourth backend, implement the `OCRBackend` protocol in `src/notes_pipeline/ocr/`, register it in `registry.build_backend`, and add a string literal to `OCRBackendName` in `config.py`. The orchestrator, retry layer, and CLI pick it up automatically.
- **Prompt changes.** All prompts live in `src/notes_pipeline/ocr/prompts.py`. Update there, run `pytest`, redeploy.
- **Concurrency caveat.** Ollama serializes vision requests per model on a single GPU. Setting `max_concurrency > 1` for `olmocr`/`llama` mainly helps overlap upload + decode; gains are modest. For `claude`, network is the bottleneck and concurrency helps.
- **Resumability.** State files in `~/notes/.state/` are JSON keyed by `<pdf_stem>.<sha256_prefix>.json`. Deleting one allows reprocessing without `--force`.
- **Vault matching.** `find_source_note` strips `-annotated`/`_annotated` suffixes, ISO-date timestamps, and falls back to a case-insensitive recursive search. Extend `_candidates()` in `vault/matching.py` if you add new iPad export naming conventions.
- **Tests.** Pure-function tests only — no live Ollama or Anthropic calls. Add integration tests only behind an env flag (e.g. `NOTES_LIVE_TESTS=1`).

---

## 13. Out of scope (do **not** do these)

- Setting up the GMKtec EVO-X2 or any Linux/ROCm work.
- Building an Obsidian plugin.
- Adding OCR backends beyond Claude / olmOCR / Llama Vision.
- Mounting the vault to a cloud service.
- Adding a web UI.

If the user asks for any of these, surface the request but do not implement.

---

**End of spec.** Execute phases A → H in order. After each **STOP** marker, summarize what you did and what you observed, then ask before proceeding.
