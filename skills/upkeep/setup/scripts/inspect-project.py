#!/usr/bin/env python3
"""Report what a repository already has set up, in one short listing, so setup reads state instead of hunting for it.

Usage: inspect-project.py [DIRECTORY] [--json]
Output: one `key: value` line per finding (or a JSON object): Git state, languages by tracked file count, package
manager and scripts, formatter, linter, and typecheck configuration, older tooling and hook managers, the hooks
directory and its hooks, conventions documents, AGENTS.md pointers, setup records under .agents/, and the AI tools on
the path. A missing value prints as `-`.
Needs: Python 3 standard library; git for the Git lines. Reads files only.
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path

LOCKFILES = {"bun.lock": "bun", "bun.lockb": "bun", "pnpm-lock.yaml": "pnpm", "yarn.lock": "yarn",
             "package-lock.json": "npm", "uv.lock": "uv", "poetry.lock": "poetry", "Cargo.lock": "cargo",
             "go.sum": "go"}
CONFIGS = {
    "biome": ["biome.json", "biome.jsonc"],
    "oxlint": [".oxlintrc.json", "oxlint.config.ts"],
    "oxfmt": [".oxfmtrc.json", ".oxfmtrc.jsonc", "oxfmt.config.ts", "oxfmt.config.mts"],
    "eslint": [".eslintrc", ".eslintrc.js", ".eslintrc.cjs", ".eslintrc.json", ".eslintrc.yml", ".eslintrc.yaml",
               "eslint.config.js", "eslint.config.mjs", "eslint.config.cjs", "eslint.config.ts"],
    "prettier": [".prettierrc", ".prettierrc.json", ".prettierrc.yml", ".prettierrc.yaml", ".prettierrc.js",
                 ".prettierrc.cjs", ".prettierrc.mjs", "prettier.config.js", "prettier.config.cjs",
                 "prettier.config.mjs"],
    "ruff": ["ruff.toml", ".ruff.toml"],
    "typescript": ["tsconfig.json"],
    "editorconfig": [".editorconfig"],
    "lint-staged": [".lintstagedrc", ".lintstagedrc.json", ".lintstagedrc.js", "lint-staged.config.js"],
    "husky": [".husky"],
    "lefthook": ["lefthook.yml", "lefthook.yaml", ".lefthook.yml"],
    "pre-commit-framework": [".pre-commit-config.yaml"],
}
PACKAGE_KEYS = {"eslint": "eslint", "prettier": "prettier", "@biomejs/biome": "biome", "oxlint": "oxlint",
                "oxfmt": "oxfmt", "typescript": "typescript", "lint-staged": "lint-staged", "husky": "husky"}
CONVENTION_NAME = re.compile(r"(convention|style|contributing|coding)", re.IGNORECASE)
POINTER = re.compile(r"\]\(([^)#]+)")
SETUP_RECORDS = ("issue-tracker.md", "triage-roles.md", "ai-tooling.md")
AI_TOOLS = ("codegraph", "rtk", "ast-grep", "playwright-cli", "ctx7", "gh", "glab", "bun", "node", "python3", "uv")


def git(root, *arguments):
    try:
        result = subprocess.run(["git", "-C", str(root), *arguments], capture_output=True, text=True, timeout=10)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return result.stdout.strip() if result.returncode == 0 else None


def tracked_files(root):
    listing = git(root, "ls-files")
    if listing is not None:
        return [line for line in listing.splitlines() if line]
    skipped = {".git", "node_modules", ".venv", "dist", "build", "target"}
    return [str(path.relative_to(root)) for path in root.rglob("*")
            if path.is_file() and not skipped.intersection(path.relative_to(root).parts)][:20000]


def package_json(root):
    try:
        return json.loads((root / "package.json").read_text())
    except (OSError, ValueError):
        return {}


def inspect(root):
    report = {"root": str(root)}
    inside = git(root, "rev-parse", "--is-inside-work-tree") == "true"
    report["git"] = "yes" if inside else "no"
    if inside:
        remotes = git(root, "remote", "-v") or ""
        report["remotes"] = sorted({line.split()[1] for line in remotes.splitlines() if line.split()})
        head = git(root, "symbolic-ref", "--short", "refs/remotes/origin/HEAD")
        report["default_branch"] = head.split("/", 1)[1] if head else None
        report["hooks_path"] = git(root, "config", "core.hooksPath")
        hooks = git(root, "rev-parse", "--git-path", "hooks")
        hooks_directory = (root / hooks) if hooks else None
        report["hooks"] = sorted(path.name for path in hooks_directory.iterdir()
                                 if path.is_file() and not path.name.endswith(".sample")) \
            if hooks_directory and hooks_directory.is_dir() else []

    files = tracked_files(root)
    extensions = Counter(Path(name).suffix.lower() for name in files if Path(name).suffix)
    report["files"] = len(files)
    report["languages"] = [f"{extension}={count}" for extension, count in extensions.most_common(8)]

    report["package_managers"] = sorted({manager for name, manager in LOCKFILES.items() if (root / name).exists()})
    package = package_json(root)
    report["package_scripts"] = sorted(package.get("scripts", {}))
    declared = {**package.get("dependencies", {}), **package.get("devDependencies", {})}
    report["packages"] = sorted(label for key, label in PACKAGE_KEYS.items() if key in declared)

    found = {tool: [name for name in names if (root / name).exists()] for tool, names in CONFIGS.items()}
    if "prettier" in package:
        found["prettier"].append("package.json#prettier")
    if "eslintConfig" in package:
        found["eslint"].append("package.json#eslintConfig")
    if "lint-staged" in package:
        found["lint-staged"].append("package.json#lint-staged")
    pyproject = root / "pyproject.toml"
    if pyproject.is_file() and "[tool.ruff" in pyproject.read_text(errors="replace"):
        found["ruff"].append("pyproject.toml#tool.ruff")
    report["configs"] = [f"{tool}={','.join(names)}" for tool, names in found.items() if names]

    report["conventions_candidates"] = sorted(name for name in files
                                              if name.lower().endswith((".md", ".mdx", ".txt"))
                                              and CONVENTION_NAME.search(Path(name).stem)
                                              and name.count("/") <= 3
                                              and not any(part.startswith(".") for part in Path(name).parts))[:10]
    agents = root / "AGENTS.md"
    if agents.is_file():
        text = agents.read_text(errors="replace")
        report["agents_md"] = "yes"
        report["agents_md_pointers"] = sorted(set(POINTER.findall(text)))[:30]
        report["agent_skills_block"] = "yes" if "## Agent skills" in text else "no"
    else:
        report["agents_md"] = "no"
    report["setup_records"] = [name for name in SETUP_RECORDS if (root / ".agents" / name).is_file()]
    report["codegraph_index"] = "yes" if (root / ".codegraph").is_dir() else "no"
    report["on_path"] = [tool for tool in AI_TOOLS if shutil.which(tool)]
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("directory", nargs="?", default=".")
    parser.add_argument("--json", action="store_true")
    options = parser.parse_args()
    root = Path(options.directory).resolve()
    if not root.is_dir():
        print(f"inspect-project: {root} is not a directory", file=sys.stderr)
        return 1
    report = inspect(root)
    if options.json:
        print(json.dumps(report, indent=2))
        return 0
    for key, value in report.items():
        if isinstance(value, list):
            value = ", ".join(value)
        print(f"{key}: {value if value not in (None, '') else '-'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
