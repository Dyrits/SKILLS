# Handoff: invoice export, upload retries decided

Supersedes: `2026-09-12-0900-invoice-export-kickoff.md`.

The export uploads the finished file to the storage bucket. Decision: uploads retry three times with a 2 second pause, because the storage provider drops about one request in fifty during its nightly maintenance window. Retrying more than three times was rejected: it hides a real outage for the 2 a.m. job.

The decision is implemented in `src/export/upload.ts`.
