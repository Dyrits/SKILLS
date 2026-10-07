# Handoff: invoice export, upload retries decided

Supersedes: `2026-09-12-0900-invoice-export-kickoff.md`
Workspace: invoice-service, branch `main`

## Goal

Upload the finished export file to the storage bucket reliably.

## State

- The retry decision is implemented in `src/export/upload.ts` (verified: read the file).

## Decisions

- Uploads retry three times with a 2 second pause, because the storage provider drops about one request in fifty during its nightly maintenance window. Retrying more than three times was rejected: it hides a real outage for the 2 a.m. job.

## Next

1. Notify the on-call channel when an upload finally fails.

## Open questions

None.

## Sources

- `src/export/upload.ts`
