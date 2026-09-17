# Upkeep

Keep the codebase and issue list healthy; generates work for the flow.

## User-invoked

- **[improve-agent-environment](./improve-agent-environment/SKILL.md)**: Suggest improvements to the coding agent's environment (steering files, coding standards, automated checks, tooling) after a session. STUB: design notes only, not functional yet. (Not in the plugin.)

## Model-invoked

- **[triage](./triage/SKILL.md)**: Move incoming issues and PRs through a state machine of triage roles into agent-ready issues.
- **[debug](./debug/SKILL.md)**: Disciplined diagnosis loop for hard bugs and regressions: tight feedback loop → minimise → hypothesise → instrument → fix → regression-test.
- **[improve-codebase-architecture](./improve-codebase-architecture/SKILL.md)**: Scan for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick.
- **[resolve-merge-conflicts](./resolve-merge-conflicts/SKILL.md)**: Work an in-progress merge or rebase conflict hunk by hunk, resolving by intent traced to each side's primary source.
