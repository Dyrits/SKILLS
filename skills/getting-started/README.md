# Getting Started

Set up once, then find your way around.

- **[setup-custom-skills](./setup-custom-skills/SKILL.md)**: Configure this repository for the workflow skills (issue tracker: local markdown or remote, ticket-writing convention, triage roles, domain documentation layout). Run once per repository. (User-invoked, ships in the plugin.)
- **[what-is-next](./what-is-next/SKILL.md)**: The router: which skill or flow fits your situation, or which boundary option (continue, clear, hand-off, compact) fits the moment. (User-invoked, ships in the plugin.)
- **[setup-git-hooks](./setup-git-hooks/SKILL.md)**: Set up versioned git hooks via core.hooksPath (no Husky) with lint-staged, Biome/Prettier, typecheck, and build. (User-invoked, not in the plugin.)
- **[setup-git-guardrails](./setup-git-guardrails/SKILL.md)**: Block dangerous git commands across Claude Code, OpenCode, and Codex before they execute, even in auto-approve mode. (User-invoked, not in the plugin.)
- **[setup-auto-handoff](./setup-auto-handoff/SKILL.md)**: Set up a Claude Code PreCompact hook that blocks compaction until a fresh handoff exists in `.agents/handoffs/`. (User-invoked, not in the plugin.)
