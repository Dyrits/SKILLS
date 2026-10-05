#!/usr/bin/env python3
"""Render the skills page, one small graph per skill, to index.html from the skills, their documentation, and flow.json.

Usage: python3 scripts/build-skill-graph.py [--check] [repository]
Needs: Python 3 standard library. Writes index.html, or with --check only reports whether it is current.
"""

import importlib.util
import json
import re
import sys
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parent
FLOW = Path("scripts/skill-graph/flow.json")
TEMPLATE = Path("scripts/skill-graph/template.html")
OUTPUT = Path("index.html")
PLACEHOLDER = "/*SKILL_GRAPH_DATA*/null"
# Sections in the order a reader reaches for them.
BUCKET_ORDER = ["setup", "workflow", "shaping", "upkeep", "version-control", "productivity", "reference"]
ENTRY = re.compile(r"^- (?:\*\*)?\[([\w-]+)\]\(\./[\w-]+/SKILL\.md\)(?:\*\*)?:\s*(.+)$")


def load_checker():
    spec = importlib.util.spec_from_file_location("check_skills", SCRIPTS / "check-skills.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def plain(markdown):
    """Markdown inline text as plain text: links keep their label, emphasis and code marks go."""
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", markdown)
    return re.sub(r"\*\*|__|`", "", text).strip()


def section(document, heading):
    match = re.search(rf"^## {re.escape(heading)}\n(.*?)(?=^## |\Z)", document, re.MULTILINE | re.DOTALL)
    if not match:
        return []
    paragraphs = re.split(r"\n\s*\n", match.group(1).strip())
    # Tables and lists read poorly as page prose; the documentation link carries them.
    return [plain(" ".join(p.split())) for p in paragraphs if p and not p.lstrip().startswith(("|", "-", "```"))]


def frontmatter(content, field):
    match = re.search(rf"^{field}:\s*(.+)$", content, re.MULTILINE)
    return match.group(1).strip().strip("'\"") if match else ""


def bucket_listing(readme):
    """A bucket README's title, blurb, and skill entries in reading order, with any subgroup heading."""
    title = re.search(r"^# (.+)$", readme, re.MULTILINE)
    blurb = re.search(r"^# .+\n\n(.+)$", readme, re.MULTILINE)
    entries, group = [], ""
    for line in readme.splitlines():
        heading = re.match(r"^## (.+)$", line)
        if heading:
            group = heading.group(1) if heading.group(1) != "Ungrouped" else "Other"
            continue
        entry = ENTRY.match(line)
        if entry:
            entries.append({"name": entry.group(1), "tagline": plain(entry.group(2)), "group": group})
    return {"title": title.group(1) if title else "", "blurb": plain(blurb.group(1)) if blurb else "", "entries": entries}


def graph(root):
    """The page data, and the problems that keep flow.json from covering the promoted skills."""
    root = Path(root).resolve()
    checker = load_checker()
    manifest = json.loads((root / ".claude-plugin/plugin.json").read_text())
    repository = manifest.get("repository", "").rstrip("/")
    flow = json.loads((root / FLOW).read_text())
    artifacts, curated = flow["artifacts"], flow["skills"]
    problems = []

    skills, listings = {}, {}
    for entry in manifest["skills"]:
        folder = root / entry
        bucket, name = folder.parent.name, folder.name
        if bucket not in listings:
            listings[bucket] = bucket_listing((folder.parent / "README.md").read_text())
        content = (folder / "SKILL.md").read_text()
        page = root / "documentation/skills" / bucket / f"{name}.md"
        document = page.read_text() if page.exists() else ""
        calls, handovers = (found - checker.EXTERNAL_SKILLS for found in checker.skill_references(folder))
        entry_flow = curated.get(name)
        if entry_flow is None:
            problems.append(f"{FLOW}: no entry for promoted skill {name}.")
            entry_flow = {"inputs": [], "outputs": [], "next": []}
        for key in ("inputs", "outputs"):
            for artifact in entry_flow[key]:
                if artifact not in artifacts:
                    problems.append(f"{FLOW}: {name} {key} names unknown artifact {artifact}.")
        skills[name] = {
            "bucket": bucket,
            "tagline": "",
            "description": frontmatter(content, "description"),
            "argumentHint": frontmatter(content, "argument-hint"),
            "summary": section(document, "What it does"),
            "fits": section(document, "Where it fits"),
            "skillUrl": f"{repository}/blob/main/{entry.removeprefix('./')}/SKILL.md",
            "pageUrl": f"{repository}/blob/main/{page.relative_to(root)}" if document else "",
            "calls": sorted(calls),
            "handovers": sorted(handovers),
            "next": entry_flow["next"],
            "inputs": entry_flow["inputs"],
            "outputs": entry_flow["outputs"],
        }
    for name in curated.keys() - skills.keys():
        problems.append(f"{FLOW}: entry {name} is not a promoted skill.")
    for name, skill in skills.items():
        for target in skill["calls"] + skill["handovers"] + skill["next"]:
            if target not in skills:
                problems.append(f"{FLOW}: {name} links to unknown skill {target}.")
        # A curated "next" that the skill already calls or hands over to is drawn once, as the stronger link.
        skill["next"] = [n for n in skill["next"] if n not in skill["calls"] and n not in skill["handovers"]]

    buckets = []
    for bucket in sorted(listings, key=lambda b: BUCKET_ORDER.index(b) if b in BUCKET_ORDER else len(BUCKET_ORDER)):
        listing = listings[bucket]
        listed = [e for e in listing["entries"] if e["name"] in skills and skills[e["name"]]["bucket"] == bucket]
        missing = {n for n, s in skills.items() if s["bucket"] == bucket} - {e["name"] for e in listed}
        for name in sorted(missing):
            problems.append(f"skills/{bucket}/README.md: no one-line entry for {name}.")
        for e in listed:
            skills[e["name"]]["tagline"] = e["tagline"]
        buckets.append({"id": bucket, "title": listing["title"], "blurb": listing["blurb"],
                        "skills": [e["name"] for e in listed],
                        "groups": {e["name"]: e["group"] for e in listed if e["group"]}})
    used = {a for s in skills.values() for a in s["inputs"] + s["outputs"]}
    for artifact in artifacts.keys() - used:
        problems.append(f"{FLOW}: artifact {artifact} is never an input or output.")
    data = {"repository": repository, "buckets": buckets, "skills": skills,
            "artifacts": {k: v for k, v in artifacts.items() if k in used}}
    return data, problems


def render(root):
    root = Path(root).resolve()
    data, problems = graph(root)
    payload = json.dumps(data, indent=1, ensure_ascii=False, sort_keys=True).replace("</", "<\\/")
    template = (root / TEMPLATE).read_text()
    if PLACEHOLDER not in template:
        problems.append(f"{TEMPLATE}: missing the {PLACEHOLDER} placeholder.")
    return template.replace(PLACEHOLDER, payload), problems


def main(arguments):
    check = "--check" in arguments
    rest = [a for a in arguments if a != "--check"]
    root = Path(rest[0] if rest else SCRIPTS.parent).resolve()
    html, problems = render(root)
    for problem in problems:
        print(f"ERROR: {problem}")
    if problems:
        return 1
    current = (root / OUTPUT).read_text() if (root / OUTPUT).exists() else None
    if check:
        if current != html:
            print(f"ERROR: {OUTPUT} is stale; run python3 scripts/build-skill-graph.py.")
            return 1
        print(f"{OUTPUT} is current.")
        return 0
    (root / OUTPUT).write_text(html)
    print(f"Wrote {OUTPUT}.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
