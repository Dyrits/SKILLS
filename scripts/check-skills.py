#!/usr/bin/env python3
"""Check skill layout, invocation metadata, dependency paragraphs, documentation, local links, and the skill map.

Usage: python3 scripts/check-skills.py [repository]
Needs: Python 3 standard library. Reads files only.
"""

import datetime
import importlib.util
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


# Skills called by name that ship outside this repository.
EXTERNAL_SKILLS = {"skill-creator", "webapp-testing"}

SKILL_ENTRIES = {"SKILL.md", "apm.yml", "agents", "scripts", "references", "assets", "evals"}
REFERENCE_NAME = re.compile(r"^[A-Z0-9]+(?:-[A-Z0-9]+)*\.md$")
ASSET_NAME = re.compile(r"^[a-z0-9]+(?:[-.][a-z0-9]+)*$")
VERIFIED_PATTERN = re.compile(r"^Verified: (\d{4}-\d{2}-\d{2})", re.MULTILINE)
STALE_AFTER_DAYS = 183
# "Call the Skill tool with "a"" or "Call the Skill tool twice, for "a" and "b"": names quoted, escaped, or in backticks.
CALL_PATTERN = re.compile(r'Skill tool(?: twice,)? (?:with|for) ((?:\\?["`][\w-]+\\?["`](?:,? (?:and |or )?)?)+)',
                          re.IGNORECASE)
# "tell the user to run `/a`": the human invokes it.
HANDOVER_PATTERN = re.compile(r"to run `/([\w-]+)")
# "If it is missing, tell the user to run `/a`": a handover that sends the human back to set something up first.
PREREQUISITE_PATTERN = re.compile(r"missing[^.|\n]*to run `/([\w-]+)")
SCANNED_SUFFIXES = {".md", ".sh"}


def call_names(match):
    return re.findall(r'["`]([\w-]+)\\?["`]', match.group(1))


def skill_references(folder):
    """Other skills a skill folder calls through the Skill tool, and those it tells the user to run."""
    calls, handovers = set(), set()
    for path in folder.rglob("*"):
        if path.suffix not in SCANNED_SUFFIXES or not path.is_file():
            continue
        text = path.read_text()
        for call in CALL_PATTERN.finditer(text):
            calls.update(call_names(call))
        handovers.update(HANDOVER_PATTERN.findall(text))
    calls.discard(folder.name)
    return calls, handovers - calls - {folder.name}


def prerequisites(folder):
    """The handovers a skill folder makes only when something it needs is missing, so they run before it, not after."""
    found = set()
    for path in folder.rglob("*"):
        if path.suffix not in SCANNED_SUFFIXES or not path.is_file():
            continue
        for match in PREREQUISITE_PATTERN.finditer(path.read_text()):
            found.add(match.group(1))
    return found - {folder.name}


def calls_block(calls, handovers=frozenset()):
    """The dependency paragraph a skill carries: the names only, since APM installs the dependencies."""
    sentences = []
    if calls:
        sentences.append("**Calls:** " + ", ".join(f"`{name}`" for name in sorted(calls)) + ".")
    if handovers:
        sentences.append("**Hands over to:** " + ", ".join(f"`/{name}`" for name in sorted(handovers)) + ".")
    return " ".join(sentences)


def frontmatter_error(content):
    """A plain (unquoted) description holding ": " or " #" is invalid YAML, and installers silently skip the skill."""
    match = re.search(r"^description:[ \t]*(.*)$", content, re.MULTILINE)
    if not match:
        return None
    value = match.group(1).strip()
    if value[:1] in "\"'>|":
        return None
    if ": " in value or " #" in value:
        return 'description is unquoted but holds ": " or " #", which is invalid YAML. Wrap it in quotes.'
    return None


