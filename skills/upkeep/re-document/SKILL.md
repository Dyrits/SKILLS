---
name: re-document
description: "Check a project's documentation against its code, correct what is stale, and ask the user when unsure; offer to write documentation when the project has none. Use when the user asks whether the documentation is current, accurate, or needs bringing up to date, or when a project has no documentation."
---

# Re-document

Bring a project's documentation back in line with its code. The code is the source of truth for what the system does today, so a stale document is corrected to match it. The exception is a document that records intent: when the code differs from one, either side may be wrong, and only the user decides.

Take one branch:

- **Check**: documentation exists. Run every section below except "Offer documentation", which runs for the gaps Check finds.
- **Create**: the project has none. Run "Find the documentation", then "Offer documentation".

## Find the documentation

Read the root `README.md` and `AGENTS.md`, then the documents `AGENTS.md` names, following [project-documents.md](references/project-documents.md). Then search the repository for documentation neither names: `documentation/` and `docs/` folders, per-package READMEs, setup guides, API and configuration references, runbooks. Judge a folder by its content, not its name. Skip generated files; the generator or its source comments are what you would correct.

Sort each document into one kind:

- **State**: describes the system as it is. A README, a setup or usage guide, an architecture document, a glossary, a reference, the lines of `AGENTS.md`.
- **Intent**: records what was agreed or decided. Requirements, specifications, decision records, a changelog, a backlog, working state.

When there is no README with content, no documentation folder, and `AGENTS.md` names nothing, the project has no documentation. A README that is only a title or template text counts as none.

Completion: every documentation file is listed with its kind and whether `AGENTS.md` names it, or the project is stated to have none.

## Check

Split each state document into claims and check each against the code.

| Claim | Check |
| --- | --- |
| A path, file, module, or class name | It exists under that name and does what the document says |
| A command to install, build, run, or test | It appears in the build tool's scripts, a `Makefile`, or CI. Run it only when it is read-only (`--help`, a dry run). Never run one that deploys, migrates, deletes, or calls a paid service |
| A flag, option, environment variable, port, or default | Search the code and configuration for it and compare the default |
| A version or dependency | Compare it with the manifest and lockfile |
| A behavior, flow, or the parts of the system | Read the code path from its entry point to its effect |
| A list or count (endpoints, commands, modules) | Enumerate it from the code and compare item by item |
| A link or code sample | The link resolves; the sample's names and signatures exist |

To decide where to read first, find the document's last commit (`git log -1 --format=%H -- <document>`) and list the code it describes that changed since (`git diff --stat <commit>..HEAD -- <paths>`). It is a hint only: an untouched document can still be wrong, and a recent edit can still be stale.

Give each claim one verdict:

- **Confirmed**: the code agrees.
- **Stale**: the code shows something else. Cite the file and line.
- **Unknown**: the evidence is outside the repository (a deployed address, an external service, a team practice), or the code is ambiguous.

Compare each intent document with the code the same way, but record a **divergence** where they differ; neither side is called stale.

Then list the gaps: every package, module, service, or entry point that no document covers, and every command, setting, or behavior the code has that a covering document omits.

With many documents, delegate one per subagent when subagents are available. Each returns its claims with a verdict and its evidence.

Completion: every claim in every state document has a verdict with evidence from the code or a stated reason the code cannot answer; every intent document is compared; every top-level part of the code is either covered by a document or listed as a gap.

## Resolve

Correct without asking a stale claim in a state document when the code is unambiguous: a renamed path, a changed default, a removed command, a broken link.

Ask the user when:

- The code might be the mistake: a divergence from an intent document, or code that looks half-finished, dead, or at odds with its own tests.
- The verdict is unknown.
- The fix needs a choice: delete a section or rewrite it, document a gap or leave it, describe planned or external behavior.

Ask in rounds through the [interview method](references/interview.md), each question stating the evidence and a recommended answer. With no user to answer (a subagent run), apply the unambiguous corrections and return the questions with their recommendations.

Completion: every stale, unknown, and divergent finding is corrected, answered by the user, or returned as a question with its recommendation.

## Correct

- Edit in place with the smallest change that makes the claim true, keeping the document's structure, voice, and numbering. Write a gap into the document that already covers its neighbors.
- For a divergence, apply the user's answer. If the document was wrong, correct a requirement or specification in place. If the code was wrong, change no document and list the defect in the report. Never rewrite a decision record or the history in a changelog: report what contradicts it.
- In `AGENTS.md`, correct a stale line, or delete it when the environment already answers it (a command list that repeats the build tool's scripts goes stale on its own). Follow [agent-instructions.md](references/agent-instructions.md). Pruning a line that is still true is out of scope.
- For a generated document, fix the source comment or report the generator and leave the output.
- Add the `AGENTS.md` line [project-documents.md](references/project-documents.md) describes for each documentation file it did not name, one line per kind.

Completion: every edited claim passes the Check again, every link in an edited document resolves, and `AGENTS.md` names every kind of documentation found.

## Offer documentation

Run this for the Create branch, and for the gaps Check found. Ask the user in one round which documents to write, with a recommendation for each. The code can support three:

- **README**: what the project is, how to install, run, and test it (from the build tool's scripts), and where things live.
- **Architecture**, following [architecture-format.md](references/architecture-format.md). Recommend it when the code has more than one part.
- **Glossary**, following [glossary-format.md](references/glossary-format.md). Recommend it when the domain types carry terms specific to the project.

Requirements, specifications, and the reasons behind decisions live outside the code. Do not infer them; list them in the report as not recorded.

For each accepted document: find an existing home and never overwrite, as [project-documents.md](references/project-documents.md) says, with `documentation/` as the default folder and the README at the repository root. Write only what the code shows, and omit a reason for a choice unless the user gave it. Then run Check on the new document. When the project has no `AGENTS.md`, tell the user and create one holding only the pointer lines; otherwise add one line per document. Link each from the README's documentation section.

On a no, write nothing. A later run asks again. With no user to answer, write nothing and return the proposed set.

Completion: the user answered for each offered document, and each accepted one is written, announced in `AGENTS.md`, and has every claim confirmed against the code.

## Report

Name every file written or edited. For each document, give the counts of confirmed, corrected, and answered claims, with the evidence for each correction. Then list what stays open: unanswered questions, divergences, defects found in the code, gaps left unwritten, and the kinds of document the code cannot supply.
