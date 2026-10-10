Fork-created skill with no upstream equivalent. It absorbed the earlier `scriptbook` skill, added in commit `4456e95`; its steps now live in [scripts.md](../../../skills/productivity/memorize/references/scripts.md) (see the [provenance audit](../../research/2026-10-03-retained-skill-provenance.md)).

## What it does

`memorize` files each lesson in the home the next agent will read when it matters, and `recall` checks that home before redoing work. It exists because agents relearn the same things every session: the helper written yesterday, the convention you corrected twice, the term the team already settled.

It chooses a home; it does not invent a new store for each kind of fact.

| Lesson | Home |
| --- | --- |
| A reusable action | A scriptbook: `.agents/scripts/` for the repository, `~/.agents/scripts/` for any repository |
| A convention or gotcha agents keep missing | The nearest `AGENTS.md` |
| A code convention, a term, or a decision | The conventions, the glossary, or an architecture decision record, using the formats the skill carries |
| Agreements, working state, delivery history | The shared project documents, following the contract the skill carries |
| A procedure only a human can carry out | A saved wizard, built from the template and steps the skill carries (adapted from [walk-through](../productivity/walk-through.md)) |
| A personal preference across projects | The harness's own memory, otherwise `~/.agents/memory/` |
| A defect in a skill itself | No local home: the agent names the skill, the step, and what went wrong in its final report, for you to report on this repository |

Facts the environment already states, such as a `package.json` script or `--help` output, stay there. Secrets and one-conversation context are never saved.

## When to reach for it

Type `/memorize`, or an agent can reach for it when a task fits: before it writes a script or a shell pipeline longer than one line, when you correct how something is done, state a standing rule ("always", "never", "from now on") or ask it to remember something, and when it rebuilds something a second time. A correction to one result ("make it blue") is just applied: only a correction that would hold for the next task is filed. A plain "remember this" still goes through it, because the harness's own memory is one home among several and a project fact belongs in the project. For writing the instruction file itself, it hands off to [write-for-agents](./write-for-agents.md).

## Scriptbooks

A scriptbook is a directory of scripts plus an `INDEX.md` with one line per script. Before writing a script, the agent reads both indexes and checks the project's task runner. A matching entry is run, or extended with one more parameter, instead of cloned into a sibling.

A script is saved only when it does one action, takes every changing value as an argument, reads credentials from environment variables, and is safe to rerun or says what it changes. Its header carries a usage example that was run once before indexing, on scratch input or as a dry run when the script changes files or remote state.

## Common questions

**Where did scriptbook go?**

It was folded into `memorize` as its script branch. The agent no longer needs a separate skill for scripts, and the same recall step covers conventions and preferences.

**Why does it care about pointers?**

A skill description alone fires unreliably during a long task. The repository evidence is a session that wrote inline Python for bulk edits while a matching saved script existed. So the nearest `AGENTS.md` gets one always-loaded pointer, added once after checking for an existing one: call `memorize` the moment the user states a standing rule, asks you to remember something, or corrects how something is done, or when something is rebuilt a second time, and read the scriptbook index before writing a script or a pipeline longer than one line. The call comes first in the line and in the turn, because a correction is acted on and forgotten unless it is filed in the turn it arrives. `memorize` adds that line itself the first time it finds the pointer missing.

**Does it duplicate a fact in several homes?**

No. A lesson lives in exactly one home, and an existing entry is updated or removed rather than doubled.

## It's working if

- The agent reuses a saved script instead of rewriting it.
- After you correct something once, you are told in one line what was saved and where.
- Every scriptbook file has one index line and every index line points to a file.
- The nearest instruction file carries the pointer exactly once.
- A project convention you state mid-session lands in the project's instruction file, not only in the agent's personal memory.

## Where it fits

This is a working habit you or an agent reach for during any task; its result is the filed lesson or the saved script. It carries its own copies of the steering-file rules from [write-for-agents](./write-for-agents.md), the project document formats, and the wizard template from [walk-through](../productivity/walk-through.md), so it files every kind of lesson without another skill. [improve-skills](../upkeep/improve-skills.md) runs after a session and files what `memorize` cannot fix locally: problems in the skills themselves.
