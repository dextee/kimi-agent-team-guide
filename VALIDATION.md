# Validation

[Home](README.md) · [Sources](SOURCES.md)

What was checked locally for this guide, and the limits of those checks. Documentation facts were verified against the official Kimi Code docs on **10 October 2026** and registered in [SOURCES.md](SOURCES.md); this page covers the repository's own quality gates.

## Completed gates

| Gate | Method | Result |
|---|---|---|
| Agent file structure | `python scripts/validate.py` — frontmatter parses, `description` present, handoff reminder in body, no per-agent `model` field | Pass (7/7 agents) |
| Counted artifacts | Validator counts — 24 selector rows, 12 workflow recipes, 7 agent files | Pass |
| Internal links | Validator resolves every relative markdown link in README, SETUP, docs, agents and SOURCES | Pass |
| Docs navigation | Every `docs/*.md` page opens with a breadcrumb line | Pass |
| Claim hygiene | Manual review: vendor-reported figures attributed; scenario routing labelled editorial; no benchmark claims; verification date stated | Pass |

## Limits

- **Live execution not included.** Whether a given account can run `k3` or HighSpeed depends on the reader's membership tier and quota; the templates were statically checked, not executed against the managed service.
- **Subagent model pool schema.** The `[secondary_model]` pool's candidate-list format is described qualitatively and points to the official configuration docs; only `default_model` is shown as concrete configuration, because it is the field the CLI's `/secondary-model` command writes.
- **External links** to kimi.com and vyrwork.com were fetched during authoring (10 October 2026) but are not re-checked on every commit.
- **Artwork.** This repository ships Mermaid source only; there are no generated images whose provenance would need verification.

## Reproduce

```bash
python scripts/validate.py
```

Expected: `PASS` on all checks, exit code 0.
