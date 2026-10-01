# Worktree skills

Supersedes: none. This handoff covers only the creation of the worktree skills.

## Outcome

Created two experimental, user-invoked skills in SKILLS:

- [`work-in-tree`](../../skills/experimental/work-in-tree/SKILL.md) creates or
  reuses an isolated checkout, keeps task work there, and leaves a verified
  destination handoff.
- [`sync-tree`](../../skills/experimental/sync-tree/SKILL.md) transfers committed
  work to the corresponding original local branch. It was initially drafted
  as `sync-local-branch`; that name and the initial application-repository
  draft were removed.

The user requested general Git worktree behavior, not a Delta-specific
workflow. `sync-tree` retains optional Land Changes eligibility through
`metadata.delta-action: land`. Neither skill publishes upstream automatically.

## Repository integration

The authoritative behavior and safety rules are in the linked `SKILL.md` files.
Each skill also has `agents/openai.yaml` and `evals/evals.json`.

Updated the [experimental listing](../../skills/experimental/README.md),
[top-level listing](../../README.md),
[router](../../skills/getting-started/what-is-next/SKILL.md), and
[router documentation](../../documentation/skills/getting-started/what-is-next.md).
Both skills remain outside the plugin and have no experimental documentation
pages. Generated evaluation workspaces are ignored by Git.

## Verification and remaining work

Validated metadata, links, JSON, whitespace, and plugin-version consistency.
Ran three dry-run scenarios per skill, with baseline comparisons. Separate
temporary Git fixtures verified isolation, fast-forward transfers, local-clone
transfers, stale ref and lease rejection, and detection of untracked files.
These checks do not establish production landing reliability.

The skills were synced to local `main`. This handoff is being amended into
the same commit before publication. Verify live Git state rather than relying
on an earlier commit ID. Global installation has not been performed.

No implementation work remains requested. If the user wants installation,
review `scripts/link-skills.sh` and obtain approval for its machine-local
changes before running it.

## Suggested skills

For further edits, call the Skill tool for `writing-for-agents` and `unslop`.
For evaluation or iteration, call it for `skill-creator`.
The new `work-in-tree` and `sync-tree` skills are user-invoked; suggest their
slash commands to the human rather than invoking them implicitly.
