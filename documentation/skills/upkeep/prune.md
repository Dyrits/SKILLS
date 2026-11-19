Fork-specific skill with no upstream equivalent. The other skills add and refactor code, but none looks for code, files, or dependencies that nothing uses any more.

## What it does

`prune` finds what a project no longer uses and removes it: source files, functions, classes, exports, dependencies, assets such as images and fonts, styles, fixtures, scripts, configuration keys, and blocks of commented-out code. It runs the ecosystem's own detector where one exists (knip, vulture, deptry, `deadcode`, `cargo machete`) and a bundled script that lists every tracked file whose name no other file mentions, which is the only check for assets.

Its defining constraint is that a missing reference is not enough to delete something. Code reaches files and symbols in ways a search cannot see, so every candidate gets one of three verdicts before anything is removed:

| Verdict | Means | What happens |
| --- | --- | --- |
| Used | A reference exists, and the detector was wrong | Kept. If the project configures the detector, the candidate goes on its ignore list |
| Unused | No reference, and no hidden way to reach it applies | Removed |
| Uncertain | A name built at run time, a framework convention, a published API, or a caller outside the repository could reach it | You decide, with the evidence and a recommendation |

Every removal must leave the project's build, tests, lint, and typecheck where they were before the run.

## When to reach for it

Type `/prune`, or an agent can reach for it when the task fits: you ask to clean up a project, find dead code, or remove unused assets or dependencies. You can scope a run to a folder, a package, or one kind ("only the dependencies").

It works only on local files. It runs detectors without adding them to the project, and asks before installing a tool on the machine. It makes no commit unless you ask for one: the result is a set of staged changes for you to review.

| The situation | The move |
| --- | --- |
| Old components, images, or packages nobody uses | `prune` |
| The code works but its structure makes change hard | [improve-codebase-architecture](./improve-codebase-architecture.md) |
| A diff needs review and supported refactors | [review-and-refactor](../workflow/review-and-refactor.md) |
| The documentation describes code that is gone | [re-document](./re-document.md) |

## How removals stay safe

- Before it touches anything, it runs the project's checks once. A check that already failed is recorded as a baseline failure and never blamed on a removal.
- It leaves alone any file with uncommitted changes, plus generated files, vendored code, migrations, and license files.
- It removes in batches of one kind and stages each batch that passes. When a check breaks, it restores that batch, splits it in halves until it finds the item the check needed, and keeps that item.
- A removal can leave other code unused, so it scans again until a scan finds nothing new.

## Common questions

**Why did it ask about a file that nothing references?**
Something outside the search may reach it: a file in the served folder that an email or another site links, a module a framework loads by folder, or an export of a library other projects install. It asks with the evidence and a recommendation rather than guessing.

**Will it remove a function that only its tests call?**
Yes, together with those tests. Code whose only caller is its own test is still unused.

**Does it install knip or vulture into my project?**
No. It runs them through `npx`, `uvx`, or `go run` and leaves the manifest alone. A tool that needs a machine install, such as `cargo machete`, waits for your approval.

**Why doesn't it use the detector's automatic fix?**
`knip --fix` and similar options delete everything they flag at once. The skill removes items by hand so each removal has its own verdict and evidence.

**What happens to documentation that mentions removed code?**
It corrects or deletes the lines in the documentation and `AGENTS.md` that name what it removed.

## It's working if

- Every removed item in the report comes with its evidence: the empty search, or the detector's finding confirmed by one.
- The build, tests, lint, and typecheck give the same results after the run as before.
- Nothing uncertain disappears without your answer.
- The changes are staged, not committed, unless you asked for a commit.
- Running the reported scan commands again finds nothing new.

## Where it fits

`prune` is periodic maintenance: run it after a feature is retired, before a release, or when a codebase has grown for a while without cleanup. It reads the check commands and entry points from the project itself and from `AGENTS.md`, and writes nothing but the removals and the documentation lines they make stale.
