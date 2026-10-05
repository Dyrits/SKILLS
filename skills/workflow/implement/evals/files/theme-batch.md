# Approved batch: reader theme toggle

Status: approved by the user in `documentation/work-in-progress.md`. Project: Pebblebrook Journal (invented).

## Agreed behavior

- The reader view has a toggle that switches between a light and a dark theme.
- The choice is remembered across visits.
- The dark theme keeps body text at a contrast ratio of at least 7:1.

## Acceptance

- Agent-checkable: the stored preference is read back as `dark` after a toggle and a reload (unit test on `preferences.get_theme()`).
- Human-checkable: whether the dark theme looks right on the article page, including images and code blocks.
