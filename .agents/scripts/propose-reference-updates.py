#!/usr/bin/env python3
"""Propose literal text replacements with three context lines; never edit files.

Usage: python3 .agents/scripts/propose-reference-updates.py --replace OLD NEW -- PATH...
Needs: Python 3 standard library. Review stdout before applying with apply_patch.
"""

import argparse
import difflib
from pathlib import Path


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--replace", nargs=2, action="append", default=[])
parser.add_argument("paths", nargs="+")
arguments = parser.parse_args()
sections = []
for filename in arguments.paths:
    path = Path(filename)
    original = path.read_text()
    proposed = original
    for before, after in arguments.replace:
        proposed = proposed.replace(before, after)
    if proposed == original:
        continue
    if not original.endswith("\n") or not proposed.endswith("\n"):
        parser.error(f"{filename}: changed files must have a final newline; no patch emitted.")
    diff = list(difflib.unified_diff(
        original.splitlines(keepends=True), proposed.splitlines(keepends=True), n=3
    ))
    sections.append("*** Update File: " + filename + "\n")
    for line in diff[2:]:
        # apply_patch uses a context selector rather than unified-diff line numbers.
        sections.append("@@\n" if line.startswith("@@") else line)
print("*** Begin Patch")
print("".join(sections), end="")
print("*** End Patch")
