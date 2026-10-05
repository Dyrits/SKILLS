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
spec = importlib.util.spec_from_file_location("build_skill_graph", Path(__file__).with_name("build-skill-graph.py"))
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class LayoutChecks(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(dir=os.environ.get("DELTA_SCRATCH_DIR"))
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.write(".claude-plugin/plugin.json", json.dumps(
            {"skills": ["./skills/reference/example", "./skills/productivity/guide"]}))
        self.write("README.md", "## Plugin skills\n[example](skills/reference/example/SKILL.md)\n"
                   "[guide](skills/productivity/guide/SKILL.md)\n")
        self.write("CLAUDE.md", "Repository instructions.\n")
        self.write("skills/productivity/guide/SKILL.md",
                   "---\nname: guide\n---\nRoute to /example and /guide.\n")
        self.write("skills/productivity/guide/agents/openai.yaml",
                   "interface:\n  display_name: Router\n")
        self.write("skills/productivity/README.md", "[router](./guide/SKILL.md)\n")
        self.write("skills/reference/example/SKILL.md", "---\nname: example\n---\nAn example skill.\n")
        self.write("skills/reference/example/agents/openai.yaml", "interface:\n  display_name: Example\n")
        self.write("skills/reference/README.md", "[example](./example/SKILL.md)\n")
        self.write("documentation/skills/reference/example.md",
                   "Upstream skill: `example`.\n\n## What it does\nOne job.\n\n"
                   "## When to reach for it\nA trigger.\n\n## Common questions\nA question.\n\n"
                   "## It's working if\nA signal.\n\n## Where it fits\nA role.\n")
        self.write("documentation/skills/productivity/guide.md",
                   "Fork-specific router.\n\n## What it does\nRoutes.\n\n"
                   "## When to reach for it\nA trigger.\n\n## Common questions\nA question.\n\n"
                   "## It's working if\nA signal.\n\n## Where it fits\nA role.\n")

        for bucket, name in (("reference", "example"), ("productivity", "guide")):
            self.write(f"skills/{bucket}/{name}/evals/evals.json", json.dumps(self.evaluations(name)))

    @staticmethod
    def evaluations(name):
        return {"skill_name": name, "evals": [
            {"id": number, "kind": kind, "prompt": "A request.", "expected_output": "A result.",
             "expectations": ["One observable.", "Another observable."]}
            for number, kind in enumerate(("trigger", "behavior", "no-trigger"), 1)]}

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

    def test_missing_evaluations(self):
        (self.root / "skills/reference/example/evals/evals.json").unlink()
        self.assertIn("missing evals/evals.json", self.result()[1])

    def test_evaluations_need_every_kind(self):
        document = self.evaluations("example")
        document["evals"][2]["kind"] = "trigger"
        self.write("skills/reference/example/evals/evals.json", json.dumps(document))
        self.assertIn("covering trigger, behavior, no-trigger", self.result()[1])

    def test_evaluations_name_must_match(self):
        self.write("skills/reference/example/evals/evals.json", json.dumps(self.evaluations("other")))
        self.assertIn("skill_name should be example", self.result()[1])

    def test_evaluation_needs_expectations_and_files(self):
        document = self.evaluations("example")
        document["evals"][0]["expectations"] = ["Only one."]
        document["evals"][1]["files"] = ["evals/files/absent.txt"]
        self.write("skills/reference/example/evals/evals.json", json.dumps(document))
        output = self.result()[1]
        self.assertIn("eval 1 needs at least two", output)
        self.assertIn("missing file evals/files/absent.txt", output)

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
        self.write(".claude-plugin/plugin.json", '{"skills": ["./skills/productivity/guide"]}')
        (self.root / "documentation/skills/reference/example.md").unlink()
        self.assertIn("missing from the plugin manifest", self.result()[1])

    def test_deprecated_skill_in_manifest(self):
        self.write("skills/deprecated/old/SKILL.md", "---\nname: old\n---\nRetired.\n")
        self.write("skills/deprecated/old/agents/openai.yaml", "interface:\n  display_name: Old\n")
        self.write("skills/deprecated/README.md", "[old](./old/SKILL.md)\n")
        self.write("skills/productivity/guide/SKILL.md",
                   "---\nname: guide\n---\nRoute to /example, /guide, and /old.\n")
        self.write(".claude-plugin/plugin.json", json.dumps({"skills": [
            "./skills/reference/example", "./skills/productivity/guide", "./skills/deprecated/old"]}))
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

    def test_second_name_in_paired_call(self):
        self.write("CLAUDE.md", 'Call the Skill tool twice, for "example" and "grill-me".\n')
        output = self.result()[1]
        self.assertIn("unknown skill grill-me", output)
        self.assertNotIn("unknown skill example", output)

    def test_deprecated_skill_is_not_callable(self):
        self.write("skills/deprecated/old/SKILL.md", "---\nname: old\n---\nRetired.\n")
        self.write("skills/deprecated/old/agents/openai.yaml", "interface:\n  display_name: Old\n")
        self.write("skills/deprecated/README.md", "[old](./old/SKILL.md)\n")
        self.write("skills/productivity/guide/SKILL.md",
                   "---\nname: guide\n---\nRoute to /example, /guide, and /old.\n")
        self.write("CLAUDE.md", 'Call the Skill tool with "old".\n')
        self.assertIn("unknown skill old", self.result()[1])

    def test_known_and_external_calls_pass(self):
        self.write("CLAUDE.md", 'Call the Skill tool with "example". Call the Skill tool with "webapp-testing".\n')
        self.assertEqual(self.result()[0], False)

    def test_historical_names_are_allowed(self):
        self.write("CLAUDE.md", 'Source skill: `documentation`, now named `document`.\n')
        self.assertEqual(self.result()[0], False)

    def test_routing_tiers_follow_policy(self):
        self.write("skills/setup/setup-delegation-policy/POLICY.md", "| Light | Haiku | Luna |\n")
        self.write("skills/workflow/divide-and-conquer/ROUTING.md", "| Light | Haiku | Luna |\n")
        self.assertNotIn("tiers differ", self.result()[1])
        self.write("skills/workflow/divide-and-conquer/ROUTING.md", "| Light | Sonnet | Luna |\n")
        self.assertIn("tiers differ", self.result()[1])

    def test_calling_skill_needs_dependency_paragraph(self):
        body = '---\nname: example\n---\nCall the Skill tool with "guide".\n'
        self.write("skills/reference/example/SKILL.md", body)
        self.assertIn("dependency paragraph should read: **Calls:** `guide`.", self.result()[1])
        self.write("skills/reference/example/SKILL.md", body + "\n" + checker.calls_block({"guide"}) + "\n")
        self.assertEqual(self.result()[0], False)

    def test_dependency_paragraph_skips_external_skills(self):
        self.write("skills/reference/example/SKILL.md",
                   '---\nname: example\n---\nCall the Skill tool with "webapp-testing".\n')
        self.assertEqual(self.result()[0], False)

    def test_stale_dependency_paragraph(self):
        self.write("skills/reference/example/SKILL.md",
                   "---\nname: example\n---\n" + checker.calls_block({"guide"}) + "\n")
        self.assertIn("dependency paragraph should read: (none)", self.result()[1])

    def test_document_dependency_waits(self):
        self.assertIn("wait until the user installs it", checker.calls_block({"document"}))
        self.assertNotIn("wait until", checker.calls_block({"guide"}))

    def test_backtick_and_script_calls_count(self):
        self.write("skills/reference/example/SKILL.md",
                   "---\nname: example\n---\nCall the Skill tool with `guide`.\n")
        self.assertIn("should read: **Calls:** `guide`.", self.result()[1])
        self.write("skills/reference/example/SKILL.md", "---\nname: example\n---\nAn example skill.\n")
        self.write("skills/reference/example/scripts/gate.sh", 'echo "Call the Skill tool with \\"guide\\"."\n')
        self.assertIn("should read: **Calls:** `guide`.", self.result()[1])

    def test_handover_needs_dependency_paragraph(self):
        body = "---\nname: example\n---\nTell the user to run `/guide`.\n"
        self.write("skills/reference/example/SKILL.md", body)
        self.assertIn("should read: **Hands over to:** `/guide`.", self.result()[1])
        block = checker.calls_block(set(), {"guide"})
        self.write("skills/reference/example/SKILL.md", body + "\n" + block + "\n")
        self.assertEqual(self.result()[0], False)

    def test_handover_for_missing_setup_is_a_prerequisite(self):
        self.write("skills/reference/example/SKILL.md", "---\nname: example\n---\n"
                   "If it is missing, tell the user to run `/guide` and stop. Tell the user to run `/other`.\n")
        self.assertEqual(checker.prerequisites(self.root / "skills/reference/example"), {"guide"})

    def test_router_carries_no_dependency_paragraph(self):
        self.write("skills/productivity/guide/SKILL.md",
                   "---\nname: guide\n---\nRoute to /example and /guide. Tell the user to run `/example`.\n")
        self.assertEqual(self.result()[0], False)

    def test_missing_where_it_fits(self):
        path = self.root / "documentation/skills/reference/example.md"
        path.write_text(path.read_text().replace("## Where it fits\nA role.\n", ""))
        self.assertIn("required sections missing", self.result()[1])

    def write_skill_map(self, skills=("example", "guide")):
        self.write("scripts/skill-graph/flow.json", json.dumps({
            "artifacts": {"note": {"label": "Note", "description": "A note."}},
            "skills": {name: {"inputs": [], "outputs": ["note"], "next": []} for name in skills}}))
        self.write("skills/productivity/README.md", "# Productivity\n\nWorkflows.\n\n- [guide](./guide/SKILL.md): Route.\n")
        self.write("skills/reference/README.md", "# Reference\n\nDisciplines.\n\n- [example](./example/SKILL.md): Example.\n")
        self.write("scripts/skill-graph/template.html", "<script>const DATA = /*SKILL_GRAPH_DATA*/null;</script>\n")
        with contextlib.redirect_stdout(io.StringIO()):
            builder.main([str(self.root)])

    def test_current_skill_map_passes(self):
        self.write_skill_map()
        self.assertEqual(self.result()[0], False)

    def test_stale_skill_map(self):
        self.write_skill_map()
        self.write("index.html", "old")
        self.assertIn("stale skill map", self.result()[1])

    def test_skill_missing_from_bucket_listing(self):
        self.write_skill_map()
        self.write("skills/reference/README.md", "# Reference\n\nDisciplines.\n\n[example](./example/SKILL.md)\n")
        self.assertIn("no one-line entry for example", self.result()[1])

    def test_skill_missing_from_map(self):
        self.write_skill_map(skills=("guide",))
        self.assertIn("no entry for promoted skill example", self.result()[1])


if __name__ == "__main__":
    unittest.main()
