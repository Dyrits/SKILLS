---
name: hand-off
description: Write the current session's work into a versioned, self-contained handoff document in .agents/handoffs/ and point to it from AGENTS.md, so another session, agent, or person can resume it. Use when the user asks for a handoff, or to write up where the work stands for another session, agent, or person.
metadata:
  forks: "mattpocock/skills/skills/productivity/handoff"
argument-hint: "What will the next session be used for?"
---

Write a handoff document so a fresh agent, in any harness and with no skill installed, can continue the work. Read [HANDOFF-FORMAT.md](HANDOFF-FORMAT.md) first and follow it exactly.

## Steps

1. **Settle local or shared.** The repository already answers it when `.agents/handoffs/` is listed in `.gitignore` (local-only), earlier handoffs are tracked (shared), or an `AGENTS.md` note says so; follow that without asking. Otherwise ask once: add `.agents/handoffs/` to `.gitignore` for local-only history, or commit handoffs for shared history.
2. **Place it in its thread.** List `.agents/handoffs/`. If this session continues a thread that already has a handoff (the one it was resumed from, or an earlier one it wrote), supersede the newest handoff of that thread. A side task forked off the current work starts a thread forked from it. Anything else starts a new thread.
3. **Write a new file** with the template's sections, in order, under its headings, including the "To resume" paragraph. Before marking a claim in State as verified, check it now (read the file, run the command); otherwise mark it assumed. If the user passed arguments, they describe the next session's focus: write Goal and Next for that focus.
4. **Update the pointer** in the nearest `AGENTS.md`, following the format's Pointer section: replace this thread's line, or add one, saying whether handoffs are shared or local. Create `AGENTS.md` with that line if none exists.
5. **Check both files against the format**: every section present and in order, the "To resume" paragraph intact, the supersedes line names a file that exists, nothing copied that a source already records, nothing secret, and exactly one `AGENTS.md` line for this thread naming the new file.
6. **Print the full path**, and tell the user the next session finds it through `AGENTS.md`, or can be pointed at the path directly.
