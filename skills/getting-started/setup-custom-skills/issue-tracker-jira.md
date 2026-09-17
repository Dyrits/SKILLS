# Issue tracker: Jira

Jira is the system of record for project issues and published specifications.

## Project

- **Project key:** `<project-key>`
- **Base URL:** `<jira-base-url>`

## Access

- **Method:** `<verified MCP connector, CLI, REST workflow, or manual>`
- **Read:** `<verified read operation, or manual>`
- **Comment:** `<available comment operation, or manual>`
- **Update:** `<available update operation, or manual>`

Record the access method as automated only after a read-only access check succeeds. List comment and update operations from the actual available tool without exercising them during setup. When access is manual, prepare the exact Markdown for the user to paste into Jira.

## Ticket writing convention

- **Source:** `<Built-in to-tickets, repository document, or skill name and template reference>`
- **Applies to:** `<refinement drafts, published tickets, or both>`
- **Rules:** `<language or required Jira metadata needed to interpret the source>`

An optional Jira ticket skill may supply the description template and quality rules. `to-tickets` still owns the tracer-bullet breakdown, blocking edges, and publication approval.

## When a skill says "fetch the relevant ticket"

Read the issue body, comments, status, links, and labels through the verified access method. Use the issue key as its identity.

## When a skill says "publish to the issue tracker"

Use the verified update operation only after the user explicitly asks to publish. Otherwise, leave the approved artifact locally and report its path.

## Wayfinding operations

Record the Jira instance's supported parent-child, blocking, assignment, and resolution operations here after verifying them. If those operations are unavailable, use textual links in the issue body and state that limitation explicitly.
