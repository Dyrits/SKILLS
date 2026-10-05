---
name: memorize
description: File a lesson in the home the next agent will read (instruction file, scriptbook, glossary, personal memory) and recall saved scripts and lessons before redoing work. Use before writing any script or multi-step shell pipeline, when the user corrects a behavior, states a standing rule ("always", "never", "from now on") or says to remember something, and when the same thing is rebuilt a second time.
---

# Memorize

Agents relearn the same things every session: the helper written yesterday, the convention the user corrected twice, the term the team already settled. **Memorize** files each lesson in the home the next agent will read when it matters; **recall** checks that home before redoing the work.

**Calls:** `document`, `model-domain`, `walk-through`, `write-for-agents`. If a called skill is not installed, tell the user its name and install command, `npx skills@latest add Dyrits/SKILLS --skill=<name>`, then carry out that step from its stated intent and report the step as done without the skill. Without `document`, wait until the user installs it or tells you to proceed: this skill's rules use its terms. **Hands over to:** `/improve-skills`. When one is not installed, give the user its install command, `npx skills@latest add Dyrits/SKILLS --skill=<name>`, along with the instruction to run it.

## Homes

| Lesson | Home | How |
| --- | --- | --- |
| A reusable action (rename files, convert a format, call an endpoint) | A scriptbook: `.agents/scripts/` for this repository, `~/.agents/scripts/` for any repository | Read [SCRIPTS.md](SCRIPTS.md) |
| A project convention, command, or gotcha agents keep missing | The nearest `AGENTS.md` or `CLAUDE.md` at the boundary where it applies | Call the Skill tool with "write-for-agents" |
| A code convention | `CONVENTIONS.md` | Call the Skill tool with "model-domain" |
| A domain term or consequential decision | `GLOSSARY.md` or an architecture decision record | Call the Skill tool with "model-domain" |
| Project agreements, working state, or delivery history | The shared project documents | Call the Skill tool with "document" |
| A procedure only a human can carry out, worth repeating | A saved wizard | Call the Skill tool with "walk-through" |
| A personal preference that holds across projects | The harness's own memory when it provides one; otherwise `~/.agents/memory/` | See **Personal memory** below |
| A defect in a skill itself (a wrong trigger, an unclear step, a missing skill) | The skills repository, reported once the session ends | Tell the user to run `/improve-skills` |

The environment is a home too: a `package.json` script, a config file, or `--help` output already states its fact. Leave those facts there.

## Recall

Before writing a script or a multi-step shell pipeline, follow the lookup step in [SCRIPTS.md](SCRIPTS.md). Before redoing work that resembles earlier work, check the home it would have been filed in. When a request depends on how the user likes things done, read the personal memory index.

Completion: a matching entry is reused or extended, or the relevant homes were checked and nothing fits.

## Memorize

Memorize when the user asks you to remember something, corrects a behavior likely to recur, or states a standing rule, and when the same thing has been rebuilt twice. Route even a plain "remember this": the harness's own memory is one home among several, so a project fact still goes to the project.

1. State the lesson in one sentence, with its reason when the reason is not obvious.
2. Pick its home from the table: the place that is read at the moment the lesson matters.
3. Read that home first. Update an existing entry instead of adding a second one, and remove an entry the lesson proves wrong.
4. Write it, then tell the user in one line what was saved and where.

Keep secrets, one-conversation context, and facts the environment already states out of every home.

Completion: the lesson exists in exactly one home, and the user knows where.

## Pointers

A home works only when the next agent reads it, and a skill description alone fires unreliably during a long task. When you create a project scriptbook, start relying on one, or find the nearest `AGENTS.md` or `CLAUDE.md` without this skill's own pointer, add the always-loaded pointer there once, checking for an existing one first:

> Before writing a script or multi-step pipeline, read `.agents/scripts/INDEX.md` and reuse or extend a match. Call the Skill tool with "memorize" when the user corrects a behavior or states a standing rule, and when something is rebuilt a second time.

## Personal memory

Use the harness's memory system when it has one, following its format. It holds personal preferences only: a teammate's agent never reads it, so a project convention filed there is lost to everyone else. Otherwise keep `~/.agents/memory/`: one fact per Markdown file with a line on why it holds, and an `INDEX.md` with one line per file, `- [Title](<file>.md): when it applies`. Read the index during recall and open only the files whose hook matches the task.

## Delegating

A subagent starts without this conversation. Put both scriptbook paths, and any memory entries that bear on the task, in its briefing.
