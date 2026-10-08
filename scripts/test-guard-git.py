#!/usr/bin/env python3
"""Exercise the setup-git-guardrails command guard and its pre-push hook against a scratch repository.

Usage: python3 scripts/test-guard-git.py
Needs: Python 3 standard library and git. Uses temporary directories only.
"""

import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "skills/setup/setup-git-guardrails/scripts"
GUARD = SCRIPTS / "guard-git.py"
PRE_PUSH = SCRIPTS / "pre-push"

# command -> lowest level that guards it (None: never guarded)
CASES = {
    "git push origin main": 1,
    "git push -fu origin feat": 1,
    "git push --force origin feat": 1,
    "git push origin +feat": 1,
    "git push origin :feat": 1,
    "git push --delete origin feat": 1,
    "git push --no-verify origin feat": 1,
    "(git push origin main)": 1,
    "sudo git push origin main": 1,
    'bash -c "git push origin main"': 1,
    "echo hi && git push origin main": 1,
    "git -C . push origin main": 1,
    "git reset --hard": 2,
    "command git reset --hard": 2,
    "xargs git reset --hard": 2,
    "sleep 1 & git reset --hard": 2,
    "git clean -fd": 2,
    "git branch -D old": 2,
    "git checkout .": 2,
    "git checkout -f": 2,
    "git checkout -- file.txt": 2,
    "git switch --discard-changes other": 2,
    "git restore file.txt": 2,
    "git stash drop": 2,
    "git worktree remove --force ../tree": 2,
    "git reflog expire --all": 2,
    "git gc --prune=now": 2,
    "git push origin feat": 3,
    "git rebase main": 3,
    "git commit --amend": 3,
    "git reset --soft HEAD~1": 3,
    "git tag -d v1": 3,
    "git push --force-with-lease origin feat": 3,
    "git push --dry-run origin main": None,
    "git push origin feat --dry-run": None,
    "git clean -n": None,
    "git clean -fn": None,
    "git restore --staged file.txt": None,
    "git branch -d merged": 3,
    "git checkout -b feat": None,
    "git checkout main": None,
    "git commit -m 'push to main'": None,
    'echo "git push origin main"': None,
    "git status": None,
    "ls": None,
}


class Repository(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.git("init", "-q", "-b", "feat")
        self.git("commit", "-q", "--allow-empty", "-m", "initial")

    def git(self, *arguments, directory=None):
        return subprocess.run(["git", *arguments], cwd=directory or self.root, capture_output=True, text=True,
                              env={**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t",
                                   "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"})


class CommandGuard(Repository):
    def run_guard(self, command, level, raw=None):
        return subprocess.run(["python3", "-I", str(GUARD), "--level", str(level)], cwd=self.root, input=raw or command,
                              capture_output=True, text=True)

    def test_every_case_is_guarded_from_its_level(self):
        for command, lowest in CASES.items():
            for level in (1, 2, 3):
                guarded = self.run_guard(command, level).returncode == 2
                with self.subTest(command=command, level=level):
                    self.assertEqual(guarded, lowest is not None and level >= lowest)

    def test_hook_payload_is_read_and_ask_json_is_printed(self):
        payload = json.dumps({"tool_input": {"command": "git reset --hard"}, "cwd": str(self.root)})
        result = subprocess.run(["python3", "-I", str(GUARD), "--level", "2", "--format", "ask-json"],
                                input=payload, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout)["hookSpecificOutput"]["permissionDecision"], "ask")

    def test_argv_payload_is_joined(self):
        payload = json.dumps({"tool_input": {"command": ["bash", "-lc", "git reset --hard"]}})
        self.assertEqual(self.run_guard("", 2, raw=payload).returncode, 2)

    def test_protected_branches_option_and_current_branch(self):
        self.git("checkout", "-q", "-b", "develop")
        guard = lambda protected: subprocess.run(
            ["python3", "-I", str(GUARD), "--level", "1", "--protected", protected], cwd=self.root,
            input="git push origin HEAD", capture_output=True, text=True).returncode
        self.assertEqual(guard("main,master"), 0)
        self.assertEqual(guard("develop"), 2)


class PrePushHook(Repository):
    ZERO = "0" * 40

    def install(self, level):
        text = PRE_PUSH.read_text().replace("LEVEL=1", f"LEVEL={level}")
        hook = self.root / ".git/hooks/pre-push"
        hook.write_text(text)
        hook.chmod(0o755)
        return hook

    def push(self, hook, remote_ref, local_sha, remote_sha):
        return subprocess.run([str(hook)], cwd=self.root, input=f"refs/heads/x {local_sha} {remote_ref} {remote_sha}\n",
                              capture_output=True, text=True).returncode

    def commit(self, name):
        (self.root / name).write_text(name)
        self.git("add", name)
        self.git("commit", "-q", "-m", name)
        return self.git("rev-parse", "HEAD").stdout.strip()

    def test_blocks_protected_deletion_and_passes_feature_branch(self):
        hook = self.install(1)
        sha = self.commit("a")
        self.assertEqual(self.push(hook, "refs/heads/main", sha, self.ZERO), 1)
        self.assertEqual(self.push(hook, "refs/heads/feat", self.ZERO, sha), 1)
        self.assertEqual(self.push(hook, "refs/heads/feat", sha, self.ZERO), 0)

    def test_level_three_blocks_non_fast_forward_only(self):
        first = self.commit("a")
        second = self.commit("b")
        hook = self.install(3)
        self.assertEqual(self.push(hook, "refs/heads/feat", second, first), 0)
        self.assertEqual(self.push(hook, "refs/heads/feat", first, second), 1)


if __name__ == "__main__":
    unittest.main()
