#!/usr/bin/env python3
"""Check skill layout, invocation metadata, dependency paragraphs, documentation, local links, and the skill map.

Usage: python3 scripts/check-skills.py [repository]
Needs: Python 3 standard library. Reads files only.
"""

import importlib.util
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


# Skills called by name that ship outside this repository.
EXTERNAL_SKILLS = {"webapp-testing"}

# "Call the Skill tool with "a"" or "Call the Skill tool twice, for "a" and "b"": names quoted, escaped, or in backticks.
CALL_PATTERN = re.compile(r'Skill tool(?: twice,)? (?:with|for) ((?:\\?["`][\w-]+\\?["`](?:,? (?:and |or )?)?)+)',
                          re.IGNORECASE)
# "tell the user to run `/a`": the human invokes it.
HANDOVER_PATTERN = re.compile(r"to run `/([\w-]+)")
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


def calls_block(calls, handovers=frozenset()):
    """The dependency paragraph a skill carries, since skills install one by one."""
    install = "`npx skills@latest add Dyrits/SKILLS --skill=<name>`"
    sentences = []
    if calls:
        listed = ", ".join(f"`{name}`" for name in sorted(calls))
        sentences.append(f"**Calls:** {listed}. If a called skill is not installed, tell the user its name and "
                         f"install command, {install}, then carry out that step from its stated intent and "
                         "report the step as done without the skill.")
        if "document" in calls:
            sentences.append("Without `document`, wait until the user installs it or tells you to proceed: "
                             "this skill's rules use its terms.")
    if handovers:
        listed = ", ".join(f"`/{name}`" for name in sorted(handovers))
        sentences.append(f"**Hands over to:** {listed}. When one is not installed, give the user its install "
                         f"command, {install}, along with the instruction to run it.")
    return " ".join(sentences)


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
        # Every skill stays reachable by the human, the model, and other skills.
        if re.search(r"^disable-model-invocation:\s*true\s*$", content, re.MULTILINE) or re.search(
            r"^\s*allow_implicit_invocation:\s*false\s*$", metadata_path.read_text(), re.MULTILINE
        ):
            errors.append(f"{relative}: skill blocks model invocation.")
        # Externals are left out: their install command is not this repository's.
        calls, handovers = (found - EXTERNAL_SKILLS for found in skill_references(path.parent))
        # The router names skills as labels for the human to pick from, not as dependencies.
        block = calls_block(calls, handovers) if relative.parts[1] != "deprecated" and name != "guide" else ""
        expected = [block] if block else []
        if re.findall(r"^\*\*(?:Calls|Hands over to):\*\*.*$", content, re.MULTILINE) != expected:
            errors.append(f"{relative}: dependency paragraph should read: {expected[0] if expected else '(none)'}")
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

    # ROUTING.md carries a fallback copy of the policy's tiers; keep the two identical.
    policy = root / "skills/getting-started/setup-delegation-policy/POLICY.md"
    routing = root / "skills/workflow/divide-and-conquer/ROUTING.md"
    if policy.exists() and routing.exists():
        tier_line = re.compile(r"^(?:- \*\*(?:Light|Balanced|Heavy|Frontier)\*\*|\| (?:Tier|Light|Balanced|Heavy|Frontier) ).*$",
                               re.MULTILINE)
        if tier_line.findall(policy.read_text()) != tier_line.findall(routing.read_text()):
            errors.append("skills/workflow/divide-and-conquer/ROUTING.md: tiers differ from the delegation policy.")

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
    callable_names = {relative.name for relative in skills if relative.parts[1] != "deprecated"}
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
                    errors.append(f"{path.relative_to(root)}: operative call to retired or unknown skill {name}.")

    # The skill map at index.html is generated; keep it covering every promoted skill and current.
    if (root / "scripts/skill-graph/flow.json").exists():
        spec = importlib.util.spec_from_file_location("build_skill_graph", Path(__file__).with_name("build-skill-graph.py"))
        builder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(builder)
        html, problems = builder.render(root)
        errors.extend(problems)
        if not problems and (not (root / "index.html").exists() or (root / "index.html").read_text() != html):
            errors.append("index.html: stale skill map; run python3 scripts/build-skill-graph.py.")

    for error in errors:
        print(f"ERROR: {error}")
    print(f"Checked {len(skills)} skills, {len(promoted)} plugin paths, "
          f"{len(actual_pages)} documentation pages, and {len(markdown)} Markdown files.")
    return bool(errors)


if __name__ == "__main__":
    sys.exit(check(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent))
