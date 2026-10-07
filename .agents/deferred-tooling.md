# Deferred tooling decisions

These are follow-up candidates, not authorization to implement or install tooling.

## Classifier-based model routing

Status: deferred at the user's request.

Consider a script using classifier.dev to classify tasks and supported client mechanisms to enforce the selected model, replacing advisory delegation-policy instructions.

Before implementation, verify classification accuracy, cost, latency, failure behavior, credential handling, and what task content would leave the machine. Classification alone does not enforce routing.

Primary-source research found no model-selection field in the documented [Claude Code hook output schema](https://code.claude.com/docs/en/hooks). [Model configuration](https://code.claude.com/docs/en/model-config) supports `/model` and `claude --model`; a classifier-driven launcher is a possible approach, not an implemented solution. Recheck current client APIs when resuming.

See [classifier.dev documentation](https://classifier.dev/docs) for the classification service. Other clients' enforcement mechanisms remain unverified.

## Unified installation and updates

Status: investigate existing solutions before proposing a repository-specific CLI.

Desired scope: select, install, and update skills, MCP servers, and potentially other development tools, with repeatable noninteractive use as well as human selection.

Evaluate Microsoft's Agent Package Manager first:

- [Package installation](https://microsoft.github.io/apm/consumer/install-packages/): agent assets, manifests, and lockfiles.
- [MCP installation](https://microsoft.github.io/apm/consumer/install-mcp-servers/): registry and explicit server definitions with runtime-specific configuration.
- [CLI installation reference](https://microsoft.github.io/apm/reference/cli/install/): update and preview options.

Documentation review is not compatibility testing. Verify this repository's bucket layout, selective installation, update behavior, preservation of local edits, supported clients, and removal behavior. Identify gaps for native executables and language-server prerequisites before building a thin adapter or a new CLI.
