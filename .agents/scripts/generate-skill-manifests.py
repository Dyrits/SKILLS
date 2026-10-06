#!/usr/bin/env python3
"""Write the APM manifests: one beside every SKILL.md that calls or hands over to another skill of this repository,
and the root apm.yml that publishes every skill as `<name>@dyrits` through an APM marketplace.

Every skill it calls through the Skill tool, and every skill it tells the user to run, becomes a sibling dependency
(`git: parent`), so `apm install` pulls the whole chain. Skills with no references get no manifest, and a manifest
whose skill lost its references is deleted. The root apm.yml lists each skill as a local marketplace package, and `apm pack`
writes them to marketplace.json at the repository root: APM reads that file first, while Claude Code only reads
.claude-plugin/marketplace.json, so the skills do not show up there as plugins. A consumer's marketplace ref
(`apm marketplace add Dyrits/SKILLS#<ref>`) is the ref every skill and dependency installs at; no tag is needed.

Usage: python3 .agents/scripts/generate-skill-manifests.py [--check] [REPOSITORY]
  --check  write nothing; exit 1 and list files that are missing, stale, or orphaned.
Needs: Python 3 standard library. Reuses scripts/check-skills.py to read the references.
"""

import importlib.util
import json
import sys
from pathlib import Path


def load_checker(root):
    spec = importlib.util.spec_from_file_location("check_skills", root / "scripts" / "check-skills.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def tagline(skill_file):
    """The first sentence of the SKILL.md description, as the short human-facing apm.yml description."""
    for line in skill_file.read_text().splitlines():
        if line.startswith("description:"):
            text = json.loads(line.split(":", 1)[1].strip()) if line.split(":", 1)[1].strip()[:1] == '"' \
                else line.split(":", 1)[1].strip()
            return text.split(". ")[0].rstrip(".") + "."
    return ""


def root_manifest(root, folders, version):
    lines = ["name: dyrits", f"version: {version}", 'description: "Agent skills for real engineering"', "license: MIT",
             "marketplace:", "  owner:", '    name: "Dylan J. Gerrits"', "    url: https://github.com/Dyrits",
             "  outputs:", "    claude: {}", "  claude:", "    output: marketplace.json", "  packages:"]
    for name, folder in folders.items():
        lines += [f"    - name: {name}", f"      source: ./{folder.relative_to(root).as_posix()}",
                  f"      description: {json.dumps(tagline(folder / 'SKILL.md'))}"]
    return "\n".join(lines) + "\n"


def manifests(root):
    checker = load_checker(root)
    version = json.loads((root / ".claude-plugin" / "plugin.json").read_text())["version"]
    folders = {path.parent.name: path.parent for path in sorted((root / "skills").glob("*/*/SKILL.md"))}
    wanted = {}
    for name, folder in folders.items():
        calls, handovers = checker.skill_references(folder)
        references = (calls | handovers | checker.prerequisites(folder)) - checker.EXTERNAL_SKILLS - {name}
        unknown = references - folders.keys()
        if unknown:
            sys.exit(f"{name} references skills this repository does not ship: {', '.join(sorted(unknown))}")
        if not references:
            continue
        lines = [f"name: {name}", f"version: {version}", f"description: {json.dumps(tagline(folder / 'SKILL.md'))}",
                 "dependencies:", "  apm:"]
        for dependency in sorted(references):
            lines += ["    - git: parent", f"      path: {folders[dependency].relative_to(root).as_posix()}"]
        wanted[folder / "apm.yml"] = "\n".join(lines) + "\n"
    wanted[root / "apm.yml"] = root_manifest(root, folders, version)
    return folders, wanted


def main():
    arguments = [argument for argument in sys.argv[1:] if argument != "--check"]
    root = Path(arguments[0] if arguments else ".").resolve()
    folders, wanted = manifests(root)
    existing = {folder / "apm.yml" for folder in folders.values() if (folder / "apm.yml").exists()}
    problems = [f"missing or stale: {path.relative_to(root)}" for path, text in wanted.items()
                if not path.exists() or path.read_text() != text]
    problems += [f"orphaned: {path.relative_to(root)}" for path in existing - wanted.keys()]
    if "--check" in sys.argv:
        print("\n".join(problems) or f"{len(wanted)} manifests current")
        sys.exit(1 if problems else 0)
    for path, text in wanted.items():
        path.write_text(text)
    for path in existing - wanted.keys():
        path.unlink()
    print(f"wrote {len(wanted)} manifests, removed {len(existing - wanted.keys())}")


if __name__ == "__main__":
    main()
