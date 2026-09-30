# Agent tooling candidates for code work

Checked 2026-09-30 against project repositories and primary documentation. These tools address different jobs; none guarantees lower overall plan usage or unchanged task quality.

## Serena: semantic code navigation and refactoring

Serena exposes symbol lookup, references, diagnostics, and symbol-aware edits through MCP, backed by local language servers by default. Its application is GPL-3.0-or-later; installation requires `uv`, with language-specific dependencies sometimes needed. Official client instructions cover Claude Code, Codex, OpenCode, Gemini CLI, and other MCP clients. Its evaluation records call counts and payload sizes, but is self-evaluated, not a token-savings benchmark or independent quality validation. Language support varies. Semantic references may omit comments and strings, so verify broad changes with text search and tests.

Sources: [README](https://github.com/oraios/serena), [client setup](https://oraios.github.io/serena/02-usage/030_clients.html), [language support](https://oraios.github.io/serena/01-about/020_programming-languages.html), [evaluation](https://oraios.github.io/serena/04-evaluation/000_evaluation-intro.html).

## Context7: current third-party library documentation

Context7 fetches source-linked documentation snippets, with library and version hints, to ground work against external APIs. It is hosted, not local. The free tier allows 1,000 calls per month; unauthenticated calls are rate-limited by IP and documented as testing-only, while real use requires an API key. Its CLI supports Codex, Claude Code, OpenCode, and other clients. I found no primary-source token or quality benchmark. Use for unfamiliar or fast-changing dependencies; confirm library/version and follow source links. It does not inspect the repository's own code.

Sources: [search API and free limit](https://context7.com/docs/search-api), [CLI and clients](https://github.com/upstash/context7/blob/master/packages/cli/README.md), [client setup](https://github.com/upstash/context7/blob/master/docs/resources/all-clients.mdx).

## jCodeMunch: indexed symbol retrieval, as a CodeGraph comparison

jCodeMunch indexes code locally with tree-sitter and retrieves exact symbols through MCP. It is free for personal use and documents Claude Code, Codex CLI, OpenCode, Gemini CLI, and other MCP clients. Its project-published benchmark reports a 96.5% mean retrieval-token reduction across 15 tasks and three pinned repositories against a grep-and-read baseline; a separate 50-run audit reports 80% versus 72% success on one naming-audit task. This is not a measurement of this user's subscription use. It overlaps substantially with CodeGraph, so compare them on representative tasks. Symbol retrieval may omit surrounding context; retain full-source reads for reviews. Optional anonymous savings sharing can be disabled.

Sources: [README and benchmarks](https://github.com/jgravelle/jcodemunch-mcp/blob/main/README.md), [client setup](https://github.com/jgravelle/jcodemunch-mcp/blob/main/CLIENTS.md), [savings methodology](https://github.com/jgravelle/jcodemunch-mcp/blob/main/TOKEN_SAVINGS.md).

## Smaller, task-specific additions

`ast-grep` adds structural search and code outlines when text search is too broad; no token-savings measurement was found in the supplied docs. Sources: [prompting](https://ast-grep.github.io/advanced/prompting), [outlines](https://ast-grep.github.io/guide/outline-code).

Microsoft's Playwright CLI offers focused browser snapshots and locator finding for web tasks. Its efficiency statement is not a measured local token result. Source: [repository](https://github.com/microsoft/playwright-cli).

For GitHub/GitLab work, `gh --json`/`--jq` and `glab api` with `jq` return selected fields instead of broad output. These are conditional CLI patterns, not new MCP services. Sources: [gh](https://cli.github.com/manual/gh_help_formatting), [glab](https://docs.gitlab.com/cli/api/).

## Practical order to evaluate

Try Context7 for dependency docs, and `ast-grep` or existing LSP for structural lookup. Trial Serena for cross-file symbol operations where clients lack equivalent LSP support. Treat jCodeMunch as a CodeGraph alternative. Use Playwright and tracker CLIs only for those tasks. Compare candidates on the same real tasks, retaining full source, raw diffs, and tests as quality checks. Reported context reduction is not total subscription savings.
