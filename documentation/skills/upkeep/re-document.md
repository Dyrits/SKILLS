Fork-specific skill with no upstream equivalent. The other skills each write their own project documents, but none checks a project's existing documentation against its code.

## What it does

`re-document` reads a project's documentation next to its code, finds what has gone stale, and corrects it. It splits each document into claims (a path, a command, a default, a flow, a list), checks each against the code, and cites the file and line behind every correction. Where the evidence is not in the repository, or the code itself may be the mistake, it asks you instead of guessing.

Its defining constraint is the split between two kinds of document:

| Kind | Examples | When the code differs |
| --- | --- | --- |
| State | README, setup guides, architecture, glossary, references, `AGENTS.md` lines | The code wins. The document is corrected |
| Intent | Requirements, specifications, decision records, changelog, backlog | Either side may be wrong. You decide, and a decision record or changelog entry is never rewritten |

When the project has no documentation, it offers to write it. The code can supply a README, an architecture document, and a glossary. It cannot supply requirements, specifications, or the reasons behind decisions, so it does not infer them and lists them in its report as not recorded.

## When to reach for it

Type `/re-document`, or an agent can reach for it when the task fits: you ask whether the documentation is current or accurate, you want it brought up to date after a stretch of changes, or the project has none. It edits local documentation files and nothing else: it changes no code, makes no commit, and writes nothing outside the repository.

| The situation | The move |
| --- | --- |
| The README no longer matches the code | `re-document` |
| A project has no README or architecture document | `re-document` offers to write them |
| Code conventions are missing or mixed up | [codify](./codify.md) |
| A session was hard and you want the environment fixed | [improve-environment](./improve-environment.md) |
| The system's functional picture needs to be built | [delineate](../workflow/delineate.md) |

## What gets checked

Each kind of claim has its own check:

- A path or name must exist and do what the document says.
- A command must appear in the build tool's scripts, a `Makefile`, or CI. The skill runs a command only when it is read-only, never one that deploys, migrates, deletes, or calls a paid service.
- A flag, port, variable, or default is compared with the code.
- A list or count is enumerated from the code and compared item by item.
- A link must resolve, and a code sample's names must exist.

As a starting point it compares each document's last commit with the code that changed since. The hint only orders the reading; every claim still gets a verdict of confirmed, stale, or unknown.

## Common questions

**It found a mismatch and asked me instead of fixing it. Why?**
It asks when the code might be the mistake (a divergence from an intent document, or code that looks half-finished), when the evidence is outside the repository, or when the fix needs a choice such as deleting a section or rewriting it. An unambiguous stale claim in a state document, such as a renamed path or a changed default, is corrected without a question.

**Does it fix the code when the document is right?**
No. If you say the code is wrong, it changes no document and lists the defect in its report.

**Does it prune or restyle `AGENTS.md`?**
It corrects a line that is no longer true, and deletes one the environment already answers, such as a command list that repeats the build tool's scripts. It leaves a line that is still true alone.

**The project's API reference is generated. Will it edit the output?**
No. It fixes the source comment or reports the generator.

**What if I decline the offer to write documentation?**
Nothing is written, and a later run asks again. Run as a subagent with no one to answer, it writes nothing and returns the proposed set.

## It's working if

- Every correction in the report cites the file and line that justify it.
- Commands, paths, and defaults in the README match the code and the build tool's scripts.
- A code change that contradicts a requirement or specification reaches you as a question, not as a silent edit.
- Every documentation file is named by an `AGENTS.md` line, one line per kind.
- A project that had no documentation ends with only the documents you accepted, each with every claim confirmed against the code.

## Where it fits

`re-document` is periodic maintenance: run it after a stretch of changes, before a release, or when a project is handed over. It reads and writes the same project documents as the workflow skills, found through `AGENTS.md`, and carries its own copies of the [interview](../shaping/interview.md) method and of the formats it writes. [delineate](../workflow/delineate.md) and [architect](../workflow/architect.md) write the glossary and architecture document from decisions with you; `re-document` keeps them true to the code afterwards.
