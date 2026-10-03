#!/usr/bin/env python3
"""Capture a Git review patch, scope, and changed-file contents without staging.

Usage: python3 .agents/scripts/capture-review-state.py OUTPUT BASE [REPOSITORY]
Needs: Python 3 and Git. Creates OUTPUT once, outside the repository.
"""

import json
import subprocess
import sys
from pathlib import Path


def capture(output, base, repository):
    root = Path(repository).resolve()
    destination = Path(output).resolve()
    if destination == root or root in destination.parents:
        raise ValueError("Review output must be outside the repository.")

    def git(*arguments):
        return subprocess.check_output(["git", "-C", str(root), *arguments])

    fixed = git("rev-parse", "--verify", f"{base}^{{commit}}").decode().strip()
    head = git("rev-parse", "HEAD").decode().strip()
    merge_base = git("merge-base", fixed, head).decode().strip()
    tracked = git("diff", "--name-only", "-z", merge_base)
    untracked = git("ls-files", "--others", "--exclude-standard", "-z")
    paths = sorted({name.decode() for name in (tracked + untracked).split(b"\0") if name})
    destination.mkdir(parents=True, exist_ok=False)
    (destination / "starting.patch").write_bytes(git("diff", merge_base))
    (destination / "commits.txt").write_bytes(git("log", f"{fixed}..{head}", "--oneline"))
    (destination / "status.txt").write_bytes(git("--no-optional-locks", "status", "--short"))
    (destination / "scope.json").write_text(json.dumps({
        "fixed_point": fixed, "starting_HEAD": head, "merge_base": merge_base, "paths": paths
    }, indent=2) + "\n")
    symlinks = {}
    for name in paths:
        source = root / name
        cursor = root
        for part in Path(name).parts:
            cursor = cursor / part
            if cursor.is_symlink():
                symlinks[name] = {
                    "type": "symlink" if cursor == source else "symlink-parent",
                    "path": str(cursor.relative_to(root)),
                    "target": str(cursor.readlink()),
                }
                break
        if name in symlinks:
            continue
        if not source.is_file():
            continue
        target = destination / "contents" / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(source.read_bytes())
    (destination / "symlinks.json").write_text(json.dumps(symlinks, indent=2) + "\n")
    print(f"{destination}: captured {len(paths)} paths against {fixed}.")


if __name__ == "__main__":
    if len(sys.argv) not in (3, 4):
        raise SystemExit(__doc__)
    capture(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) == 4 else ".")
