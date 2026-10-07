Upstream source: `handoff`, verified in the `d81f3a1` tree. This fork adds durable versioned session handoffs, and folded its former reading skill, `take-over`, into the handoff itself.

## What it does

`hand-off` writes the work of the session you are in into a **handoff document**: one markdown file, written to `.agents/handoffs/` in the workspace as a versioned, timestamped file, and points to it from `AGENTS.md`. The file is self-contained: it says how to resume from it, so the next agent needs no skill installed, only the file.

What it buys is **portability**, not compression. That makes the skill narrower than it sounds. You need a file only when the work has to *travel*: to a new harness, a new directory, a colleague, or a side task you want to fork off. If nothing is travelling, you do not need a handoff: staying in the session, `/clear`, a subagent and `/compact` cover the ordinary end-of-phase case, and `/compact` covers it more often than this skill does.

## When to reach for it

You usually invoke this by typing `/hand-off`. Pass a note about what the next session is for, and the document is written for it. An agent or another skill can also reach for it when you ask in plain words for a write-up another session can pick up.

Four situations are the whole trigger when you choose:

| Situation | Why a file |
| --- | --- |
| Swapping harness (Claude → Codex) | The new harness cannot see the old context |
| Moving to a different directory or repository | A prototype directory is the common case |
| Sending the work to a colleague | They need something they can read |
| Forking a side task found mid-phase | You keep working; a second agent takes the fork |

Staying in the same workspace does not automatically call for compaction. Continue when context remains useful; clear only when authoritative sources preserve the next task; compact when you need the same session with less conversation. [guide](./guide.md) helps choose the boundary.

## Branching is the use people skip

The skill's description reads like session resumption: write a summary, end here, resume there. Read that way it looks like a worse `/compact`, so it gets skimmed past. The fork case is the one worth knowing. You **stay in your session** and hand a copy of the accumulated context to a second agent working in parallel.

That is what the detour through [prototype](../shaping/prototype.md) uses. You are deep in a design conversation, you hit a question that only running code will settle, and you do not want to spend the thread you built on finding out. Hand off to a prototype session, get the answer, hand the answer back, and reference it from the original thread. Two crossings, one live conversation, nothing re-explained.

These choices preserve different things. Compaction compresses conversational context. Clearing removes that context, but should leave authoritative work state intact. A handoff makes session-specific context portable.

## What travels, and what doesn't

Every handoff follows one fixed format, `HANDOFF-FORMAT.md`. A header names the handoff it supersedes and the workspace, then a fixed "To resume" paragraph tells the reader how to use the file (read it whole, check unverified claims against the sources, follow earlier handoffs only when needed, confirm before starting, never edit it). Six sections follow in a fixed order: Goal, State, Decisions, Next, Open questions, Sources. Each claim in State is marked verified (and how) or assumed, so the next agent knows what it can build on. Secrets are redacted before it's written.

The format names no skills to call next. The next session may run in another harness with a different skill set, so the handoff describes the work and leaves the tooling to whoever picks it up.

What it deliberately does not carry is anything already written down. Specifications, plans, ADRs, issues, commits and diffs are referenced by path or URL, never copied. That keeps the file small, and it keeps the settled detail in one place instead of two that drift.

## Common questions

**Handoff or compact?**
Use compact to reduce conversational detail within the same session. Use a handoff when another session, agent, or workspace needs the brief. The handoff's advantage is a portable file, not a claim that it summarizes better.

**So what's the actual difference between compact, clear and handoff?**
- Compact compresses context within the same session.
- Clear discards conversational context. Preserve necessary work state first.
- Hand off writes a portable brief for another session.

Summaries are secondary sources. Keep pointers to the requirements, specifications, decisions, and evidence they summarize.

**Where did my handoff file go?**
`.agents/handoffs/YYYY-MM-DD-HHMM-<slug>.md` in the workspace: same place every time, sorted by name gives you the newest first, and nothing depends on per-OS temp paths. The skill prints the full path when it writes; keep it before you move on.

