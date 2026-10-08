#!/usr/bin/env python3
"""List the agent harnesses configured on this machine, from what is on disk, without naming any harness.

Usage: detect-harnesses.py [--project DIR] [--json]
A directory in the home directory, in ~/.config, or (with --project) at the project root counts as a harness when it
holds a steering file (AGENTS.md, CLAUDE.md, GEMINI.md, QWEN.md) or an agents/skills directory, or at least two weaker
signs (commands, rules, hooks, an MCP file). Per candidate it reports the command found on the path, its steering
files, whether they already carry the delegation section, and which tier agents exist.
Output: one line per configured candidate (a steering file, a command on the path, or agent files), then one line naming
the skills-only directories (a skills installer writes those for many harnesses, installed or not), or a JSON list.
The result is a list of candidates for the user to confirm.
Needs: Python 3 standard library. Reads files only.
"""

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

STEERING = ("AGENTS.md", "CLAUDE.md", "GEMINI.md", "QWEN.md")
STRONG_DIRECTORIES = ("agents", "skills", "subagents")
WEAK_SIGNS = ("commands", "rules", "hooks", "prompts", "mcp.json", "mcp_config.json", "mcp-servers.json")
TIERS = ("light", "balanced", "heavy", "frontier")
HEADING = re.compile(r"^## Delegation and model routing\s*$", re.MULTILINE)


def inspect(directory):
    """The evidence a directory holds that it belongs to an agent harness, or None."""
    steering = [name for name in STEERING if (directory / name).is_file()]
    strong = [f"{name}/" for name in STRONG_DIRECTORIES if (directory / name).is_dir()]
    weak = [name for name in WEAK_SIGNS if (directory / name).exists()]
    if not (steering or strong or len(weak) >= 2):
        return None
    policy = any(HEADING.search((directory / name).read_text(errors="replace")) for name in steering)
    tiers = sorted({path.stem for name in ("agents", "subagents") if (directory / name).is_dir()
                    for path in (directory / name).iterdir() if path.stem in TIERS})
    name = directory.name.lstrip(".")
    command = shutil.which(name) or shutil.which(name.replace("-cli", ""))
    configured = bool(steering or command or tiers or (directory / "agents").is_dir())
    return {"name": name, "configured": configured, "directory": str(directory), "command": command,
            "steering": steering, "policy": policy, "tier_agents": tiers, "evidence": steering + strong + weak}


def candidates(project):
    home = Path.home()
    roots = [(home, True), (home / ".config", False)]
    if project:
        roots.append((Path(project), True))
    for root, dot_only in roots:
        if not root.is_dir():
            continue
        for entry in sorted(root.iterdir()):
            hidden = entry.name.startswith(".")
            if entry.is_dir() and (hidden or not dot_only) and entry.name not in (".git", ".Trash", ".config"):
                found = inspect(entry)
                if found:
                    found["scope"] = "project" if project and root == Path(project) else "home"
                    yield found


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--project")
    parser.add_argument("--json", action="store_true")
    options = parser.parse_args()
    found = list(candidates(options.project))
    if options.json:
        print(json.dumps(found, indent=2))
        return 0
    for item in found:
        if item["configured"]:
            print(f"{item['name']}  {item['directory']}  scope={item['scope']}  command={item['command'] or '-'}  "
                  f"steering={','.join(item['steering']) or '-'}  policy={'yes' if item['policy'] else 'no'}  "
                  f"tier_agents={','.join(item['tier_agents']) or '-'}  evidence={','.join(item['evidence'])}")
    skills_only = [item["name"] for item in found if not item["configured"]]
    if skills_only:
        print("skills-only: " + ", ".join(skills_only))
    return 0


if __name__ == "__main__":
    sys.exit(main())
