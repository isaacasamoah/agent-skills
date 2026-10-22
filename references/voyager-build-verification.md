# Optional build-and-verification workflow

Candidate for the user-selected Osmani development setup. This is not a Voyager requirement. Other setups supply their own workflow and quality checks. Review and trial before adoption.

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

