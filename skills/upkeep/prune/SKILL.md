---
name: prune
description: "Find and remove what a project no longer uses: dead code, unused files, exports, dependencies, assets, styles, scripts, and configuration, each removal backed by evidence and passing checks. Use when the user asks to clean up, find dead or unused code, or remove unused assets or dependencies."
---

# Prune

Remove what nothing in the project uses: source files, functions, classes, exports, dependencies, assets (images, fonts, media), styles, fixtures, scripts, configuration keys, and blocks of commented-out code.

Nothing is removed on the absence of a reference alone. Code reaches files and symbols through names built at run time, framework conventions, and callers outside the repository, and a search cannot see those. So each candidate gets a verdict with evidence, and each removal must leave the project's checks as they were.

The user may scope the run to a path, a package, or a kind (only dependencies, only assets). Otherwise, prune the whole repository.

## Prepare

1. Read `AGENTS.md` and the README for the commands that build, test, lint, and typecheck the project; confirm each in the build tool's scripts, a `Makefile`, or CI.
2. Run those checks once and record the result. A check that already fails is a **baseline failure**: it is not evidence against a removal, and it is listed in the report.
3. Run `git status`. A file with uncommitted changes is the user's work in progress: remove nothing from it, and list it in the report.
4. List the **entry points** (the places execution starts): the manifest's `main`, `bin`, `exports`, and scripts; HTML pages; Dockerfiles, CI, cron, and deployment configuration; and the folders a framework loads by convention (file-based routes, migrations, autoloaded modules, plugin registries).
5. Decide whether the project publishes a library. If it does, its public API is used by consumers you cannot see.

Completion: the check commands are listed with their baseline results, the entry points are listed, and the public API is identified or the project is stated to publish none.

## Find candidates

- **Code and dependencies**: run the ecosystem's tool from [tools.md](references/tools.md). Read its configuration first when the project has one; its ignore list records decisions already made.
- **Assets, styles, fixtures, scripts**, and code in an ecosystem without a tool: from the project root, run this skill's [find-unreferenced.py](scripts/find-unreferenced.py) on the folders that hold them. It prints each Git-tracked file whose name no other tracked text file mentions. Add `--stem` for source modules imported without an extension.

  ```sh
  python3 -I scripts/find-unreferenced.py [--stem] [--exclude GLOB]... PATH...
  ```

- **Configuration**: search the code for each environment variable, feature flag, and configuration key the configuration files define.
- **Commented-out code**: blocks of code turned into comments, as opposed to comments that explain.

With many packages, delegate one package per subagent when subagents are available; each returns its candidates with their verdicts and evidence.

Completion: every tool and folder in scope has been scanned, and its candidates are listed.

## Classify

Search the whole repository for each candidate's name and path, including configuration, markup, templates, CI, and documentation (`git grep -n -F <name>`). Then check the ways code reaches a thing without naming it:

| Reach | Examples |
| --- | --- |
| A name built at run time | Template-string imports, `require(variable)`, `import.meta.glob`, `getattr`, reflection, `"icon-" + name + ".svg"` |
| A convention or a folder | File-based routes, migrations, autoloading, decorators or annotations that register, dependency injection, files loaded by folder or glob, a folder a document links instead of its files |
| An entry point outside the code | The manifest, HTML `<script>` and `<link>`, CSS `url()`, Dockerfiles, CI, cron, serverless configuration |
| A caller outside the repository | A published library's public API, a served file requested by URL (favicon, `robots.txt`, `/.well-known/`, images in emails), another repository, a name stored in a database |

Give each candidate one verdict:

- **Used**: a reference exists. The tool was wrong; when the project configures the tool, add the candidate to its ignore list.
- **Unused**: no reference, and no reach in the table applies.
- **Uncertain**: a reach in the table could apply, the candidate is in the public API, or the evidence is outside the repository.

Code that only its own tests call is unused; remove it with those tests. Leave these alone whatever the evidence: generated files (report the generator instead), vendored third-party code, migrations, and license files.

Completion: every candidate has a verdict and its evidence: the empty search, the reference found, or the reach that applies.

## Ask

Ask the user about every uncertain candidate in one round. For each, state the evidence and a recommended answer, for example: "`public/og-legacy.png`: no reference in the repository, but it sits in the served folder and an old post may link it. Recommend: keep." With no user to answer (a subagent run), keep the uncertain candidates and return the questions with their recommendations.

Completion: every uncertain candidate is answered or returned as a question.

## Remove

Remove the unused candidates and those the user approved, in batches of one kind (dependencies, then files, then symbols), so a failing check points to a batch.

- Remove a dependency with the package manager's command, so the lockfile follows.
- With a symbol, remove the imports, tests, and fixtures that only served it.
- Correct or delete the lines of documentation and `AGENTS.md` that name what you removed.

After each batch, run the checks from Prepare:

- **All pass, apart from baseline failures**: stage the batch (`git add -A -- <paths>`). The staged state is the checkpoint.
- **A check fails that passed at baseline**: undo the batch with `git restore -- <paths>`, then retry it in halves until the failing item is found. Mark that item used, with the failing check as evidence, and remove the rest.

A removal can leave other things unused. Run the scan again after the last batch, and classify and remove what it adds, until a scan finds nothing new.

Make no commit unless the user asked for one; the staged changes are the result to review.

Completion: every unused and approved candidate is removed or marked used by a failing check, the checks match the baseline, and a final scan finds no new candidate.

## Report

- Each removed item with its evidence, grouped by kind, and `git diff --cached --stat`.
- Each kept item with its reason: used by a reference, a failing check, the user's answer, or an open question with its recommendation.
- The baseline failures, the files skipped for uncommitted changes, and the generators of generated files that hold unused code.
- The scan commands, so the user can rerun them.
