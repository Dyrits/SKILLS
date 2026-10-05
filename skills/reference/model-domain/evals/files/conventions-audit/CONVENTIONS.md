# Conventions

How code is written in this project.

## Errors

- **Errors cross module boundaries as typed results**: thrown strings are never used, because callers cannot tell them apart.
- **A refund over 500 euros always asks for a manager's approval**: the finance policy requires it.

## Text

- **Visible text lives in data, in English and Dutch**: a translator can change wording without touching code.

## Tests

- **One behaviour per test, named after the behaviour**: a failing name should explain the failure.
- **Run `npm run lint` and the full tests before committing**: keeps the main branch green.
