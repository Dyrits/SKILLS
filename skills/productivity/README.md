# Productivity

Human-facing workflows you run, not about code. Skills sit flat in this folder; the groupings below are reading order, not directories.

## Sharpening

Understanding built or repaired in conversation.

### User-invoked

Reachable only when you type them (Claude Code: `disable-model-invocation: true`; Codex: `policy.allow_implicit_invocation: false` in `agents/openai.yaml`).

- **[grill-me](./grill-me/SKILL.md)**: Get relentlessly interviewed about a plan or design until every branch of the design tree is resolved.
- **[ask-someone-else](./ask-someone-else/SKILL.md)**: Turn a decision you can't answer alone into a Markdown questionnaire for the one person who can (filled in async, or together over a meeting).
- **[wait-what](./wait-what/SKILL.md)**: Fire this the moment a message doesn't land. The agent re-pitches it with the context you were missing, in your language, using your `CONTEXT.md` vocabulary.

## Transport

Work moving across session boundaries.

### User-invoked

- **[handoff](./handoff/SKILL.md)**: Compact the current conversation into a versioned handoff document in `.agents/handoffs/`.
- **[takeover](./takeover/SKILL.md)**: Resume work from the latest handoff in `.agents/handoffs/`, following the supersedes chain deeper only when needed.

## Ungrouped

### User-invoked

- **[teach](./teach/SKILL.md)**: Teach the user a new skill or concept over multiple sessions, using the current directory as a stateful teaching workspace.
