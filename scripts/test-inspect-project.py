#!/usr/bin/env python3
"""Exercise the setup skill's project inspector against scratch repositories.

Usage: python3 -I scripts/test-inspect-project.py
Needs: Python 3 standard library and git. Uses temporary directories only.
"""

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "skills/getting-started/setup/scripts/inspect-project.py"


def inspect(directory):
    result = subprocess.run(["python3", "-I", str(SCRIPT), str(directory), "--json"],
                            capture_output=True, text=True, check=True)
    return json.loads(result.stdout)


class Inspector(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()

    def write(self, relative, text=""):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    def test_empty_folder_reports_no_git_and_no_files(self):
        report = inspect(self.root)
        self.assertEqual(report["git"], "no")
        self.assertEqual(report["files"], 0)
        self.assertEqual(report["agents_md"], "no")

    def test_reports_tools_older_tooling_and_conventions(self):
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        self.write("package.json", json.dumps({"scripts": {"typecheck": "tsc"},
                                               "devDependencies": {"eslint": "9", "prettier": "3"}}))
        self.write("eslint.config.js")
        self.write("biome.json", "{}")
        self.write("bun.lock")
        self.write("src/index.ts")
        self.write("CONTRIBUTING.md")
        self.write(".agents/handoffs/style-notes.md")
        self.write("AGENTS.md", "## Agent skills\n\nSee [conventions](./documentation/conventions.md).\n")
        subprocess.run(["git", "-C", str(self.root), "add", "-A"], check=True)
        report = inspect(self.root)
        self.assertEqual(report["git"], "yes")
        self.assertIn("bun", report["package_managers"])
        self.assertEqual(report["package_scripts"], ["typecheck"])
        self.assertEqual(report["packages"], ["eslint", "prettier"])
        self.assertIn("biome=biome.json", report["configs"])
        self.assertIn("eslint=eslint.config.js", report["configs"])
        self.assertEqual(report["conventions_candidates"], ["CONTRIBUTING.md"])
        self.assertEqual(report["agents_md_pointers"], ["./documentation/conventions.md"])
        self.assertEqual(report["agent_skills_block"], "yes")

    def test_reports_hooks_path(self):
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        subprocess.run(["git", "-C", str(self.root), "config", "core.hooksPath", ".githooks"], check=True)
        self.write(".githooks/pre-commit", "#!/bin/sh\n")
        report = inspect(self.root)
        self.assertEqual(report["hooks_path"], ".githooks")
        self.assertEqual(report["hooks"], ["pre-commit"])


if __name__ == "__main__":
    unittest.main()
