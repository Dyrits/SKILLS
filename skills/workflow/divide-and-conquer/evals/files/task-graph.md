# Report export: authorized task graph

Originating agreement: `documentation/capabilities/export/specification.md` (approved). This file lists its tasks, all authorized for implementation. Starting commit: `3f9c1ab`. Project: Larkspur Reports, a small invented web application.

| Task | Outcome | Blocked by | Notes |
| --- | --- | --- | --- |
| T1 | Rename the configuration key `report.format` to `report.default_format`, with the single reader updated | None | One file, one test, settled acceptance |
| T2 | A report can be downloaded as CSV through the existing report service | None | Ordinary implementation, one seam (`ReportService.export`) |
| T3 | Export requests are checked against the viewer's permissions, so a viewer never exports a report they cannot open | None | Touches authorization and the audit log, crosses three modules |
| T4 | The user guide documents CSV export and the permission rule | T2, T3 | Documentation only |
| T5 | An end-to-end check downloads a CSV as a permitted viewer and is refused as a forbidden one | T2, T3 | Needs the test server fixture |

Tasks T1 to T3 are on the frontier. The project has no `.agents/issue-tracker.md`; all tasks are local drafts under `documentation/capabilities/export/tasks/`.
