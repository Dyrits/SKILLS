# Merge project setup into one skill that drives upstream command-line tools

Status: accepted.

This supersedes two points of [0005: Make skills autonomous](./0005-make-skills-autonomous.md): the `setup-ai-workspace` and `codify` bullets under Skill boundaries, and the setup half of "Tooling is separate from skill orchestration". The rest of 0005 stands, including the deferred installer and the retirement of `setup-delegation-policy`, which this record leaves untouched.

## Context

Setting up a repository took four skills (`setup-ai-workspace`, `setup-git-hooks`, `setup-git-guardrails`, `setup-ai-tooling`) that people ran together, once, at the start. 0005 planned to fold hooks and guardrails into `codify`, but `codify` writes conventions and keeps auditing them, while hooks and guardrails are installed once.

Most of the tokens a setup run spent went on things a command-line tool already does: reading prose about each tool, fetching documentation to rediscover install commands, reading full install output, and hand-merging settings the tool's own installer writes. `setup-git-hooks` also added a dependency (lint-staged) that a repository already running Biome or oxc does not need.

## Decisions

- **One `setup` skill** replaces `setup-ai-workspace`, `setup-git-hooks`, `setup-git-guardrails`, and `setup-ai-tooling`. It inspects the repository, offers four areas (workspace, code checks, Git guardrails, AI tooling) with their current state, and runs the ones the user picks. Each area is a bundled reference file read only when picked.
- **An empty repository** gets the areas that do not depend on a stack. `setup` asks which language and framework the project uses but does not decide them: choosing a stack belongs to `architect`. Code checks wait until a stack exists.
- **Upstream command-line tools do the installing.** The skill carries a dated catalogue: for each tool, how to detect it, its non-interactive install command, and one check that it works. The agent reads documentation only when a listed command fails. Install output goes to a log file; the agent reads the exit status and the log's tail, and the whole log only on failure. No repository-specific installer or menu program is built; scripts are bundled only where no upstream tool covers the job (project inspection, harness detection, the Git guard).
- **Code checks use the project's own tools, with no lint-staged.** A pre-commit hook in a committed `.githooks/` directory runs the formatter and linter the repository already has (Biome, oxlint, oxfmt, or a language's own toolchain) on staged files, then a typecheck. A repository on older tooling (ESLint, Prettier) is offered a move to Biome or oxc through their migration commands, never moved without agreement.
- **Conventions documentation feeds the configuration.** `setup` reads the project's conventions (found through `AGENTS.md`, or in contribution guides and editor configuration) and applies their tool rules (indentation, quotes, line width, lint rules) to the configuration it writes. It asks when a documented rule and an existing configuration disagree, and reports a missing conventions document without creating one.
- **The catalogue stays current through repository maintenance**, not through research on every run: each entry records when it was last verified, and refreshing it is upkeep work here.
- **`codify` moves to `upkeep/`.** It keeps conventions and their audit; enforcement through hooks belongs to `setup`.
- **`setup-delegation-policy` stays separate.** It writes only machine-wide steering files, and a skill named for one repository should not edit the home directory.

## Considered options

- **Folding hooks and guardrails into `codify`, as 0005 planned**: rejected. It mixes a recurring conversation about conventions with a one-time installation.
- **A repository-specific installer with a menu and flags**: rejected for now. It adds code to maintain without touching where setup tokens went, and 0005 already asks to evaluate existing installers first.
- **Keeping four skills and adding a router**: rejected. A router adds a fifth description to keep loaded while the four still run together.

## Consequences

One description has to trigger for every area, so it names each one ("pre-commit hooks", "guard destructive Git commands"), and the skill accepts a single area when asked for only one. The catalogue goes stale as tools release; an entry past its verification date is a maintenance signal, not a reason to research during setup. Token savings from the catalogue and quiet output are expected but not measured.
