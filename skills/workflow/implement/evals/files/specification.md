# Slugs for article titles

Status: approved. Project: Pebblebrook Journal, an invented publishing tool. The module is `journal/slugs.py`, tested with pytest.

## Agreed behavior

- `make_slug(title)` returns a lowercase, hyphen-separated slug for an article title.
- Letters and digits are kept; every run of other characters becomes one hyphen; leading and trailing hyphens are removed.
- A title with no letters or digits yields the slug `untitled`.
- Slugs are cut at 60 characters, never ending in a hyphen.

## Acceptance

- `make_slug("Hello, World!")` is `hello-world`.
- `make_slug("  --  ")` is `untitled`.
- A 100-character title of repeated words yields a slug of at most 60 characters that does not end in `-`.

## Unresolved proposals (not agreed)

- Transliterating accented letters (`é` to `e`) was proposed; no decision yet.
