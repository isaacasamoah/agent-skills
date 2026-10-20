---
name: feasibility-experiment
description: Tests whether an uncertain capability can work through a bounded code experiment on the real surface. Use when a technical spike, proof of concept or smallest real demonstration is needed before committing to a prototype. Not for comparing established approaches or verifying a finished release.
---

# Feasibility Experiment

## Overview

Answer one uncertain capability question with the smallest implementation that preserves the real conditions of the claim. Reduce surrounding complexity, not the requirement being tested.

## When to Use

- A proposed feature depends on behavior we have not established.
- The user asks for a bounded spike or proof that a specific mechanism works.
- A previous demonstration worked only with a prepared environment or privileged path.

**Not for:** routine implementation of a known capability, comparative research (`comparative-experiment`), or acceptance of a completed feature (`test-driven-development`, `browser-testing-with-devtools`, or the project's native proof procedure).

## Process

### 1. Agree on the claim and its real conditions

Read the design brief, project instructions and existing evidence. State:

- The capability under investigation and the decision this result will inform.
- The actual user journey and the boundary that could fail.
- Required inputs, environments, existing software and permissions.
- What observation would establish the bounded claim, what would contradict it, and what would leave it unresolved.

Keep generality explicit. "An ordinary terminal" and "a terminal launched by our harness" are different claims. If the brief says "any terminal", agree the intended domain and coverage needed; a successful sample cannot establish an unrestricted universal claim. A narrower interim result must remain narrower, not silently replace the brief.

Use [the experiment protocol](../../references/experiment-protocol.md) for the shared record, evidence and isolation requirements. Follow `source-driven-development` for version-sensitive mechanisms.

### 2. Choose the smallest discriminating experiment

Remove unrelated features, styling and abstractions. Keep every condition whose removal would make the test stop answering the question.

For docking, use an independently opened terminal if that is the claim. Do not require a special launch wrapper, transparent setting or cooperative provider simply because it makes identification easier. A substitute outside the uncertain boundary may be useful, but name it and explain what it prevents us concluding. A substitute at that boundary is not proof.

Include a known-different case that exposes a misleading success: an unrelated terminal must not be selected or controlled, for example. Choose relevant failure or recovery cases in proportion to the claim.

Agree a bounded scope, budget and stopping rule before running. If required access or hardware is absent, report the missing condition. Do not redesign the test to make it pass.

### 3. Implement and exercise the real path

Use an owned branch or isolated workspace and the project's existing tooling. Write only enough code to run the claim. Follow `test-driven-development` for new behavior that can be tested; those tests supplement the real-surface observation.

Exercise the actual interface, service or device named in the claim. Trace the action to its effect. A command receipt, a visible window, an event and a completed agent task are separate observations; check the ones the claim requires.

Capture setup, exact revision, actions, outputs and relevant negative cases. Have the user try an interaction when its feel or behavior is part of the question. Do not infer an experience from a screenshot or state flag.

### 4. Report the result without widening it

Apply the experiment protocol's result states. Show what worked, what failed, what was substituted and what remains unknown. Separate a failed attempt from evidence that the capability is impossible.

Offer the next discriminating test or a prototype path within the agreed budget. A successful experiment does not authorize production reuse, merging or release. Preserve the evidence and record whether the experimental code should be retained, replaced or remains undecided.

## Common Rationalizations

| Rationalization | Reality |
|---|---|
| "The prepared terminal proves docking works" | It proves that prepared path. Preserve the ordinary-terminal condition when that is the question. |
| "A minimal test can skip the native UI" | Only if the claim does not depend on that UI. Minimality does not remove the failing boundary. |
| "The request was accepted, so the action worked" | Verify the actual effect and completion the claim requires. |
| "The attempt failed, so the idea is impossible" | A failure may identify a broken setup, limited mechanism or missing evidence. |

## Red Flags

- A required condition disappears between the brief and the test.
- A mock, special account or cooperative launcher supplies the answer under investigation.
- The demonstration cannot distinguish the intended target from an unrelated one.
- Results are described more broadly than the environments exercised.
- Budget expiry is reported as success or silently restarts another loop.

## Verification

- [ ] The agreed claim, actual surface and scope are recorded before the run.
- [ ] The test preserves the uncertain boundary and records substitutions.
- [ ] The real action and required effect have attributable evidence.
- [ ] A known-different or failure case can expose a false success.
- [ ] Conclusions match the demonstrated scope; missing coverage remains explicit.
- [ ] The result, remaining uncertainty and next decision are recorded for a fresh session.
