## What it does

`takeover` is the other half of [handoff](./handoff.md): it resumes work from the newest document in `.agents/handoffs/`, treating that file as the brief for the session. The defining constraint is that it walks the history **lazily**: it reads the newest handoff, and follows the `supersedes` chain deeper only when the newest document leaves something unresolvable, instead of preloading the whole archive.

## When to reach for it

You invoke this by typing `/takeover`; the agent won't reach for it on its own. Reach for it at the start of a session that is meant to continue handed-off work: you point it at nothing, it finds the newest file itself. For writing a handoff rather than consuming one, use [handoff](./handoff.md).

## The loop it runs

Find the newest handoff by filename sort (the `YYYY-MM-DD-HHMM-<slug>.md` names sort chronologically), read it fully, resolve the artifacts it points at (specifications, plans, ADRs, issues, commits) by path or URL, call the skills its "suggested skills" section names, then confirm the brief back in two or three sentences before starting work. That confirmation is the cheap insurance: a stale or wrong handoff costs two sentences to catch here, an hour to discover mid-task.

The chain rule is the skill's leading idea: **newest first, deeper only on demand**. A handoff that can't be understood without its predecessor was a badly written handoff; the skill treats that as a recoverable defect rather than a reason to read everything.

## Common questions

**The newest handoff references a file that no longer exists.** Follow `supersedes` to the previous handoff for the context of what that file was, but resolve the gap against the primary sources (git log, the issue tracker) rather than the summary. The handoff is a secondary source; the repository is the truth.

**There are no handoffs in `.agents/handoffs/`.** The skill says so and asks for a path or a fresh brief rather than guessing. An empty directory means either the work was never handed off or the handoff was written elsewhere (an older version of `handoff` wrote to the OS temp directory).

## It's working if

- The fresh agent starts working instead of asking you to re-explain the setup.
- It read one handoff file, not five, to get there.
- Its two-sentence brief back to you matches what you thought you handed off.
- It called the suggested skills rather than improvising equivalents.

## Where it fits

`takeover` pairs with [handoff](./handoff.md) at the seam between sessions: `handoff` writes out, `takeover` reads back in. The pair covers the same-harness, same-directory resume that `/compact` cannot, because the context travels through a file rather than through the session. When you're at a phase boundary and unsure which of continue, clear, hand off, delegate or compact fits, [what-is-next](../getting-started/what-is-next.md) carries the tree that orders those five; `takeover` is what you type at the far side of the `/handoff` crossing.
