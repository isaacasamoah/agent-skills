---
name: voyager-orchestration
description: Coordinates authorized agent work through Voyager using delegation, communication, escalation, adjudication and Fleets. Use when the user or approved workflow explicitly selects Voyager for coordination. Not for choosing a development process, writing specifications, a single review, or parallel work without Voyager selection.
---

# Voyager orchestration

## Overview

Coordinate the user's chosen workflow through Voyager. Each participant keeps its project instructions, content skills and permitted tools. Voyager provides identity, authority, delivery and lifecycle information.

## When to Use

- The user wants existing or new Voyager agents to collaborate on an authorized task.
- An approved workflow selects Voyager to coordinate its assigned work.
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

- the outcome and acceptance criteria, with the required check, expected result and evidence for each criterion;
- the owner and permitted source/worktree, starting revision and write scope;
- links to the project's own instructions, inputs and relevant content skill;
- dependencies and what must finish before this task starts;
- the already-approved output destinations;
- the allowed actions, review and release boundaries;
- any agreed resource limit and stopping condition;
- the evidence and report required for completion.

Keep required results distinct from optional improvements. Judge required criteria as pass, fail or inconclusive against the actual reviewed result. Missing evidence is not a pass, and the worker cannot weaken a criterion to satisfy it.

Reuse the canonical plan entry if it already contains these fields. Send a short assignment with references rather than copying the whole project context into every agent.

### 3. Delegate and observe

Reuse an appropriate assigned agent when its identity, permissions and state fit the task. Create a new agent only when authorized and supported. Do not change ranks or assignments beyond the caller's actual authority.

Run independent tasks in parallel. Serialize conflicting writes and dependent tasks. Allocate disjoint worktrees or file ownership as the project requires. Do not ask workers to ignore each other's changes.

Retain the service's request, session and turn identifiers and event cursor. On an uncertain response, inspect the existing operation. Do not launch a replacement or repeat the effect simply because an acknowledgement was lost.

Use supported events or bounded observation to track progress. Delivery acceptance is not task completion. A closed viewer, quiet terminal or completed tool call is not evidence that the requested result exists.

### 4. Escalate and adjudicate

Escalate a concrete decision to the assigned supervisor or owner using Voyager's supported route. Include the unresolved question, relevant evidence, alternatives and the action waiting on the answer. Continue only independent authorized work.

A recorded escalation is still an unanswered question. Do not treat delivery, silence, elapsed time, another agent's assertion or a review verdict as the user's approval.

Adjudicate only within assigned authority. Compare the result with its acceptance criteria and evidence. State acceptance, a specific revision request, or the resolved decision through the supported operation. Preserve the actual human decision and its scope when relaying it. A supervisor's technical acceptance does not grant human-reserved merge, release, publication or spending approval.

### 5. Reconcile and report

Verify the returned artifacts and relevant successful native completion event, with correct task, session and revision attribution. Report partial, failed, blocked and uncertain outcomes explicitly. A successful event does not prove the artifact is correct.

Have the designated integrator reconcile interfaces and run the project's required integration checks. Return the result through the assignment chain with evidence and any outstanding decision. Update the canonical task owner, not a second orchestration ledger.

Keep task outcome, runtime state, window visibility, registration and release status separate. Stop or remove resources only when authorized, within actual capability and after checking ownership. Preserve the identities and history needed to resume or audit the work.

## Workflow boundaries

Voyager provides communication and permitted coordination operations. The selected workflow supplies roles, sequence, quality checks and stopping conditions. Changing development skills must not require rewriting Voyager's coordination procedure. Changing the coordination provider must not require rewriting the development skills.

Use this skill only when Voyager is selected for the coordination. Parallelizable work, an installed Voyager app or a request for one review is not a trigger by itself. Do not also launch workers through another command or agent framework for the same assignment. An existing workflow command that launches its own agents needs an explicit adaptation before Voyager takes over that launch responsibility.

Osmani's orchestration-patterns reference describes how its commands and personas compose; it is not a second auto-triggered skill. It remains guidance for that setup. Do not change upstream persona rules or silently run an entire development lifecycle merely because Voyager can delegate.

If the user explicitly selects the candidate captain/build/verify workflow, read [the optional workflow](../../references/voyager-build-verification.md). It owns the specific review skill, two-pass limit and final verifier. Other projects may supply a different procedure. Its availability does not authorize execution, and its restrictions do not redefine every Fleet.

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
