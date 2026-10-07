---
name: codify
description: Define the project's code conventions by drafting candidate rules from how the code is already written and confirming each with the user and its reason, or audit an existing conventions file. Use when the user wants to write down or check how code is written here, or when a review or architecture audit finds no conventions.
---

# Codify

Turn how the team writes code into portable rules a reviewer can apply to any diff, each with the reason it exists.

**Calls:** `document`, `interview`.

Call the Skill tool with "document" first: its conventions format says what belongs in the file, where every other kind of rule goes, and the file's structure. Apply it to every candidate below.

## Offer

When the user asked directly to create or write conventions, skip the offer and run the interview below; a request overrides an earlier `Conventions: declined` in `.agents/domain.md`.

When a calling skill raised it, check `.agents/domain.md` first. If it records `Conventions: declined`, return to the caller without asking. Otherwise ask whether to create the conventions now. On yes, run the interview below; on no, record the decline (see Declining) and return.

## Interview

The caller passes a focus: **code** (review, setup) or **architecture** (audit); default to **code**. Call the Skill tool with "interview", asking about the focus's topics in rounds, each question with a recommended answer drawn from what the code already does consistently. Skip a topic the user has no rule for.

- **Code**: naming (files, functions, booleans, abbreviations); function and file size, and when to extract; types (strictness, `any` or its equivalent, nullability); error handling (throw or return, where errors are caught, what gets logged); state and side effects (mutation, purity, where input and output happen); comments and documentation; tests (what gets one, naming, fakes versus mocks, one behaviour per test); dependencies (when a new library is acceptable); what reviewers repeatedly flag.
- **Architecture**: layering and dependency direction, module layout, where seams belong, what must never be coupled, testing approach per layer.

Draft candidates from **patterns in how the code is written** (naming, error style, test shape), never from what the product does. When the code is inconsistent, show both patterns and ask which is the rule. Keep each candidate only once the user confirms it and gives its reason in their own words: a rule without a reason is the first to be misapplied. Write each confirmed rule through "document", or route it to its home when it does not belong in the conventions.

Completion: every topic in the focus has been asked about once, and every confirmed rule is either written with its reason or routed, with the user told where it went.

## Audit

When asked to check existing conventions, apply the copy test to the whole file (would every rule hold in another project on the same stack, with an unrelated domain?), check each rule against what belongs, and propose a move for every rule that is not portable, splitting mixed rules. Move nothing without the user's approval.

Completion: every rule is confirmed as portable or has a proposed move.

## Declining

When the user declines, record `Conventions: declined` under the Conventions heading of `.agents/domain.md` (skip when that file does not exist), so later runs do not ask again. Writing a rule later removes the line.
