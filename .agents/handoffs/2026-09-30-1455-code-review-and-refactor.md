# Code review and refactor phase

**Supersedes:** [2026-09-30-1423-upstream-port-and-review-boundary.md](./2026-09-30-1423-upstream-port-and-review-boundary.md), for the review-boundary question and this session's follow-up only.
The upstream port remains complete; its adoption record and inventory still describe that work.

## Completed work and user decisions

The user requested renaming `code-review` to `code-review-and-refactor` and making it apply supported refactors with the context gathered during review.
The resulting [skill](../../skills/workflow/code-review-and-refactor/SKILL.md) and [documentation](../../documentation/skills/workflow/code-review-and-refactor.md) are the primary sources for the final procedure.
The old maintained entrypoint and documentation page were removed; manifests, listings, router, workflow references, and publishing references use the new name.

The user clarified that implementation owns red/green and this skill owns the refactor phase of TDD.
The independent Standards and Specifications reviewers inspect a stable starting diff, one coordinator applies supported refactors, and the same reviewers verify the changes using their existing contexts.
Behavior changes required by the specifications return to implementation rather than being treated as structural refactors.

The user rejected expanding the caller skills with detailed phase instructions.
[implement](../../skills/workflow/implement/SKILL.md) retains its original concise structure with the new closing skill name.
[implement-all](../../skills/workflow/implement-all/SKILL.md) retains its concise integration review step, delegates remaining implementation issues, and commits the refactors.
Keep detailed review and refactoring instructions in the review skill.

The user requested plural **Specifications** for the axis and its active references, since one ticket can contain multiple specifications.
A subsequent repository-wide agreement scan corrected "a settled specifications", clarified "one ticket or a small set of specifications", and made "the Specifications reviewer finds" explicit.
The current maintained skill and its documentation use the plural throughout.

## Verification

- `claude plugin validate . --strict` passed after the manifest changes and again before publication.
- `npm run check-plugin-version` passed; package and plugin versions remain `0.1.1`.
- Ruby's YAML parser verified skill names, invocation-policy consistency, and renamed metadata; promoted paths and documentation coverage passed.
- The changed Markdown link scan checked 208 relative targets successfully, and the promoted pages and listings passed structural checks.
- `git diff --check` passed after the wording corrections and before publication.
- Repository-wide agreement searches were reviewed; the remaining "set of specifications needs" phrases have a singular subject and are correct.

These are structural and editorial checks, not a live behavioral trial of the new review and refactor workflow.
The Python skill validator could not run because PyYAML is unavailable; Ruby parsing supplied the metadata checks instead.
The GitHub CLI is unavailable, so the documentation question hunt used the session's questions, existing documentation, and Git history rather than fetching repository issues.

## Local harness state

All 41 installed copies under `~/.agents/skills` matched the starting revision and had no extra files before relinking.
`scripts/link-skills.sh` refreshed the maintained skills, and all 82 links across `~/.agents/skills` and `~/.claude/skills` were verified to resolve into this repository.
The former `code-review` entry was removed from both harnesses; its identical copied directory was retained at `/var/folders/v4/3387cnf96tg0hw51lfjlbw0r0000gn/T/dyrits-old-code-review-fd5u1xdn/code-review`.
The installed renamed skill now follows repository edits through its symlink.

## Git state and publication

The user explicitly requested this handoff, committing the session's changes, and pushing them.
At writing, the changes and this handoff are uncommitted on `main` in `/Users/dgerrits/Codelab/Dyrits/SKILLS`.
`git fetch origin` succeeded, and `origin/main` and local `HEAD` both resolved to `f09721f` before the new commit.
The normal commit and fast-forward push follow creation of this document; this paragraph records the state before those actions rather than claiming they already succeeded.
Use `git status --short --branch` and `git log -1 --oneline` to confirm the resulting commit, and refresh origin before deciding whether any publication remains outstanding.
No pull or merge request was requested.

## Suggested skills and next session

- Call the Skill tool with `writing-for-agents` before changing skill instructions, and with `unslop` for repository prose.
- Use `code-review-and-refactor` for the refactor phase or an explicitly requested review and refactor; an explicit report-only request remains supported.
- If behavioral validation is requested, exercise the new skill in an isolated fixture with passing behavior tests and observable standards findings, and verify both refactoring and reviewer reuse.
- To resume, the user can invoke `/take-over`; this handoff is the new session's brief.

The skill implementation is complete; no further implementation task has been specified.
