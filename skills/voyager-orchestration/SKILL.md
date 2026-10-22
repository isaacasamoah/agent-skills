---
name: voyager-orchestration
description: Coordinates authorized work through Voyager using assigned agents, delegation, escalation, adjudication and Fleets. Use when the user requests Voyager coordination or an approved plan calls for parallel Voyager work. Not for selecting project conventions, writing specifications, or deciding that work needs more agents.
---

# Voyager orchestration

## Overview

Coordinate the user's chosen workflow through Voyager. Each participant keeps its project instructions, content skills and permitted tools. Voyager provides identity, authority, delivery and lifecycle information.

## When to Use

- The user wants existing or new Voyager agents to collaborate on an authorized task.
- An approved plan has independent work that can run in parallel.
- A participant needs a decision, revision, or evidence-based completion judgment.

Use ordinary project work for a single task that needs no coordination. This skill does not require Osmani skills, the Lab, Obsidian, a particular model, or a particular programming language.

## Process

### 1. Read the actual Voyager contract

Use the current instance's supplied Voyager instructions and its supported capability inspection. Establish the service identity, caller, rank, supervisor, direct reports and relevant attachment state. Read the applicable CLI or adapter reference supplied by that installed Voyager version. If unavailable, report the missing capability; do not invent commands or use an owner connection as a fallback.

Resolve targets by returned identity and workspace, including kind and assignment. A display name alone is insufficient. Do not inspect or disclose private caller credentials.

Ranks describe service authority, not expertise. Fleets organize presentation and do not by themselves grant supervision, execution rights or approval. Use only capabilities actually granted by the current service.

### 2. Prepare a bounded assignment

Take the work breakdown from the user's chosen plan or planning procedure. Do not create a competing plan or impose a different lifecycle.

For each delegated task establish:

- the outcome and acceptance criteria;
- the owner and permitted source/worktree, starting revision and write scope;
- links to the project's own instructions, inputs and relevant content skill;
- dependencies and what must finish before this task starts;
- the already-approved output destinations;
- the allowed actions, review and release boundaries;
- any agreed resource limit and stopping condition;
- the evidence and report required for completion.

Reuse the canonical plan entry if it already contains these fields. Send a short assignment with references rather than copying the whole project context into every agent.

### 3. Delegate and observe

Reuse an appropriate assigned agent when its identity, permissions and state fit the task. Create a new agent only when authorized and supported. Do not change ranks or assignments beyond the caller's actual authority.

Run independent tasks in parallel. Serialize conflicting writes and dependent tasks. Allocate disjoint worktrees or file ownership as the project requires. Do not ask workers to ignore each other's changes.

Retain the service's request, session and turn identifiers and event cursor. On an uncertain response, inspect the existing operation. Do not launch a replacement or repeat the effect simply because an acknowledgement was lost.

Use supported events or bounded observation to track progress. Delivery acceptance is not task completion. A closed viewer, quiet terminal or completed tool call is not evidence that the requested result exists.

### 4. Escalate and adjudicate

Escalate a concrete decision to the assigned supervisor or owner using Voyager's supported route. Include the unresolved question, relevant evidence, alternatives and the action waiting on the answer. Continue only independent authorized work.

A recorded escalation is still an unanswered question. Do not treat delivery, silence, elapsed time, another agent's assertion or a review verdict as Isaac's approval.

Adjudicate only within assigned authority. Compare the result with its acceptance criteria and evidence. State acceptance, a specific revision request, or the resolved decision through the supported operation. Preserve the actual human decision and its scope when relaying it. A supervisor's technical acceptance does not grant human-reserved merge, release, publication or spending approval.

### 5. Reconcile and report

Verify the returned artifacts and relevant successful native completion event, with correct task, session and revision attribution. Report partial, failed, blocked and uncertain outcomes explicitly. A successful event does not prove the artifact is correct.

Have the designated integrator reconcile interfaces and run the project's required integration checks. Return the result through the assignment chain with evidence and any outstanding decision. Update the canonical task owner, not a second orchestration ledger.

