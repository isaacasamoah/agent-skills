---
name: elucidate
description: Explains a working prototype through a source-grounded interactive HTML architecture walkthrough. Use when mapping systems and interfaces, following end-to-end journeys or distinguishing current behavior from proposed changes before specification. Not for writing the implementation plan or reviewing a finished diff.
---

# Elucidate

## Overview

Make a prototype understandable enough for its owner to explain, challenge and deliberately improve the design. Produce an interactive HTML architecture guide grounded in source and observations, with proposals visibly separate from the implementation.

## When to Use

- A prototype works, but its full structure and behavior need to be understood before specification.
- The user wants to inspect components, interfaces and code through a connected architecture map.
- Feedback and release constraints need to be placed against the system they affect.

**Not for:** a narrow code question, authoring requirements from scratch (`spec-driven-development`), scheduling implementation (`planning-and-task-breakdown`), or judging a finished change (`code-review-and-quality`).

## Process

### 1. Establish the design question and freeze the evidence

Read the user's brief, drawings, prototype instructions, recorded experiments and accepted decisions. Confirm the intended audience, scope and established document home. Inspect the actual repository, revision and dirty state.

Identify the source snapshot and any running artifact separately. Record which observations belong to which revision. If source or required evidence is missing, mark the specific gap rather than filling it from a previous discussion.

### 2. Trace the system from real entry points

Map the components that own behavior, the data they own and the interfaces between them. Trace representative user journeys through UI, service, processes, storage and external dependencies as applicable. Follow failure, recovery, permission and lifecycle paths where they change the explanation.

Read relevant source directly. Use targeted investigation for an uncertain subsystem; optional independent readers may divide a large system when available and authorized. Reconcile their claims against source before presenting them.

Define product and code vocabulary consistently. Distinguish records from live processes, requested effects from completed outcomes, and relationships that look similar but have different semantics. Use the project's real distinctions rather than imposing a generic architecture.

### 3. Build the architecture model

Create meaningful component nodes and explicit interface edges. Every node identifies its responsibility, owned state and source. Every edge names its endpoints, direction, transport or call mechanism, payload and relevant error or permission semantics.

Support progressive detail: overview, concise explanation, behavior and invariants, then source links or selected excerpts. Pin links to the inspected revision when possible. Link UX demonstrations for timing, gesture or visual behavior that prose cannot adequately specify.

Mark each claim as implemented, observed under stated conditions, proposed, deferred or unresolved where that distinction matters. Source inspection does not establish that the native application, installation or platform support works.

### 4. Explain the proposed improvements with the user

Place feedback and proposed changes next to the affected components or interfaces. Explain the concrete consequences for clarity, knowledge ownership, coupling and required protections. Use the project's chosen principles; do not decorate the map with unsupported quality scores.

Present meaningful alternatives and their tradeoffs when a design decision remains open. Separate the current implementation from the preferred design and let the user participate in consequential choices. Do not quietly turn an explanation into an accepted redesign.

When requested, add a separate release view identifying scope, deferred capabilities, platform gaps, packaging, lifecycle and upgrade constraints, proof needed and approval points. This is design input for specification and planning, not permission to execute that release.

### 5. Deliver and test the reading surface

Save one canonical HTML guide in the agreed project location. Keep supporting evidence and structured data linked. Build the diagram and detail panes from one consistent architecture model rather than maintaining independent copies of the same facts.

Test node and edge selection, journey navigation, source links, keyboard operation and readable narrow layouts. Inspect the rendered guide. Prefer a portable local page; if a dependency needs a network connection or special viewer, state that requirement.

Walk through a complete journey with the user. Invite corrections and questions; use them to update the same guide. Do not require a quiz or treat a read receipt as shared understanding.

### 6. Hand the understood design to specification

Record accepted changes, proposals still awaiting choice, factual gaps and demonstrated limits. Link the guide, code sketch if one exists, prototype or UX references and relevant experiment evidence from the design handoff.

Invoke `spec-driven-development` only when requested or authorized to proceed. That skill owns the requirements and approval process; `api-and-interface-design` owns detailed contract design. Link those artifacts instead of writing another competing specification here.

## Common Rationalizations

| Rationalization | Reality |
|---|---|
| "The diagram explains the architecture" | Unnamed edges and disconnected boxes do not explain the behavior. Trace a real journey to source. |
| "The code exists, so the feature works" | Source establishes implementation; runtime observations establish behavior under their stated conditions. |
| "The new design is cleaner, so show only that" | The user needs to distinguish what exists from what they are being asked to choose. |
| "A long source listing is complete" | Detail must support a coherent explanation and be discoverable from the overview. |

## Red Flags

- Nodes have no meaningful ownership or edges have no interface semantics.
- Proposed and deferred behavior is drawn as implemented.
- Source links float to a changing branch or refer to another revision without disclosure.
- The explanation hides failures, platform assumptions or unsupported journeys.
- The guide passes static checks but its interactions were never exercised.
- A separate prose specification repeats the map's facts and begins to diverge.

## Verification

- [ ] The source snapshot, evidence scope and outstanding gaps are recorded.
- [ ] Components and interfaces trace to actual source at that snapshot.
- [ ] Complete journeys explain behavior, ownership and relevant failure boundaries.
- [ ] Current, observed, proposed and deferred claims remain distinguishable.
- [ ] The HTML guide's interactions, links, keyboard use and layout were exercised.
- [ ] User feedback and accepted decisions update the canonical guide.
- [ ] The specification handoff links the guide and experience evidence without duplicating their authority.
