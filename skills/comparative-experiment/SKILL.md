---
name: comparative-experiment
description: Compares research hypotheses or technical approaches using a planned experiment and comparable data. Use when running controlled trials, comparing methods or benchmarks, or preparing batches of independent research experiments. Not for a single capability proof, literature-only research or ordinary performance debugging.
---

# Comparative Experiment

## Overview

Choose tests that distinguish plausible explanations and approaches. Make both practical progress and changes in understanding visible, without turning an attractive score into an unsupported conclusion.

## When to Use

- Two or more approaches could solve the problem and evidence should guide the choice.
- A research question needs hypotheses, controlled inputs and measured outcomes.
- Several independent trials can share a comparison protocol and run as a batch.

**Not for:** proving one uncertain capability (`feasibility-experiment`), a literature review without new observations (`source-driven-development` for software sources), or diagnosing a measured bottleneck (`performance-optimization`).

## Process

### 1. Frame the question and research existing approaches

Read the relevant brief, prior attempts and raw examples. State the question, the decision it informs and the current observation separately from its possible explanations.

Search primary literature and creator documentation for established approaches before proposing variants. Read relevant full sources rather than relying on search summaries. Record versions, assumptions, contradictory findings and evidence limits. For software, follow `source-driven-development`.

Select research tools by the question: scholarly search for papers, citation metadata for source identity, repository inspection for actual implementations, and a reproducible analysis tool for measurements. Discovery finds candidates; it does not establish that their claims are true. Avoid installing a research framework unless the experiment needs it.

### 2. Agree the hypothesis and comparison protocol

Write an explanation and a discriminating prediction. Template:

> We think X accounts for observation Y because of evidence Z. We will compare A with B. If X is right, we expect this outcome; this other outcome would count against it.

Use [the experiment protocol](../../references/experiment-protocol.md) as the single owner of shared record and evidence fields. Before results are visible, fix:

- Baseline, variants, variables under investigation and what stays constant.
- Data source, inclusion criteria, sampling unit and whether examples are natural or constructed.
- Primary outcome, relevant error categories, cost/time and the improvement that would matter.
- A repeat, paired or blocked design appropriate to variability; randomize order when order could bias the result.
- Budget, stopping rule and an untouched confirmation set or repeat when selecting among many candidates.

Choose metrics at the boundary of the claim. Measure intermediate stages and the final outcome separately; an improvement in one stage does not establish an improvement in the whole system.

**Example: a knowledge-sharing pipeline.** Candidate retrieval, relationship classification, notification usefulness and improvement in the final work are different outcomes. Finding more relevant candidates does not by itself establish that the resulting notifications help anyone.

### 3. Prepare independently runnable trials

Record each trial's protocol revision, variant, input set, environment, seed where meaningful, resource budget and unique output location. The record must be sufficient without earlier conversation or "same settings as before".

Keep the shared evaluator and source data fixed. Identify conditions that could couple the trials and account for them in the comparison.

**Example: shared hardware.** Two benchmarks using one GPU may compete for resources. Separate code directories do not make their timing measurements independent.

### 4. Run, inspect and compare

Record all attempts, including failures, exclusions, neutral results and discarded variants. Check actual outputs against summaries. Use the agreed controls and costs. A failed run is a failed run, not a zero-quality measurement unless that treatment was defined beforehand.

Compare matching units and conditions. Report sample sizes, observed effects, variability and uncertainty. Identify dependencies between observations before treating them as independent repetitions. If statistical inference is appropriate, use a suitable method and state its assumptions; do not manufacture significance from a tiny or dependent sample.

**Example: transcript research.** Several messages from one conversation may share the same context and cannot automatically count as independent repetitions.

Separate exploration from confirmation. After inspecting many variants, freeze the selected candidate and evaluate on the untouched confirmation data or independent repeat. A changed criterion starts a newly labelled comparison; it cannot rewrite the old result.

### 5. Explain what changed and choose the next test

Answer both: did the behavior improve, and did our understanding improve? Show examples alongside measurements. Update the current explanation, keeping rejected alternatives and unresolved questions visible.

Use the protocol's result states. A tie, tradeoff, null result or inconclusive comparison is a valid outcome. Choose the next attempt because it distinguishes a remaining explanation, within the agreed budget. Report a need for more budget rather than silently extending it.

## Common Rationalizations

| Rationalization | Reality |
|---|---|
| "We changed several things, but the score improved" | Attribute the combined result only to that combination; isolate effects before claiming a cause. |
| "An intermediate metric improved, so the whole system is better" | Each stage and the final outcome require evidence that measures that claim. |
| "The best of ten must be better" | Selection can reward noise. Confirm the frozen choice independently. |
| "Separate runs are independent" | Shared resources and source data can still couple the observations. |
| "The unsuccessful runs are uninteresting" | They constrain explanations and prevent repeating dead ideas. |

## Red Flags

- No baseline or comparison plan before viewing results.
- Different data, models or budgets presented as a controlled comparison without qualification.
- Evaluator or selection criteria changed to favor a candidate.
- Tiny, synthetic or correlated samples described as general evidence.
- A leaderboard without an explanation of the changed cases or practical tradeoffs.
- Completed trial counts used as evidence of improved outcomes.

## Verification

- [ ] The question, hypotheses, fixed conditions and primary outcome precede the runs.
- [ ] Each trial has complete inputs, ownership, output identity and resource bounds.
- [ ] Raw measurements and failures are retained and comparable under the protocol.
- [ ] The conclusion distinguishes stages, data provenance, uncertainty and costs.
- [ ] Candidate selection and confirmation are separated or the absence is explicit.
- [ ] The current explanation and next discriminating test are understandable without the transcript.