def check(repository):
    root = Path(repository).resolve()
    errors = []
    manifest = json.loads((root / ".claude-plugin/plugin.json").read_text())
    plugin_paths = {Path(path) for path in manifest["skills"]}
    if len(plugin_paths) != len(manifest["skills"]):
        errors.append("Plugin manifest contains duplicate skill paths.")

    skill_files = sorted((root / "skills").glob("*/*/SKILL.md"))
    skills = {path.parent.relative_to(root): path for path in skill_files}
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
        problem = frontmatter_error(content)
        if problem:
            errors.append(f"{relative}: {problem}")
        metadata_path = path.parent / "agents/openai.yaml"
        if not metadata_path.exists():
            errors.append(f"{relative}: missing agents/openai.yaml.")
            continue
        # Every skill stays reachable by the human, the model, and other skills.
        if re.search(r"^disable-model-invocation:\s*true\s*$", content, re.MULTILINE) or re.search(
            r"^\s*allow_implicit_invocation:\s*false\s*$", metadata_path.read_text(), re.MULTILINE
        ):
            errors.append(f"{relative}: skill blocks model invocation.")
        # Externals are left out: APM does not install them.
        calls, handovers = (found - EXTERNAL_SKILLS for found in skill_references(path.parent))
        block = calls_block(calls, handovers)
        expected = [block] if block else []
        closing = content.find("\n---", 4)
        if closing != -1 and re.search(r"^\*\*(?:Calls|Hands over to):\*\*", content[:closing], re.MULTILINE):
            errors.append(f"{relative}: dependency paragraph sits inside the frontmatter.")
        if re.findall(r"^\*\*(?:Calls|Hands over to):\*\*.*$", content, re.MULTILINE) != expected:
            errors.append(f"{relative}: dependency paragraph should read: {expected[0] if expected else '(none)'}")
        bucket_readme = path.parent.parent / "README.md"
        if not bucket_readme.exists():
            errors.append(f"{relative}: missing bucket README.")
            continue
        bucket = bucket_readme.read_text()
        skill_link = f"./{name}/SKILL.md"
        if skill_link not in bucket:
            errors.append(f"{relative}: missing bucket README link.")
        if relative not in plugin_paths:
            errors.append(f"{relative}: missing from the plugin manifest.")
        if str(relative) + "/SKILL.md" not in listing:
            errors.append(f"{relative}: missing top-level README entry.")
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

    # references/ROUTING.md carries a fallback copy of the policy's tiers; keep the two identical.
    policy = root / "skills/setup/setup-delegation-policy/assets/policy.md"
    routing = root / "skills/workflow/divide-and-conquer/references/ROUTING.md"
    if policy.exists() and routing.exists():
        tier_line = re.compile(r"^(?:- \*\*(?:Light|Balanced|Heavy|Frontier)\*\*|\| (?:Tier|Light|Balanced|Heavy|Frontier) ).*$",
                               re.MULTILINE)
        if tier_line.findall(policy.read_text()) != tier_line.findall(routing.read_text()):
            errors.append("skills/workflow/divide-and-conquer/references/ROUTING.md: tiers differ from the delegation policy.")

    # Skill layout follows the Agent Skills specification: support files sit in scripts/ (executed), references/
    # (read, UPPERCASE names), or assets/ (templates and payloads copied elsewhere, kebab-case names).
    for relative in skills:
        folder = root / relative
        for entry in folder.iterdir():
            if entry.name not in SKILL_ENTRIES:
                errors.append(f"{entry.relative_to(root)}: move it into scripts/, references/, or assets/.")
        for entry in (folder / "references").glob("*"):
            if not REFERENCE_NAME.match(entry.name):
                errors.append(f"{entry.relative_to(root)}: reference names are UPPERCASE, such as GUIDE-NAME.md.")
        for entry in (folder / "assets").glob("*"):
            if not ASSET_NAME.match(entry.name):
                errors.append(f"{entry.relative_to(root)}: asset names are kebab-case, such as asset-name.md.")

    for relative in plugin_paths - skills.keys():
        errors.append(f"{relative}: manifest target does not exist.")
    actual_pages = set((root / "documentation/skills").glob("*/*.md"))
    for page in actual_pages - expected_pages:
        errors.append(f"{page.relative_to(root)}: orphan documentation page.")
    if any((root / "skills/experimental").rglob("*")):
        errors.append("skills/experimental still contains entries.")

    markdown = [root / "README.md", root / "AGENTS.md"]
    markdown += list((root / ".agents").glob("*.md"))
    markdown += list((root / "skills").rglob("*.md"))
    markdown += sorted(actual_pages)
    callable_names = {relative.name for relative in skills}
    callable_names |= EXTERNAL_SKILLS
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
        for call in CALL_PATTERN.finditer(text):
            for name in call_names(call):
                if name not in callable_names:
                    errors.append(f"{path.relative_to(root)}: operative call to unknown skill {name}.")

    # A dated catalogue ("Verified: YYYY-MM-DD") goes stale as tools release. A stale date is a maintenance
    # prompt, not a broken repository, so it warns without failing. Six months is about how often the catalogued
    # tools ship a major release or a new default.
    warnings = []
    today = datetime.date.today()
    for path in markdown:
        for match in VERIFIED_PATTERN.finditer(path.read_text()):
            age = (today - datetime.date.fromisoformat(match.group(1))).days
            if age > STALE_AFTER_DAYS:
                warnings.append(f"{path.relative_to(root)}: verified {match.group(1)}, {age} days ago; recheck its commands.")

    # The skill map at index.html is generated; keep it covering every skill and current.
    if (root / "scripts/skill-graph/flow.json").exists():
        spec = importlib.util.spec_from_file_location("build_skill_graph", Path(__file__).with_name("build-skill-graph.py"))
        builder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(builder)
        html, problems = builder.render(root)
        errors.extend(problems)
        if not problems and (not (root / "index.html").exists() or (root / "index.html").read_text() != html):
            errors.append("index.html: stale skill map; run python3 scripts/build-skill-graph.py.")

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    print(f"Checked {len(skills)} skills, {len(plugin_paths)} plugin paths, "
          f"{len(actual_pages)} documentation pages, and {len(markdown)} Markdown files.")
    return bool(errors)


if __name__ == "__main__":
    sys.exit(check(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent))
