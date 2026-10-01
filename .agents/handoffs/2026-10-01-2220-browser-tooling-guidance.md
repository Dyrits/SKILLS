# Browser tooling guidance in setup-ai-tooling

Supersedes: nothing. It extends [2026-10-01-0056-experimental-ai-tooling.md](./2026-10-01-0056-experimental-ai-tooling.md), which remains the record of the two experimental tooling skills.

## What happened

The user asked whether Claude needs Playwright to navigate webpages, then whether to prefer Playwright or Chrome DevTools MCP, then asked for both experimental tooling skills to be updated where relevant.

Conclusions reached:

- Reading static pages, documentation, or plain HTTP needs no browser; built-in fetch and search or `curl` suffice.
- Playwright CLI is the default for driving pages (forms, logins, client-rendered content, snapshots, locators, traces) and adds no tool schema to context.
- Chrome DevTools MCP is for diagnosing a page (console, network, performance traces, Core Web Vitals). It is Chrome only, adds context load, and exposes the profile when attached to a running browser.

## Changes

- [setup-ai-tooling/SKILL.md](../../skills/experimental/setup-ai-tooling/SKILL.md): step 2 now routes browser work by task through `TOOLS.md` instead of offering Playwright CLI alone.
- [setup-ai-tooling/TOOLS.md](../../skills/experimental/setup-ai-tooling/TOOLS.md): the "Task-specific clients" section holds the decision rule, the reuse-first rule, and a read-only verification.
- `monitor-ai-tooling` is unchanged: its measurement and report files are tool-agnostic and already cover every configured tool.

See the commit diff for exact wording.

## Open items

- The `setup-ai-tooling` evaluation (`evals/evals.json`) was not rerun. Its fixture says no browser task is identified, so it should still pass, but that is unverified.
- No eval case exercises the new browser choice. Add one if the rule needs regression coverage.
- Both skills are experimental: no plugin entry, no documentation page, no `what-is-next` change.

## Suggested skills

- `writing-for-agents` when editing either `SKILL.md` or `TOOLS.md`.
- `skill-creator` to run or extend the evaluations.
