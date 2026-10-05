Fork-specific companion to `hand-off`, first added as `takeover` in commit `f85ffd7` for resuming durable session handoffs and renamed `take-over` in `b9e7f0a`. The [provenance audit](../../research/2026-10-03-retained-skill-provenance.md) records the first-add and rename evidence.

## What it does

`take-over` is the other half of [hand-off](./hand-off.md). It resumes work from the newest document in `.agents/handoffs/`, reading history lazily: it follows the `supersedes` chain only when the newest handoff leaves a question unresolved. It resolves source pointers and flags assumptions before confirming the brief.

## When to reach for it

Type `/take-over`, or an agent or another skill can reach for it when the task fits. Reach for it at the start of a session continuing handed-off work. It finds the newest file itself. For writing a handoff rather than consuming one, use [hand-off](./hand-off.md).

## The loop it runs

Find the newest handoff by filename sort (the `YYYY-MM-DD-HHMM-<slug>.md` names sort chronologically), read it fully, and resolve the artifacts it points at by path or URL. Check current names before using suggested skills. Confirm the brief in two or three sentences before starting work, so stale context is caught before implementation.

The chain rule is the skill's leading idea: **newest first, deeper only on demand**. A handoff that can't be understood without its predecessor was a badly written handoff; the skill treats that as a recoverable defect rather than a reason to read everything.

## Common questions

**The newest handoff references a file that no longer exists.** Follow `supersedes` to the previous handoff for the context of what that file was, but resolve the gap against the primary sources (git log, the issue tracker) rather than the summary. The handoff is a secondary source; the repository is the truth.

**There are no handoffs in `.agents/handoffs/`.** The skill says so and asks for a path or a fresh brief rather than guessing. An empty directory means either the work was never handed off or the handoff was written elsewhere.

## It's working if

- The fresh agent starts working instead of asking you to re-explain the setup.
- It read one handoff file, not five, to get there.
- Its two-sentence brief back to you matches what you thought you handed off.
- It used suggested skills by their current names and left any step only a human can perform to the human.

## Where it fits

`take-over` is a reach-for-it-anytime standalone paired with [hand-off](./hand-off.md) between sessions. It restores session-specific context while project documents remain authoritative for requirements, agreements, and unfinished work. [guide](./guide.md) helps you choose whether to continue, clear, hand off, or compact; use this skill after the handoff.
