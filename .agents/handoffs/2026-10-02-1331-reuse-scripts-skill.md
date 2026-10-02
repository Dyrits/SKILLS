# Handoff: scriptbook skill

Supersedes: none (the previous handoff, `2026-10-01-1501-worktree-skills.md`, covers unrelated work).

## Next session focus

The work below is committed and pushed to `origin/main`. The skill was first named `reuse-scripts` and renamed to `scriptbook` before the final amend, so the commit message and this file's name still use the earlier wording. Pick up from "Not done".

## What happened

The user asked whether a model-invoked skill that stops agents from rebuilding throwaway scripts is relevant. It is, narrowly: it should fire only before writing a script or multi-step shell pipeline, and defer to an existing `justfile`, `Makefile` or `package.json` scripts. The user chose these design points:

- Libraries: project `.agents/scripts/` first, then global `~/.agents/scripts/`, each with a manual `INDEX.md`.
- Ships in `skills/experimental/`, not the plugin.
- No language constraint on scripts.

Then the user asked to delete every `evals/` directory in the repository, since they are not required by any repository rule. Done.

## Contents of the commit

- Added `skills/experimental/scriptbook/SKILL.md` and `agents/openai.yaml`. No `evals/` and no documentation page, both intentional.
- Modified `skills/experimental/README.md`, top-level `README.md`, `skills/getting-started/what-is-next/SKILL.md` and `documentation/skills/getting-started/what-is-next.md` to register the skill.
- Deleted the four tracked `skills/experimental/*/evals/evals.json` files (`monitor-ai-tooling`, `setup-ai-tooling`, `sync-tree`, `work-in-tree`).
- Left alone on purpose: three historical handoffs in `.agents/handoffs/` that mention evals.

Run `git show --stat HEAD` for the exact contents rather than trusting this list.

## Decisions to keep

- Handoffs in `.agents/handoffs/` are committed (shared history), as in prior sessions.
- No em-dashes anywhere in repository prose.
- Commit message style: short imperative subject, as in `git log` (for example "Add experimental worktree setup and sync skills").
- Commit messages end with the Co-Authored-By line from the session's attribution reminder.

## Not done

- The skill has never been run against test prompts. The user declined evals, so any validation is a manual try-out.
- `scripts/link-skills.sh` was not run, so the skill is not linked into `~/.claude/skills` yet.

## Suggested skills

None required.
