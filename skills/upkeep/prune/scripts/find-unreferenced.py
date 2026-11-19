#!/usr/bin/env python3
"""List tracked files whose name appears in no other tracked text file.

Usage: find-unreferenced.py [--stem] [--exclude GLOB]... PATH...

Candidates are the Git-tracked files under each PATH. A candidate counts as
referenced when its file name (``logo.png``) appears as a whole token in any
other tracked text file of the repository; with ``--stem``, its name without
the extension (``logo``) also counts, for modules imported without one.
``--exclude`` drops candidates matching a glob (repeatable), matched against
the path relative to the repository root.

Output: one unreferenced path per line, relative to the repository root, then
a summary line on standard error. Exit codes: 0 when the run completed (with
or without results), 2 on a usage or Git error.

The check errs toward "referenced": a common name such as ``index`` matches
almost everywhere. It cannot see a name built from strings at run time
(``"icon-" + name + ".svg"``), a glob, or a reference from outside the
repository, so an unreferenced path is a candidate, not a verdict.

Needs: Python 3.8+ and Git.
"""

import argparse
import fnmatch
import os
import re
import subprocess
import sys

# Characters that can sit inside a file name as written in code, markup, or
# configuration. Path separators, quotes, and brackets end a token, so
# "/images/logo.png" yields the token "logo.png".
TOKEN = re.compile(rb"[A-Za-z0-9_@.+-]+")

# Files larger than this are almost always data or bundles, not source that
# references other files; reading them would slow the scan without benefit.
MAX_TEXT_BYTES = 2 * 1024 * 1024


def git(root, *arguments):
    result = subprocess.run(["git", "-C", root, *arguments], capture_output=True)
    if result.returncode != 0:
        print("git %s failed: %s" % (" ".join(arguments), result.stderr.decode(errors="replace").strip()), file=sys.stderr)
        sys.exit(2)
    return result.stdout


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("paths", nargs="+", metavar="PATH")
    parser.add_argument("--stem", action="store_true", help="also count the name without its extension")
    parser.add_argument("--exclude", action="append", default=[], metavar="GLOB")
    options = parser.parse_args()

    probe = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True)
    if probe.returncode != 0:
        print("not inside a Git repository", file=sys.stderr)
        return 2
    root = probe.stdout.decode().strip()

    tracked = [p.decode() for p in git(root, "ls-files", "-z").split(b"\0") if p]
    prefixes = []
    for path in options.paths:
        relative = os.path.relpath(os.path.abspath(path), root).replace(os.sep, "/")
        prefixes.append("" if relative == "." else relative.rstrip("/") + "/")
    candidates = [
        p for p in tracked
        if any(p.startswith(prefix) or p + "/" == prefix for prefix in prefixes)
        and not any(fnmatch.fnmatch(p, pattern) for pattern in options.exclude)
    ]
    if not candidates:
        print("no tracked files under the given paths", file=sys.stderr)
        return 0

    # For each token, remember up to two files containing it: enough to know
    # whether a file other than the candidate itself mentions the token.
    holders = {}
    for path in tracked:
        full = os.path.join(root, path)
        try:
            if os.path.getsize(full) > MAX_TEXT_BYTES:
                continue
            with open(full, "rb") as handle:
                content = handle.read()
        except OSError:
            continue  # a tracked file deleted in the working tree
        if b"\0" in content[:8192]:
            continue  # binary
        for token in set(TOKEN.findall(content)):
            seen = holders.setdefault(token, [])
            if len(seen) < 2:
                seen.append(path)

    def referenced(path, name):
        return any(holder != path for holder in holders.get(name.encode(), ()))

    unreferenced = []
    for path in candidates:
        name = path.rsplit("/", 1)[-1]
        names = [name]
        stem = name.split(".", 1)[0]
        if options.stem and stem and stem != name:
            names.append(stem)
        if not any(referenced(path, n) for n in names):
            unreferenced.append(path)

    for path in unreferenced:
        print(path)
    print("%d of %d candidates unreferenced" % (len(unreferenced), len(candidates)), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
