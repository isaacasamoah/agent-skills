# Worktree task documents and completed work

Use this convention when a feature or project phase has met its acceptance criteria and the user or approved workflow has accepted its completion. Reconcile its documents alongside worktree cleanup. A merged PR, an old document or a removed worktree alone does not prove the phase is complete.

The selected development workflow still owns verification, task completion, review, merging and shipping. Finish those steps before moving their records. Never move an incomplete plan or another session's active work to make the active folders look tidy.

## Standard destinations

| Document | While active | Once complete |
|---|---|---|
| Obsidian design or architecture explainer | `explainer/design/` | `done/explainer/design/` |
| Obsidian build or system walkthrough | `explainer/walkthroughs/` | `done/explainer/walkthroughs/` |
| Obsidian research for that feature or phase | `research/` | `done/research/` |
| Task specification and modules | Selected worktree root | `spec-history/` in its canonical Obsidian project |
| Task plan and checklist | Selected worktree `tasks/` | The same Obsidian `spec-history/` |

Each task worktree owns its root `SPEC.md`, selected spec modules and `tasks/plan.md` with `tasks/todo.md`. Keep these task documents local to that worktree, outside commits and the primary checkout. Continue using the selected specification, planning, build and review skills. Where a command normally commits the plan or task-status update, this local placement convention excludes those documents from the commit; implementation commits, verification and approval gates remain required. A code rollback does not restore local planning state, so reconcile the plan and checklist against the actual code before resuming.

Before creating new task documents, check whether their paths are already tracked or occupied by inherited work. Preserve existing tracked documents and incomplete work; do not overwrite them, untrack them or rewrite history to apply this convention. Resolve that existing-document conflict with the owner first. For new untracked documents, add only their exact repository-relative paths to the common Git directory's `info/exclude`, preserving existing entries. This local ignore list is shared by the repository's worktrees; ignored files still exist for filesystem-based tools. Verify `git ls-files` does not include the selected documents and inspect staged paths before committing. Do not use forced staging for them or ignore all Markdown or the whole tasks directory.

After the implementation PR is merged and this task is accepted complete, preserve its spec, modules, plan and checklist as Markdown in `spec-history/` at the canonical Obsidian project root. Archive before removing the worktree. Do not put these records in repository `done/` or `tasks/done/`. Use flat, descriptive names prefixed by the worktree's subject, for example `voice-preservation-spec.md`, `voice-preservation-voice-module.md`, `voice-preservation-plan.md` and `voice-preservation-todo.md`. Keep internal links valid and record the merged PR or local integration evidence in project navigation. If a name already exists, compare contents and resolve a conflict before moving anything; never overwrite a previous record.

Create a listed destination only when needed. This authorizes `spec-history/` and the done destinations above, with evidence folders inside the completed human-document categories, not arbitrary extra categories or a folder per feature. Keep standing instructions, constraints, technical guides and current project navigation in their existing homes. Existing tracked specs, archives and done records stay in place unless the user approves their migration. External trackers keep their own history.

## Preserve documents and links

1. Identify the completed scope and its acceptance evidence. Check that no active feature, session, plan or task still owns the documents. Project-wide research that is still in use remains active.
2. Move the canonical documents rather than copying them. Move evidence used only by those documents into `evidence/` within their done category. Keep shared evidence at its existing canonical location and repair links to it. Do not duplicate shared evidence or discard it because one consumer finished.
3. Repair incoming and outgoing links, including relative HTML/Markdown links, native Obsidian URLs, specification indexes, status/log navigation and paths used by build or validation tools. Preserve revisions, decisions, review findings and meaningful historical commands. A historical pathname is not a live dependency.
4. Verify that moved files and required evidence retain their contents, repaired targets exist and the reading view works. Keep a useful index or status/log link so completed work remains findable. Label completed work where the distinction matters.
5. Only then remove an eligible worktree using the Git skill's checks. Preserve unique packages or evidence outside it and verify the move before removal. If work still needs a checkout, record the concrete dependency. A document mention alone calls for resolving the reference, not permanent retention.

The archived specification records the accepted intent for the implemented behavior. Read it when relevant. For later changes, create the new task's worktree-local specification and link the relevant history; leave the archived record unchanged rather than maintaining two editable copies. Context refresh follows the current task's selected documents; it does not load all spec history.

## Keep cleanup proportionate

Use the existing walkthrough, status and log to record the move and any unresolved dependency. Do not add a background archiver, infer completion from file age or close unrelated work automatically. If completion is uncertain, leave the documents active and state the uncertainty.
