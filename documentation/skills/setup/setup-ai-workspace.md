Upstream skill: `setup-matt-pocock-skills`, adapted here as `setup-ai-workspace`.

## What it does

Configures one repository's task tracker, ticket-writing convention, and triage-role vocabulary. Its output is editable Markdown under `.agents/`, plus an agent-instruction block. It changes project configuration, not the installed skills. Code conventions, tooling, hooks, guardrails, and machine-wide settings are out of its scope; it reports a missing conventions file instead of writing one.

The tracker choice does not move specification authority. Agreed living behavior and acceptance stay in the capability's specifications in the repository. Remote tasks link to or summarize that specification. Local documents can be maintained within scope without publishing remote records.

## When to reach for it

Run `/setup-ai-workspace` once per repository, or when the tracker or conventions change. An agent can also reach for it when the workspace is unconfigured.

| Situation | Use |
| --- | --- |
| Workflow skills guess task locations or role strings | Run setup |
| The project already has a tracker and templates | Run setup to record the existing conventions |
| You want code conventions written down | [codify](./codify.md) |
| You want tooling, commit hooks, Git guardrails, or the delegation policy | Run [setup-ai-tooling](./setup-ai-tooling.md), [setup-git-hooks](./setup-git-hooks.md), [setup-git-guardrails](./setup-git-guardrails.md), or [setup-delegation-policy](./setup-delegation-policy.md) on their own |

## The configuration contract

- `.agents/issue-tracker.md` records local or remote operations, the writing convention, and wayfinding operations.
- `.agents/triage-roles.md` maps category and intake-state roles, when triage is installed.
- An `## Agent skills` block in `AGENTS.md` points at those files, which is how other skills find them. Lines for the project documents come from whichever skill creates each one.

When the repository shows several domain contexts, it asks whether the domain has several, and explains where each context's glossary will live once the first term is settled.

Future work uses the shared project-document model. Project requirements constrain all work. A local backlog records candidates and deferrals; with a remote tracker, the local backlog links to the authoritative backlog instead. Work-in-progress remains local for execution, verification, and resumption with either tracker. Feature documents separate optional requirements, living specifications, unresolved proposals, and tasks. Files appear only when useful.

## Common questions

**Do I have to use GitHub?**

No. GitHub, GitLab, Jira, and local Markdown are supported. Another tracker works through a verified connector, command-line tool, API workflow, or an explicitly manual workflow. Local task bodies live under `documentation/capabilities/<capability>/tasks/`; remote task references can use a title and link instead of a copied body.

**Does setup create my remote labels?**

No. The role file maps names; it does not provision them. Graphify labels also need to exist before commands that require them can succeed. Local Markdown uses `Category:` and `Status:` instead.

**Do I need to re-run setup after updating skills?**

Re-run it when an older configuration no longer matches the workflows consuming it. Day-to-day edits to the configuration can be made directly. A new document model does not authorize moving old history automatically.

**Which file does it write to?**

The root `AGENTS.md`. Setup creates it when it does not exist, and updates an existing `## Agent skills` block in place without touching your other instructions.

## It's working if

- Workflow skills read the tracker and writing conventions without guessing.
- Local specifications remain the living authority even with a remote tracker.
- Remote publication happens only when requested.
- Role strings match your tracker, and existing history remains intact.
- You can inspect and edit every configuration file; no installed `SKILL.md` changed.

## Where it fits

This is run-once setup for [specify](../workflow/specify.md), [taskify](../workflow/taskify.md), [triage](../upkeep/triage.md), and [graphify](../shaping/graphify.md). It carries its own copy of the shared document rules.
