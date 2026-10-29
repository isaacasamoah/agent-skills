# Put completed work in done

Use this convention when a feature or project phase has met its acceptance criteria and the user or approved workflow has accepted its completion. Reconcile its documents alongside worktree cleanup. A merged PR, an old document or a removed worktree alone does not prove the phase is complete.

The selected development workflow still owns verification, task completion, review, merging and shipping. Finish those steps before moving their records. Never move an incomplete plan or another session's active work to make the active folders look tidy.

## Standard destinations

| Document | While active | Once complete |
|---|---|---|
| Obsidian design or architecture explainer | `explainer/design/` | `done/explainer/design/` |
| Obsidian build or system walkthrough | `explainer/walkthroughs/` | `done/explainer/walkthroughs/` |
| Obsidian research for that feature or phase | `research/` | `done/research/` |
| Repository feature or module specification | Repository root | `done/` at the repository root |
| Repository plan and task list | `tasks/` | `tasks/done/` |

Paths are relative to the owning Obsidian project or source repository. Keep only active specifications in the repository root and active plans/tasks directly in `tasks/`. A root `SPEC.md` that indexes specifications can remain as navigation, with clear links to active and completed specifications. Keep standing instructions, constraints, technical guides and current project navigation in their existing homes.

Keep canonical documents directly in these folders. Preserve descriptive specification filenames. Rename generic plans and task lists when moving them, for example `tasks/done/connection-retry-plan.md` and `tasks/done/connection-retry-todo.md`. Do not overwrite a previous phase or create a folder per feature. An external tracker keeps its own history; do not copy it into a second task ledger.

Create a done destination when it is first needed. This authorizes the listed folders and their evidence folders, not arbitrary extra categories. Existing `archive/` material stays where it is unless the user requests a separate migration. New completed work uses `done/`.

## Preserve documents and links

1. Identify the completed scope and its acceptance evidence. Check that no active feature, session, plan or task still owns the documents. Project-wide research that is still in use remains active.
2. Move the canonical documents rather than copying them. Move evidence used only by those documents into `evidence/` within their done category. Keep shared evidence at its existing canonical location and repair links to it. Do not duplicate shared evidence or discard it because one consumer finished.
3. Repair incoming and outgoing links, including relative HTML/Markdown links, native Obsidian URLs, specification indexes, status/log navigation and paths used by build or validation tools. Preserve revisions, decisions, review findings and meaningful historical commands. A historical pathname is not a live dependency.
4. Verify that moved files and required evidence retain their contents, repaired targets exist and the reading view works. Keep a useful index or status/log link so completed work remains findable. Label completed work where the distinction matters.
5. Only then remove an eligible worktree using the Git skill's checks. Preserve unique packages or evidence outside it and verify the move before removal. If work still needs a checkout, record the concrete dependency. A document mention alone calls for resolving the reference, not permanent retention.

The done specification remains authoritative for the completed behavior. If a later task changes that behavior, explicitly select and move the specification back to the active location, or identify its successor and update the index. Do not treat completed specifications as obsolete or keep two editable copies. Context refresh follows the current task's selected documents; it does not load the whole done history.

## Keep cleanup proportionate

Use the existing walkthrough, status and log to record the move and any unresolved dependency. Do not add a background archiver, infer completion from file age or close unrelated work automatically. If completion is uncertain, leave the documents active and state the uncertainty.
