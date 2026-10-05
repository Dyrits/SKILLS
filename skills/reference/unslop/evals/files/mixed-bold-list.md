## Why we picked Drizzle

- **Schema in TypeScript.** Tables live in one file, so a column rename fails the build in every query that used it.
- **Performance:** Performance improved after the move.
- **Migrations:** Migrations are generated from the schema diff and committed under `db/migrations/`.

Before you run it, check three things:

1. `DATABASE_URL` is set.
2. The `db/migrations/` directory exists.
3. The `drizzle-kit` binary is on your path.
