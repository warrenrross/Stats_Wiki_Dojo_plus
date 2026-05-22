---
name: wrap-up
description: Close out a work session cleanly by updating CLAUDE.md with session history, checking related docs for needed updates, saving persistent memory, and confirming all files are saved. Use this skill whenever the user says "wrap up", "close out the session", "end of session", "let's wrap", "session cleanup", or asks you to document what was done before closing. Trigger proactively when the user signals they're done for the day or are wrapping up a major task.
---

# Wrap-Up

The goal is to leave the project in a clean, well-documented state so the next session can start fast with full context.

## Steps

1. **Update or create `CLAUDE.md`** at the project root
   - Add or update a "Session History" table entry with today's date and a concise bullet of what was accomplished
   - Update "Known Issues" — add anything discovered, mark resolved issues done
   - Update "Pending Tasks" — remove completed items, add new ones surfaced this session
   - Update "Architectural Decisions" if any new ones were made
   - If `CLAUDE.md` doesn't exist, create it with all relevant sections (see structure below)

2. **Check related docs for needed updates**
   - `README.md` at project root — update if the setup instructions, structure, or dependencies changed
   - Any subdirectory `CLAUDE.md` files relevant to the session's work area
   - If `wiki/CLAUDE.md` exists and wikilink format was changed, note the new convention

3. **Save persistent memory**
   - Save any user preferences or feedback that should carry to future sessions
   - Save any project-level decisions that aren't derivable from reading the code
   - Use the memory system at `~/.claude/projects/<project-slug>/memory/`
   - Check `MEMORY.md` index before writing to avoid duplicates

4. **Handle untracked files**
   - Check `git status` — identify untracked or modified files
   - If `_freeze/` is untracked in a Quarto project, note it in CLAUDE.md Known Issues (it should be committed for CI)
   - Do NOT auto-commit — just flag anything important

5. **Consider skill development**
   - If the session involved a repeatable multi-step workflow (scaffolding, converting files, fixing a class of errors), consider whether it warrants a new skill
   - If so, briefly describe the skill idea to the user and ask if they want it created
   - If creating, follow the skill-creator skill's workflow

6. **Confirm and report**
   - List every file modified during wrap-up
   - State what's pending for next session (top 3 items max)

---

## CLAUDE.md Structure (when creating from scratch)

```markdown
# CLAUDE.md — [Project Name]

## What This Project Is
[1-2 sentence description of purpose and audience]

## Session-Start Checklist
1. Read this file
2. [project-specific step]
3. [project-specific step]

## Key Workflows
### [Workflow Name]
```bash
command here
```

## Architecture Decisions
| Decision | Rationale |
|----------|-----------|
| ... | ... |

## Directory Structure
[tree or table]

## Known Issues
| Issue | Status | Notes |
|-------|--------|-------|

## Pending Tasks
1. [Next task]

## Session History
| Date | Work Done |
|------|-----------|
| YYYY-MM-DD | [summary] |
```

---

## Notes

- Keep session history entries concise — one line per major deliverable, not a full narrative
- Architectural decisions belong here, not in comments or commit messages — they should survive renames and refactors
- If the user asks "what's left?" at wrap-up, check Pending Tasks and Known Issues before answering
- Do not commit files during wrap-up unless the user explicitly asks
