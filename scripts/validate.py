#!/usr/bin/env python3
"""Static checks for the Kimi Agent Team Guide repository.

Checks:
 1. Every agents/guide_*.md file has parseable YAML frontmatter with a
    description and a body that ends with a handoff reminder.
 2. Counted artifacts stay consistent: 7 agents, 24 selector tasks,
    12 workflow recipes.
 3. Internal markdown links in README.md, SETUP.md and docs/ resolve to
    files that exist.
 4. Every docs/*.md page opens with a breadcrumb navigation line.

Exits non-zero if any check fails. Read-only; changes nothing.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXPECTED_AGENTS = 7
EXPECTED_TASKS = 24
EXPECTED_RECIPES = 12

failures: list[str] = []
passes: list[str] = []


def check(ok: bool, label: str, detail: str = "") -> None:
    (passes if ok else failures).append(f"{label}{' — ' + detail if detail else ''}")


def parse_frontmatter(text: str) -> dict[str, object] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    block = text[4:end]
    data: dict[str, object] = {}
    try:
        import yaml  # type: ignore

        loaded = yaml.safe_load(block)
        return loaded if isinstance(loaded, dict) else None
    except ImportError:
        # Minimal fallback: require a `name:` and `description:` line.
        for key in ("name", "description"):
            m = re.search(rf"^{key}:\s*(.+)$", block, re.MULTILINE)
            if not m:
                return None
            data[key] = m.group(1).strip()
        return data
    except Exception:
        return None


def links_in(path: Path) -> list[tuple[str, str]]:
    text = path.read_text(encoding="utf-8")
    out = []
    for m in re.finditer(r"\[[^\]]*\]\(([^)\s]+)\)", text):
        target = m.group(1)
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        out.append((target.split("#")[0], target))
    return out


# 1. Agent files
agent_files = sorted((ROOT / "agents").glob("guide_*.md"))
check(len(agent_files) == EXPECTED_AGENTS, "agent count", f"{len(agent_files)} found")
for f in agent_files:
    text = f.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    check(fm is not None, f"frontmatter parses: {f.name}")
    if fm:
        check(bool(fm.get("description")), f"description present: {f.name}")
    check("last message" in text.lower(), f"handoff reminder in body: {f.name}")
    check("model" not in (fm or {}), f"no per-agent model field: {f.name}")

# 2. Counted artifacts
selector = (ROOT / "docs" / "task-selector.md").read_text(encoding="utf-8")
task_rows = re.findall(r"^\| \d+ \|", selector, re.MULTILINE)
check(len(task_rows) == EXPECTED_TASKS, "selector task count", f"{len(task_rows)} rows")

workflows = (ROOT / "docs" / "workflows.md").read_text(encoding="utf-8")
recipe_heads = re.findall(r"^### \d+\.", workflows, re.MULTILINE)
check(len(recipe_heads) == EXPECTED_RECIPES, "recipe count", f"{len(recipe_heads)} recipes")

# 3. Internal links resolve
checked_links = 0
for md in [ROOT / "README.md", ROOT / "SETUP.md", *sorted((ROOT / "docs").glob("*.md")),
           ROOT / "WORK_WITH_VYR.md", ROOT / "agents" / "README.md", ROOT / "SOURCES.md"]:
    for stripped, original in links_in(md):
        if not stripped:
            continue
        checked_links += 1
        check((md.parent / stripped).resolve().exists(),
              f"link resolves: {md.name} -> {original}")

# 4. Breadcrumb lines on docs pages
for md in sorted((ROOT / "docs").glob("*.md")):
    first_content = next((ln for ln in md.read_text(encoding="utf-8").splitlines()
                          if ln.strip()), "")
    check("[Home](../README.md)" in first_content, f"breadcrumb line: {md.name}")

print(f"PASS {len(passes)} checks")
for item in passes:
    print(f"  ok  {item}")
if failures:
    print(f"\nFAIL {len(failures)} checks")
    for item in failures:
        print(f"  !!  {item}")
    sys.exit(1)
print(f"\nAll checks passed ({checked_links} internal links verified).")
