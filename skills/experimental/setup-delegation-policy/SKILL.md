---
name: setup-delegation-policy
description: Install the delegation and model routing rule into the global steering files on this machine.
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
- `~/.zcode/AGENTS.md` (ZCode)
- `~/.gemini/GEMINI.md` (Gemini CLI)

Each harness reads its own file, and a file that exists but is empty still counts as present. OpenCode reads `~/.claude/CLAUDE.md` as a fallback, but only while it has no `AGENTS.md` of its own, so installing to both is what keeps it covered when that file appears later. ZCode is documented as not reading `CLAUDE.md` at runtime at all, so it has no fallback to rely on.

For each one that exists, install the policy:

- No `## Delegation and model routing` section yet: append the file's contents, separated by a blank line.
- A section with that heading already there: replace it in place, from its heading up to the next `##` heading or end of file. Re-syncing must never leave two copies.

Where a harness the user works in has no global steering file at all, say so and ask whether to create it rather than creating it unasked.

Report one line per file: written, re-synced, or absent.

### 3. Give each binding harness an agent per tier

Some harnesses bind a model per named agent instead of taking a model on the delegation call, and there the tier **is** the agent: a tier with no agent named after it is a tier the policy cannot reach, so installing the rule alone installs something unfollowable. OpenCode, ZCode and Gemini CLI all work this way. Claude Code needs none of it, because its per-call `model` override outranks any agent definition, and Codex has no delegation tool to point at.

For each such harness present, follow [TIER-AGENTS.md](TIER-AGENTS.md) and write one agent file per tier. Only OpenCode's ladder is chosen live, by reading the catalogue and asking: it carries several providers and rotates. ZCode's and Gemini's are pre-defined there, so writing them is the whole job.

### 4. Report how the tiers bind on this machine

The policy tells the agent to find its own lever at runtime, so do not restate it. Report instead what the policy cannot know, the configuration as it stands today:

- Which delegation tool each harness exposes, and whether it takes a per-call model override.
- Which model each tier resolved to, and what that tier costs per million tokens.
- Any tier a harness cannot carry, named, with what its ceiling is instead.
- What `agent.*.model` in `~/.config/opencode/opencode.json` binds the built-in agents to: which of them share one model, whether a read-only agent such as `explore` sits above Light, and whether the default primary agent `build` is bound at all or left on the top-level `model`.
- Where there is no delegation tool at all, that the routing half of the policy is inert and the split-the-work half still applies.

The tier agents from step 3, and any model aliases they depend on, are this skill's to write. Everything else in that configuration is the user's, so report it and leave it.

### 5. Verify

- [ ] Each steering file written to carries exactly one `## Delegation and model routing` heading (`grep -c` it).
- [ ] The installed section is identical to `POLICY.md`: extract it from each file, from the heading to the next `##` or end of file, and diff it against the source. A section that merely exists may be a stale copy.
- [ ] Each of those files still reads as the document it was: the policy landed as a section, not inside a fenced block or mid-sentence.
- [ ] Where step 3 ran, its own checks pass.

## Removing it

When the user asks to uninstall, delete the `## Delegation and model routing` section from each of the files in step 2, from its heading up to the next `##` heading or end of file, and leave the rest of each file untouched. Verify with the same `grep -c`, expecting zero.

Ask separately about the OpenCode tier agents, naming the files. They are inert once the rule is gone, and a user who is re-syncing rather than leaving will want them kept.

## Notes

- Nothing here needs a restart. Steering files are read per turn.
- `POLICY.md` is the single source of truth. Editing the rule means editing that file and re-running this skill, rather than hand-patching the installed copies.
- Repository-scoped `CLAUDE.md` and `AGENTS.md` files are deliberately untouched: this is a rule about how the agent works, not about any one codebase.
