# Experimental AI tooling skills

Supersedes: [2026-09-30-2347-setup-ai-workspace-rename.md](./2026-09-30-2347-setup-ai-workspace-rename.md) for workspace, tooling, and publication state.
The earlier handoff remains the record of the workspace rename.

## User decisions and artifacts

The user wanted free tools for ticket refinement, implementation, review, tests, and AI tool creation, with reliable navigation and evidence of token reduction.
Preserving complete review and diagnostic evidence is required, especially with RTK filters.
The user already uses CodeGraph automation, Context7 MCP, and a usage monitor, and reported that automatic handoffs did not prevent allowance interruptions.
The user chose separate setup and reporting skills and explicitly placed both in `experimental`.

- [setup-ai-tooling](../../../skills/experimental/setup-ai-tooling/SKILL.md) owns installation, client integrations, verification, a project baseline, and session recovery coverage.
- [monitor-ai-tooling](../../../skills/experimental/monitor-ai-tooling/SKILL.md) reads existing local measurements and produces reports without changing configuration.
- [Tool candidates research](../../../documentation/research/2026-09-30-agent-tooling-candidates.md) captures primary sources and comparisons.
- [Workspace setup](../../../skills/getting-started/setup-ai-workspace/SKILL.md) offers the same tooling procedure as an optional stage when the separately installed experimental skill is available.

Reference files, invocation metadata, and evaluation fixtures live beside each skill.
The accompanying commit records router, documentation, bucket listing, and experimental definition updates.
Both skills are excluded from the plugin and promoted listings and have no human documentation pages.
Both local skill directories link to their experimental paths.
No candidate tools were installed or indexed during this session.

## Verification and limits

Placement, manifest exclusions, documentation removals, relative links, evaluation JSON, invocation YAML, local symlinks, plugin version consistency, and `git diff --check` passed.
`claude plugin validate . --strict` passed for the marketplace manifest.
The earlier direct plugin-manifest check reported the existing root `CLAUDE.md` warning, documented in the superseded handoff.

Light-tier `gpt-6-luna` runners produced a behavioral smoke comparison across four fixture cases and 19 assertions.
Both with-skill and baseline outputs passed every assertion, so the comparison showed no improvement over baseline.
Each configuration had one observed output per case, with no reliable token or timing data.
An initial runner saw assertions accidentally and was replaced with a fresh prompt-only runner before grading.
Temporary artifacts are under `/private/tmp/ai-tooling-skill-evals/iteration-1/`, with a viewer at `/private/tmp/ai-tooling-skill-evals/review.html`.
Those artifacts may disappear; the committed fixtures preserve the scenarios.
These checks establish neither real installation quality nor personal token savings.

## Git state and next session

Work is on `main` in `/Users/dgerrits/Codelab/Dyrits/SKILLS`, tracking `origin/main`.
The user explicitly requested this handoff, a commit, and a normal push.
Handoff history is shared and tracked.
This document precedes the commit and push; confirm their final state with `git status --short --branch` and `git log -1 --oneline`.
The research artifact excluded from the previous rename commit belongs to this tooling work and is included now.
The user specified no further implementation task.
If asked to continue evaluation, start with an actual project and its existing integrations, then check raw diffs, diagnostics, exit status, and attribution before making savings claims.

## Suggested skills

- Call the Skill tool with `writing-for-agents` when changing skill instructions and `unslop` when writing repository prose.
- Call the Skill tool with `skill-creator` when extending the skills or their evaluations.
- Use `setup-ai-tooling` only within an explicit setup request or a selected workspace tooling stage.
- `monitor-ai-tooling` and `hand-off` are user-invoked; the human invokes them when needed.
