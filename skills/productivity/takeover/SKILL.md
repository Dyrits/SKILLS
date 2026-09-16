---
name: takeover
description: Resume work from the latest handoff document in .agents/handoffs/, following the supersedes chain deeper only when the newest document leaves questions open.
argument-hint: "Optional: a note on what this session will focus on"
disable-model-invocation: true
---

Resume work from the last handoff document written by the `handoff` skill.

## Steps

1. **Find the latest handoff**: list `.agents/handoffs/`, sort by filename (the `YYYY-MM-DD-HHMM-<slug>.md` names sort chronologically), take the newest.
2. **Read it fully** before doing anything else. It is the contract for this session: the next agent treats its claims as fact, so while reading, flag anything stated as fact that was only an assumption.
3. **Follow the chain only if needed**: each handoff names the one it supersedes. Read earlier handoffs **only** when the newest one references something you can't resolve (a decision whose reasoning isn't there, a path that no longer exists, a "supersedes" question).
4. **Resolve referenced artifacts**: open the specs, plans, ADRs, issues, commits and diffs the document points at, by path or URL. They are the primary sources; the handoff is a summary of them.
5. **Call the suggested skills**: the document has a "suggested skills" section naming what to reach for. Use the Skill tool for those rather than improvising.
6. **Confirm the brief back to the user in two or three sentences** before starting: what was in flight, what you'll do next. This catches stale or wrong handoffs before they cost an hour.
7. **Start working.** Leave the handoff files untouched: if this session reaches a new phase boundary, the user runs `handoff` again, which writes a new versioned file.

If the user passed arguments, treat them as this session's focus and weigh them over the handoff's "what's next" when the two differ, telling the user where they diverge.

If `.agents/handoffs/` is empty or missing, say so and ask the user for the handoff path or a fresh brief instead of guessing.
