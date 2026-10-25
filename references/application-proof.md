# Application proof

Use this local standard when planning, implementing or reviewing user-facing application behavior. It supplements the selected development workflow and the project's CONSTRAINTS.md. It does not change upstream skill procedures, task completion, review ownership or release permissions. This is an approved trial standard; its effectiveness still needs evaluation in real builds.

## Keep one maintained proving fixture per application

Extend the application's existing runner with reusable actions and small named user journeys. Share launch, input, observation, identity checks and cleanup. One fixture may contain several files and support several surfaces. Do not copy a complete runner for each feature, specification or branch.

Keep the fixture versioned with the application. Ordinary Git checkouts contain their own copies of that source; they are not separate fixture designs. Run the candidate revision's fixture against the candidate application. Integrate shared improvements through the normal Git workflow, without creating a mutable runner outside version control or importing unreviewed changes from another branch.

Each run owns its state, output and processes. Record the candidate revision and launch configuration. Verify process ownership before cleanup. Serialize native input or audio work when runs share a desktop and cannot be isolated. A shared fixture must not imply shared mutable runtime state.

Use the existing specification's acceptance criteria to name the required journeys, outcomes and relevant failure states. Record which are automated, manually demonstrated or unproved. This describes required user capabilities, not every possible combination of inputs. Keep unit and boundary tests where they provide distinct evidence; do not force all verification through the UI.

Exercise the real user surface for user journeys. Service responses and logs can corroborate the result but cannot substitute for the interaction being claimed. Name simulated or unavailable surfaces explicitly. When consolidating runners, prove that the accepted journeys still work before removing their old implementations. Start with the active change, not a rewrite of historical tests.

## Keep acceptance code within the test budget

Authored tests and proving code used for acceptance must not exceed the production code they actually exercise. This is a size constraint checked in review, not a coverage metric or evidence of correctness.

Before implementation, record the measurement scope and proving command in the project's existing CONSTRAINTS.md. If the contract is absent, establish it through [constraint-driven-development](../skills/constraint-driven-development/SKILL.md). Preserve existing project rules. Report a conflicting rule for resolution rather than silently choosing a weaker interpretation.

In the normal review evidence:

1. Name the candidate revision, test files, shared helpers and one-off proving scripts. Include authored fixture setup, fakes, drivers, mutation helpers and programs embedded in generated strings, wherever stored. Count each source line once in the combined inventory. Report maintained and one-off subtotals.
2. Name the production files or function ranges those checks exercise. Count the union of those ranges once. Whole-file size alone does not establish that the whole file is exercised. Do not use unrelated application code to enlarge the budget.
3. Count physical lines in normally formatted source. Record repeatable commands, such as `wc -l FILE` and `sed -n 'START,ENDp' FILE | wc -l`, with the exact inputs. Report complete totals and the change's additions and deletions. Include shared helpers in the total even if this change did not modify them.
4. Exclude unmodified third-party frameworks from both sides. Count custom replacements and authored extensions. Screenshots, logs and generated evidence are outputs, not authored tests; a custom program that validates those outputs is acceptance code. A generic line-count command is only measurement.
5. Show that a relevant broken behavior fails its check, using a focused mutation or equivalent negative control under [code-review-and-quality](../skills/code-review-and-quality/SKILL.md). Reuse existing checks where they already provide this evidence. Keep systematic review and real-surface proof alongside the size result.

Do not pad production code, compress test formatting, remove necessary assertions or weaken journeys to meet the cap. Simplify duplication while retaining effective checks. If the necessary proof still exceeds the budget, report the counts and conflict and stop acceptance. Only the user can approve a policy change. Existing test volume is not an automatic exception.

## Finish with evidence

The review must identify the fixture used, exercised journeys, unavailable checks, source inventory, counts and defect-detection result. Use the project's existing review artifact, not another task ledger. A green build, a small test suite or an installed instruction alone does not establish that the application works.

The selected workflow still owns implementation, independent review where required, completion and shipping. This reference does not start orchestration or authorize merging or releasing. Refine the standard from observed build results, including duplication removed, defects detected and necessary proof blocked by the cap.
