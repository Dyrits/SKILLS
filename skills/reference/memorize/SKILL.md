---
name: memorize
description: 'File a lesson in the home the next agent will read, and recall saved scripts and lessons before redoing work. Use the moment the user says "always", "never", "from now on" or "remember", or corrects how something is done rather than one result; before writing a script or a pipeline longer than one line; and when you rebuild something a second time. Use it even when the harness has its own memory: a project lesson belongs in the project.'
---

# Memorize

Agents relearn the same things every session: the helper written yesterday, the convention the user corrected twice, the term the team already settled. **Memorize** files each lesson in the home the next agent will read when it matters; **recall** checks that home before redoing the work.

**Calls:** `document`, `walk-through`, `write-for-agents`. **Hands over to:** `/improve-skills`.

## Homes

| Lesson | Home | How |
| --- | --- | --- |
| A reusable action (rename files, convert a format, call an endpoint) | A scriptbook: `.agents/scripts/` for this repository, `~/.agents/scripts/` for any repository | Read [SCRIPTS.md](SCRIPTS.md) |
| A project convention, command, or gotcha agents keep missing | The nearest `AGENTS.md` at the boundary where it applies | Call the Skill tool with "write-for-agents" |
| A code convention | The project's conventions | Call the Skill tool with "document" |
| A domain term or consequential decision | The glossary or a decision record | Call the Skill tool with "document" |
| Project agreements, working state, or delivery history | The shared project documents | Call the Skill tool with "document" |
| A procedure only a human can carry out, worth repeating | A saved wizard | Call the Skill tool with "walk-through" |
| A personal preference that holds across projects | The harness's own memory when it provides one; otherwise `~/.agents/memory/` | See **Personal memory** below |
| A defect in a skill itself (a wrong trigger, an unclear step, a missing skill) | The skills repository, reported once the session ends | Tell the user to run `/improve-skills` |

The environment is a home too: a `package.json` script, a config file, or `--help` output already states its fact. Leave those facts there.

## Recall

Before writing a script or a shell pipeline longer than one line, follow the lookup step in [SCRIPTS.md](SCRIPTS.md). Before redoing work that resembles earlier work, check the home it would have been filed in. When a request depends on how the user likes things done, read the personal memory index unless the harness has already loaded it.

Completion: a matching entry is reused or extended, or the relevant homes were checked and nothing fits.

## Memorize

Memorize the moment the user corrects you, states a standing rule, or asks you to remember something, and when the same thing has been rebuilt twice. A correction is a lesson when it would apply to the next task too ("we use pnpm here"); a change to this one result ("make it blue") is just done, not filed. Do it in that turn, before carrying on with the task: a lesson deferred to the end of a long task is a lesson lost. Route even a plain "remember this": the harness's own memory is one home among several, so a project fact still goes to the project.

1. State the lesson in one sentence, with its reason when the reason is not obvious.
2. Pick its home from the table: the place that is read at the moment the lesson matters.
3. Read that home first. Update an existing entry instead of adding a second one, and remove an entry the lesson proves wrong.
4. Write it, then tell the user in one line what was saved and where.

Keep secrets, one-conversation context, and facts the environment already states out of every home.

Completion: the lesson exists in exactly one home, and the user knows where.

## Pointers

A home works only when the next agent reads it, and a skill description alone fires unreliably during a long task. When you create a project scriptbook, start relying on one, or find the nearest `AGENTS.md` without this skill's own pointer, add the always-loaded pointer there once, checking for an existing one first:

> Call the Skill tool with "memorize" the moment the user states a standing rule, asks you to remember something, or corrects how something is done, and when something is rebuilt a second time. Before writing a script or a pipeline longer than one line, read `.agents/scripts/INDEX.md` and reuse or extend a match.

## Personal memory

Use the harness's memory system when it has one, following its format. It holds personal preferences only: a teammate's agent never reads it, so a project convention filed there is lost to everyone else. Otherwise keep `~/.agents/memory/`: one fact per Markdown file with a line on why it holds, and an `INDEX.md` with one line per file, `- [Title](<file>.md): when it applies`. Read the index during recall and open only the files whose hook matches the task.

## Delegating

A subagent starts without this conversation. Put both scriptbook paths, and any memory entries that bear on the task, in its briefing.
