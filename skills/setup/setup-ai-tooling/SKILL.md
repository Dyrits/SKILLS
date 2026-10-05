---
name: setup-ai-tooling
description: "Set up free AI development tools for a project and its installed agent clients. Use when explicitly asked to install or configure AI tooling, or when workspace setup includes an approved tooling stage."
---

# Setup AI tooling

Provision **tooling**, with complete review evidence and a measurable baseline.
Run installation and configuration only within an explicit tooling setup request, including a tooling stage the user selected during workspace setup.
Call the Skill tool with "write-for-agents" when changing agent instructions.

**Calls:** `write-for-agents`. If a called skill is not installed, tell the user its name and install command, `npx skills@latest add Dyrits/SKILLS --skill=<name>`, then carry out that step from its stated intent and report the step as done without the skill. **Hands over to:** `/monitor-ai-tooling`. When one is not installed, give the user its install command, `npx skills@latest add Dyrits/SKILLS --skill=<name>`, along with the instruction to run it.

## Process

### 1. Inspect

Inspect the project languages, existing Makefile or package scripts, instruction files, tool versions, and installed agent clients.
Check existing project and global integrations before proposing changes: a binary, a project index, and a connected agent are separate states.
Inspect only relevant configuration sections and report credentials by presence, never value.
Read [TOOLS.md](TOOLS.md) for the tools relevant to this project; verify their current commands against the installed version's help and official documentation.
Support Claude Code, Codex, OpenCode, and other detected clients through their documented adapters; record each client's actual coverage.
Done when every candidate has a suitability decision, an existing-state assessment, and a supported integration path or a stated gap.

### 2. Select the changes

Recommend CodeGraph for supported source projects, existing language servers, and Context7 for dependency documentation.
Reuse working integrations, including Context7 MCP, and existing project automation.
Offer ast-grep when a representative structural search adds value; for browser work, choose between Playwright CLI and Chrome DevTools MCP by the task in [TOOLS.md](TOOLS.md); offer tracker CLIs for the project's tracker.
Keep Serena optional when CodeGraph and native language support already cover navigation.
Use free tools and free service tiers; treat account requirements and quotas as setup constraints.

Present the concrete project changes, global changes, protected commands, and verification commands together.
Ask only for decisions or permissions the request has not already settled, including new account access or a tool that requires payment for this user's use.
An explicit request for project and missing global setup covers routine installation and configuration within that scope.
Done when the selected set and scope are settled; existing working tools need no replacement.

### 3. Configure and verify

Install missing dependencies through the available package manager and supported client adapters.
Merge settings and hooks; preserve unrelated configuration and make reruns idempotent.
Use existing Makefile targets where suitable; initialize a CodeGraph index only when missing, then refresh and verify a known symbol against its source.
Check a representative structural search against a known match before enabling ast-grep guidance.
Verify Context7 with a small lookup for an actual dependency and version, without registering a duplicate server.

Keep original patches, source reads, search results used as evidence, and diagnostic output available to the agent.
For RTK, follow the protected-command checks in [TOOLS.md](TOOLS.md) before enabling automatic rewrites.
Complete diffs and failure output are required for review and diagnosis; an archived original that the agent never reads does not satisfy this requirement.
Leave an unverified adapter or filter disabled and describe the gap.
Done when each configured client has a functional check, protected output and exit status survive the actual adapter, and rerunning setup preserves existing configuration.

### 4. Record the baseline and recovery path

Write the project record at `.agents/ai-tooling.md` with:

- Project root, setup time, selected tools and versions, project/global scope, and integration status per client.
- Source documentation, verification commands and results, known gaps, protected commands, and raw-output bypasses.
- Local measurement sources, their schema/version, time range and project attribution, baseline counter values, and retention limits.
- Representative read-only tasks with correctness criteria, command duration, and output bytes where measured; leave unavailable values unknown.
- A verified session recovery method per client, including transcript location or resume command and any existing checkpoint mechanism.

Reuse local tool tracking and the user's existing monitor; collect counters through deterministic commands or existing hooks without recurring model calls.
Keep measurement history and diagnostic artifacts local and excluded from version control; commit the configuration record only after removing credentials and personal session paths.
For CodeGraph, record measured lookup behavior; mark personal token savings unavailable unless a comparable task baseline exists.
Check persisted-session recovery using a harmless existing session where possible.
Distinguish context compaction from exhausted plan allowance: recovery must work without requiring a new model-generated handoff after allowance exhaustion.
Done when the record points to real measurement sources, counters are scoped honestly, and each client's recovery coverage is verified or explicitly unavailable.

### 5. Finish

Summarize configured tools, reused integrations, disabled filters, global changes, and verification gaps.
Tell the user to run `/monitor-ai-tooling` later for an on-demand report.
Report command-output reduction, task token counts, and provider allowance as different quantities; claim equivalent task quality only where the comparison checked the same correctness criteria.
