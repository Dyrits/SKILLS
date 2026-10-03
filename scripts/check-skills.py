#!/usr/bin/env python3
"""Check skill layout, invocation metadata, documentation, and local links.

Usage: python3 scripts/check-skills.py [repository]
Needs: Python 3 standard library. Reads files only.
"""

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


def check(repository):
    root = Path(repository).resolve()
    errors = []
    manifest = json.loads((root / ".claude-plugin/plugin.json").read_text())
    promoted = {Path(path) for path in manifest["skills"]}
    if len(promoted) != len(manifest["skills"]):
        errors.append("Plugin manifest contains duplicate skill paths.")

    skill_files = sorted((root / "skills").glob("*/*/SKILL.md"))
    skills = {path.parent.relative_to(root): path for path in skill_files}
    router = (root / "skills/getting-started/guide/SKILL.md").read_text()
    top = (root / "README.md").read_text()
    listing = top.split("## Plugin skills", 1)[-1]
    required_sections = (
        "What it does", "When to reach for it", "Common questions", "It's working if", "Where it fits"
    )
    expected_pages = set()
    names = set()
    for relative, path in skills.items():
        name = relative.name
        if name in names:
            errors.append(f"Duplicate skill name: {name}")
        names.add(name)
        content = path.read_text()
        name_field = re.search(r"^name:\s*(.+)$", content, re.MULTILINE)
        if not name_field or name_field.group(1).strip("'\"") != name:
            errors.append(f"{relative}: frontmatter name does not match directory.")
        metadata_path = path.parent / "agents/openai.yaml"
        if not metadata_path.exists():
            errors.append(f"{relative}: missing agents/openai.yaml.")
            continue
        user_only = bool(re.search(r"^disable-model-invocation:\s*true\s*$", content, re.MULTILINE))
        codex_user_only = bool(re.search(
            r"^\s*allow_implicit_invocation:\s*false\s*$", metadata_path.read_text(), re.MULTILINE
        ))
        if user_only != codex_user_only:
            errors.append(f"{relative}: invocation policy differs between clients.")
        if not re.search(rf"/{re.escape(name)}(?![\w-])", router):
            errors.append(f"{relative}: router does not name /{name}.")
        bucket_readme = path.parent.parent / "README.md"
        if not bucket_readme.exists():
            errors.append(f"{relative}: missing bucket README.")
            continue
        bucket = bucket_readme.read_text()
        skill_link = f"./{name}/SKILL.md"
        if skill_link not in bucket:
            errors.append(f"{relative}: missing bucket README link.")
        deprecated = relative.parts[1] == "deprecated"
        if deprecated and relative in promoted:
            errors.append(f"{relative}: deprecated skill is in the plugin manifest.")
        elif not deprecated and relative not in promoted:
            errors.append(f"{relative}: missing from the plugin manifest.")
        if relative in promoted:
            if str(relative) + "/SKILL.md" not in listing:
                errors.append(f"{relative}: missing promoted top-level README entry.")
            page = root / "documentation/skills" / relative.relative_to("skills")
            page = page.with_suffix(".md")
            expected_pages.add(page)
            if not page.exists():
                errors.append(f"{relative}: missing human-facing documentation page.")
                continue
            document = page.read_text()
            if re.search(r"^# ", document, re.MULTILINE):
                errors.append(f"{page.relative_to(root)}: human-facing page must not have an H1.")
            positions = [document.find(f"## {heading}\n") for heading in required_sections]
            if -1 in positions or positions != sorted(positions):
                errors.append(f"{page.relative_to(root)}: required sections missing or out of order.")
            first = document.splitlines()[0] if document else ""
            if not re.match(r"(Upstream|Source|Provenance|Fork-|Derived from upstream)", first):
                errors.append(f"{page.relative_to(root)}: missing top provenance note.")

    for relative in promoted - skills.keys():
        errors.append(f"{relative}: manifest target does not exist.")
    actual_pages = set((root / "documentation/skills").glob("*/*.md"))
    for page in actual_pages - expected_pages:
        errors.append(f"{page.relative_to(root)}: orphan documentation page.")
    if any((root / "skills/experimental").rglob("*")):
        errors.append("skills/experimental still contains entries.")

    markdown = [root / "README.md", root / "CLAUDE.md"]
    markdown += list((root / ".agents").glob("*.md"))
    markdown += list((root / "skills").rglob("*.md"))
    markdown += sorted(actual_pages)
    link_pattern = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
    for path in markdown:
        text = path.read_text()
        if "—" in text:
            errors.append(f"{path.relative_to(root)}: em dash in active prose.")
        # Examples inside fenced blocks are not actual navigation links.
        prose = re.sub(r"(?ms)^```.*?^```\s*$", "", text)
        for match in link_pattern.finditer(prose):
            target = match.group(1)
            if re.match(r"^[a-zA-Z][\w+.-]*:", target) or target.startswith("#"):
                continue
            target = unquote(target.split("#", 1)[0])
            if not target or any(char in target for char in "<>{}*"):
                continue
            resolved = (root / target.lstrip("/")) if target.startswith("/") else path.parent / target
            if not resolved.exists():
                errors.append(f"{path.relative_to(root)}: broken link {target}")
        if re.search(r'call the Skill tool[^\n]*(?:"grilling"|"grill-me"|"to-tickets"|"to-specifications"'
                     r'|"code-review-and-refactor"|"to-pull-request"|"documentation"|"writing-for-agents"'
                     r'|"divide-and-conquer"|"test-driven-development"|"wizard"|"codebase-design"|"domain-modeling"|"scriptbook")',
                     text, re.IGNORECASE):
            errors.append(f"{path.relative_to(root)}: operative call to retired skill.")

    for error in errors:
        print(f"ERROR: {error}")
    print(f"Checked {len(skills)} skills, {len(promoted)} plugin paths, "
          f"{len(actual_pages)} documentation pages, and {len(markdown)} Markdown files.")
    return bool(errors)


if __name__ == "__main__":
    sys.exit(check(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent))
