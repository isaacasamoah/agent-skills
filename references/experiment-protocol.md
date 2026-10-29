# Experiment protocol

Shared by `feasibility-experiment` and `comparative-experiment`. Keep one authoritative experiment record; reports and trial summaries are views of it. Use the project's established record location and format. Do not copy private transcripts into a public repository.

## Before a run

Record enough to reproduce the attempt without the conversation:

| Field | Meaning |
|---|---|
| Identity | Experiment, protocol revision, trial and variant IDs |
| Question | What is uncertain and which decision the answer informs |
| Claim | Capability or explanation under test, including its scope |
| Prediction | Expected observation and evidence that would count against it |
| Conditions | Required real surface, inputs, permissions and dependencies |
| Change | Variables this attempt may change |
| Controls | Baseline and conditions kept fixed |
| Data | Source, inclusion rule, sampling unit, dataset version or hash |
| Evaluation | Primary outcome, error cases and practical decision criterion |
| Limits | Run, time, resource or cost budget and stopping rule |
| Ownership | Workspace, resources, owner and unique output destination |

For a small feasibility spike, omit comparison-only fields that do not apply and explain the missing baseline if necessary. For comparative work, record concrete settings rather than "as before". The trial description must agree with the frozen record.

## Evidence from each attempt

- Actual source revision, patch or dirty-state snapshot and environment versions.
- Exact setup and commands or user actions, including relevant settings and seeds.
- Inputs and raw outputs, error evidence and measurements with units.
- Observed real-surface effects, distinguishing transport receipts from outcomes.
- Substitutions, deviations, resource contention, failed runs and exclusions.
- Expected versus actual result and the claim it supports or weakens.

Evidence is a pointer to an actual artifact or observation, not an assurance of success. Preserve the raw result if a summary or derived judgment is later corrected. Keep secrets and unrelated private data out of records.

## Result states

| State | Use |
|---|---|
| Supported in scope | The stated criterion was met under the recorded conditions |
| Not supported in scope | A valid observation failed the stated criterion |
| Inconclusive | The evidence cannot distinguish the relevant explanations |
| Blocked | A required resource, access or condition prevented a valid attempt |

A comparison can support a practical choice without establishing a universal causal explanation. An unsuccessful implementation does not establish impossibility. A failure of the test setup does not become evidence against the underlying idea unless the protocol makes that failure the outcome of interest.

## Trial integrity

Each trial refers to the frozen protocol revision and identifies its variant and inputs. Keep the evaluator and shared inputs fixed, retain distinct outputs, and record any resource interference that could affect comparison.

Record effective settings and environment; requested settings are not evidence of effective settings. Explain missing or non-comparable runs before aggregation. Never overwrite another trial's result to make the record complete.

## Close or resume

Keep the current question, current understanding and next proposed test easy to find. Retain each attempt's reason, prediction, result, interpretation and evidence link. Record rejected explanations as well as successful variants.

Stop at the agreed limit. Record unresolved questions and any further authorization needed. A fresh session reads the current record and actual workspace state before continuing. A new direction or changed evaluation is a new labelled comparison, not a silent rewrite of past evidence.
