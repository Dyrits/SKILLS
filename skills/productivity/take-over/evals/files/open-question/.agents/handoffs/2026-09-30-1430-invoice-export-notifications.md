# Handoff: invoice export, failure notifications

Supersedes: `2026-09-24-1615-invoice-export-retries.md`
Workspace: invoice-service, branch `main`

## Goal

Tell the on-call channel when an export upload fails for good.

## State

- The upload retries are in place, as decided in the previous handoff (verified: read `src/export/upload.ts`).
- Failure notifications are half implemented in `src/export/notify.ts` (assumed: written by a colleague, not run).

## Decisions

None.

## Next

1. Finish `notify.ts` so the on-call channel is told only after the final retry fails.
2. Add its test.

## Open questions

None.

## Sources

- `documentation/capabilities/invoice-export/notifications.md`
- `src/export/notify.ts`
