#!/usr/bin/env python3
"""Exercise the harness detector against a fake home directory, and keep its two bundled copies identical.

Usage: python3 scripts/test-detect-harnesses.py
Needs: Python 3 standard library. Uses temporary directories only.
"""

import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

SKILLS = Path(__file__).resolve().parent.parent / "skills/getting-started"
COPIES = [SKILLS / "setup-delegation-policy/scripts/detect-harnesses.py",
          SKILLS / "setup/scripts/detect-harnesses.py"]


class Detector(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.home = Path(temporary.name).resolve()

    def make(self, relative, text=None):
        path = self.home / relative
        if text is None:
            path.mkdir(parents=True, exist_ok=True)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text)

    def detect(self, *arguments):
        result = subprocess.run(["python3", "-I", str(COPIES[0]), "--json", *arguments], capture_output=True,
                                text=True, env={**os.environ, "HOME": str(self.home)})
        return {item["name"]: item for item in json.loads(result.stdout)}

    def test_reports_steering_policy_and_tier_agents(self):
        self.make(".alpha/AGENTS.md", "x\n\n## Delegation and model routing\n\nbody\n")
        self.make(".alpha/agents/light.md", "---\n---\n")
        self.make(".beta/skills")
        self.make(".noise/settings.json", "{}")
        found = self.detect()
        self.assertTrue(found["alpha"]["configured"] and found["alpha"]["policy"])
        self.assertEqual(found["alpha"]["tier_agents"], ["light"])
        self.assertFalse(found["beta"]["configured"])
        self.assertNotIn("noise", found)

    def test_config_directory_and_project_root(self):
        self.make(".config/gamma/CLAUDE.md", "no policy\n")
        project = self.home / "project"
        self.make("project/.delta/skills")
        found = self.detect("--project", str(project))
        self.assertFalse(found["gamma"]["policy"])
        self.assertEqual(found["delta"]["scope"], "project")

    def test_bundled_copies_are_identical(self):
        self.assertEqual(COPIES[0].read_text(), COPIES[1].read_text())


if __name__ == "__main__":
    unittest.main()
