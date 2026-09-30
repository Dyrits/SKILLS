# Upstream port and review boundary

**Supersedes:** [2026-09-20-1011-upstream-sync-to-pull-request.md](./2026-09-20-1011-upstream-sync-to-pull-request.md), for upstream synchronisation state only.
Other topic-specific handoffs remain relevant to their own work.

## User intent and completed work

The user wanted the latest upstream skills while preserving this fork's changes, names, branding, and archival structure, without rebasing its history.
The integration is complete locally on `main` in `/Users/dgerrits/Codelab/Dyrits/SKILLS`.
The user then asked for a summary and this handoff; they have not specified a new implementation task.

Read [the adoption record](../../.upstream/sync/2026-09-30.md) for the changes, retained fork decisions, documentation corrections, and verification.
[Its JSON inventory](../../.upstream/sync/2026-09-30.json) maps all changed upstream paths and archived sources.
[The archive index](../../.upstream/README.md) explains the snapshot layout.
These artifacts hold the detailed port decisions; this handoff supplies the session state that they do not.

## Git state

- Upstream remote is `https://github.com/mattpocock/skills`; origin is this fork.
- Upstream was fetched again after the port, and its tip remained `d81f3a183412e71a5b1e84ca21bc1a35eea03a60`.
- `2ea153f` records upstream ancestry with an `ours` merge and changes no content.
- `dd44788` contains the content port and its archive and documentation.
- Before this handoff commit, `HEAD` was 31 commits ahead of upstream and zero behind, and local `main` was 23 commits ahead of the recorded `origin/main`.
- The working tree was clean before writing this handoff.
- No commits were pushed to origin in this session; origin was not fetched during the port, so refresh it before deciding how to publish.
- This repository tracks handoffs; commit this new document rather than adding the directory to `.gitignore`.

## Review question that started the session

The user asked whether `code-review` actually reviews or also refactors.
Both the local skill and upstream's current skill instruct agents to report findings and aggregate them, without an editing step.
The smell baseline uses imperative fix suggestions, and neither skill explicitly prohibits edits, so the wording leaves an ambiguity.
Some inherited test-driven-development documentation incorrectly claimed the review performs refactoring; that documentation was corrected in the content port.
`code-review/SKILL.md` itself was intentionally left unchanged.
If the user later requests an explicit review-only guardrail, that would be a new skill change, requiring its documentation to be resynchronised.

## Local harness state

After committing the port, all 41 installed copies under `~/.agents/skills` were compared with the pre-sync repository revision and matched exactly, with no extra local files or edits.
The documented `scripts/link-skills.sh` was then run successfully.
All 41 skill links in each of `~/.agents/skills` and `~/.claude/skills` were verified to resolve into this repository.
Future repository updates now reach those installed skills through their symlinks.
Unrelated third-party skills were not replaced.

## Verification and limits

The adoption record lists the verification gates and their scope.
The completed structural pass checked 41 skill metadata pairs, 33 promoted documentation/listing entries, 42 exact upstream archives, 20 unchanged earlier archive files, 35 unchanged fork feature or identity files, and 331 local Markdown links without introducing broken targets.
The ten changed skill resources outside the router and parallel implementation skill preserved their local instructions exactly apart from the glossary convention.
The renamed glossary format preserved its local wording.
The archived retired entrypoint uses `SKILL.md.source`; no `SKILL.md` exists under `.upstream/`.

These were structural and preservation checks, not live behavioral trials of all skills or tracker actions.
PyYAML was unavailable, so skill frontmatter and harness YAML were parsed successfully with Ruby's YAML parser.
Temporary verification helpers are under `/tmp/dyrits-*`; their continued presence is not required to understand the committed result.

## Next session

Confirm the working tree and branches before starting new work.
The port is complete; do not repeat it or rebase onto upstream.
If the user asks to publish, fetch origin, check whether a normal fast-forward push is available, and push through the repository's normal policy.
No push or pull request was requested during this session.
For another upstream update, begin from the recorded tip in the inventory and follow the ancestry-then-port policy in [architecture decision record 0001](../../documentation/architecture-decision-record/0001-maintain-as-an-independent-fork.md).

## Suggested skills

- Call the Skill tool with `writing-for-agents` before modifying skill instructions or steering files.
- Call the Skill tool with `unslop` for repository prose.
- If the user requests a review of this port, call the Skill tool with `code-review`, using `eccd606` as the fixed point and the adoption record plus the user's request as the specification sources.
- If the user requests a pull or merge request description, call the Skill tool with `to-pull-request`.
- Invoke `resolve-merge-conflicts` only if a future Git operation actually has conflicts.