Keep task outcome, runtime state, window visibility, registration and release status separate. Stop or remove resources only when authorized, within actual capability and after checking ownership. Preserve the identities and history needed to resume or audit the work.

## Build and verify a feature fleet

This candidate workflow is for an explicitly authorized build fleet with an agreed specification and implementation plan. It is not the default for research, ordinary messages or every Voyager task. Trial it on real slices and compare intervention, rework and verification outcomes before shared adoption. A skill cannot grant service permissions.

### Assign one captain

Give one captain responsibility for the complete feature, integration, cohesion and quality. Only that captain creates workers and assigns their work. Builders and verifiers may exchange questions and evidence but do not instruct each other or create agents. Use one delegation layer. Fleet membership is grouping, not permission; check the actual service contract before any operation. If required permissions or communication are unavailable, report the gap rather than substituting owner access.

The captain reads the full agreed specification and plan, then sends each worker the bounded assignment and relevant source sections. Use the existing plan for task state, dependencies and verification attempts. Do not maintain a second fleet task list. Set concurrency and any resource budget for the authorized run; do not assume unlimited workers.

### Build, check cohesion and verify each slice

1. Dispatch independent slices in parallel only where write ownership and dependencies permit. Builders follow the project's implementation and testing skills and return their changes, passing checks and evidence.
2. Check that the result fits the specification and other completed work. Return a cohesion failure to its builder with specific findings; do not send known-incoherent work as a verification candidate.
3. Assign independent verification. Every pass includes systematic `code-review-and-quality`, relevant tests and analysis, and the affected end-to-end user journey on the real product. Neither code review nor runtime proof substitutes for the other. Missing access or evidence means verification is incomplete.
4. Have the verifier return one consolidated report to the captain, identifying the reviewed revision, checks, evidence and required fixes. The captain assigns corrections to the builder; the verifier does not direct the builder.
5. Allow the first verification and one correction attempt followed by re-verification. If required findings remain, escalate with what failed and what was tried. Do not reset the attempt count by replacing a worker, renaming a slice or reclassifying a failure. Avoid an unbounded cohesion-fix loop before verification; if the next attempt has no supported path forward, escalate.
6. After a slice passes, notify the user with what is ready, how to try it and links to verification evidence. Continue authorized work without waiting for acknowledgement. A progress update is not an approval request, and silence is not approval. Retain the ability to incorporate user steering.

### Integrate and finish

The captain integrates the slices and runs the complete feature checks. Then assign a fresh verifier that did not build or coordinate the feature to independently review the integrated result against the full specification. Include systematic code review, relevant tests and analysis, and the complete real user journey. Use the same first-pass, one-correction, re-verification limit for this final stage.

Choose an acceptable in-scope solution when one meets the specification. Record optional improvements for later. Escalate when success requires changing scope or weakening acceptance criteria; do not silently lower the bar. Tie proof to the actual reviewed result and recheck affected evidence after changes.

Finish with integrated, independently verified work ready for user review. Report remaining limitations and evidence through the existing project records. Recursive delegation, deeper management layers and automatic shipping are outside this workflow. Technical acceptance does not authorize merge, activation or release.

## Common Rationalizations

| Rationalization | Response |
|---|---|
| A higher rank can instruct any lower-ranked agent | Inspect actual assignments and capabilities. |
| The Fleet owns all its members | Visual grouping and authority are separate. |
| The launch receipt says completed | Verify the intended task outcome and native completion. |
| A new agent will be easier than recovering the current one | Resolve the existing operation before proposing replacement. |
| A reviewer approved it, so it can ship | Technical acceptance and human release authority are separate. |

## Red Flags

- Project rules or coding practices copied into this coordination skill.
- Rank names used to bypass assignment checks.
- A second task list maintained alongside the canonical plan.
- Uncertain delivery followed by repeated effects.
- A result reported as complete without artifacts and attributed execution evidence.

## Verification

- The installed service contract and capabilities were checked.
- Each assignment retained its project's context and bounded authority.
- Dependencies and write ownership were respected.
- Identifiers and receipts distinguish delivery from completed work.
- Decisions are attributed to the authorized actor and exact request.
- Integration and release status are stated separately.
