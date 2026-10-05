---
name: monitor-ai-tooling
description: "Report AI tooling usage, measured output reduction, quality signals, and gaps from existing local measurements. Use when the user asks how the AI tooling is performing or what it saves."
---

# Monitor AI tooling

Run an on-demand **report** from existing measurements.
Collection stays deterministic; this skill does not install tools or start recurring model analysis.

**Hands over to:** `/setup-ai-tooling`. When one is not installed, give the user its install command, `npx skills@latest add Dyrits/SKILLS --skill=<name>`, along with the instruction to run it.

## Process

### 1. Establish the evidence

Read `.agents/ai-tooling.md` if present, the requested project and period, and the available local measurement sources.
Use configured tool analytics, saved verification results, or an export from the user's existing monitor.
Inspect source schemas and installed help before choosing read-only export commands; preserve source files and redact credentials or unrelated session content from the report.
For RTK, inspect `gain` and supported history/export options without changing counters or configuration.
Prefer local collection without network requests or additional model calls.
If setup or data is missing, produce a gaps report: name the gaps a future measurement period fills, and for missing setup tell the user to run `/setup-ai-tooling`.
Treat no observations as unknown usage, not proof a tool was unused.
Done when every source has a provenance, unit, period, scope, and project attribution or an explicit attribution gap.

### 2. Compare compatible observations

Use [MEASUREMENT.md](MEASUREMENT.md) for units, comparisons, and savings claims.
Compare counters only across the same source, scope, schema, and counter lifetime.
Account for resets, tool upgrades, missing periods, and overlapping clients before calculating deltas.
Report global measurements as global when project attribution is unavailable.
For a task comparison, check equivalent task scope and correctness criteria before drawing a quality or savings conclusion.
Inspect measured tool calls, duration, output bytes, adapter failures, raw-output recalls, and correctness checks where available.
For CodeGraph and ast-grep, keep personal token savings unknown when only successful lookup checks exist.
Done when every calculated result can be traced to compatible observations and every unmeasured quantity remains unknown.

### 3. Write the report

Write a dated report under `.agents/tooling/reports/`, or the user's requested local destination, following [REPORT.md](REPORT.md).
Include source references and machine-readable supporting observations when the source provides them.
Separate actual provider usage, command-output reduction, estimated tokens, task comparisons, and published benchmarks.
Keep Token Monitor independent; an integration change is a separate setup task.
Rank recommendations by evidence, with a specific next measurement where evidence is thin.
An unverified protected-command bypass is a quality finding even when output reduction looks good.
Done when the report accounts for every configured tool, source gaps, quality findings, and next actions without fabricating a total savings figure.

### 4. Finish

Summarize observed benefits, quality problems, and unknowns with the report path.
For configuration changes, tell the user to run `/setup-ai-tooling`; leave installations, hook edits, and account changes to an explicit setup request.
