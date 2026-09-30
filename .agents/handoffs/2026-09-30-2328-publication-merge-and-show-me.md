# Publication merge and show-me publication

**Supersedes:** [2026-09-30-2301-show-me-and-centralized-credits.md](./2026-09-30-2301-show-me-and-centralized-credits.md) for working-tree, local installation, and publication state only.
That handoff remains the record of the show-me and attribution decisions.

## User decisions and completed work

The user accepted the recommendation to merge `publish-review` into [publish-message](../../skills/experimental/publish-message/SKILL.md), which now accepts conclusions and findings from any established review source.
[inline-suggestions.md](../../skills/experimental/publish-message/inline-suggestions.md) holds the optional diff validation and submission branch.
The standalone publish-review entrypoint and harness metadata were removed.
The review workflow, router, listings, and affected promoted documentation now name the single command.

Publication preserves finding dispositions and verification limits, distinguishes local refactors from changes present in the destination branch, and approves the exact complete set before posting.
The skill remains user-invoked and experimental, excluded from the plugin.
The current skill and reference hold the complete procedure; keep detailed publication instructions there.

The user then explicitly requested checking the previous uncommitted handoff, writing this handoff, committing both handoffs and all changes, and pushing.
The earlier handoff and current files were reviewed together.
Its show-me promotion, to-pull-request integration, and centralized README credits remain included in the pending publication.
See that handoff and its linked source files for the detailed decisions.

## Verification and limits

- `claude plugin validate . --strict` passed for the marketplace manifest.
- Direct validation of `.claude-plugin/plugin.json` passed with the existing warning that root `CLAUDE.md` is not loaded as plugin project context.
- `npm run check-plugin-version` passed, with package and plugin versions synchronized at `0.1.1`.
- Ruby parsed frontmatter and harness metadata for all five changed skills and verified matching names and invocation policies.
- A combined scan checked 123 relative links across the 15 changed Markdown files present before this handoff, plus paths, documentation coverage, and listings for all 34 promoted skills.
- `git diff --check` passed.

These are structural and editorial checks.
No live tracker publication, behavioral evaluation, or generated HTML preview was run.
Python's optional YAML module remains unavailable; Ruby supplied YAML validation.
The protected `.agents` directory required filesystem escalation to write this explicitly requested handoff.

## Local installation

The repository-required `scripts/link-skills.sh` refreshed maintained skills in both `~/.agents/skills` and `~/.claude/skills` after the publication merge.
Both publish-message links resolve into this repository and expose the new inline reference.
The retired publish-review installation was verified against its tracked version, archived at `/private/tmp/retired-publish-review-2dslwvqy`, and removed from both harness skill lists.
This supersedes the prior handoff's installation state, which preceded the general relinking.

## Git state and next session

Work is on `main` in `/Users/dgerrits/Codelab/Dyrits/SKILLS`.
Before this handoff and the requested commit, local HEAD and freshly fetched `origin/main` both resolved to `8beeace`.
Both sessions' changes, the previous uncommitted handoff, and this document are to be committed together and pushed normally to `origin/main`.
This records the state before those actions; inspect `git status --short --branch`, `git log -1 --oneline`, and the refreshed remote before deciding whether publication remains outstanding.
The user requested no pull or merge request and specified no further implementation task.
Handoff history is shared and tracked in this repository.

## Suggested skills

- Call the Skill tool with `writing-for-agents` before changing skill instructions, and with `unslop` for repository prose.
- Call the Skill tool with `show-me` when a visual explanation would help the next task.
- `publish-message` and `hand-off` are user-invoked; the human invokes them when needed.
