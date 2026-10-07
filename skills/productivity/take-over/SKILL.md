---
name: take-over
description: "Resume work from a handoff document in .agents/handoffs/ written by hand-off, following the supersedes chain only when questions stay open. Use when the user asks to take over, resume, or continue from a handoff."
argument-hint: "Optional: a handoff path, or what this session will focus on"
---

Resume work from a handoff written by `hand-off`. [HANDOFF-FORMAT.md](HANDOFF-FORMAT.md) is the contract between the two: read it first, so you know the sections, the thread rules, and what verified and assumed mean.

## Steps

1. **Pick the handoff.** If the user passed a path, use that file. Otherwise list `.agents/handoffs/` and take the newest by filename. If the arguments name a topic, take the newest handoff whose slug or title matches it instead. With neither a path nor a topic, check the second newest too: when the newest does not supersede it, the two are separate threads (a fork, or unrelated work), and either may be the one in flight. Name both in the brief and ask which one to resume.
2. **Read it fully** before doing anything else. Note each claim marked assumed, and each claim in State that is not marked at all: treat both as unverified.
3. **Resolve the Sources** by path or URL. They are the primary sources; the handoff summarizes them. Check every unverified claim you noted against them, and flag any claim a source contradicts.
4. **Follow the chain only if needed.** Read the superseded handoff **only** when the one you picked relies on something you cannot resolve from it and its sources (a decision whose reason is missing, a path that no longer exists). Go one link at a time. When a source is missing and the chain does not explain it, say so and ask the user; never rebuild it from the summary.
5. **Confirm the brief in two or three sentences** before starting: what was in flight, what you will do next, and any flagged claim, missing source, or missing section. This catches a stale or wrong handoff before it costs an hour.
6. **Start working.** Leave every handoff file untouched: a later state goes into a new handoff, written with `hand-off`.

If the user passed a focus, weigh it over the handoff's Next when the two differ, and say where they diverge.

If `.agents/handoffs/` is empty or missing, and the user gave no path, say so and ask for the handoff path or a fresh brief instead of guessing.
