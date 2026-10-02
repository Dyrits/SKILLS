---
name: scriptbook
description: Scriptbook, reuse before writing. Check the saved-script index before writing any script or multi-step shell pipeline for an action, run a match instead of rebuilding it, and save new parameterized scripts with an index entry.
---

# Scriptbook

Agents rebuild the same helper (rename files, convert a format, call an endpoint, extract a field) in every section of a task, and again in the next session. Saved scripts with an index turn that rebuild into a lookup.

Two scriptbooks, each a directory holding scripts plus an `INDEX.md`:

- **Project**: `.agents/scripts/`, for scripts that rely on this repository's layout, tooling, or conventions.
- **Global**: `~/.agents/scripts/`, for scripts that work in any repository.

Create a directory and its `INDEX.md` the first time something is saved there.

## 1. Look up

Before writing a script or a multi-step shell pipeline, read both `INDEX.md` files. Also check the project's own task runner (`justfile`, `Makefile`, `package.json` scripts): a command that exists there is the answer, so skip the index for it.

Completion: the action matches an entry or runner command, or both indexes and the runner have been read and none fits.

## 2. Run or extend

Run a matching entry with the arguments the task needs. When an entry fits except for one input, add a parameter to it, rerun its usage example, and update its index line. A sibling script that differs by one value is a duplicate.

## 3. Write only when nothing fits

A script is worth saving when a later section of this task, another task, or another agent would run it with different arguments. Save it when it meets all four:

- One action, named by a verb and a noun (`convert-csv-to-json`, `extract-har-urls`).
- Every changing value (paths, IDs, URLs, dates) is an argument, so no edit is needed to reuse it.
- Credentials come from environment variables.
- Rerunning it is safe, or its header says what it changes.

A script that only makes sense for this one dataset runs inline and is not saved.

## 4. Save and index

Pick the project scriptbook when the script depends on this repository, the global scriptbook otherwise. Write the script as an executable file that opens with a header comment giving what it does, its arguments, and one usage example. Run that example once before indexing.

Add one line to the matching `INDEX.md`, kept in alphabetical order:

```
- `name.ext`: what it does in one sentence. Usage: `name.ext <args>`. Needs: interpreter or tools.
```

Completion: every file in the scriptbook has exactly one index line and every index line points to a file.

## Delegating

A subagent starts without this conversation. Put both scriptbook paths in its briefing so its lookup finds what you already saved.
