Fork-created skill: it has no upstream equivalent. Commit `ed43af2` replaced the fork's earlier classifier routing skills with it, as a standing multi-harness delegation policy. The [provenance audit](../../research/2026-10-03-retained-skill-provenance.md) records the evidence.

## What it does

Installs one standing rule, "Delegation and model routing", into the global steering file of each agent harness on this machine, and gives harnesses that bind a model per agent one agent per tier. The rule tells an agent to decide at the top of a unit of work whether to do it here, hand it to one subagent, split it, or have a second agent review, and to pick the least expensive model that can do the bounded task reliably.

It is installed rather than invoked because a skill fires only after reasoning has begun, and by then the decision has bent toward the plan already forming. A rule in an always-loaded file is carried every turn.

No harness is built in. A bundled script, `detect-harnesses.py`, lists the harnesses it finds on disk (directories holding a steering file or agents, with the command on the path and whether the policy is already installed), with no harness named in advance. The skill asks you to confirm the list, and then asks per harness whether to configure, reconfigure, remove, or skip. It reads each harness's own documentation for its steering file, its agent format, and its model list.

## When to reach for it

Type `/setup-delegation-policy`, or an agent can reach for it. Because it edits files outside any one repository, its trigger is your explicit request.

## What it changes

| File or setting | Effect |
| --- | --- |
| Each chosen harness's global steering file | Gets the policy section appended, or replaced in place so there is never a second copy |
| Tier agent files | Written only for harnesses where the agent carries the model, using models you pick from that harness's own list. A harness with a per-call model override needs none |
| Repository `AGENTS.md` | Untouched: this is a rule about how the agent works, not about one codebase |

The source of truth is [POLICY.md](../../../skills/setup/setup-delegation-policy/POLICY.md); [TIER-AGENTS.md](../../../skills/setup/setup-delegation-policy/TIER-AGENTS.md) holds the procedure for tier agents. To change the rule, edit `POLICY.md` and rerun the skill instead of patching installed copies.

## Common questions

**Does it create steering files I do not have?**

No. A harness with no global steering file is reported, and the skill asks before creating one.

**Who chooses the models?**

You do. For a harness that binds a model per agent, the skill reads the harness's model list, shows each option with its price when published, recommends one per tier, and writes your choice. Subscription-covered models are recommended over free-listed ones, which can disappear without warning.

**How do I keep the installed copies current?**

Rerun it and choose Reconfigure. It replaces the section from its heading to the next `##` heading, and verifies each installed section against `POLICY.md` with a diff.

**Does it pin model versions?**

No. The policy names tiers, with model names only as examples, and tells the agent to use the latest available version of the chosen family at dispatch time.

**How do I remove it?**

Choose Remove for the harness. The section is removed from its steering file and the rest left alone. The skill asks separately about the tier agent files, since they are inert without the rule.

## It's working if

- Each steering file you wrote to has exactly one `## Delegation and model routing` heading.
- The installed section is identical to `POLICY.md`.
- The report says, per harness, how each tier binds and which model each tier resolved to.
- Agents state the tier and resolved model when they dispatch work.

## Where it fits

Run-once, machine-wide setup, rerun when `POLICY.md` changes. It sits beside [setup-ai-workspace](./setup-ai-workspace.md), which configures one repository, and [setup-ai-tooling](./setup-ai-tooling.md), which provisions tools.
