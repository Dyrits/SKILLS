Upstream skills: `setup-matt-pocock-skills`, `setup-pre-commit`, and `git-guardrails-claude-code`, adapted here as `setup-ai-workspace`, `setup-git-hooks`, and `setup-git-guardrails`, then merged with the fork-created `setup-ai-tooling` into `setup`. [Architecture decision record 0007](../../architecture-decision-record/0007-merge-project-setup-into-one-skill.md) records why; the [provenance audit](../../research/2026-10-03-retained-skill-provenance.md) records the originals.

## What it does

Configures one repository, or an empty project, for AI-assisted work. A bundled script first reports what is already set up, then the skill offers four areas with their state and sets up the ones you pick:

| Area | What you get |
| --- | --- |
| Workspace | Your task tracker (local Markdown, GitHub, GitLab, Jira, or another), the ticket-writing convention, triage role names, and an `## Agent skills` block in `AGENTS.md` pointing at them |
| Code checks | A committed pre-commit hook that runs your formatter and linter on staged files, then a typecheck |
| Git guardrails | A human decision before Git commands that lose work or rewrite shared history, for each agent harness you use |
| AI tooling | A code index, documentation lookup, structural search, browser and tracker clients, and a recorded baseline |

The tools install themselves. The skill carries a dated catalogue listing, for each tool, how to detect it, its non-interactive install command, and one check that it works. The agent runs those commands with their output sent to a log, reads only the end of the log, and opens documentation only when a listed command fails. Upstream, each area was its own skill and each run re-read the tools' documentation; the merge exists to cut that cost.

## When to reach for it

Type `/setup`, or an agent can reach for it when you ask to set up or reconfigure a repository or one of its areas ("add pre-commit hooks", "guard destructive Git commands", "set up AI tooling"). Naming one area runs only that one.

| Situation | Use |
| --- | --- |
| A new or unconfigured repository | This skill, all areas |
| An empty folder with no stack chosen yet | This skill; code checks wait until code exists |
| You want code conventions written down or audited | [codify](../upkeep/codify.md) |
| You want the delegation rule on every repository on this machine | [setup-delegation-policy](./setup-delegation-policy.md) |
| You want to choose the stack itself | [architect](../workflow/architect.md) |

## Code checks without extra dependencies

The hook calls the tools the repository already has. The catalogue has one file per language (JavaScript and TypeScript, Python, Go, Rust), and the agent reads only those for the languages it found. Biome checks staged files itself; oxlint, oxfmt, Ruff, and gofmt receive the staged file list from Git. lint-staged is gone. Another language gets its toolchain's own formatter and linter, looked up in its documentation. The hook checks and never rewrites, so a partly staged file is never changed behind your back.

When the repository runs on older tooling, the skill offers a move and keeps your tools if you decline: ESLint or Prettier to Biome or to oxlint and oxfmt through their migration commands, Black, isort, or Flake8 to Ruff. It shows what the move would drop. For TypeScript it uses an existing `typecheck` script first, then `bun check` on a Bun project, then `tsc --noEmit`; Go and Rust typecheck as they lint.

Your conventions feed the configuration. The skill reads the conventions document `AGENTS.md` names, or a contribution or style guide and `.editorconfig`, and carries their tool rules (indentation, quotes, line width, lint rules) into the tool configuration. It asks when a documented rule and an existing configuration disagree.

## Common questions

**Does it pick my framework in an empty project?**

No. It asks which language and framework you will use and takes the answer as given. Choosing a stack is [architect](../workflow/architect.md)'s job. Without an answer, it sets up what does not depend on one.

**What if a tool I want is not in the catalogue?**

The agent can still set it up by reading its documentation, at the token cost the catalogue avoids, and the report says which tool needed that.

**How does the catalogue stay current?**

Each catalogue file carries the date it was last verified, and this repository's checks warn once a date is six months old. Refreshing it is maintenance here, not research during your setup.

**Will it replace my Husky or lefthook setup?**

Only if you agree. Otherwise it adds the checks to your existing hook manager.

**Do I have to use GitHub?**

No. GitHub, GitLab, Jira, and local Markdown are supported, and another tracker works through a verified connector, command-line tool, or an explicitly manual workflow. The role file maps names and does not create remote labels.

**Is the guard a sandbox?**

No. It reads command text, so Git aliases, scripts that run Git, and `eval` get past it. It catches mistakes; branch protection on the remote is the only hard stop. Where nobody can answer a prompt, expect the guarded command to be refused.

**Can it claim how many tokens I saved?**

Only where a comparable task baseline exists. Command-output reduction, task token counts, and provider allowance are reported as different quantities.

## It's working if

- The opening report matches what you know is set up, and you were asked only about what is not.
- `git config core.hooksPath` prints `.githooks`, and a commit with a misformatted file fails with the tool's message.
- Piping `git push origin main` into the guard exits 2 with a reason, and pushing a feature branch goes through without a prompt.
- Each AI tool passed its check, such as a known symbol retrieved through CodeGraph matching the file, and `.agents/ai-tooling.md` holds no credentials.
- Workflow skills find the tracker and role names through `AGENTS.md` without guessing.
- Running it again changes nothing that already works.

## Where it fits

Run-once setup per repository, run again when the tracker, the tools, or the guard level change. [specify](../workflow/specify.md), [taskify](../workflow/taskify.md), [triage](../upkeep/triage.md), and [graphify](../shaping/graphify.md) read the workspace configuration it writes; [monitor-ai-tooling](../upkeep/monitor-ai-tooling.md) reads the tooling baseline. It carries its own copies of the shared document rules.
