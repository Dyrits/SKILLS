# Handoff format

A handoff is self-contained: the next agent resumes from the file alone, found through the pointer in `AGENTS.md`, with no skill installed.

## Location and name

`.agents/handoffs/YYYY-MM-DD-HHMM-<slug>.md` at the workspace root. The timestamp is when the file was written; the slug is the topic in dash-case. Names sort chronologically, so the newest handoff sorts last. A written handoff is never edited or overwritten: a later state gets a new file.

## Threads

A thread is one line of work. A handoff's `Supersedes` line names the earlier handoff of the same thread it replaces, which chains the thread. A handoff that starts a thread writes `none`; a side task forked off a running thread writes `none (forked from <filename>)`.

## Template

Every section appears, in this order, under these headings. A section with nothing to say holds `None.`

```markdown
# Handoff: <topic>

Supersedes: `<filename>` | none | none (forked from `<filename>`)
Workspace: <repository and branch, or directory>

To resume: read this whole file first. Treat every claim in State not marked verified as unverified, and check it against the Sources. Read the superseded handoff only when something here cannot be resolved from this file and its Sources. Confirm what was in flight and what you will do next with the user before starting. Never edit this file: a later state goes into a new handoff.

## Goal

What the work is for and what done looks like, in one to three sentences.

## State

What is done and what is in flight, and where it lives (branch, files). Mark each claim the next agent will build on as verified, saying how (test run, file read, command output), or as assumed.

## Decisions

Each decision taken so far that the next agent must respect, with its reason and where it is recorded, if anywhere.

## Next

The ordered next steps. The first one is where the next session starts.

## Open questions

What is unresolved, and who or what can answer it.

## Sources

Paths and URLs of the primary sources: specifications, plans, issues, commits, diffs.
```

## Rules

- Reference recorded material by path or URL instead of copying it; write down only what the session added.
- Replace secrets (keys, tokens, passwords) and personal data with `[redacted]`.
- Copy the "To resume" paragraph verbatim; it is how a reader with no skill installed knows how to use the file.
- Name no skills or harness-specific commands for the next agent to call: the next session may run in another harness with other skills installed. Project commands (a test or build command) belong in State or Next like any other fact.

## Pointer

The nearest `AGENTS.md` holds one line per thread in flight, naming the current handoff of that thread:

```markdown
To resume <topic>, read the [current handoff](.agents/handoffs/<filename>). Handoffs are <shared and committed | local and not committed>.
```

A new handoff replaces the line naming the handoff it supersedes; a handoff that starts or forks a thread adds a line. When a handoff records its goal as done, remove its thread's line instead.
