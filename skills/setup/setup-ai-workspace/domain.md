# Domain Documentation

How the workflow skills should consume this repository's domain documentation when exploring the codebase. The `document` skill knows where each document lives.

## Before exploring, read these

- **The glossary**, or, when the repository has several contexts, the glossary map and each context's glossary relevant to the topic.
- **The decision records** that touch the area you're about to work in, including context-scoped ones.

If any of these don't exist, **proceed silently**. Don't flag their absence; don't suggest creating them upfront. They are created lazily when terms or decisions actually get resolved.

Before updating project or capability documents, call the Skill tool with "document" for the shared document model. Read applicable project and capability requirements as constraints; surface conflicts rather than silently changing those obligations.

## Conventions

**The conventions file** holds the project's code conventions, domain-agnostic and portable to any project on the same stack. Read it before reviewing code or auditing architecture.

If it doesn't exist, the review and architecture skills offer to create it unless a `Conventions: declined` line below says otherwise.

Conventions: {present | declined}

## Use the glossary's vocabulary

When your output names a domain concept, such as a task title, refactor proposal, hypothesis, or test name, use the term as defined in the glossary. Don't drift to synonyms the glossary explicitly avoids.

If the concept you need isn't in the glossary yet, that's a signal: either you're inventing language the project doesn't use (reconsider) or there's a real gap (note it for `/delineate`).

## Flag decision record conflicts

If your output contradicts an existing decision record, surface it explicitly rather than silently overriding:

> _Contradicts decision record 0007 (event-sourced orders), but worth reopening because…_
