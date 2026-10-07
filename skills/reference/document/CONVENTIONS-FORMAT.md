# Conventions format

The conventions file holds the project's code conventions: how code is written here, applied by a reviewer to any diff and enforceable by no tool.

The file is **project-agnostic**: its rules apply to this project but could be transposed to another one, because none is tied to the product or its domain. It is the technical counterpart of the functional records (the glossary, requirements, specifications) and never names the product, its users, or its domain terms. The test for the whole file: copy it into another project on the same stack, with an unrelated domain, and every rule still applies there unchanged.

## What belongs

A convention is project-agnostic: it would still hold if the product changed entirely and only the stack and the team stayed. "Errors cross module boundaries as typed results, never thrown strings" is project-agnostic. "The line never breaks" is not: it describes what this product does, and a reviewer cannot apply it to an unrelated diff. A rule that needs a domain term to be stated is not a convention.

A requirement and a convention answer different questions: a requirement says what the product must do or never do and is imposed from outside the code; a convention says how code is written here and is the team's own choice. When the two seem to clash, the requirement wins and the convention shapes how it is met.

Route everything else to its home and tell the user where it went:

| The candidate is | It belongs in |
| --- | --- |
| What the product must do or never do, a content or wording rule | Requirements when it binds the whole product; the capability's requirements or specifications when it binds one capability |
| A hard-to-reverse design choice with real alternatives | A decision record |
| The meaning of a domain term | The glossary |
| How the agent works: verification, approvals, who confirms what | `AGENTS.md`, through `write-for-agents` |
| Something a linter, formatter, type checker, hook, or CI job can check | That tool's configuration; offer to wire it |

A candidate can split: "visible text lives in data, in two languages" yields the project-agnostic convention "no user-facing string literals in rendering code" and a requirement for the language pair.

## Structure

```md
# Conventions

How code is written in this project. Project-agnostic: every rule could be transposed to another project on the same stack. Product rules live in requirements, domain terms in the glossary, and a requirement outranks any rule here.

## {Topic from the interview}

- **{Rule}**: {the reason it exists, and the case it does not cover}
```

## Rules

- **Project-agnostic only.** No product, user, or domain term appears in the file. See What belongs.
- **Cache only what the agent cannot find by looking.** Skip anything already visible in configuration, scripts, or the directory layout.
- **One meaning, one place.** Link to decision records and the glossary instead of restating them.
- **Create lazily.** Write the file when the first rule is agreed, not as an empty scaffold.

## Checking an existing file

Apply the copy test to the whole file, run each rule through What belongs, and propose a move for every rule that is not project-agnostic, splitting mixed rules. Move nothing without the user's approval.
