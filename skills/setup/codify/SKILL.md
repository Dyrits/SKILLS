---
name: codify
description: Define the project's code conventions by drafting candidate rules from how the code is already written and confirming each with the user and its reason, or audit an existing conventions file. Use when the user wants to write down or check how code is written here, or when a review or architecture audit finds no conventions.
---

# Codify

Turn how the team writes code into project-agnostic rules a reviewer can apply to any diff, each with the reason it exists.

**Calls:** `document`, `interview`.

## Offer

When the user asked directly to create or write conventions, skip the offer and run the interview below.

When a calling skill raised it, ask whether to create the conventions now. On yes, run the interview below; on no, return to the caller. Nothing is recorded, so a later run asks again. With no user to ask, as when running as a subagent, return without asking and tell the caller the conventions are missing.

## Interview

The caller passes a focus: **code** (review, setup) or **architecture** (audit); default to **code**. Call the Skill tool with "interview", asking about the focus's topics in rounds, each question with a recommended answer drawn from what the code already does consistently. Skip a topic the user has no rule for.

- **Code**: naming (files, functions, booleans, abbreviations); function and file size, and when to extract; types (strictness, `any` or its equivalent, nullability); error handling (throw or return, where errors are caught, what gets logged); state and side effects (mutation, purity, where input and output happen); comments and documentation; tests (what gets one, naming, fakes versus mocks, one behaviour per test); dependencies (when a new library is acceptable); what reviewers repeatedly flag.
- **Architecture**: layering and dependency direction, module layout, where seams belong, what must never be coupled, testing approach per layer.

Draft candidates from **patterns in how the code is written** (naming, error style, test shape), never from what the product does. When the code is inconsistent, show both patterns and ask which is the rule. Keep each candidate only once the user confirms it and gives its reason in their own words: a rule without a reason is the first to be misapplied. Hand each confirmed rule to the conventions by calling the Skill tool with "document"; it files the rule or routes it to its home, and you tell the user where each went.

Completion: every topic in the focus has been asked about once, and every confirmed rule is either written with its reason or routed, with the user told where it went.

## Audit

When asked to check existing conventions, call the Skill tool with "document" to check the conventions file, then present each move it proposes to the user. Move nothing without the user's approval.

Completion: the user has seen every proposed move and approved or declined each.
