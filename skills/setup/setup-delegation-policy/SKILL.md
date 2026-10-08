---
name: setup-delegation-policy
description: "Install, reconfigure, or remove the delegation and model routing rule, and the tier agents it needs, for each agent harness on this machine. Use when the user asks to set up, change, or remove delegation or model routing."
---

# Setup delegation policy

Delegation pays off when it happens at the **top** of a unit of work, before any reasoning has bent the decision. A skill cannot hold that ground: it fires only when something reminds the agent to reach for it, and by then the reasoning has already started. A standing rule in an always-loaded steering file is carried on every turn instead, which is why the rule is installed rather than invoked.

[POLICY.md](POLICY.md) is that rule, written in tiers with model names only as examples, so it holds on any harness. The entire file is the payload, copied verbatim starting at its `## Delegation and model routing` heading.

No harness is assumed. For each one, find its steering file, its delegation mechanism, and its models from its own documentation and tools, because locations and schemas change between releases.

## Steps

### 1. Choose the harnesses and the action

Run `python3 -I scripts/detect-harnesses.py` (add `--json` for structured output). It lists the candidates found on disk, with no harness named in advance: each line gives the directory, the command on the path, the steering files, whether they already carry the delegation section (`policy=`), and the tier agents present. Directories holding only installed skills come back as one `skills-only` line. Add the harness you are running in if it is missing, show the user the list, and ask them to confirm it and add any harness it missed.

For each harness, report its state from the script and ask what to do, with a recommendation:

- **Configure** when nothing is installed.
- **Reconfigure** when something is, to re-sync the rule and rebind the tiers.
- **Remove** to delete what this skill installed.
- **Skip**.

Completion: every confirmed harness has an action.

### 2. Configure or reconfigure each harness

1. **Steering file.** Find the harness's global steering file, the always-loaded instructions it reads on every turn. A file that exists but is empty still counts. With no section headed `## Delegation and model routing`, append the payload after a blank line. With one, replace it in place, from its heading up to the next `##` heading or the end of the file, so re-syncing never leaves two copies. When the harness has no global steering file, ask whether to create it.
2. **Tier binding.** Inspect the harness's delegation tool. A per-call model override needs no tier files: the rule has the agent pass the tier's model at the call. A harness that binds the model to a named agent needs one agent per tier, because a tier with no agent named after it is a tier the rule cannot reach. Follow [TIER-AGENTS.md](TIER-AGENTS.md) to offer the user the models the harness actually has, and write the files. A harness with no delegation tool at all keeps the split-the-work half of the rule and has no routing.

Completion: each harness carries exactly one section identical to `POLICY.md`, and each tier it can bind has an agent or a per-call override.

### 3. Remove each harness

Delete the `## Delegation and model routing` section from its steering file, from its heading up to the next `##` heading or the end of the file, and leave the rest untouched. Then ask separately about the tier agent files, naming them. They are inert once the rule is gone, and a user who is re-syncing rather than leaving will want them kept.

### 4. Verify

- [ ] Each steering file written to has exactly one `## Delegation and model routing` heading (`grep -c` it), and none where the action was Remove.
- [ ] The installed section is identical to `POLICY.md`: extract it from each file and diff it against the source. A section that merely exists may be a stale copy.
- [ ] Each file still reads as the document it was: the section landed as a section, not inside a fenced block or mid-sentence.
- [ ] Where tier agents were written, the checks in [TIER-AGENTS.md](TIER-AGENTS.md) pass.

### 5. Report

Per harness, what was written, re-synced, removed, or skipped, and what the policy cannot know: how each tier binds (per-call override or named agent), the model each tier resolved to and its price when published, the checked versions of each chosen model family under `POLICY.md`'s model-version rule, any tier the harness cannot carry and the ceiling it has instead, and the harness's own bindings for its built-in agents. Those built-in bindings, and every other setting in the harness, are the user's: report them and leave them.

## Notes

- Steering files are read per turn, so nothing needs a restart.
- `POLICY.md` is the single source of truth. To change the rule, edit that file and run this skill again, rather than patching installed copies.
- Repository-scoped steering files stay untouched: this is a rule about how the agent works, not about any one codebase.
