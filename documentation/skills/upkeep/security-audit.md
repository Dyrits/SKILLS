Source: the `security-audit` skill from Cloudflare's [security-audit-skill](https://github.com/cloudflare/security-audit-skill) project (MIT), imported at upstream commit `c1c8a8c1471069fb0e188eeaff69b8e8db6564a8`. It does not come from the upstream fork. The import changes only the layout and wording: companion documents moved to lowercase names under `references/`, the validators and schema moved to `scripts/`, and em-dashes and the `repo` abbreviation were rewritten to the repository's language rules. One behavior differs: upstream saves runs outside the audited repository (`~/security-audit-skill/<repo-name>/run-<N>`), while this copy saves them in `documentation/security-audit/`, like the architecture audit reports, ignored by Git by default. The rest of the methodology is unchanged, so a later upstream sync can diff against that commit.

## What it does

`security-audit` looks for vulnerabilities that cross a real trust boundary and gives owners the source evidence, a safe reproduction, a priority, and the smallest effective fix. It reports a vulnerability only when an agent other than the one that found it has checked it against the source.

It runs in two modes:

| Mode | When | What it produces |
| --- | --- | --- |
| Guidance | Security questions, focused reviews, triage of a specific finding | An answer in the conversation, with no files written |
| Full audit | An explicit codebase audit or pen-test request, a comprehensive review, or a request for report artifacts | Six phases and a run directory of reports |

A full audit maps the architecture and a coverage ledger, sends isolated hunters over the ledger units, gives every candidate to a fresh verifier who tries to disprove it, writes `findings.json`, has fresh agents verify the final records, and derives `REPORT.md`, `FINDINGS-DETAIL.md`, and `NEEDS-VALIDATION.md` from them.

## When to reach for it

Type `/security-audit`, or ask for a security audit, a vulnerability hunt, or a pen test of the code; an agent reaches it the same way. When a request could mean either mode, it asks one question before creating files.

| Your situation | Skill |
| --- | --- |
| Audit a whole codebase, or answer a security question about it | This one |
| Diagnose a known bug or a regression | [debug](./debug.md) |
| Find structural refactoring opportunities | [improve-codebase-architecture](./improve-codebase-architecture.md) |

## Prerequisites

- An agent harness that can run parallel subagents.
- Node.js for the two zero-dependency validators in `scripts/`.
- To execute target code (builds, tests, fuzzers), an OS-enforced sandbox with no external network, an allowlisted environment, resource limits, and writes confined to scratch directories. Without one, the skill keeps every lead that would need execution as `needs_validation` and gives a safe validation plan instead.

## Verdicts and coverage

Every record in `findings.json` carries one of three verdicts, and `scripts/validate-findings.cjs` rejects a record that mixes them:

| Verdict | Means | Severity |
| --- | --- | --- |
| `confirmed` | A complete source trace and a bounded observed result | Required, never above the demonstrated impact |
| `needs_validation` | A source-grounded lead blocked on one exact unresolved fact, such as deployment configuration absent from the repository | None |
| `rejected` | A verifier disproved the candidate | None |

The coverage ledger (`coverage-ledger.json`, checked by `scripts/validate-coverage-ledger.cjs`) records what each unit covered, deferred, or left out of scope. Runs against the same repository are additive: a later run reads earlier ledgers and findings, revalidates changed source, and targets the gaps. The `quick`, `standard`, and `deep` profiles and an optional agent budget trade breadth for cost without lowering the evidence bar.

## Common questions

**Where do the reports go?**

In `documentation/security-audit/run-<N>/`, one directory per run, beside the [architecture audit](./improve-codebase-architecture.md) reports. When the skill creates the directory, it adds a line to `AGENTS.md` and an entry to `.gitignore`, because findings describe vulnerabilities that may not be fixed yet. To commit runs, say so; the skill leaves the ignore rule out after you confirm. An existing home named in `AGENTS.md`, or a directory you name, takes precedence.

**Can the audited code read earlier findings?**

No. Every source copy and sandbox view of the repository leaves the audit directory out, so code run during an audit never sees earlier results.

**Will it run my code or contact my services?**

It never probes deployed endpoints, shared infrastructure, or paid APIs, and it never installs dependencies. It runs target code only inside a sandbox that meets every listed control; otherwise it reads source only.

**Is one run enough?**

No. Upstream reports that a single run found roughly half of what repeated runs found in total, and the final coverage statement never claims the target is exhausted.

**Why is a missing security header not a finding?**

A finding needs a named lower-trust principal, a crossed boundary, and a concrete result. A missing best practice with no reachable boundary violation, or a second defense behind one that already holds, is reported as a hardening note.

## It's working if

- A guidance-mode question gets an answer without a run directory appearing.
- A full audit creates a new `documentation/security-audit/run-<N>/` that `git status` does not list (unless you chose to commit runs).
- A full audit ends with both validators passing and the three reports written, or with `run_status: "incomplete"` and its reason stated in the report.
- Every confirmed finding names the file path, the crossed boundary, the observed result, and a source-level fix with a regression case.
- Leads that depend on facts outside the repository appear in `NEEDS-VALIDATION.md` without a severity.

## Where it fits

Periodic maintenance, run on demand or before a release. Its confirmed findings become work for the delivery flow, and [triage](./triage.md) can turn them into tracked tasks.
