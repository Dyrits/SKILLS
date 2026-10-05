# Handoff: setup bucket, guide move, and `.agents/` configuration

Supersedes: none. Follows [2026-10-04-2021-upstream-v1-3-1-and-improve-environment.md](2026-10-04-2021-upstream-v1-3-1-and-improve-environment.md) on a separate topic.

## Next session: commit and push

The working tree on `main` holds three finished, verified restructures, not yet committed. The user approved the changes; the next step is to commit and push to `origin` (`git@github.com:Dyrits/SKILLS.git`). Pushing to `main` is outward-facing: confirm with the user before pushing unless they already said to.

1. Review `git status` and `git diff --stat` (about 75 files, mostly renames plus path rewrites).
2. **Leave `.gitignore` out of the commit unless the user says otherwise.** Its change (removing `skills/*/*-workspace/`) predates this session and is the user's own.
3. Re-run the checks below before committing; they all passed at handoff time.
4. Commit with a message in the repository's style (subject line, short body, then `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`). One commit is fine, or one per restructure if the user prefers. Include this handoff file: handoffs are committed as shared history in this repository.
5. Push after confirmation.

## What changed (see the diff for detail)

- **`skills/getting-started/` → `skills/setup/`**, with `documentation/skills/getting-started/` → `documentation/skills/setup/`. Bucket title "Setup", blurb "Set up once per repository or machine." Updated the manifest, both READMEs, `CLAUDE.md`, documentation links, `scripts/check-skills.py`, `scripts/test-check-skills.py`, `scripts/build-skill-graph.py` (`BUCKET_ORDER`), and `scripts/skill-graph/template.html` (CSS variable `--setup`).
- **`guide` → `skills/productivity/guide/`** (documentation page too), under a new **Navigation** group in `skills/productivity/README.md`. The router path in `check-skills.py` was updated.
- **Consumer-project agent configuration moved from `documentation/agents/` to `.agents/`** (`issue-tracker.md`, `triage-roles.md`, `domain.md`, `ai-tooling.md`) in every skill, `PROJECT-DOCUMENTS.md`, `flow.json`, and documentation pages. `skills/setup/setup-ai-workspace/SKILL.md` now detects a legacy `documentation/agents/` and, with approval, moves its files there with `git mv` and updates pointers; its documentation page has a matching common question.
- History records were intentionally left with old paths: architecture decision record 0001, `documentation/research/`, `documentation/evaluation/waza.md`, older handoffs, `.upstream/`.

## Verification commands

```sh
python3 scripts/build-skill-graph.py --check
python3 scripts/check-skills.py
python3 scripts/test-check-skills.py
claude plugin validate . --strict
```

`scripts/link-skills.sh` was already re-run; installed links point at the new folders.

## Decisions from this session

- Upstream renamed `CONTEXT.md` → `GLOSSARY.md` (not the reverse); this fork already uses `GLOSSARY.md`, owned by `model-domain`. No change made.
- The user declined, for now, allowing user-only skills (`disable-model-invocation: true`). The rule in `.agents/invocation.md` (every skill model-invocable) stands. Background: in Claude Code a user-only skill's description leaves context but the Skill tool refuses it even when another skill names it; Codex's `allow_implicit_invocation: false` still allows explicit `$skill`.

## Suggested skills

- `guide` (model or user): if the user wants a next step after pushing.
- `hand-off` (user): at the next session boundary.
