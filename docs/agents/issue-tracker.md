# Issue tracker: Local Markdown

Issues and specs for this repo live as markdown files in `.scratch/`.

## POEX Coach boundary

This tracker belongs to POEX Coach, even when an implementation session runs in another repository. Pass its absolute path and the relevant local spec/ticket paths in each assignment. Jira remains the official source for scope and issue status.

Only the coach writes `.scratch/<feature-slug>/TASK.md`. Executor sessions read it and return evidence to the coach. Other local files require the exact proposed change and Francisco's approval before writing, as defined by AGENTS.md. “Publish to the issue tracker” names a destination; it does not grant write permission.

Plugin triage labels describe readiness. The coach tracks ticket execution in the `## Tickets` table of TASK.md using the canonical POEX states; `ready-for-agent` does not mean implemented or integrated. Consult the assignment's integration condition before considering a blocking ticket complete. Ticket files own scope, criteria and dependencies; do not duplicate execution states in their content or in TASK.md YAML. If the route omits tickets, do not create the table or ticket files.

## Conventions

- One feature per directory: `.scratch/<feature-slug>/`
- The spec is `.scratch/<feature-slug>/spec.md`
- Implementation issues are one file per ticket at `.scratch/<feature-slug>/issues/<NN>-<slug>.md`, numbered from `01`, never a single combined tickets file
- Triage state is recorded as a `Status:` line near the top of each issue file (see `triage-labels.md` for the role strings)
- Comments and conversation history append to the bottom of the file under a `## Comments` heading

## When a skill says "publish to the issue tracker"

Create a new file under `.scratch/<feature-slug>/` (creating the directory if needed).

## When a skill says "fetch the relevant ticket"

Read the file at the referenced path. The user will normally pass the path or the issue number directly.

## Wayfinding operations

Used by `/wayfinder`. The **map** is a file with one **child** file per ticket.

- **Map**: `.scratch/<effort>/map.md` (the Notes / Decisions-so-far / Fog body).
- **Child ticket**: `.scratch/<effort>/issues/NN-<slug>.md`, numbered from `01`, with the question in the body. A `Type:` line records the ticket type (`research`/`prototype`/`grilling`/`task`); a `Status:` line records `claimed`/`resolved`.
- **Blocking**: a `Blocked by: NN, NN` line near the top. A ticket is unblocked when every file it lists is `resolved`.
- **Frontier**: scan `.scratch/<effort>/issues/` for files that are open, unblocked, and unclaimed; first by number wins.
- **Claim**: set `Status: claimed` and save before any work.
- **Resolve**: append the answer under an `## Answer` heading, set `Status: resolved`, then append a context pointer (gist + link) to the map's Decisions-so-far in `map.md`.
