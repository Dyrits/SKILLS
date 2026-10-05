# GUIDELINES.md Format

`GUIDELINES.md` holds the project's code conventions: how code is written here, applied by a reviewer to any diff and enforceable by no tool. `review-and-refactor` and `improve-codebase-architecture` read it; `memorize` files new conventions into it.

## What belongs

A guideline is **portable**: it would still hold if the product changed entirely and only the stack and the team stayed. "Errors cross module boundaries as typed results, never thrown strings" is portable. "The line never breaks" is not: it describes what this product does, and a reviewer cannot apply it to an unrelated diff.

Route everything else to its owner, through the named skill, and tell the user where it went:

| The candidate is | It belongs in | Through |
| --- | --- | --- |
| What the product must do or never do, a content or wording rule | `documentation/requirements.md` when it binds the whole product; the capability's requirements or specifications when it binds one capability | `document` |
| A hard-to-reverse design choice with real alternatives | an architecture decision record | this skill |
| The meaning of a domain term | `GLOSSARY.md` | this skill |
| How the agent works: verification, approvals, who confirms what | `AGENTS.md` or `CLAUDE.md` | direct edit |
| Something a linter, formatter, type checker, hook, or CI job can check | that tool's configuration | offer to wire it |

A candidate can split: "visible text lives in data, in two languages" yields the portable guideline "no user-facing string literals in rendering code" and a requirement for the language pair.

## Offer

Check `.agents/domain.md` first. When it records `Guidelines: declined`, return to the caller without asking.
Otherwise ask whether to create `GUIDELINES.md` now. On yes, run the interview below; on no, record the decline (see Declining) and return.

## Interview

The caller passes a focus: **code** (review, setup) or **architecture** (audit); default to **code**. Walk the focus's topics in order, one question at a time, each with a recommended answer drawn from what the code already does consistently. Skip a topic the user has no rule for.

- **Code**: naming (files, functions, booleans, abbreviations); function and file size, and when to extract; types (strictness, `any` or its equivalent, nullability); error handling (throw or return, where errors are caught, what gets logged); state and side effects (mutation, purity, where input and output happen); comments and documentation; tests (what gets one, naming, fakes versus mocks, one behaviour per test); dependencies (when a new library is acceptable); what reviewers repeatedly flag.
- **Architecture**: layering and dependency direction, module layout, where seams belong, what must never be coupled, testing approach per layer.

Draft candidates from **patterns in how the code is written** (naming, error style, test shape), never from what the product does. Keep each candidate only once the user confirms it and gives its reason in their own words: a rule without a reason is the first to be misapplied. Run every confirmed rule through **What belongs** before writing it down.

The interview is done when every topic in the focus has been asked about once and every confirmed rule is either written or routed.

## Structure

```md
# Guidelines

## {Topic from the interview}

- **{Rule}**: {the reason it exists, and the case it does not cover}
```

## Rules

- **Portable only.** See What belongs.
- **Cache only what the agent cannot find by looking.** Skip anything already visible in configuration, scripts, or the directory layout.
- **One meaning, one place.** Link to architecture decision records and `GLOSSARY.md` instead of restating them.
- **Create lazily.** Write the file when the first rule is agreed, not as an empty scaffold.

## Auditing an existing file

When asked to check an existing `GUIDELINES.md`, run each rule through What belongs and propose a move for every rule that is not portable, splitting mixed rules. Move nothing without the user's approval.

## Declining

When the user declines, record `Guidelines: declined` under the Guidelines heading of `.agents/domain.md` (skip when that file does not exist), so later runs do not ask again. Writing a rule later removes the line.
