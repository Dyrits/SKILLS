# Saved searches

Status: approved. Project: Fernlea Catalogue (invented), a web catalogue for a lending library. Path: `documentation/capabilities/search/specification.md`.

## Agreed behavior

- A signed-in member can save the current search (query and filters) under a name of up to 40 characters.
- Saved searches appear in a "Saved" menu on the search page; selecting one reruns it.
- A member can rename or delete a saved search.
- A member can have at most 20 saved searches; the 21st is refused with a clear message.
- Saved searches are private to the member.

## Design

- Persisted by the existing `SearchService` through a new `SavedSearchStore` interface; the web page calls `SearchService.save`, `list`, `rename`, `delete`.
- The search page currently builds its query string inline in `search_page.py`; it needs a small prefactoring so the query and filters can be read as one value.

## Acceptance

- Saving, listing, renaming, deleting, and the limit of 20 are each demonstrable through `SearchService`.
- The "Saved" menu is visible and usable in the browser (human check).

## Open decision

- Whether a member can share a saved search with another member is undecided and is not part of this scope until settled.
