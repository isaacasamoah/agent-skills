---
name: working-docs
description: Places and maintains project working documents in their canonical home. Use when deciding where to save a project walkthrough and its evidence, selecting document formats, or updating a specification, code sketch reference, plan, research report, project status or log. Not for choosing architecture, decomposing implementation, or coordinating agents.
---

# Working docs

## Overview

Choose the document's purpose, owner and existing destination before writing it. Keep each fact authoritative in one place and produce the appropriate reading format from that source.

## When to Use

- The user requests a persistent explanation, specification, plan or research result.
- Work changes a project's current status, accepted decisions or evidence.
- An existing document needs updating, replacing or archiving.

Ordinary chat answers do not need a new document. Follow the relevant content skill for the actual reasoning and deliverable.

## Process

### 1. Resolve the project and destination

Read the project's AGENTS.md and the declared documentation root. Use the named existing document when one already owns the subject. Search that project's files before creating another version.

If the project, destination or purpose is unclear, ask whether this document should be produced and where it belongs. Do not create a folder or subfolder, invent a miscellaneous category, or save a substitute somewhere else while waiting. An approval that names the new directory is sufficient; do not request the same approval again.

For an idea without a project, use the explicitly assigned exploration project. Do not silently turn a new idea into a new project.

### 2. Select the authoritative artifact

Use the project's declared layout. The default layout, when adopted by a project, is:

| Purpose | Existing destination | Authority and format |
|---|---|---|
| Understand an existing or proposed system; walkthrough or review | explainer/ | HTML for explainers and reviews intended for Isaac to read; otherwise the owning skill's format |
| Define agreed behavior and contracts; UX requirements and code sketches | specs/ | The specification skill's format; linked native code and UX artifacts |
| Break an agreed specification into tasks | plans/ | The planning skill's format, or the project's declared external tracker |
| Investigate a question or compare approaches | research/ | HTML findings; Markdown run instructions only when needed; linked raw evidence in its native format |
| Resume current work | status.md at the project documentation root | Markdown current state and links |
| Record what happened and why | log.md at the project documentation root | Markdown dated history and links |

The table does not authorize creating missing directories. Reviews use explainer/ with a review suffix under this layout; surface the mismatch if the project's established convention differs.

HTML is the default for documents Isaac reads, including explainers, elucidate outputs and research findings. Specifications and plans keep their owning skill's format. Other agent-facing deliverables also follow their owning skill; agent instructions, status and log are Markdown. Code, schemas, drawings and measurements retain their native formats and are linked as evidence rather than rewritten as prose.

Do not create HTML copies of specifications or plans by default, even when Isaac will read them. If he explicitly requests a separate reading view, derive it from the authoritative source and identify that source's revision or hash. Never maintain two independent editable specifications. Author human-facing explainers and research directly in HTML without an unused Markdown twin.

### 3. Write the content with its owning skill

Use the selected specification, planning, elucidation, research or review procedure. This skill controls document placement, authority and format; it does not replace those procedures.

Preserve upstream skills. When their default paths conflict with the project's explicit output policy, follow the project policy and state the deviation. If the conflict would change the actual workflow, ask before proceeding.

Keep project commands and standing conventions in project instructions, behavioral requirements in the specification, scheduling and task state in the plan, and current resume information in status. Reference the owner instead of copying its content. Clearly mark examples, proposals, accepted decisions, observed results and unresolved questions.

### 4. Make the document traceable and usable

Give the document a stable, meaningful subject name. Include project, purpose, state, source revision when relevant, and links to its inputs and related artifacts. For immutable experiment evidence, include the run identifier or date. Update a living document in place; use version control for history.

Keep human HTML portable and usable offline where practical. Use readable source formatting, local assets and no required third-party scripts. Test navigation and referenced files. Verify the rendered view when changing its layout or interaction. Show when a generated view is out of date.

Keep private transcripts, household data and personal planning out of public repositories. A public README or PR can link only audience-accessible material; publish an explicitly approved summary when the canonical working document is private.

### 5. Leave one clear resume point

Update status when the current outcome, next action or blocker changes. Record consequential decisions and completed work in log, with evidence links. Do not paste the session transcript or repeat the entire plan.

Keep log entries newest first. Add each new entry at the top, below the log title, so the latest information is immediately visible. Keep older entries intact and place any log-writing guidance after the entries.

Within parallel work, one assigned editor updates the project status and log. Contributors return their results and links to that editor. This ownership convention applies regardless of the orchestration tool.

Do not overwrite an incomplete plan, another writer's change or an accepted document silently. Propose supersession or archival and preserve the prior record.

## Common Rationalizations

| Rationalization | Response |
|---|---|
| A new folder will make this easier to file | First establish whether the output is needed and where it belongs. |
| A second spec will be easier for the human to read | Keep the specification in its owning skill's format. Create a separate reading view only when requested. |
| The report is finished because it was saved | Check the reading surface, evidence and destination. |
| Status should contain all previous progress | Status is the current resume point. History belongs in log. |

## Red Flags

- An unrequested HTML copy of a specification or plan, or independent copies of the same requirements.
- An output saved outside the declared project home.
- A new folder created without approval.
- A private absolute path offered as a usable public PR reference.
- A generated reading view that conceals its source or stale state.

## Verification

- The project, purpose and existing destination are explicit.
- No unapproved directory was created.
- Each substantive fact has an identified authoritative artifact.
- Human-facing explainers and research use HTML; other agent-facing deliverables follow their owning skill's format.
- Specifications and plans have no unrequested HTML copy; agent instructions, status and log are Markdown.
- References resolve and any derived view matches its source.
- Current status and consequential history are recorded once.
