# Cobblestone service

Cobblestone is a small invoicing API written in TypeScript. It is very important to be thorough and careful when working in this repository.

## Commands

- Run `npm test` to run the tests. This runs vitest.
- Run `npm run lint` to lint. This runs biome.
- Run `npm run build` to build. This runs tsc.

## Rules

- Always be careful and write high quality code.
- Never use `var`. Never use `any`. Never leave console.log statements in.
- Money amounts are stored as integer cents because the payment provider rejects decimals, and two earlier releases shipped rounding bugs from float math. Never add a float to a money column.
- Always write high quality code and be careful.
- See `docs/legacy-importer.md` for the importer (this file was deleted in March).
- When you finish a task, summarize what you did.

## Deploying

The full deploy runbook is below.

1. Merge to main.
2. Wait for CI.
3. Run `./scripts/release.sh`, which tags the release, builds the image, pushes it, and runs the smoke tests. If the smoke tests fail the script rolls back and prints the failing step. After a rollback, open the incident channel and post the failing step with the commit hash, then tag the on-call engineer and wait for acknowledgement before retrying.
4. Update the changelog.
5. Announce in the team channel with the version, the highlights, and the rollback status, linking the changelog entry and the pull request.
