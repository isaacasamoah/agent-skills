# Optional delegated build-and-verification workflow

Candidate for the user-selected Osmani development setup. The procedure is independent of its coordination provider. Voyager is one explicit binding; another provider must meet the same assignment, evidence and permission requirements. This procedure is not a Voyager requirement. Review and trial before adoption.

## Separate the procedure from its coordination provider

This reference owns the build sequence, worker roles, quality checks, correction limits and definition of done. It consumes an agreed specification and plan. The chosen provider owns identity, permitted agent creation, communication, delivery and execution observations. It must distinguish assigning work from reporting information, and accepted delivery from completed work.

Select one provider for the run. If it cannot supply independent verification, bounded assignments or required completion evidence, report the gap before dispatch. Do not quietly substitute another launcher, broaden permissions or treat a message as an instruction. No provider-specific command belongs in a builder's development skill.

## Choose the execution mode

Keep the user's ordinary supervised development flow as the default. Select this candidate only when the user explicitly requests a delegated build-and-verify run, or an already-approved workflow explicitly selects it. A large plan, parallelizable work, the word "auto", or Voyager being available does not select it.

| Request | Behavior | Does not imply |
|---|---|---|
| Implement the next task, or `/build` where that command is installed | The current builder completes the next planned task with its required checks, then stops. | A fleet, whole-plan execution or automatic independent review. |
| `/build auto` or `/build all`, where installed | The current builder follows the existing command: require a spec, establish the baseline, prepare/approve the plan if needed, and execute its tasks in dependency order with the same testing loop and blocker rules. | A fleet or a fresh independent verifier after each slice. |
| Run the approved spec and plan as our delegated build-and-verify workflow with an explicitly selected provider | One authorized captain assigns builders and independent verifiers, checks cohesion, integrates, reports and escalates within this reference. | Design/spec/plan generation, recursive delegation or shipping. |
| Use Voyager to send a task, gather reports, or request a review | Follow generic voyager-orchestration and the selected task procedure. | This whole-feature workflow. |
| Review the result, or `/review` where installed | Follow code-review-and-quality. The actual command runs its skill in the current session; a separate reviewer must be assigned explicitly. | A new independent context merely because the word review was used. |

The command names above describe existing wrappers, not new Voyager commands or a claim that they are installed in every setup. Preserve the existing [build command](../.claude/commands/build.md) unchanged. A bare request to build follows the project default; do not silently upgrade it into whole-plan or delegated execution. If a request combines incompatible modes, clarify that selection before launching workers.

## Triggers, exclusions and examples

Start only when all are established: the selected workflow, approved spec and plan, permission to delegate through the selected provider, available capabilities, explicit assignment criteria and an applicable resource bound. Missing inputs are a preparation blocker, not permission for the captain to invent them. The coordinator may be a standalone vessel with explicit authority; visible Fleet grouping is optional and never grants authority.

| Example request | Expected routing |
|---|---|
| "Use our build-and-verify workflow through Voyager for this approved spec and plan. Delegate the slices and return the verified feature." | Select this candidate; check inputs and actual permissions, then execute the authorized run. |
| "Continue the same authorized build-and-verify run from its recorded next slice." | Resume that run and its existing task/attempt records. Reconcile uncertain operations before continuing. |
| "Build the next slice and let me review it." | Ordinary single-task build and stop. |
| "Run build auto on this plan." | Existing build-auto procedure. No automatic fleet. |
| "Here is a spec. Work out the plan." | Planning, with its own review boundary. No fleet. |
| "These tasks could run in parallel." | A possibility to assess, not delegation authorization. |
| "Group these agents into a fleet." | Grouping only; no instruction rights, shared goal or build run inferred. |
| "Use Voyager to ask another agent to review this diff." | Generic authorized delegation plus the review procedure, not whole-feature execution. |
| "Use our existing ship command." | Existing shipping procedure. Do not also create this workflow's worker set. |
| "Launch a build fleet" when several workflow definitions exist | Identify the intended saved workflow and inputs before dispatch; the label alone must not select an arbitrary process. |

## Relationship to the existing orchestration reference

The [orchestration pattern catalog](orchestration-patterns.md) favors direct work and user-steered transitions between specification, planning, building, review and shipping. This candidate begins after specification and planning are agreed, and ends with a verified feature for user review. It automates only the explicitly delegated build-and-verify interval. Scope decisions, exhausted corrections and release remain at their established boundaries.

The captain must add concrete value through dependency scheduling, integration, cohesion and acceptance decisions. A captain that only relays or paraphrases results should be replaced by the simpler direct workflow. Workers stay single-purpose and never delegate. Do not invoke a command that starts a competing coordinator or another worker tree for the same assignment.

A slice builder receives only its bounded slice and relevant spec context. It uses incremental-implementation and test-driven-development directly; do not send it `/build auto` for the full feature plan. The captain alone owns progress in the canonical full plan. Builder reports distinguish implemented/passing-local-checks from independently verified. This prevents the builder's completion mark from releasing dependent work prematurely.

