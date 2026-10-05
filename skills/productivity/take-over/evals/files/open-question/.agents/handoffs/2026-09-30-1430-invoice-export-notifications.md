# Handoff: invoice export, failure notifications

Supersedes: `2026-09-24-1615-invoice-export-retries.md`.

## State

The upload retries are in place, using the retry decision from the previous handoff. Failure notifications are specified in `documentation/capabilities/invoice-export/notifications.md` and half implemented in `src/export/notify.ts`.

## What is next

Finish `notify.ts` so the on-call channel is told only after the final retry fails, then add its test.

## Suggested skills

`test-first`.
