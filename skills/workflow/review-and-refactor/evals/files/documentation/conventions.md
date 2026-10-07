# Conventions (Tidewater Shop, invented example)

- Money is always an integer number of cents. Never use floats for money.
- Public functions carry type annotations and a one-line docstring.
- Names are full words; no single-letter names outside loop indices.
- Raise `ValueError` with a message for invalid input; never return a sentinel such as `-1`.
- Formatting and import order are enforced by `ruff`; do not review them.
