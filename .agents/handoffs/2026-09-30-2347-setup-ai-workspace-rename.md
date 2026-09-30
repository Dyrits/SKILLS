# Setup AI workspace rename

Supersedes: [2026-09-30-2328-publication-merge-and-show-me.md](./2026-09-30-2328-publication-merge-and-show-me.md) for current working-tree, installation, and publication state.
The earlier handoff remains the record of the publication and show-me decisions.

## User decision and completed work

The user chose `setup-ai-workspace` as the setup skill's new name and requested updating its references, then writing a handoff, committing, and pushing.
The skill configures repository conventions for AI-assisted work.
Its current source is [SKILL.md](../../../skills/getting-started/setup-ai-workspace/SKILL.md), and its human documentation is [setup-ai-workspace.md](../../../documentation/skills/getting-started/setup-ai-workspace.md).
The rename, metadata, router, plugin manifest, installation instructions, and reference updates are recorded in the commit accompanying this handoff.
Seed templates and invocation policy retain their behavior.
Frozen upstream material retains its historical identity; the sync inventory's maintained target paths follow the rename.

## Verification and limits

- `git diff --check` passed.
- Structural checks passed for manifest paths, invocation metadata, unchanged seed templates, the canonical installation block, upstream inventory targets, and 29 relative links.
- `claude plugin validate . --strict` passed for the marketplace manifest.
- `claude plugin validate .claude-plugin/plugin.json --strict` failed on the existing root `CLAUDE.md` warning, which says the file is not loaded as plugin project context.
- The reference scan found no old skill name outside frozen upstream material before this handoff was written.

No behavior evaluation was needed for the rename.
`scripts/link-skills.sh` refreshed both local harness directories, and both new skill symlinks resolve into this repository.
The two stale symlinks for the old setup name were removed after verifying their targets.

## Git state and next session

Work is on `main` in `/Users/dgerrits/Codelab/Dyrits/SKILLS`, with `origin/main` as its configured upstream.
The user authorized a normal push to `origin/main`.
This handoff is written before the commit and push; check `git status --short --branch` and `git log -1 --oneline` to confirm their final state.
Handoff history is shared and tracked here.
An unrelated untracked artifact, `documentation/research/2026-09-30-agent-tooling-candidates.md`, appeared during this session and is excluded from the rename commit.
The user specified no further implementation task.

## Suggested skills

- Call the Skill tool with `writing-for-agents` before editing skill instructions and with `unslop` for repository prose.
- `hand-off` and `setup-ai-workspace` are user-invoked; the human invokes them when needed.
