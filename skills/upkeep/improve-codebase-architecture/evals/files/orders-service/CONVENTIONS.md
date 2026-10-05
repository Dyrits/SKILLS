# Conventions

- Modules own their persistence; callers never write to another module's tables.
- Money is integer cents, never floats.
- Prefer one public entry point per module.
