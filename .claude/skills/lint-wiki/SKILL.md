---
name: lint-wiki
description: Audit the wiki for structural problems — orphan pages, stub entries, broken cross-references, missing tier tags, and formulas not linked back to a concept page. Use this skill when the user says "lint the wiki", "check for broken links", "find orphan pages", "wiki health check", "what's missing in the wiki", or "audit the wiki".
---

# Lint Wiki

Systematically check `wiki/` for structural integrity problems. Report findings as a prioritized punch list; do not auto-fix — let the user decide what to address.

---

## Checks

Run all checks, then report grouped by severity.

### 1. Stub entries in `wiki/index.md`

A stub is a row in the index table that has plain text instead of a Markdown link — e.g.:

```
| hw1-examples | Homework 1 worked problems (stub) |
```

vs. a real entry:

```
| [hw1-examples](examples/hw1-examples.md) | ... |
```

**How to find:** Read `wiki/index.md`. Look for table rows where the first cell contains no `[` character (plain text, not a link).

**Report:** List each stub with the unit/tier section it appears in.

---

### 2. Linked pages that don't exist

Every `[name](path.md)` link in `wiki/index.md` should resolve to an actual file.

**How to find:**
```bash
grep -oP '\(([^)]+\.md)\)' wiki/index.md | tr -d '()' | while read path; do
  full="wiki/$path"
  [ -f "$full" ] || echo "MISSING: $full"
done
```

**Report:** List each broken link with the index section it appears in.

---

### 3. Orphan wiki pages (no inbound links)

A wiki page is orphaned if nothing links to it — not `index.md`, not any other wiki page.

**How to find:**
```bash
# List all .md files in wiki/ subdirectories
find wiki/concepts wiki/examples wiki/r-code wiki/reference -name "*.md" | while read page; do
  base=$(basename "$page" .md)
  # Search for any link to this page across all wiki files
  count=$(grep -r --include="*.md" "$base" wiki/ | grep -v "^$page" | wc -l)
  [ "$count" -eq 0 ] && echo "ORPHAN: $page"
done
```

**Report:** List orphaned pages. Note: some pages may be intentionally standalone (e.g., `reference/formula-sheet.md` is linked from `graph-navigation.qmd` outside the wiki).

---

### 4. Pages missing `tier:` frontmatter

Every content page in `wiki/` must have `tier:` in its YAML frontmatter (construct, procedure, script, or reference). Pages without it were created incorrectly.

**How to find:**
```bash
find wiki/concepts wiki/examples wiki/r-code wiki/reference -name "*.md" | while read page; do
  grep -q "^tier:" "$page" || echo "MISSING TIER: $page"
done
```

**Report:** List pages with missing tier.

---

### 5. Pages missing `tags:` frontmatter

Every content page should have `tags:` with at least one `unit-X` tag.

**How to find:**
```bash
find wiki/concepts wiki/examples wiki/r-code wiki/reference -name "*.md" | while read page; do
  grep -q "^tags:" "$page" || echo "MISSING TAGS: $page"
done
```

---

### 6. Index entries not matching actual file names

Check that `wiki/index.md` link paths point to files that actually exist AND that all files in `wiki/` subdirectories are represented in the index.

**How to find — files in index but not on disk:** (covered by check 2)

**How to find — files on disk but not in index:**
```bash
find wiki/concepts wiki/examples wiki/r-code wiki/reference -name "*.md" | while read page; do
  base=$(basename "$page" .md)
  grep -q "$base" wiki/index.md || echo "NOT IN INDEX: $page"
done
```

Ignore: `wiki/CLAUDE.md`, `wiki/process-capability.md` (known harmless root stubs).

---

### 7. `[[bracket links]]` remaining in any wiki file

These are Obsidian wikilinks that Quarto renders as literal text, not links.

**How to find:**
```bash
grep -rn "\[\[" wiki/ --include="*.md"
```

**Report:** List every occurrence with file and line number.

---

### 8. Known stubs in `wiki/CLAUDE.md` "Known Issues" table

Read `wiki/CLAUDE.md` and check whether anything listed there as "Not yet filled" or a stub has now been created but the table wasn't updated.

---

## Report Format

```
## Wiki Lint Report — YYYY-MM-DD

### 🔴 Critical (breaks navigation or site render)
- MISSING FILE: wiki/examples/foo.md — linked from index.md Unit 2 Tier 3
- BRACKET LINK: wiki/concepts/bar.md line 14: [[old-link]]

### 🟡 Structural (weakens the wiki graph)
- ORPHAN: wiki/examples/baz.md — no inbound links found
- NOT IN INDEX: wiki/r-code/new-page.md

### 🟢 Metadata (frontmatter completeness)
- MISSING TIER: wiki/concepts/qux.md
- MISSING TAGS: wiki/examples/quux.md

### ✅ All clear
[category] — no issues found
```

---

## Notes

- Do not auto-fix. Report and let the user decide what to address.
- After the user fixes issues, they can run `/lint-wiki` again to verify the all-clear.
- Orphans that are linked from `.qmd` files outside `wiki/` (lessons, dojo) are not truly orphaned — check `lessons/` and `dojo/` before flagging.
