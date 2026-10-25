# Build walkthrough

Produce or update a walkthrough for every build, verification and review loop, including small PRs, correction rounds and work stopped for a decision. It is the user's plain-language digest of the PR or increment. Keep a small change brief; the standard is consistent information, not a minimum document length. A single test rerun or progress update is not a new loop.

The walkthrough explains the work and its evidence. The specification, implementation plan, test results and code reviews retain their existing authority. Writing a walkthrough neither performs those checks nor authorizes acceptance, merging, installation or shipping.

## Read the existing evidence

Use the approved intent, actual change, owning task records, review findings, test and real-surface receipts, relevant user decisions and current runtime state. Read the task transcript when it is needed to establish decisions or skill use. Keep original technical review records and run evidence with their owning source or existing approved evidence location, and link them from the walkthrough. Do not publish private transcripts. Name gaps rather than inventing missing evidence or rerunning the build just to write about it.

Identify the source revision and tested artifact separately from what is currently running. Verify readable PR, commit, source and evidence links. Apply the developer writing guidance and [Unslop](../skills/unslop/SKILL.md) before drafting and in a final pass.

## Explain the result and how to inspect it

Use these questions to organize one coherent account. Combine sections for smaller work and expand linked detail for larger work.

### What can the user do now?

Lead with the result and its status. Explain the original need, what changed and how the user encounters it. Use the product's familiar terms and explain unfamiliar ones. State whether the work is built, verified, awaiting inspection, blocked, merged or installed, without treating those states as interchangeable.

### How did we build and check it?

Explain the meaningful increments, dependency decisions and review/correction cycle. Connect important findings to the changes they caused. State when a stopping rule or user decision affected the work. Link the full reviews rather than reproducing every finding or narrating every tool call.

Explain which skills were actually used, when and why they applied, and what they changed about the work. Prefer a concrete account such as "The interface-design skill kept Resume separate from submitting work; the independent review checked that reading history submits nothing." A compact skill/action/evidence table can help. Do not list the whole catalog, infer invocation from a successful result or treat loading a skill as proof of following it.

### What does the evidence establish?

Summarize relevant automated checks, systematic review and real user journeys separately. Explain important constraints and how they were checked. Distinguish source inspection, simulated input, real-product observations and physical-device or platform evidence. Preserve failed, intermittent, unavailable and inconclusive checks. A passing repeat does not establish that the earlier failure was fixed.

### What should the user try?

Give the exact artifact or running app, necessary starting state, actions and expected visible results. Identify the cases where human inspection adds evidence the automation lacks. For example: stop a saved conversation, find it in Previous agents, resume it, and confirm that the same conversation opens without repeating its task. Do not imply that owner testing replaces the agreed technical checks.

### What remains, and what decision is needed?

Name meaningful limitations, unresolved issues and deferred work. Make the next decision explicit, including any remaining approval boundary. Keep a blocked result useful by explaining what is blocked, what is already established and the smallest decision needed to continue.

## Keep one readable account

Save the canonical HTML walkthrough in `explainer/walkthroughs/` within the approved project documentation home. Name it for the feature, such as `resume-panel-build-walkthrough.html`. Date snapshots; update a living walkthrough in place after each loop and show its latest verification date. Keep one canonical walkthrough per PR or increment, updating it for corrections rather than creating a document per retry. A feature with stacked PRs may use clearly linked PR sections in one walkthrough if each PR's outcome and evidence remain easy to find.

Use progressive detail: result and inspection instructions should be easy to find; source inventories, review histories and large skill tables can be linked or expandable. Screenshots belong in a neighboring `screenshots/` folder. Status and log link to the walkthrough rather than becoming duplicate reports or task ledgers. Keep the PR description useful on its own and give the local walkthrough a readable link to the PR. Link back from a public PR only when the walkthrough has an accessible public destination; do not present a private Obsidian path as a public source.

When later approval or a runtime change alters the result, revise the affected opening and inspection instructions consistently. Do not leave an obsolete "nothing is running" statement beside a newer trial-launch note. Preserve previous events as clearly dated history when they still matter.

## Check the walkthrough

- A reader unfamiliar with the implementation can explain what changed and why.
- Skill use is tied to actual work and evidence, with uncertainty stated where attribution is incomplete.
- Review, tests and real-surface proof retain their separate meanings and material limits.
- The user can follow the inspection steps and recognize the expected outcome.
- Current source, tested artifact, running state and next decision agree with the linked evidence.
- Local links and narrow-screen reading work, without creating a second development contract.
