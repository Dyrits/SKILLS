#!/usr/bin/env python3
"""Replace literal text across files: print a reviewable patch, or apply it.

Usage: python3 .agents/scripts/update-references.py --replace OLD NEW [--replace OLD NEW ...]
           [--search [--exclude PATHSPEC ...] | -- PATH ...] [--format diff|apply-patch] [--apply]
Example: python3 .agents/scripts/update-references.py --replace '"wizard"' '"walk-through"'
           --search --exclude .agents/handoffs --apply
Needs: Python 3 standard library; Git for --search. Run from the repository root.

Without --apply, files are untouched and the patch goes to stdout: a unified diff that
`git apply` accepts, or Codex apply_patch input with --format apply-patch.
With --apply, files are rewritten and the unified diff of what changed goes to stdout.
--search finds every tracked or untracked, non-ignored text file containing an OLD value.
"""

import argparse
import difflib
import subprocess
import sys
from pathlib import Path


def search(values, excludes):
    pathspecs = ["."] + [f":(exclude){exclude}" for exclude in excludes]
    patterns = [argument for value in values for argument in ("-e", value)]
    result = subprocess.run(
        ["git", "grep", "-l", "-I", "-F", "--untracked", *patterns, "--", *pathspecs],
        capture_output=True, text=True, check=False,
    )
    if result.returncode not in (0, 1):
        sys.exit(f"git grep failed: {result.stderr.strip()}")
    return result.stdout.split()


def unified(filename, original, proposed):
    lines = difflib.unified_diff(
        original.splitlines(keepends=True), proposed.splitlines(keepends=True),
        fromfile=f"a/{filename}", tofile=f"b/{filename}", n=3,
    )
    return "".join(line if line.endswith("\n") else line + "\n\\ No newline at end of file\n"
                   for line in lines)


def apply_patch_section(parser, filename, original, proposed):
    if not original.endswith("\n") or not proposed.endswith("\n"):
        parser.error(f"{filename}: apply-patch output needs a final newline; no patch emitted.")
    lines = difflib.unified_diff(
        original.splitlines(keepends=True), proposed.splitlines(keepends=True), n=3
    )
    body = list(lines)[2:]
    # apply_patch uses a context selector rather than unified-diff line numbers.
    return "*** Update File: " + filename + "\n" + "".join(
        "@@\n" if line.startswith("@@") else line for line in body
    )


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--replace", nargs=2, action="append", required=True,
                        metavar=("OLD", "NEW"))
    parser.add_argument("--search", action="store_true",
                        help="find files containing any OLD value with git grep")
    parser.add_argument("--exclude", action="append", default=[], metavar="PATHSPEC",
                        help="path to skip during --search; repeatable")
    parser.add_argument("--format", choices=("diff", "apply-patch"), default="diff")
    parser.add_argument("--apply", action="store_true", help="rewrite the files")
    parser.add_argument("paths", nargs="*")
    arguments = parser.parse_args()

    if arguments.search == bool(arguments.paths):
        parser.error("give either --search or a list of paths, not both or neither.")
    if arguments.apply and arguments.format != "diff":
        parser.error("--apply reports a unified diff; drop --format apply-patch.")
    paths = (search([old for old, _ in arguments.replace], arguments.exclude)
             if arguments.search else arguments.paths)

    changes = []
    for filename in paths:
        original = Path(filename).read_text()
        proposed = original
        for before, after in arguments.replace:
            proposed = proposed.replace(before, after)
        if proposed != original:
            changes.append((filename, original, proposed))

    if arguments.format == "apply-patch":
        sections = [apply_patch_section(parser, *change) for change in changes]
        print("*** Begin Patch\n" + "".join(sections) + "*** End Patch")
    else:
        print("".join(unified(*change) for change in changes), end="")

    if arguments.apply:
        for filename, _, proposed in changes:
            Path(filename).write_text(proposed)
    action = "updated" if arguments.apply else "would change"
    print(f"{action} {len(changes)} file(s)", file=sys.stderr)


if __name__ == "__main__":
    main()
