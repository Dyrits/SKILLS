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
import subprocess
import tempfile
import unittest
from pathlib import Path


spec = importlib.util.spec_from_file_location("check_skills", Path(__file__).with_name("check-skills.py"))
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)
spec = importlib.util.spec_from_file_location("build_skill_graph", Path(__file__).with_name("build-skill-graph.py"))
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class LayoutChecks(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(dir=os.environ.get("DELTA_SCRATCH_DIR"))
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.write(".claude-plugin/plugin.json", json.dumps(
            {"skills": ["./skills/reference/example", "./skills/productivity/helper"]}))
        self.write("README.md", "## Plugin skills\n[example](skills/reference/example/SKILL.md)\n"
                   "[helper](skills/productivity/helper/SKILL.md)\n")
        self.write("AGENTS.md", "Repository instructions.\n")
        self.write("skills/productivity/helper/SKILL.md",
                   "---\nname: helper\n---\nAn example helper skill.\n")
        self.write("skills/productivity/helper/agents/openai.yaml",
                   "interface:\n  display_name: Helper\n")
        self.write("skills/productivity/README.md", "[helper](./helper/SKILL.md)\n")
        self.write("skills/reference/example/SKILL.md", "---\nname: example\n---\nAn example skill.\n")
        self.write("skills/reference/example/agents/openai.yaml", "interface:\n  display_name: Example\n")
        self.write("skills/reference/README.md", "[example](./example/SKILL.md)\n")
        self.write("documentation/skills/reference/example.md",
                   "Upstream skill: `example`.\n\n## What it does\nOne job.\n\n"
                   "## When to reach for it\nA trigger.\n\n## Common questions\nA question.\n\n"
                   "## It's working if\nA signal.\n\n## Where it fits\nA role.\n")
        self.write("documentation/skills/productivity/helper.md",
                   "Fork-specific helper.\n\n## What it does\nHelps.\n\n"
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

    def test_codex_blocks_model_invocation(self):
        self.write("skills/reference/example/agents/openai.yaml",
                   "policy:\n  allow_implicit_invocation: false\n")
        failed, output = self.result()
        self.assertTrue(failed)
        self.assertIn("skill blocks model invocation", output)

    def test_claude_blocks_model_invocation(self):
        self.write("skills/reference/example/SKILL.md",
                   "---\nname: example\ndisable-model-invocation: true\n---\nAn example skill.\n")
        self.assertIn("skill blocks model invocation", self.result()[1])

    def test_evaluations_are_not_required(self):
        self.assertFalse(any((self.root / "skills").rglob("evals")))
        self.assertFalse(self.result()[0])

    def test_broken_relative_link(self):
        self.write("AGENTS.md", "[missing](missing.md)\n")
        self.assertIn("broken link missing.md", self.result()[1])

    def test_missing_provenance(self):
        path = self.root / "documentation/skills/reference/example.md"
        path.write_text(path.read_text().replace("Upstream skill: `example`.", "## Example"))
        self.assertIn("missing top provenance", self.result()[1])

    def test_orphan_documentation_page(self):
        self.write("documentation/skills/reference/retired.md", "Retired.\n")
        self.assertIn("orphan documentation page", self.result()[1])

    def test_skill_missing_from_manifest(self):
        self.write(".claude-plugin/plugin.json", '{"skills": ["./skills/productivity/helper"]}')
        (self.root / "documentation/skills/reference/example.md").unlink()
        self.assertIn("missing from the plugin manifest", self.result()[1])

    def add_skill_in_deprecated_bucket(self):
        self.write("skills/deprecated/old/SKILL.md", "---\nname: old\n---\nAn ordinary skill.\n")
        self.write("skills/deprecated/old/agents/openai.yaml", "interface:\n  display_name: Old\n")
        self.write("skills/deprecated/README.md", "[old](./old/SKILL.md)\n")
        self.write("skills/productivity/helper/SKILL.md",
                   "---\nname: helper\n---\nA helper skill.\n")
        self.write(".claude-plugin/plugin.json", json.dumps({"skills": [
            "./skills/reference/example", "./skills/productivity/helper", "./skills/deprecated/old"]}))
        with (self.root / "README.md").open("a") as listing:
            listing.write("[old](skills/deprecated/old/SKILL.md)\n")
        self.write("documentation/skills/deprecated/old.md",
                   (self.root / "documentation/skills/reference/example.md").read_text())

    def test_deprecated_bucket_obeys_uniform_requirements(self):
        self.add_skill_in_deprecated_bucket()
        self.assertEqual(self.result()[0], False)
        self.write(".claude-plugin/plugin.json", '{"skills": ["./skills/productivity/helper", "./skills/reference/example"]}')
        (self.root / "documentation/skills/deprecated/old.md").unlink()
        output = self.result()[1]
        self.assertIn("skills/deprecated/old: missing from the plugin manifest", output)
        self.assertIn("skills/deprecated/old: missing human-facing documentation page", output)

    def test_deprecated_bucket_requires_dependencies(self):
        self.add_skill_in_deprecated_bucket()
        self.write("skills/deprecated/old/SKILL.md",
                   '---\nname: old\n---\nCall the Skill tool with "example".\n')
        output = self.result()[1]
        self.assertIn("skills/deprecated/old: dependency paragraph should read: **Calls:** `example`.", output)

    def test_retired_operative_call(self):
        self.write("AGENTS.md", 'Call the Skill tool with "grilling".\n')
        self.assertIn("operative call to unknown", self.result()[1])

    def test_renamed_operative_calls(self):
        for retired in ("code-review-and-refactor", "to-pull-request",
                        "documentation", "writing-for-agents"):
            with self.subTest(skill=retired):
                self.write("AGENTS.md", f'Call the Skill tool with "{retired}".\n')
                self.assertIn("operative call to unknown", self.result()[1])

    def test_second_name_in_paired_call(self):
        self.write("AGENTS.md", 'Call the Skill tool twice, for "example" and "grill-me".\n')
        output = self.result()[1]
        self.assertIn("unknown skill grill-me", output)
        self.assertNotIn("unknown skill example", output)

    def test_deprecated_bucket_skill_is_callable(self):
        self.add_skill_in_deprecated_bucket()
        self.write("AGENTS.md", 'Call the Skill tool with "old".\n')
        self.assertEqual(self.result()[0], False)

    def test_linker_includes_every_bucket(self):
        self.add_skill_in_deprecated_bucket()
        self.write("scripts/link-skills.sh", Path(__file__).with_name("link-skills.sh").read_text())
        home = self.root / "home"
        subprocess.run(["bash", str(self.root / "scripts/link-skills.sh")],
                       env={**os.environ, "HOME": str(home)}, check=True, capture_output=True, text=True)
        for harness in (".claude", ".agents"):
            for bucket, name in (("reference", "example"), ("productivity", "helper"), ("deprecated", "old")):
                target = home / harness / "skills" / name
                self.assertTrue(target.is_symlink())
                self.assertEqual(target.resolve(), self.root / "skills" / bucket / name)

    def test_known_and_external_calls_pass(self):
        self.write("AGENTS.md", 'Call the Skill tool with "example". Call the Skill tool with "webapp-testing". '
                   'Call the Skill tool with "skill-creator".\n')
        self.assertEqual(self.result()[0], False)

    def test_historical_names_are_allowed(self):
        self.write("AGENTS.md", 'Source skill: `documentation`, now named `document`.\n')
        self.assertEqual(self.result()[0], False)

    def test_routing_tiers_follow_policy(self):
        self.write("skills/setup/setup-delegation-policy/POLICY.md", "| Light | Haiku | Luna |\n")
        self.write("skills/workflow/divide-and-conquer/ROUTING.md", "| Light | Haiku | Luna |\n")
        self.assertNotIn("tiers differ", self.result()[1])
        self.write("skills/workflow/divide-and-conquer/ROUTING.md", "| Light | Sonnet | Luna |\n")
        self.assertIn("tiers differ", self.result()[1])

    def test_calling_skill_needs_dependency_paragraph(self):
        body = '---\nname: example\n---\nCall the Skill tool with "helper".\n'
        self.write("skills/reference/example/SKILL.md", body)
        self.assertIn("dependency paragraph should read: **Calls:** `helper`.", self.result()[1])
        self.write("skills/reference/example/SKILL.md", body + "\n**Calls:** `helper`.\n")
        self.assertEqual(self.result()[0], False)

    def test_dependency_paragraph_skips_external_skills(self):
        self.write("skills/reference/example/SKILL.md",
                   '---\nname: example\n---\nCall the Skill tool with "webapp-testing". '
                   'Call the Skill tool with "skill-creator".\n')
        self.assertEqual(self.result()[0], False)

    def test_unquoted_description_with_colon_is_invalid(self):
        for description, flagged in (("Write things: and more.", True), ('"Write things: and more."', False),
                                     ("'Write things: and more.'", False), ("Write things, and more.", False)):
            self.write("skills/reference/example/SKILL.md", f"---\nname: example\ndescription: {description}\n---\nBody.\n")
            self.assertEqual("invalid YAML" in self.result()[1], flagged, description)

    def test_dependency_paragraph_inside_frontmatter(self):
        self.write("skills/reference/example/SKILL.md",
                   '---\nname: example\n**Calls:** `helper`.\n---\nCall the Skill tool with "helper".\n')
        self.assertIn("dependency paragraph sits inside the frontmatter", self.result()[1])

    def test_stale_dependency_paragraph(self):
        self.write("skills/reference/example/SKILL.md", "---\nname: example\n---\n**Calls:** `helper`.\n")
        self.assertIn("dependency paragraph should read: (none)", self.result()[1])

    def test_dependency_paragraph_carries_no_install_instructions(self):
        body = '---\nname: example\n---\nCall the Skill tool with "helper".\n\n**Calls:** `helper`.'
        self.write("skills/reference/example/SKILL.md", body + " If a called skill is not installed, install it.\n")
        self.assertIn("dependency paragraph should read: **Calls:** `helper`.", self.result()[1])
        self.assertNotIn("install", checker.calls_block({"document"}, {"helper"}))

    def test_backtick_and_script_calls_count(self):
        folder = self.root / "skills/reference/example"
        self.write("skills/reference/example/SKILL.md",
                   "---\nname: example\n---\nCall the Skill tool with `helper`.\n")
        self.assertEqual(checker.skill_references(folder)[0], {"helper"})
        self.write("skills/reference/example/SKILL.md", "---\nname: example\n---\nAn example skill.\n")
        self.write("skills/reference/example/scripts/gate.sh", 'echo "Call the Skill tool with \\"helper\\"."\n')
        self.assertEqual(checker.skill_references(folder)[0], {"helper"})

    def test_handover_needs_dependency_paragraph(self):
        body = "---\nname: example\n---\nTell the user to run `/helper`.\n"
        self.write("skills/reference/example/SKILL.md", body)
        self.assertIn("should read: **Hands over to:** `/helper`.", self.result()[1])
        self.write("skills/reference/example/SKILL.md", body + "\n**Hands over to:** `/helper`.\n")
        self.assertEqual(self.result()[0], False)

    def test_handover_for_missing_setup_is_a_prerequisite(self):
        self.write("skills/reference/example/SKILL.md", "---\nname: example\n---\n"
                   "If it is missing, tell the user to run `/helper` and stop. Tell the user to run `/other`.\n")
        self.assertEqual(checker.prerequisites(self.root / "skills/reference/example"), {"helper"})

    def test_missing_where_it_fits(self):
        path = self.root / "documentation/skills/reference/example.md"
        path.write_text(path.read_text().replace("## Where it fits\nA role.\n", ""))
        self.assertIn("required sections missing", self.result()[1])

    def write_skill_map(self, skills=("example", "helper")):
        self.write("scripts/skill-graph/flow.json", json.dumps({
            "artifacts": {"note": {"label": "Note", "description": "A note."}},
            "skills": {name: {"inputs": [], "outputs": ["note"], "next": []} for name in skills}}))
        self.write("skills/productivity/README.md", "# Productivity\n\nWorkflows.\n\n- [helper](./helper/SKILL.md): Route.\n")
        self.write("skills/reference/README.md", "# Reference\n\nDisciplines.\n\n- [example](./example/SKILL.md): Example.\n")
        self.write("scripts/skill-graph/template.html", "<script>const DATA = /*SKILL_GRAPH_DATA*/null;</script>\n")
        with contextlib.redirect_stdout(io.StringIO()):
            builder.main([str(self.root)])

    def test_current_skill_map_passes(self):
        self.write_skill_map()
        self.assertEqual(self.result()[0], False)

    def test_skill_map_includes_deprecated_bucket(self):
        self.add_skill_in_deprecated_bucket()
        self.write("skills/deprecated/README.md", "# Other\n\nSkills.\n\n- [old](./old/SKILL.md): Ordinary.\n")
        self.write_skill_map(skills=("example", "helper", "old"))
        self.assertEqual(self.result()[0], False)
        self.write_skill_map()
        self.assertIn("no entry for skill old", self.result()[1])

    def test_stale_skill_map(self):
        self.write_skill_map()
        self.write("index.html", "old")
        self.assertIn("stale skill map", self.result()[1])

    def test_skill_missing_from_bucket_listing(self):
        self.write_skill_map()
        self.write("skills/reference/README.md", "# Reference\n\nDisciplines.\n\n[example](./example/SKILL.md)\n")
        self.assertIn("no one-line entry for example", self.result()[1])

    def test_skill_missing_from_map(self):
        self.write_skill_map(skills=("helper",))
        self.assertIn("no entry for skill example", self.result()[1])


if __name__ == "__main__":
    unittest.main()
