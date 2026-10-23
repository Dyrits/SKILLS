# Code checks

A pre-commit hook in a committed `.githooks/` directory runs the project's formatter and linter on staged files, then its typecheck. Reuse the tools the repository already has, and add a dependency only for a job nothing covers. No lint-staged or similar runner: each tool reads staged files itself or takes them as arguments.

The tools, their commands, and their migrations are in one catalogue per language, read only for the languages the inspection found: [JavaScript and TypeScript](checks-javascript.md), [Python](checks-python.md), [Go](checks-go.md), [Rust](checks-rust.md). For another language, use its toolchain's own formatter and linter, looked up in its documentation, and say in the report that it had no catalogue.

## Steps

### 1. Choose the tools

Work from the inspection's `languages`, `configs`, `packages`, and `package_scripts` lines, the conventions' tool rules, and each language's catalogue:

- **A catalogue tool is present**: use it and install nothing.
- **Older tooling**: offer the catalogue's move, never make it unasked. Name what the move would drop, from the migration preview. When the user declines, wire the existing tools into the hook.
- **Nothing present**: recommend the catalogue's default.
- **A hook manager is present (Husky, lefthook, the pre-commit framework, lint-staged)**: ask whether to replace it with `.githooks/` or to add the checks to it. When kept, add the commands there and skip step 3.
- **Style**: carry each conventions rule a tool can hold (indentation, line width, quotes, import order, banned constructs) into its configuration. When a documented rule disagrees with an existing configuration, ask which wins. With neither, ask, offering the catalogue's style defaults.
- **Build**: offer to run the build in the hook as well; recommend against it, since it slows every commit.

Completion: each staged language has one formatter and one linter, or none by the user's choice, and the typecheck command is chosen where the language has one.

### 2. Install and configure

Install only the missing tools, as quiet commands. Write a tool's configuration only when none exists, from its own init command where it has one, then apply the style choices. Run an accepted migration, run the new check on the whole repository, and remove the old tools and configuration only after that check passes and the user agrees.

When the conventions document names a tool this area replaced, update that line; when there is no conventions document, say so in the report and create none.

Completion: each chosen tool runs once on the whole repository with exit 0, or its findings are reported to the user.

### 3. Write the hook

Write `.githooks/pre-commit` from this frame, with each language's hook lines from its catalogue, and make it executable:

```sh
#!/bin/sh
# Checks staged files, then typechecks. Written by setup; edit freely.
set -eu
has_staged() { ! git diff --cached --quiet --diff-filter=ACMR -- "$@"; }
staged() { git diff --cached --name-only -z --diff-filter=ACMR -- "$@"; }

# One block per language, from its catalogue.
```

The hook checks and never writes, so a partly staged file is never rewritten behind the committer's back; they run the formatter and stage again.

Move any hook already in `.git/hooks/` into `.githooks/`, then run `git config core.hooksPath .githooks`. Make clones get it too, as the catalogue says for the project's package manager.

Completion: `git config core.hooksPath` prints `.githooks`, and the hook is executable.

### 4. Verify and commit

Run `.githooks/pre-commit` with nothing staged and expect exit 0. Then stage a deliberately misformatted scratch file in a checked language, run the hook and expect a failure naming it, and unstage and delete the file.

Commit only the files this area wrote: `.githooks/`, tool configuration, and the manifest and lockfile it changed. Ask first when the branch is the default branch and other changes are uncommitted. The commit runs through the new hook.

Completion: the hook passed clean, failed on the scratch file, and the commit went through it.

## Notes

- `core.hooksPath` replaces `.git/hooks/` entirely; hooks left there stop running.
- For parallel steps or per-file-type runners, lefthook is the next step up.
