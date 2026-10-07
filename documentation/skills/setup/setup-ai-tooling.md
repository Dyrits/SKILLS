Fork-created skill: it has no upstream equivalent. It was added in commit `1394bed`; the third-party tools it installs are not the source of this workflow. The [provenance audit](../../research/2026-10-03-retained-skill-provenance.md) records the evidence.

## What it does

Provisions free AI development tools for one project and the agent clients installed on the machine, then records a measurable baseline. It reuses working integrations instead of reinstalling them, and it leaves an unverified adapter or output filter disabled rather than guessing.

It runs only inside an explicit tooling request.

## When to reach for it

Type `/setup-ai-tooling`, or an agent can reach for it when you ask to install or configure AI tooling. It does not start on its own for ordinary coding work.

| Situation | Use |
| --- | --- |
| A project has no code index, documentation lookup, or structural search | Run this skill |
| Tools exist but you want evidence they help | [monitor-ai-tooling](../upkeep/monitor-ai-tooling.md) |
| You want the repository's tracker and conventions configured | [setup-ai-workspace](./setup-ai-workspace.md) |

## What it configures

[TOOLS.md](../../../skills/setup/setup-ai-tooling/TOOLS.md) holds the per-tool branches. Selection follows the project:

- CodeGraph for supported source projects, and Context7 for dependency documentation.
- ast-grep when a representative structural search adds value.
- Playwright CLI or Chrome DevTools MCP for browser work, chosen by the task.
- Tracker command-line tools for the project's tracker.
- RTK output rewriting only after protected-command checks pass, so diffs, file reads, searches, and test output survive intact.

Serena stays optional when CodeGraph and native language support already cover navigation.

## The baseline record

The skill writes `.agents/ai-tooling.md`: selected tools and versions, scope, per-client integration status, verification results, known gaps, protected commands, local measurement sources, and a verified session recovery method per client. Measurement history stays local and out of version control; credentials are reported by presence, never value.

## Common questions

**Will it replace tools I already have?**

No. A binary, a project index, and a connected agent are checked as separate states, and a working integration is reused. Rerunning setup preserves existing configuration.

**Does it need paid services?**

No. It uses free tools and free service tiers, and asks before anything that needs payment or new account access.

**Does it work outside Claude Code?**

It supports Codex, OpenCode, and other detected clients through their documented adapters, and records each client's actual coverage, including gaps.

**Can it claim how many tokens I saved?**

Only where a comparable task baseline exists. Command-output reduction, task token counts, and provider allowance are reported as different quantities, and personal token savings are marked unavailable otherwise.

## It's working if

- Each configured client passes a functional check, such as a known symbol retrieved through CodeGraph and matched against the file.
- Protected output and exit status survive the actual adapter.
- `.agents/ai-tooling.md` exists, points to real measurement sources, and carries no credentials or personal session paths.
- Rerunning the skill changes nothing that already works.

## Where it fits

Run-once setup per project, run on its own request; [setup-ai-workspace](./setup-ai-workspace.md) configures the project records and leaves tooling to it. [monitor-ai-tooling](../upkeep/monitor-ai-tooling.md) is its periodic follow-up. [guide](../productivity/guide.md) routes the rest.