This is a candidate outside the endorsed upstream catalog. Its addition rule requires at least two real uses, a concrete demonstration artifact, a reason existing patterns were insufficient and an identified failure mode. No real fleet trial has established those conditions yet. Do not present the reference or deterministic checks as proof of improved outcomes.

### Assign one captain

Give one captain responsibility for the complete feature, integration, cohesion and quality. Only that captain creates workers and assigns their work. Builders and verifiers may exchange questions and evidence but do not instruct each other or create agents. Use one delegation layer. Grouping is not permission; check the selected provider contract before any operation. If required permissions or communication are unavailable, report the gap rather than substituting owner access.

The captain reads the full agreed specification and plan, then sends each worker the bounded assignment and relevant source sections. Use the existing plan for task state, dependencies and verification attempts. Do not maintain a second fleet task list. Set concurrency and any resource budget for the authorized run; do not assume unlimited workers. Start with sequential slices unless the approved plan and run limits allow parallel execution. A stalled worker or missing evidence cannot cause indefinite waiting or automatic replacement; apply the agreed stopping condition and reconcile delivery state.

### Define what good looks like before dispatch

Each plan assignment states the required outcome, quality constraints, check or user action, expected result, environment and evidence destination. Add a baseline or known-different case when useful to establish that the check detects the relevant failure. The verifier reports pass, fail or inconclusive for each required criterion against the tested result. Missing evidence stays inconclusive. The captain may resolve a false-positive finding with evidence, but may not waive a valid required failure or lower the criteria to stay within the retry limit.

### Build, check cohesion and verify each slice

1. Dispatch independent slices in parallel only where write ownership and dependencies permit. Builders follow the project's implementation and testing skills and return their changes, passing checks and evidence.
2. Check that the result fits the specification and other completed work. Return a cohesion failure to its builder with specific findings; do not send known-incoherent work as a verification candidate. Before starting the run, specify the pre-verification correction limit in the plan. Proposed initial default: one cohesion correction attempt, then escalation if the result still does not fit. This is a trial default, separate from the confirmed verification-pass limit.
3. Assign independent verification. Every pass includes systematic `code-review-and-quality`, relevant tests and analysis, and the affected end-to-end user journey on the real product. Neither code review nor runtime proof substitutes for the other. Missing access or evidence means verification is incomplete.
4. Have the verifier return one consolidated report to the captain, identifying the reviewed revision, checks, evidence and required fixes. The captain assigns corrections to the builder; the verifier does not direct the builder.
5. Allow the first verification and one correction attempt followed by re-verification. If required findings remain, escalate with what failed and what was tried. Do not reset the attempt count by replacing a worker, renaming a slice or reclassifying a failure. Avoid an unbounded cohesion-fix loop before verification; if the next attempt has no supported path forward, escalate.
6. After a slice passes, notify the user with what is ready, how to try it and links to verification evidence. Continue authorized work without waiting for acknowledgement. A progress update is not an approval request, and silence is not approval. Retain the ability to incorporate user steering.

### Integrate and finish

The captain integrates the slices and runs the complete feature checks. Then assign a fresh verifier that did not build or coordinate the feature to independently review the integrated result against the full specification. Include systematic code review, relevant tests and analysis, and the complete real user journey. Use the same first-pass, one-correction, re-verification limit for this final stage.

Choose an acceptable in-scope solution when one meets the specification. Record optional improvements for later. Escalate when success requires changing scope or weakening acceptance criteria; do not silently lower the bar. Tie proof to the actual reviewed result and recheck affected evidence after changes.

Finish with integrated, independently verified work ready for user review. Report remaining limitations and evidence through the existing project records. Recursive delegation, deeper management layers and automatic shipping are outside this workflow. Technical acceptance does not authorize merge, activation or release.


## Voyager binding

When the run explicitly selects Voyager, use voyager-orchestration for supported CLI operations, identity, permissions, delivery reconciliation and completion evidence. Inspect current capabilities. Preserve the caller environment and request identifiers. Map the coordinator to a vessel with the required explicit authority and workers to permitted assigned vessels. Fleet grouping remains optional and does not define the workflow or grant rights.

Voyager's current send operation instructs an agent; it is not an unrestricted peer-information channel. If the selected workflow needs a communication capability that the service lacks, report that gap or use an explicitly agreed coordinator-mediated route. Do not assume a new messaging command exists.

Do not run the normal command's built-in delegation alongside Voyager delegation for the same work. A provider adapter translates these responsibilities; it does not rewrite the spec, checks, retry limits or release policy. The current adapter is a documented candidate, not a verified portable implementation.

## Trial and refinement

Before calling this an endorsed pattern, compare authorized real runs with the existing supervised or build-auto approach using the same acceptance criteria. Record missed defects, user intervention, rework, integration failures, elapsed time and model use. Include missing/stale evidence, an unresolved second verifier pass, an unavailable real-product check and uncertain delivery. Verify that none produces a false completion, duplicate worker or silent scope change.

The useful question is whether the captain produces a more coherent, correctly verified feature for acceptable effort. If it only adds messages, use the simpler mode. Refine these examples from observed routing failures rather than adding broad triggers that select fleets for ordinary work.
