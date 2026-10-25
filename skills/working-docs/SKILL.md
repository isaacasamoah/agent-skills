---
name: working-docs
description: Places and maintains human-facing Obsidian documentation. Use when choosing walkthrough or review destinations, research formats, screenshot evidence, project navigation, status or log. Not for authoring or executing repository work; defer to its canonical skills.
---

# Working docs

## Overview

Keep human-facing documentation in its approved Obsidian home. Link to development artifacts where they are maintained. This skill owns documentation presentation and navigation; the development skills own specifications, implementation plans and task execution.

## When to Use

- Choose the destination or reading format for a walkthrough, research report or review.
- Update human-facing project navigation, status or log from verified decisions and results.
- Organize a document's screenshots and supporting evidence.

Ordinary chat does not need a document. For a mixed request, use this skill for the human-facing portion and the relevant development skill for the rest.

## Process

### 1. Identify the owner before choosing a path

Read the project's instructions and declared documentation root. Search the existing documents before creating another version. Route each artifact to its owner:

| Artifact | Owner |
|---|---|
| Development requirements and specification | [spec-driven-development](../spec-driven-development/SKILL.md) |
| Implementation plan, dependencies and task-list target | [planning-and-task-breakdown](../planning-and-task-breakdown/SKILL.md) |
| Building, verification and task completion | The selected build command and [incremental-implementation](../incremental-implementation/SKILL.md), with its required testing and review skills |
| Branches, worktrees, commits and releases | [git-workflow-and-versioning](../git-workflow-and-versioning/SKILL.md) |
| Human-facing walkthroughs, research, review presentation, navigation, status and log | This skill, with the content skill that produces the explanation or review |

Follow the canonical development skills and the selected project's supported repository convention for development artifacts. Working-docs does not redirect them into Obsidian or replace their lifecycle. For example, VoyagerShell's selected specification is docs/SPEC.md; its plan is tasks/plan.md and its default task list is tasks/todo.md. A designated external tracker remains an upstream-supported option. Keep the todo list associated with its active plan; status.md is a resume pointer, not another task ledger.

If an older local instruction sends these artifacts to Obsidian, identify the conflict and request or propose a bounded reconciliation with its owner. Do not silently override instructions, migrate existing specifications, or change the upstream path validator, completion ordering, approval gates or retention rules. An explicit user decision resolves the named conflict only.

### 2. Select the human-facing document and destination

Use the project's approved Obsidian layout. Common destinations are:

| Purpose | Destination | Format |
|---|---|---|
| Proposed UX, design or architecture: what we intend to build and why | explainer/design/ | HTML |
| Implemented-system walkthrough, build/verification evidence or review: what exists and whether it meets the intent | explainer/reviews/ | HTML |
| Research or comparison | research/ | HTML, with linked evidence in its native format |
| Project navigation and resume point | status.md at the documentation root | Markdown |
| Dated decisions and completed work | log.md at the documentation root | Markdown, newest first |

For these project documentation homes, `research/`, `explainer/design/`, `explainer/reviews/` and each document's `screenshots/` evidence folder are the approved writing destinations. Keep the existing singular `explainer/` name. Name documents for their subject and purpose, such as `voice-design.html` or `voice-build-review.html`; include a date for a specific run or snapshot. Research gathers evidence or compares options before a choice; a design explainer communicates the intended choice. A review may compare that intent with implemented behavior, but is not a second specification.

Old Obsidian `specs/` and `plans/` belong under `archive/specs/` and `archive/plans/`. Keep them findable through an archive link in project status, preserve their contents and repair moved links. These archived documents are historical context, not active development contracts. Archive only with user authorization; do not move repository-owned specs or plans. This does not authorize reorganizing unrelated project folders or automatically recategorizing existing explainers.

If the project, purpose or destination is unclear, resolve that before writing. Do not invent a category, project or substitute folder. Do not ask again when the user has already authorized the destination. For an idea without a project, use the explicitly assigned exploration project.

### 3. Write with the content skill

Use the appropriate elucidation, research or review skill for substance, and the writing guidance for clarity. Human-facing explainers and research use HTML by default. Agent instructions remain Markdown; code, schemas and measurements retain their native formats. Working-docs does not choose architecture, produce a development plan, execute tasks or change review standards.

Link to the authoritative specification, plan, task list or tracker. Do not reproduce requirements as a second editable contract, maintain another completion checklist, or treat a status summary as task completion evidence. A human-facing summary may explain the outcome and link to its owner.

Do not create HTML copies of development specs or plans by default. If the user explicitly requests a reading view, derive it from the authoritative artifact, identify its source revision and say where edits belong. Avoid an unused Markdown twin of a human-facing HTML report.

### 4. Keep evidence and navigation usable

Give documents clear names and state their project, purpose and status. Distinguish proposals, accepted decisions, observations and open questions. Update living documents in place and use version control for history.

Store screenshots in a screenshots/ subfolder beside the document they support, such as research/screenshots/, explainer/design/screenshots/ or explainer/reviews/screenshots/. This evidence subfolder is part of the approved layout. Name captures so their document and purpose are clear, and use relative links. Preserve content and update links when moving existing screenshots.

Source and run evidence may remain with the code that owns them. Link to it rather than relocating development artifacts for a report. Keep HTML portable and usable offline where practical. Check navigation and local links; inspect the rendered result when changing layout or interaction. Identify stale derived views.

Keep private transcripts and personal material out of public repositories. Public readers need accessible sources or an explicitly approved public summary.

### 5. Leave a concise resume point

Update status when the current outcome, next action or blocker changes, linking to the owning development artifacts. Record consequential decisions and completed work in log. Do not copy the plan or mark development tasks complete through this skill.

Prepend new log entries below the title, preserving older entries. Keep log-writing guidance after the entries. In coordinated work, one assigned editor owns project status/log; other participants return findings and links to that editor.

Preserve another writer's changes and incomplete work. Any change to development plans, task lists or their retention belongs to the owning development procedure.

## Common Rationalizations

| Rationalization | Response |
|---|---|
| The user reads the spec, so it belongs in Obsidian | Readership does not change the development artifact's owner or supported path. |
| There is a plans/ folder in the vault | An existing folder is not a new task-list convention. |
| Status should repeat the task checklist | Link to the task list and summarize only the resume point. |
| A prettier copy can become the contract | Keep one authoritative artifact; label explicitly requested derived views. |

## Red Flags

- Moving a repository spec, plan or task list into Obsidian through this skill.
- Redefining build completion, commit ordering, approval gates or retention rules.
- Duplicated requirements, checklists or task-status authority.
- An output outside its approved documentation home, or an unrequested folder.
- A public document linking to private local material as though readers can access it.

## Verification

- Human-facing documentation has an explicit owner, approved destination and appropriate format.
- Development artifacts remain under their canonical skills and supported project convention.
- Links to the authoritative spec, plan and task list resolve without duplicating their state.
- No upstream development procedure, completion gate or retention rule changed.
- Screenshots are beside their document in screenshots/; changed layouts were inspected.
- Status and newest-first log summarize decisions without becoming another task ledger.
