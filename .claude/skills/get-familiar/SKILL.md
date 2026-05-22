---
name: get-familiar
description: Orients Claude to a new project by reading all available documentation in the current directory and its subdirectories. Use this skill whenever the user says "get familiar", "orient yourself", "get up to speed", "read the project docs", "familiarize yourself", "what's this project about", or any similar phrase indicating they want Claude to survey and understand the project structure before starting work. Trigger proactively at the start of a session when the user seems to be onboarding Claude to a new codebase or project.
---

# Get Familiar

The goal is to build a solid mental model of the project before doing any work. Read everything available, then give the user a confident, grounded summary.

## Steps

1. **Read the root-level documentation**
   - Look for `CLAUDE.md` first (project-specific Claude instructions take priority)
   - If not found, look for `README.md`
   - Read whichever is found (both if both exist)

2. **List all subdirectories** in the current working directory

3. **Search subdirectories for documentation**
   - In each subdirectory, check for `CLAUDE.md` and/or `README.md`
   - For any found, read them — request permission if needed
   - Go one level deep (subdirectories of subdirectories only if they seem clearly relevant, e.g., a `docs/` or `src/` folder)

4. **Synthesize and report**
   - Give a brief summary of what the project is, its structure, key data sources or components, and anything the user should know before asking you to do work
   - End with: "Ready to get to work."

## Notes

- Don't read every file in the project — focus on documentation files (`CLAUDE.md`, `README.md`, `*.md` files at the root)
- If a subdirectory has no documentation, just note it by name and move on
- Keep the summary concise — the user wants orientation, not a lecture
- If you already have context from the current conversation, incorporate it rather than re-reading files you've already seen
