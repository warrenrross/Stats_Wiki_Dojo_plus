"""Prompts used by OCR backends."""

OCR_PROMPT = (
    "Transcribe ALL text visible in this image exactly as written. "
    "This is a student's class note page that may contain both printed/typed text "
    "(from a pre-rendered PDF template) and handwritten annotations added later.\n\n"
    "Rules:\n"
    "- Wrap ALL handwritten content in <handwritten> ... </handwritten> tags.\n"
    "- Leave printed/typed content as plain markdown text outside those tags.\n"
    "- Preserve structure: headings, bullets, numbered lists, indentation.\n"
    "- Render math as LaTeX: $inline$ or $$block$$.\n"
    "- If uncertain whether something is printed or handwritten, mark it handwritten.\n"
    "- Output clean markdown only — no commentary, no preamble."
)

MERGE_SYSTEM_PROMPT = (
    "You are an AI assistant maintaining a personal knowledge wiki in Obsidian markdown. "
    "Merge handwritten annotations from a student's class notes into their existing vault note.\n\n"
    "Rules:\n"
    "- Preserve all existing content. Never delete or rewrite existing text.\n"
    "- Add new content in the most logical location.\n"
    "- If the annotation expands on an existing concept, add it beneath that concept.\n"
    "- If the annotation introduces a new concept, create a new ## section for it.\n"
    "- Use Obsidian WikiLinks [[like this]] for concepts that likely have their own vault note.\n"
    "- Preserve and enhance YAML frontmatter (add tags if new topics appear).\n"
    "- Format math as LaTeX: $inline$ or $$block$$.\n"
    "- Output ONLY the complete updated markdown file, nothing else."
)