**My handoff vanished between sessions.**
It doesn't: the file lives in the workspace, survives reboots, and every handoff is kept, never overwritten, so you have a history of the work's transit documents (each names the one it supersedes). Two caveats. If `.agents/handoffs/` is gitignored it is still local-only: a clone or a colleague's machine won't have it, so commit the directory if the handoff needs to travel that far. And the same durability rule applies to anything the document *points at*: don't leave referenced artifacts in temp.

**How do I actually hand it to the next agent?**
Usually you don't need to: the line in `AGENTS.md` points the next session at the current handoff of each thread in flight. To be explicit, open the fresh session and point it at the path: read this file, then continue. Point at the file rather than pasting the summary into a shell command: a summary containing backticks or `$(...)` gets mangled when it's interpolated into `claude "<summary>"`, and the usual failure is silent truncation rather than an error, so the new agent starts with a quietly incomplete brief.

**Is this the same as `/branch`, `--fork-session`, or the built-in `/hand-off`?**
Analogous, not identical, and `/branch` isn't a shipped skill here; `/hand-off` is the canonical name. A fork inherits an exact copy of the context; this skill produces a *targeted* compression aimed at a stated next task, in a file. Where a fork will do (same machine, same harness, same directory), a fork is less work. The file wins the moment the destination is somewhere the fork can't go.

**Why does it write to `AGENTS.md`?**
So the next session finds the handoff without being told. It keeps one line per thread in flight, replaces that line with each new handoff, and removes it when a handoff records the goal as done. When handoffs are local-only, the line says so, since a clone will not have the file.

**When does something belong in `AGENTS.md` instead?**
Ask whether it's true next month. `AGENTS.md` is standing context about the project, loaded into every session whether it's relevant or not. A handoff is about one piece of work in flight and is dead once that work lands. Facts that keep getting re-explained are an `AGENTS.md` problem; a half-finished task is a handoff.

**It captures the what, not the why.**
A repeated criticism, and the reason the format has a Decisions section that carries each decision with its reason. State what the next session is for so the relevant reasoning survives. Confident claims the session never checked, such as "X isn't built" or "Y is done", must be marked assumed; the "To resume" paragraph tells the next agent to check those against the sources before building on them.

**What about a side task I fork off?**
It starts its own thread: its supersedes line reads `none (forked from <file>)`, so the original thread's handoff stays the head of its own line. Each live thread has its own line in `AGENTS.md`, so the next session sees both and asks which one to resume unless you name it.

**Does work-in-progress replace a handoff?**

No. `documentation/work-in-progress.md` owns unfinished current work, blockers, and recovery state. The handoff carries session-specific reasoning and pointers for another agent. Keep them consistent without copying the same task history into both.

**Why is it a skill rather than a slash command?**
Both work; they suit different situations. As a skill it ships and updates through the same install path as everything else here, which is what makes it shareable. Agents can reach it when you ask in plain words; typing `/hand-off` works the same as before.

**Will it ask me about git every time?**
No. It asks once, and only when the repository does not already answer. A `.gitignore` entry for `.agents/handoffs/` means local-only history, tracked earlier handoffs mean shared history, and an `AGENTS.md` note settles it either way; the skill follows whichever it finds.

## It's working if

- The document is a small fraction of the conversation, and the specifications, issues and diffs appear in it as paths and URLs rather than as copied text.
- You can read it cold, without the original session open, and know what to do next.
- The fresh agent starts working instead of asking you to re-explain the setup.
- In the fork case, your original session is still sitting there untouched when you come back to it.
- Every section of the format is there, and each claim in State says whether it was verified.
- `AGENTS.md` has exactly one line for this thread, naming the newest handoff.
- Nothing in it is a key, a token, or a password.

## Where it fits

`hand-off` is a reach-for-it-anytime standalone between sessions, not a development chain step. An approved [prototype](../shaping/prototype.md) in another session can use a handoff for the question and return evidence, but isolation is not a universal prototype requirement. [guide](./guide.md) helps choose the session boundary.
