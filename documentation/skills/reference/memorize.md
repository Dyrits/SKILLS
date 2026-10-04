Fork-created skill with no upstream equivalent. It absorbed the earlier `scriptbook` skill, added in commit `4456e95`; its steps now live in [SCRIPTS.md](../../../skills/reference/memorize/SCRIPTS.md) (see the [provenance audit](../../research/2026-10-03-retained-skill-provenance.md)).

## What it does

`memorize` files each lesson in the home the next agent will read when it matters, and `recall` checks that home before redoing work. It exists because agents relearn the same things every session: the helper written yesterday, the convention you corrected twice, the term the team already settled.

It chooses a home; it does not invent a new store for each kind of fact.

| Lesson | Home |
| --- | --- |
| A reusable action | A scriptbook: `.agents/scripts/` for the repository, `~/.agents/scripts/` for any repository |
| A convention or gotcha agents keep missing | The nearest `AGENTS.md` or `CLAUDE.md` |
| A code convention, a term, or a decision | `GUIDELINES.md`, `GLOSSARY.md`, or an architecture decision record, through [model-domain](./model-domain.md) |
| Agreements, working state, delivery history | The shared project documents, through [document](./document.md) |
| A procedure only a human can carry out | A saved wizard, through [walk-through](../productivity/walk-through.md) |
| A personal preference across projects | The harness's own memory, otherwise `~/.agents/memory/` |
| A defect in a skill itself | No local home: the agent tells you that [improve-skills](../upkeep/improve-skills.md) reports it on this repository |

Facts the environment already states, such as a `package.json` script or `--help` output, stay there. Secrets and one-conversation context are never saved.

## When to reach for it

Type `/memorize`, or an agent or another skill can reach for it when a task fits: the moment it rebuilds something a second time, when you correct a behavior, when you ask it to remember something, and before it writes any script or multi-step shell pipeline. For writing the instruction file itself, it hands off to [write-for-agents](./write-for-agents.md).

## Scriptbooks

A scriptbook is a directory of scripts plus an `INDEX.md` with one line per script. Before writing a script, the agent reads both indexes and checks the project's task runner. A matching entry is run, or extended with one more parameter, instead of cloned into a sibling.

A script is saved only when it does one action, takes every changing value as an argument, reads credentials from environment variables, and is safe to rerun or says what it changes. Its header carries a usage example that was run once before indexing.

## Common questions

**Where did scriptbook go?**

It was folded into `memorize` as its script branch. The agent no longer needs a separate skill for scripts, and the same recall step covers conventions and preferences.

**Why does it care about pointers?**

A skill description alone fires unreliably during a long task. The repository evidence is a session that wrote inline Python for bulk edits while a matching saved script existed. So the nearest `AGENTS.md` or `CLAUDE.md` gets one always-loaded line pointing at the scriptbook index, added once after checking for an existing one. [setup-ai-workspace](../getting-started/setup-ai-workspace.md) writes that line as part of its agent-instruction block.

**Does it duplicate a fact in several homes?**

No. A lesson lives in exactly one home, and an existing entry is updated or removed rather than doubled.

**What if a skill it calls or hands over to is not installed?**
It names the missing skill with its install command, carries out that step from its stated intent, and tells you the step ran without it. Without `document` it waits instead, because its rules use that skill's terms: install it, or tell it to proceed anyway. When it tells you to run a skill you don't have, it gives the install command with it. The skills involved are listed at the top of its [`SKILL.md`](../../../skills/reference/memorize/SKILL.md).

## It's working if

- The agent reuses a saved script instead of rewriting it.
- After you correct something once, you are told in one line what was saved and where.
- Every scriptbook file has one index line and every index line points to a file.
- The nearest instruction file carries the scriptbook pointer exactly once.

## Where it fits

This is a standalone discipline that other skills call; it produces no deliverable of its own. It routes to [write-for-agents](./write-for-agents.md), [model-domain](./model-domain.md), [document](./document.md), and [walk-through](../productivity/walk-through.md) depending on the lesson. [improve-skills](../upkeep/improve-skills.md) runs after a session and files what `memorize` cannot fix locally: problems in the skills themselves. [guide](../getting-started/guide.md) maps the whole system.
