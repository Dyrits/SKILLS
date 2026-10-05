Fork-created skill: it has no upstream equivalent. Commit `ed43af2` replaced the fork's earlier classifier routing skills with it, as a standing multi-harness delegation policy. The [provenance audit](../../research/2026-10-03-retained-skill-provenance.md) records the evidence.

## What it does

Installs one standing rule, "Delegation and model routing", into the global steering files on this machine, and gives harnesses that bind a model per agent one agent per tier. The rule tells an agent to decide at the top of a unit of work whether to do it here, hand it to one subagent, split it, or have a second agent review, and to pick the least expensive model that can do the bounded task reliably.

It is installed rather than invoked because a skill fires only after reasoning has begun, and by then the decision has bent toward the plan already forming. A rule in an always-loaded file is carried every turn.

## When to reach for it

Type `/setup-delegation-policy`, or an agent or another skill can reach for it. Because it edits files outside any one repository, its trigger is your explicit request, and `setup-ai-workspace` calls it only after you agree.

## What it changes

| File or setting | Effect |
| --- | --- |
| `~/.claude/CLAUDE.md`, `~/.config/opencode/AGENTS.md`, `~/.codex/AGENTS.md`, `~/.zcode/AGENTS.md`, `~/.gemini/GEMINI.md` | Each file that exists gets the policy section appended, or replaced in place so there is never a second copy |
| Tier agent files | Written for OpenCode, ZCode, and Gemini CLI, where the agent carries the model. Claude Code and Codex use a per-call model override instead |
| Repository `CLAUDE.md` and `AGENTS.md` | Untouched: this is a rule about how the agent works, not about one codebase |

The source of truth is [POLICY.md](../../../skills/setup/setup-delegation-policy/POLICY.md); [TIER-AGENTS.md](../../../skills/setup/setup-delegation-policy/TIER-AGENTS.md) holds the per-harness tier agents. To change the rule, edit `POLICY.md` and rerun the skill instead of patching installed copies.

## Common questions

**Does it create steering files I do not have?**

No. A harness with no global steering file is reported, and the skill asks before creating one.

**How do I keep the installed copies current?**

Rerun it. It replaces the section from its heading to the next `##` heading, and verifies each installed section against `POLICY.md` with a diff.

**Does it pin model versions?**

No. The policy names tiers, with model names only as examples, and tells the agent to use the latest available version of the chosen family at dispatch time.

**How do I remove it?**

Ask for uninstall. The section is removed from each file and the rest left alone. The skill asks separately about OpenCode tier agent files, since they are inert without the rule.

## It's working if

- Each steering file you wrote to has exactly one `## Delegation and model routing` heading.
- The installed section is identical to `POLICY.md`.
- The report says, per harness, which delegation tool it exposes and which model each tier resolved to.
- Agents state the tier and resolved model when they dispatch work.

## Where it fits

Run-once, machine-wide setup, rerun when `POLICY.md` changes. It sits beside [setup-ai-workspace](./setup-ai-workspace.md), which configures one repository and tells you to run this skill when the policy is missing, and [setup-ai-tooling](./setup-ai-tooling.md), which provisions tools. [guide](../productivity/guide.md) routes the rest.
