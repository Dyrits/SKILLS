#!/usr/bin/env python3
"""Exercise the layout check against small temporary repository fixtures.

Usage: python3 scripts/test-check-skills.py
Needs: Python 3 standard library. Uses temporary files only.
"""

import contextlib
import importlib.util
import io
import json
import os
import tempfile
import unittest
from pathlib import Path


spec = importlib.util.spec_from_file_location("check_skills", Path(__file__).with_name("check-skills.py"))
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class LayoutChecks(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(dir=os.environ.get("DELTA_SCRATCH_DIR"))
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.write(".claude-plugin/plugin.json", json.dumps(
            {"skills": ["./skills/reference/example", "./skills/getting-started/guide"]}))
        self.write("README.md", "## Plugin skills\n[example](skills/reference/example/SKILL.md)\n"
                   "[guide](skills/getting-started/guide/SKILL.md)\n")
        self.write("CLAUDE.md", "Repository instructions.\n")
        self.write("skills/getting-started/guide/SKILL.md",
                   "---\nname: guide\n---\nRoute to /example and /guide.\n")
        self.write("skills/getting-started/guide/agents/openai.yaml",
                   "interface:\n  display_name: Router\n")
        self.write("skills/getting-started/README.md", "[router](./guide/SKILL.md)\n")
        self.write("skills/reference/example/SKILL.md", "---\nname: example\n---\nAn example skill.\n")
        self.write("skills/reference/example/agents/openai.yaml", "interface:\n  display_name: Example\n")
        self.write("skills/reference/README.md", "[example](./example/SKILL.md)\n")
        self.write("documentation/skills/reference/example.md",
                   "Upstream skill: `example`.\n\n## What it does\nOne job.\n\n"
                   "## When to reach for it\nA trigger.\n\n## Common questions\nA question.\n\n"
                   "## It's working if\nA signal.\n\n## Where it fits\nA role.\n")
        self.write("documentation/skills/getting-started/guide.md",
                   "Fork-specific router.\n\n## What it does\nRoutes.\n\n"
                   "## When to reach for it\nA trigger.\n\n## Common questions\nA question.\n\n"
                   "## It's working if\nA signal.\n\n## Where it fits\nA role.\n")

    def write(self, relative, content):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)

    def result(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            failed = checker.check(self.root)
        return failed, output.getvalue()

    def test_consistent_fixture(self):
        self.assertEqual(self.result()[0], False)

    def test_invocation_mismatch(self):
        self.write("skills/reference/example/agents/openai.yaml",
                   "policy:\n  allow_implicit_invocation: false\n")
        failed, output = self.result()
        self.assertTrue(failed)
        self.assertIn("invocation policy differs", output)

    def test_broken_relative_link(self):
        self.write("CLAUDE.md", "[missing](missing.md)\n")
        self.assertIn("broken link missing.md", self.result()[1])

    def test_missing_provenance(self):
        path = self.root / "documentation/skills/reference/example.md"
        path.write_text(path.read_text().replace("Upstream skill: `example`.", "## Example"))
        self.assertIn("missing top provenance", self.result()[1])

    def test_orphan_documentation_page(self):
        self.write("documentation/skills/reference/retired.md", "Retired.\n")
        self.assertIn("orphan documentation page", self.result()[1])

    def test_skill_missing_from_manifest(self):
        self.write(".claude-plugin/plugin.json", '{"skills": ["./skills/getting-started/guide"]}')
        (self.root / "documentation/skills/reference/example.md").unlink()
        self.assertIn("missing from the plugin manifest", self.result()[1])

    def test_deprecated_skill_in_manifest(self):
        self.write("skills/deprecated/old/SKILL.md", "---\nname: old\n---\nRetired.\n")
        self.write("skills/deprecated/old/agents/openai.yaml", "interface:\n  display_name: Old\n")
        self.write("skills/deprecated/README.md", "[old](./old/SKILL.md)\n")
        self.write("skills/getting-started/guide/SKILL.md",
                   "---\nname: guide\n---\nRoute to /example, /guide, and /old.\n")
        self.write(".claude-plugin/plugin.json", json.dumps({"skills": [
            "./skills/reference/example", "./skills/getting-started/guide", "./skills/deprecated/old"]}))
        self.assertIn("deprecated skill is in the plugin manifest", self.result()[1])

    def test_retired_operative_call(self):
        self.write("CLAUDE.md", 'Call the Skill tool with "grilling".\n')
        self.assertIn("operative call to retired", self.result()[1])

    def test_renamed_operative_calls(self):
        for retired in ("code-review-and-refactor", "to-pull-request",
                        "documentation", "writing-for-agents"):
            with self.subTest(skill=retired):
                self.write("CLAUDE.md", f'Call the Skill tool with "{retired}".\n')
                self.assertIn("operative call to retired", self.result()[1])

    def test_historical_names_are_allowed(self):
        self.write("CLAUDE.md", 'Source skill: `documentation`, now named `document`.\n')
        self.assertEqual(self.result()[0], False)

    def test_missing_where_it_fits(self):
        path = self.root / "documentation/skills/reference/example.md"
        path.write_text(path.read_text().replace("## Where it fits\nA role.\n", ""))
        self.assertIn("required sections missing", self.result()[1])


if __name__ == "__main__":
    unittest.main()
