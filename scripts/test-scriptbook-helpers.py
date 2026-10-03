#!/usr/bin/env python3
"""Exercise review capture safety and reference-patch output on temporary files.

Usage: python3 scripts/test-scriptbook-helpers.py
Needs: Python 3 and Git. Uses temporary repositories, with commit hooks disabled.
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


ROOT = Path(__file__).resolve().parent.parent
CAPTURE = ROOT / ".agents/scripts/capture-review-state.py"
PROPOSE = ROOT / ".agents/scripts/propose-reference-updates.py"
spec = importlib.util.spec_from_file_location("capture_review", CAPTURE)
capture_review = importlib.util.module_from_spec(spec)
spec.loader.exec_module(capture_review)


class HelperChecks(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(dir=os.environ.get("DELTA_SCRATCH_DIR"))
        self.addCleanup(temporary.cleanup)
        self.temporary = Path(temporary.name)
        self.repository = self.temporary / "repository"
        self.repository.mkdir()
        self.git("init", "--quiet", "--initial-branch=main")
        (self.repository / "README.md").write_text("Baseline.\n")
        self.git("add", "README.md")
        self.git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                 "-c", "core.hooksPath=/dev/null", "-c", "commit.gpgSign=false",
                 "commit", "--quiet", "-m", "Baseline")
        self.base = self.git("rev-parse", "HEAD").strip()
        self.output = self.temporary / "review"

    def git(self, *arguments):
        return subprocess.check_output(
            ["git", "-C", str(self.repository), *arguments], text=True
        )

    def capture(self):
        with contextlib.redirect_stdout(io.StringIO()):
            capture_review.capture(self.output, self.base, self.repository)

    def test_regular_changed_file_is_captured(self):
        (self.repository / "README.md").write_text("Changed.\n")
        self.capture()
        self.assertEqual((self.output / "contents/README.md").read_text(), "Changed.\n")

    def test_external_symlink_is_not_read(self):
        external = self.temporary / "external.txt"
        external.write_text("Dummy external contents, not review input.\n")
        (self.repository / "outside").symlink_to(external)
        self.capture()
        self.assertFalse((self.output / "contents/outside").exists())
        metadata = json.loads((self.output / "symlinks.json").read_text())
        self.assertEqual(metadata["outside"]["target"], str(external))

    def test_symlink_parent_of_deleted_file_is_not_read(self):
        directory = self.repository / "tracked"
        directory.mkdir()
        (directory / "file.txt").write_text("Tracked contents.\n")
        self.git("add", "tracked/file.txt")
        self.git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                 "-c", "core.hooksPath=/dev/null", "-c", "commit.gpgSign=false",
                 "commit", "--quiet", "-m", "Track directory")
        self.base = self.git("rev-parse", "HEAD").strip()
        (directory / "file.txt").unlink()
        directory.rmdir()
        external = self.temporary / "external-directory"
        external.mkdir()
        (external / "file.txt").write_text("Dummy external contents.\n")
        directory.symlink_to(external, target_is_directory=True)
        self.capture()
        self.assertFalse((self.output / "contents/tracked/file.txt").exists())
        metadata = json.loads((self.output / "symlinks.json").read_text())
        self.assertEqual(metadata["tracked/file.txt"]["type"], "symlink-parent")

    def test_patch_rejects_missing_final_newline(self):
        source = self.temporary / "source.md"
        source.write_text("old")
        result = subprocess.run(
            ["python3", str(PROPOSE), "--replace", "old", "new", "--", str(source)],
            capture_output=True, text=True, check=False
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("final newline", result.stderr)
        self.assertEqual(result.stdout, "")

    def test_patch_has_separate_lines_and_markers(self):
        source = self.temporary / "source.md"
        source.write_text("old\n")
        result = subprocess.run(
            ["python3", str(PROPOSE), "--replace", "old", "new", "--", str(source)],
            capture_output=True, text=True, check=True
        )
        self.assertIn("-old\n+new\n", result.stdout)
        self.assertTrue(result.stdout.endswith("*** End Patch\n"))


if __name__ == "__main__":
    unittest.main()
