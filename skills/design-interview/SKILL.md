---
name: design-interview
description: Clarifies unresolved design requirements in an existing brief, drawings, flows or prototype. Use when reviewing supplied design material, preserving specific UX requirements, or identifying decisions and feasibility questions before building. Not for discovering an intent from scratch or planning an already settled design.
---

# Design Interview

## Overview

Start from the user's design work and reduce uncertainty about what should be built. Preserve settled decisions and clarify the remaining requirements through a focused conversation.

## When to Use

- The user brings a design brief, drawings, flows or a prototype with unresolved requirements.
- Specific interaction details need to survive the transition from design to implementation.
- A design review needs to distinguish user choices from factual questions to investigate.

**Not for:** an underspecified initial idea with no design material (`interview-me`), generating idea variations (`idea-refine`), or decomposing an agreed specification (`planning-and-task-breakdown`).

## Process

### 1. Read and reflect the supplied design

Read the brief and relevant project context. Inspect drawings as images, not filenames or extracted text alone. Identify the revision or artifact being discussed.

Reflect the intended users, problem, journey and boundaries in plain language. Separate the user's decisions from your interpretations. Preserve their terminology and chosen interaction details.

### 2. Record what is settled and what is uncertain

Use the project's existing design artifact as the requirements record. Mark each important point as agreed, proposed, a factual question to investigate, or a decision needing the user. Link visual examples rather than replacing them with prose.

Look for gaps in the normal journey, failure and recovery, relevant permissions, UX behavior, constraints and exclusions. Include only the dimensions that affect this design. Investigate facts available in the code or supplied evidence before asking the user to decide.

### 3. Interview about the unresolved decisions

Read and follow the [interview-me process](../interview-me/SKILL.md) for questioning, confirmation and stopping. This skill supplies the existing design as its starting context.

Work through prerequisites before decisions that depend on them. Keep recommendations visibly provisional. When an answer changes the design, update the same requirements record and explain which earlier choice it affects.

For an uncertain capability, record the question a feasibility experiment must answer. Do not replace an unknown with an invented requirement or treat agreement on a design as evidence that it works.

**Example: reviewing a terminal interaction.** A brief may already require an ordinary terminal opened by the user, while leaving automatic voice activation undecided. Preserve the terminal requirement; discuss the voice preference. Whether that terminal can be controlled remains a factual question to test.

### 4. Close with the clarified requirements

Keep the confirmed design, remaining decisions and factual uncertainties together, with links to the drawings or prototype. Follow `interview-me`'s stopping rule before downstream work.

The result settles the requirements discussed. It does not certify feasibility, choose an implementation architecture or authorize a build. The design can inform a bounded experiment or `spec-driven-development` when that next step is requested.

## Common Rationalizations

| Rationalization | Reality |
|---|---|
| "I'll restart discovery to be thorough" | Existing decisions and drawings are evidence. Ask about the gaps. |
| "The sketch makes every requirement obvious" | A sketch may leave behavior, recovery and permissions unresolved. |
| "My recommendation is the requirement" | It remains a proposal until the user agrees. |
| "The user approved the design, so it must be feasible" | Capability needs evidence from an appropriate test. |

## Red Flags

- Replacing the user's specific experience with an easier generic design.
- Asking for facts already available in the supplied material.
- Reopening settled decisions without a concrete conflict or new evidence.
- Treating a proposed answer as an agreed requirement.
- Creating a competing specification instead of updating the design record.

## Verification

- [ ] The reflection matches the supplied brief and visual artifacts.
- [ ] Agreed requirements, proposals, factual questions and user decisions are distinguishable.
- [ ] The interview addressed unresolved decisions and preserved relevant interaction details.
- [ ] Changed answers update the existing requirements record and affected choices.
- [ ] Remaining uncertainty is explicit; design confirmation is not reported as feasibility proof.
- [ ] Confirmation and stopping follow the referenced interview process.
