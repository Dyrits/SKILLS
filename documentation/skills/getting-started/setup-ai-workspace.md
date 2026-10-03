Upstream skill: `setup-matt-pocock-skills`, adapted here as `setup-ai-workspace`. The [archived setup page](../../../.upstream/snapshots/d81f3a1/files/docs/engineering/setup-matt-pocock-skills.md) records its origin.

## What it does

Configures one repository's task tracker, ticket-writing convention, triage-role vocabulary, and domain documentation. Its output is editable Markdown under `documentation/agents/`, plus an agent-instruction block. It changes project configuration, not the installed skills. It then offers the other getting-started setups, so one run can prepare the whole workspace.

The tracker choice does not move specification authority. Agreed living behavior, design, and acceptance stay in `documentation/<feature>/specifications.md`. Remote tasks link to or summarize that specification. Local documents can be maintained within scope without publishing remote records.

## When to reach for it

Run `/setup-ai-workspace` yourself once per repository, or when the tracker or conventions change. It is user-invoked; agents and other skills cannot launch it for you.

| Situation | Use |
| --- | --- |
| Workflow skills guess task locations or role strings | Run setup |
| The project already has a tracker and templates | Run setup to record the existing conventions |
| You only need to maintain project documents | Use [document](../reference/document.md) |
| You also want tooling, commit hooks, Git guardrails, automatic handoff, or the delegation policy | Accept them in the optional setup stage, or name them in the request |

## The configuration contract

- `documentation/agents/issue-tracker.md` records local or remote operations, the writing convention, and wayfinding operations.
- `documentation/agents/triage-roles.md` maps category and intake-state roles, when triage is installed.
- `documentation/agents/domain.md` records glossary and architecture-decision conventions.
- An `## Agent skills` block points consumers at those files and the shared documentation rules.

## Optional setups

After the configuration is written, setup offers the other getting-started setups in one multi-select question, marking which are already in place: [setup-ai-tooling](./setup-ai-tooling.md), [setup-git-hooks](./setup-git-hooks.md), [setup-git-guardrails](./setup-git-guardrails.md), and [setup-auto-handoff](./setup-auto-handoff.md) run inside the session, each asking its own questions. [setup-delegation-policy](./setup-delegation-policy.md) is machine-wide and user-invoked, so setup tells you to run `/setup-delegation-policy` yourself.

Future work uses the shared project-document model. Project requirements constrain all work. A local backlog records candidates and deferrals; with a remote tracker, `documentation/backlog.md` links to the authoritative backlog instead. Work-in-progress remains local for execution, verification, and resumption with either tracker. Feature documents separate optional requirements, living specifications, unresolved proposals, and tasks. Files appear only when useful.

## Common questions

**Do I have to use GitHub?**

No. GitHub, GitLab, Jira, and local Markdown are supported. Another tracker works through a verified connector, command-line tool, API workflow, or an explicitly manual workflow. Local task bodies live under `documentation/<feature>/tasks/`; remote task references can use a title and link instead of a copied body.

**Does setup create my remote labels?**

No. The role file maps names; it does not provision them. Graphify labels also need to exist before commands that require them can succeed. Local Markdown uses `Category:` and `Status:` instead.

**Do I need to re-run setup after updating skills?**

Re-run it when an older configuration no longer matches the workflows consuming it. Day-to-day edits to the configuration can be made directly. A new document model does not authorize moving old history automatically.

**It wrote to `CLAUDE.md`, but my agent reads `AGENTS.md`.**

Setup prefers an existing `CLAUDE.md`, then an existing `AGENTS.md`. If both conventions are used in your repository, keep the relevant instructions reachable by the agent you use. If neither file exists, setup asks which to create.

## It's working if

- Workflow skills read the tracker and writing conventions without guessing.
- Local specifications remain the living authority even with a remote tracker.
- Remote publication happens only when requested.
- Role strings match your tracker, and existing history remains intact.
- You can inspect and edit every configuration file; no installed `SKILL.md` changed.

## Where it fits

This is run-once setup for [specify](../workflow/specify.md), [taskify](../workflow/taskify.md), [triage](../upkeep/triage.md), and [graphify](../shaping/graphify.md). [Document](../reference/document.md) owns the shared document rules; [guide](guide.md) routes the workflow.
