# Proof: the imported security-audit skill is intact and registered

- **Verdict:** proven for the import and registration (C1 to C7); the run-location behavior (C8) is unproven
- **Work:** branch `add-security-audit-skill` on `1f7bc18`, adding `skills/upkeep/security-audit` from `cloudflare/security-audit-skill` at `c1c8a8c1471069fb0e188eeaff69b8e8db6564a8`
- **Agreement:** the user's request to add the skill if relevant, keeping this repository's layout, language, and registration rules (`AGENTS.md`), and to save runs in `documentation/security-audit/` like the architecture audit reports
- **Environment:** macOS, Node.js (built-in `node --test`), Python 3, Claude Code CLI; mutations run in a scratch worktree `$E` of the branch, never in the main checkout
- **Date:** 2026-10-28

## Setup

```sh
E=$(mktemp -d)/e && git worktree add --detach "$E" add-security-audit-skill && cd "$E"
S=skills/upkeep/security-audit
P=documentation/verification/2026-10-28-security-audit-import/checks.py
```

Restore each mutated file with `git checkout -- <file>` (or `git stash -u` for moved files) before the next check.

## Claims

| # | Claim | Source | Verdict |
| --- | --- | --- | --- |
| C1 | The validators and their tests run from `scripts/`, with the schema found beside the validator | Layout rule in `AGENTS.md` | proven |
| C2 | Every relative link in `SKILL.md` and `references/` resolves after the rename to lowercase | Layout rule in `AGENTS.md` | proven |
| C3 | The skill's prose has no em-dashes | Language rule in `AGENTS.md` | proven |
| C4 | The promotion procedure block is identical in `hunting.md` and `validation-and-reporting.md`, as `SKILL.md` asserts | Upstream contract | proven |
| C5 | The skill is registered: plugin manifest, both READMEs, documentation page, and skill graph (`check-skills.py`) | Registration rule in `AGENTS.md` | proven |
| C6 | The APM manifests are current | `generate-skill-manifests.py` | proven |
| C7 | The plugin passes `claude plugin validate . --strict` | `AGENTS.md` | proven |
| C8 | A full audit saves its run in `documentation/security-audit/run-<N>/`, ignored by Git, with an `AGENTS.md` line | User request | unproven |

## Evidence

### C1: validators run from `scripts/`

- **Check:** `(cd $S/scripts && node --test validate-findings.test.cjs validate-coverage-ledger.test.cjs)`
- **Result:** `pass 65`, `fail 0`; the same count as the upstream checkout before the move.
- **Shown able to fail:** mutation. `mv $S/scripts/report-schema.json ..` gives `fail 1`.

### C2, C3, C4: links, em-dashes, promotion block

- **Check:** `python3 -I $P .`
- **Result:** `links, em-dashes, promotion block: PASS`, exit 0.
- **Shown able to fail:** mutation. Changing `(references/hunting.md)` to `(references/hunt.md)` in `SKILL.md` prints `BROKEN LINK SKILL.md -> references/hunt.md` and exits 1. Inserting ` — x` after the first line of the promotion block in `references/hunting.md` prints `EM-DASH references/hunting.md 1` and `PROMOTION BLOCK MISMATCH`, exit 1.

### C5: registration

- **Check:** `python3 scripts/check-skills.py`
- **Result:** `Checked 42 skills, 42 plugin paths, 42 documentation pages, and 258 Markdown files.`, no `ERROR`.
- **Shown able to fail:** mutation. Deleting the `./skills/upkeep/security-audit` line from `.claude-plugin/plugin.json` gives `ERROR: skills/upkeep/security-audit: missing from the plugin manifest.`; deleting its `scripts/skill-graph/flow.json` entry gives `ERROR: scripts/skill-graph/flow.json: no entry for skill security-audit.`

### C6: manifests

- **Check:** `python3 .agents/scripts/generate-skill-manifests.py --check`
- **Result:** `43 manifests current`, exit 0.
- **Shown able to fail:** mutation. Removing the `path: skills/upkeep/security-audit` dependency from the root `apm.yml` gives `missing or stale: apm.yml`, exit 1.

### C7: plugin validation

- **Check:** `claude plugin validate . --strict`
- **Result:** `Validation passed` (with the existing README install-line warning).
- **Shown able to fail:** mutation. Pointing the plugin entry at `./skills/upkeep/security-audits` gives `Path not found: ./skills/upkeep/security-audits`.

### C8: run location

- **Unproven:** observing it needs a full audit run by an agent with the skill loaded (a skill evaluation), which this session did not run. The instruction is in `SKILL.md` under Full audit setup (Audit home, Output directory).

## Regressions

All `package.json` scripts ran in `$E`: `check-plugin-version`, `check-skills`, `check-skill-manifests`, `test-skills-check`, `test-scriptbook-helpers`, `test-guard-git`, and `test-inspect-project` exit 0. `test-detect-harnesses` exits 2 because `scripts/test-detect-harnesses.py` does not exist; it fails the same way on the starting commit `1f7bc18`, so it is pre-existing.

## Reproduction

A fresh-context agent (Haiku, Light tier) that had not seen the implementation reran the Setup, every check and mutation for C1 to C7, and the Regressions scripts against `85988ab` on 2026-10-28. Every result matched. Two differences in detail, not in outcome: the broken-link mutation prints its line three times, because `SKILL.md` links `hunting.md` three times, and the C5 mutations print extra `flow.json` errors alongside the stated ones.
