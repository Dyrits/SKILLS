---
name: hand-off
description: Write the current session's work into a versioned handoff document in .agents/handoffs/ that another agent resumes with take-over. Use when the user asks for a handoff, or to write up where the work stands for another session, agent, or person.
metadata:
  forks: "mattpocock/skills/skills/productivity/handoff"
argument-hint: "What will the next session be used for?"
---

Write a handoff document so a fresh agent, in any harness, can continue the work. [HANDOFF-FORMAT.md](HANDOFF-FORMAT.md) is the contract with `take-over`: read it first and follow it exactly.

## Steps

1. **Settle local or shared.** The repository already answers it when `.agents/handoffs/` is listed in `.gitignore` (local-only), earlier handoffs are tracked (shared), or an AGENTS.md note says so; follow that without asking. Otherwise ask once: add `.agents/handoffs/` to `.gitignore` for local-only history, or commit handoffs for shared history. Record the answer in an AGENTS.md note.
2. **Place it in its thread.** List `.agents/handoffs/`. If this session continues a thread that already has a handoff (the one it was resumed from, or an earlier one it wrote), supersede the newest handoff of that thread. A side task forked off the current work starts a thread forked from it. Anything else starts a new thread.
3. **Write a new file** with the template's sections, in order, under its headings. Before marking a claim in State as verified, check it now (read the file, run the command); otherwise mark it assumed. If the user passed arguments, they describe the next session's focus: write Goal and Next for that focus.
4. **Check the file against the format**: every section present and in order, the supersedes line names a file that exists, nothing copied that a source already records, nothing secret.
5. **Print the full path** and tell the user to start the next session with it, for example "take over from `<path>`".
