# Productivity

Human-facing workflows you run, not about code. Skills sit flat in this folder; the groupings below are reading order, not directories.

## Sharpening

Understanding built or repaired in conversation.

### User-invoked

Reachable only when you type them (Claude Code: `disable-model-invocation: true`; Codex: `policy.allow_implicit_invocation: false` in `agents/openai.yaml`).

- **[ask-someone-else](./ask-someone-else/SKILL.md)**: Turn a decision you can't answer alone into a Markdown questionnaire for the one person who can (filled in async, or together over a meeting).
- **[re-explain](./re-explain/SKILL.md)**: Fire this the moment a message does not land. The agent explains it again with missing context, in your language, using your `GLOSSARY.md` vocabulary.

### Model-invoked

- **[illustrate](./illustrate/SKILL.md)**: Explain the current topic with the smallest useful diagram, code sketch, or focused HTML artifact.

## Transport

Work moving across session boundaries.

### User-invoked

- **[hand-off](./hand-off/SKILL.md)**: Compact the current conversation into a versioned handoff document in `.agents/handoffs/`.
- **[take-over](./take-over/SKILL.md)**: Resume work from the latest handoff in `.agents/handoffs/`, following the supersedes chain deeper only when needed.

## Procedures

Recurring routines and one-off procedures, designed, improved, or walked through.

### User-invoked

- **[design-workflow](./design-workflow/SKILL.md)**: Turn recurring work loops into implementable workflow specifications.

### Model-invoked

- **[optimize-process](./optimize-process/SKILL.md)**: Map and improve a recurring process, including agent work and human review in practical impact estimates.
- **[walk-through](./walk-through/SKILL.md)**: Generate a guided script (a wizard) for steps only a human can perform.

## Outbound

Results leaving the session for other people or services.

### User-invoked

- **[publish-message](./publish-message/SKILL.md)**: Publish established conclusions to any connected service, adapted to its conventions, after approval of exact text and destination.

### Model-invoked

- **[classify](./classify/SKILL.md)**: Classify safe-to-send text with classifier.dev and retain uncertain results for review.

## Ungrouped

### User-invoked

- **[teach](./teach/SKILL.md)**: Teach the user a new skill or concept over multiple sessions, using the current directory as a stateful teaching workspace.
