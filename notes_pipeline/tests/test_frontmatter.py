from notes_pipeline.vault.frontmatter import extract_tags_from_frontmatter


def test_list_tags():
    md = "---\ntitle: t\ntags:\n  - math\n  - physics\n---\n\nbody"
    assert extract_tags_from_frontmatter(md) == ["math", "physics"]


def test_inline_list_tags():
    md = "---\ntags: [a, b, c]\n---\n\nbody"
    assert extract_tags_from_frontmatter(md) == ["a", "b", "c"]


def test_single_string_tag():
    md = "---\ntags: solo\n---\n\nbody"
    assert extract_tags_from_frontmatter(md) == ["solo"]


def test_no_frontmatter_returns_empty():
    assert extract_tags_from_frontmatter("just body text") == []


def test_missing_tags_returns_empty():
    md = "---\ntitle: x\n---\n\nbody"
    assert extract_tags_from_frontmatter(md) == []


def test_malformed_frontmatter_returns_empty():
    md = "---\nthis is not: : : valid yaml :::\n---\n"
    # Either YAML parses leniently or function swallows the error -> empty list
    assert extract_tags_from_frontmatter(md) == []
