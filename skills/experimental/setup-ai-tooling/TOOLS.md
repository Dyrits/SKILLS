# Tool branches

Use the installed version's help to resolve command and adapter differences.
Follow the official source for installation; a documented client adapter must be verified in that client before it is recorded as connected.

## CodeGraph

[Official setup and tools](https://github.com/colbymchenry/codegraph) describe agent wiring, project indexing, synchronization, and source retrieval.
Check the existing `codegraph` executable or project runner, `.codegraph/`, and each client's MCP connection independently.
An existing Makefile target such as this is a starting point, not a reason to reinstall working integrations:

```makefile
codegraph:
	npx --package=@colbymchenry/codegraph codegraph install --yes
	npx --package=@colbymchenry/codegraph codegraph init
	npx --package=@colbymchenry/codegraph codegraph sync
```

Preview client configuration with `codegraph install --print-config <client>` when supported.
Use `init` for a missing project graph and `sync` for an existing graph; inspect the installed help before adapting the target.
Verify `status` and a known symbol through `explore`, then check that the retrieved source matches the current file.
Keep a conditional initialization step in repeated project automation so an existing graph is preserved.
Use source reads when dynamic dispatch, unsupported languages, or stale indexing leave gaps.
Published benchmark percentages are external evidence, not this project's measured savings.

## RTK

[Official configuration](https://github.com/rtk-ai/rtk/blob/develop/docs/guide/getting-started/configuration.md) documents adapters, exclusions, bypasses, and recovery storage.
[Savings methodology](https://github.com/rtk-ai/rtk/blob/develop/docs/guide/resources/savings-explained.md) explains its output-byte measurements and token estimates.
Verify the binary is Rust Token Killer using its version and `gain` command; another project shares the executable name.
Preview `init` with the installed version's dry-run mode before merging configuration.

Protect Git patches and source evidence through adapter exclusions, including `git diff`, `git show`, file reads, structural/text searches, and the project's test/build/diagnostic commands.
For versions supporting `[hooks].exclude_commands`, merge exclusions into the existing list rather than replacing it.
Include actual invocation variants, such as `git -C`, package-manager wrappers, and project scripts, in the checks.
A textual exclusion alone is insufficient: verify the installed adapter's rewritten command and output on a large patch with context, a rename, and a deliberately failing command with distinctive stderr and a nonzero exit status.
Compare against the original command and preserve its exit status.
Use the documented `RTK_DISABLED=1` or `rtk proxy` bypass only after verifying that it works for that adapter and version.
When an adapter cannot enforce protection, use explicit RTK commands for selected summaries and leave broad rewriting disabled.
Remove or narrow pre-existing guidance that prefixes every command with RTK if the user authorized changing that integration.

Recovery storage is a convenience with size and retention limits; preserve complete diagnostic evidence independently when those limits can apply.
Verify the raw diagnostic output is read before a failure conclusion.
Keep RTK tracking enabled where supported and record the local analytics source and scope.
Do not replace the user's Token Monitor or infer actual remaining plan allowance from RTK's quota estimate.

## Context7

[Official client setup](https://github.com/upstash/context7) and [service limits](https://context7.com/docs/search-api) describe supported access.
Reuse an existing MCP connection or CLI integration and verify one dependency-specific, version-matched query.
For a missing connection, use the free tier through the documented client adapter; leave account creation or key entry to the user when needed.
Record free-tier constraints and store credentials through the client's normal secret mechanism.
Retrieved documentation should retain its source links and relevant version.

## Language support and structural search

Reuse working language servers through the client's native integration where available.
Verify a known definition or reference and a harmless diagnostic using the project's language configuration.
[ast-grep patterns](https://ast-grep.github.io/guide/pattern-syntax) match syntax with metavariables; this adds structural searches that symbol navigation alone does not answer.
Recommend it when a real query needs a particular call shape, argument structure, or enclosing node.
Use search mode and check a known positive and negative example; code rewrites require a separate implementation request.
[Serena](https://github.com/oraios/serena) is an optional language-server adapter for capabilities missing from the existing client and CodeGraph setup.
Choose it for an identified gap, rather than installing a second navigation layer by default.

## Task-specific clients

Browser tooling follows the task; offer a browser client only when a real task needs one.
Static pages, documentation, and plain HTTP need no browser: the client's built-in fetch and search or `curl` cover them.
Reuse a working browser integration, including one already connected, before adding another.

[Microsoft Playwright CLI](https://github.com/microsoft/playwright-cli) is the default for *driving* pages: navigation, forms, logins, client-rendered content, focused snapshots, locator discovery, screenshots, and traces.
It runs headless across Chromium, Firefox, and WebKit, and as a CLI it adds no tool schema to the agent's context.
Preserve the project's test framework and inspect real page state before choosing locators.

[Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) is the choice for *diagnosing* a page: console messages, network requests, performance traces, and Core Web Vitals.
It is Chrome only, and its MCP tool definitions add context load.
Attaching it to a running browser exposes that session's profile, so confirm the scope with the user first.

Install one when the work is one kind and both only when the project has both kinds; verify with a read-only page load that returns a snapshot or trace.

[GitHub CLI formatting](https://cli.github.com/manual/gh_help_formatting) and [GitLab API commands](https://docs.gitlab.com/cli/api/) support precise tracker retrieval.
For ticket refinement and review, fetch complete relevant bodies, discussions, and pages while selecting away unrelated response metadata.
Verify tracker access with a read-only operation; tooling setup publishes no tracker messages.
