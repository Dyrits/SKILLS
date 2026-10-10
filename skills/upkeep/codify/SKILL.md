---
name: codify
description: Define the project's code conventions by drafting candidate rules from how the code is already written and confirming each with the user and its reason, or audit an existing conventions file. Use when the user wants to write down or check how code is written here, or when a review or architecture audit finds no conventions.
---

# Codify

Turn how the team writes code into project-agnostic rules a reviewer can apply to any diff, each with the reason it exists.

## Offer

When the user asked directly to create or write conventions, skip the offer and run the interview below.

When it came up during other work (a review or an audit that found no conventions), ask whether to create the conventions now. On yes, run the interview below; on no, return to that work. Nothing is recorded, so a later run asks again. With no user to ask, as when running as a subagent, return without asking and report that the conventions are missing.

## Interview

Pick a focus: **code** (review, setup) or **architecture** (audit); default to **code**. Follow the [interview method](references/interview.md), asking about the focus's topics in rounds, each question with a recommended answer drawn from what the code already does consistently. Skip a topic the user has no rule for.

- **Code**: naming (files, functions, booleans, abbreviations); function and file size, and when to extract; types (strictness, `any` or its equivalent, nullability); error handling (throw or return, where errors are caught, what gets logged); state and side effects (mutation, purity, where input and output happen); comments and documentation; tests (what gets one, naming, fakes versus mocks, one behaviour per test); dependencies (when a new library is acceptable); what reviewers repeatedly flag.
- **Architecture**: layering and dependency direction, module layout, where seams belong, what must never be coupled, testing approach per layer.

Draft candidates from **patterns in how the code is written** (naming, error style, test shape), never from what the product does. When the code is inconsistent, show both patterns and ask which is the rule. Keep each candidate only once the user confirms it and gives its reason in their own words: a rule without a reason is the first to be misapplied. Write each confirmed rule to the conventions file following [conventions-format.md](references/conventions-format.md), or route it to the home its What belongs table names, and tell the user where each went. The paths and creation rules for those homes are in [project-documents.md](references/project-documents.md); write a requirement following [requirements-format.md](references/requirements-format.md), a decision record following [decision-record-format.md](references/decision-record-format.md), a term following [glossary-format.md](references/glossary-format.md), and an `AGENTS.md` line following [agent-instructions.md](references/agent-instructions.md).

Completion: every topic in the focus has been asked about once, and every confirmed rule is either written with its reason or routed, with the user told where it went.

## Audit

When asked to check existing conventions, check the conventions file as [conventions-format.md](references/conventions-format.md) describes under Checking an existing file, then present each proposed move to the user. Move nothing without the user's approval.

Completion: the user has seen every proposed move and approved or declined each.
