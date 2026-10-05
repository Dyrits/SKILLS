#!/usr/bin/env python3
"""Stage a skill's evals for a dry run without showing the runner its expectations.

Writes WORKSPACE/<skill>/eval-<id>/prompt.txt for each selected eval, copies the skill's
evals/files/ to WORKSPACE/<skill>/files/, and writes WORKSPACE/<skill>/grading-sheet.md with
every expectation for the grader.

Usage: python3 .agents/scripts/stage-eval-run.py WORKSPACE SKILL_DIRECTORY [KIND ...]
Example: python3 .agents/scripts/stage-eval-run.py /tmp/skill-evals/run-1 skills/workflow/taskify behavior
Needs: Python 3. Refuses to overwrite an existing skill workspace.
"""

import json
import shutil
import sys
from pathlib import Path


def stage(workspace, skill_directory, kinds):
    skill = Path(skill_directory).resolve()
    data = json.loads((skill / "evals" / "evals.json").read_text())
    target = Path(workspace).resolve() / data["skill_name"]
    target.mkdir(parents=True, exist_ok=False)
    fixtures = skill / "evals" / "files"
    if fixtures.is_dir():
        shutil.copytree(fixtures, target / "files")
    sheet = [f"# Grading sheet: {data['skill_name']}", ""]
    staged = []
    for case in data["evals"]:
        if kinds and case["kind"] not in kinds:
            continue
        folder = target / f"eval-{case['id']}"
        folder.mkdir()
        (folder / "prompt.txt").write_text(case["prompt"] + "\n")
        sheet += [f"## Eval {case['id']} ({case['kind']})", "", f"Expected: {case['expected_output']}", ""]
        sheet += [f"- [ ] {line}" for line in case["expectations"]] + [""]
        staged.append(case["id"])
    (target / "grading-sheet.md").write_text("\n".join(sheet))
    return target, staged


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    where, ids = stage(sys.argv[1], sys.argv[2], set(sys.argv[3:]))
    print(f"Staged evals {ids} in {where}")
