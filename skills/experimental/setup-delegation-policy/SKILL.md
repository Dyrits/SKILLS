---
name: setup-delegation-policy
description: Install the delegation and model routing rule into the global steering files on this machine, so every session decides where a task runs and on which model tier. Run once per machine, and again to re-sync after the rule changes.
disable-model-invocation: true
---

# Setup Delegation Policy

Delegation pays off when it happens at the **top** of a unit of work, before any reasoning has bent the decision. A skill cannot hold that ground: it fires only when something reminds the agent to reach for it, and by then the reasoning has already started. A standing rule in an always-loaded steering file is carried on every turn instead, which is the whole point of installing it rather than invoking it.

[POLICY.md](POLICY.md) is that rule, written in tiers with model names only as examples, so it holds on any harness.

## Steps

### 1. Read the policy

Read [POLICY.md](POLICY.md) in full. The entire file is the payload: it is copied verbatim, starting at its `## Delegation and model routing` heading.

### 2. Install it into every global steering file present

Check each of these and note which exist:

- `~/.claude/CLAUDE.md` (Claude Code)
- `~/.config/opencode/AGENTS.md` (OpenCode)
- `~/.codex/AGENTS.md` (Codex CLI)

OpenCode reads `~/.claude/CLAUDE.md` as a fallback, but only while it has no `AGENTS.md` of its own, so installing to both is what keeps it covered when that file appears later.

For each one that exists, install the policy:

- No `## Delegation and model routing` section yet: append the file's contents, separated by a blank line.
- A section with that heading already there: replace it in place, from its heading up to the next `##` heading or end of file. Re-syncing must never leave two copies.

Where a harness the user works in has no global steering file at all, say so and ask whether to create it rather than creating it unasked.

Report one line per file: written, re-synced, or absent.

### 3. Report how the tiers bind on this machine

The policy tells the agent to find its own lever at runtime, so do not restate it. Report instead what the policy cannot know, the configuration as it stands today:

- Which delegation tool this harness exposes, and whether it takes a per-call model override.
- Where models are bound per agent (OpenCode's `agent.*.model` in `~/.config/opencode/opencode.json`), which agents currently share one model, and whether a read-only agent such as `explore` or `plan` sits above Light.
- Where there is no delegation tool at all, that the routing half of the policy is inert and the split-the-work half still applies.

Leave every change to that configuration to the user.

### 4. Verify

- [ ] Each steering file written to carries exactly one `## Delegation and model routing` heading (`grep -c` it).
- [ ] The installed section is identical to `POLICY.md`: extract it from each file, from the heading to the next `##` or end of file, and diff it against the source. A section that merely exists may be a stale copy.
- [ ] Each of those files still reads as the document it was: the policy landed as a section, not inside a fenced block or mid-sentence.

## Removing it

When the user asks to uninstall, delete the `## Delegation and model routing` section from each of the files in step 2, from its heading up to the next `##` heading or end of file, and leave the rest of each file untouched. Verify with the same `grep -c`, expecting zero.

## Notes

- Nothing here needs a restart. Steering files are read per turn.
- `POLICY.md` is the single source of truth. Editing the rule means editing that file and re-running this skill, rather than hand-patching the installed copies.
- Repository-scoped `CLAUDE.md` and `AGENTS.md` files are deliberately untouched: this is a rule about how the agent works, not about any one codebase.
