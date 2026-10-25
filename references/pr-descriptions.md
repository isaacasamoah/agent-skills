# Readable PR descriptions

Use this local standard when creating or updating a pull request title or body. Follow [git-workflow-and-versioning](../skills/git-workflow-and-versioning/SKILL.md) for the Git workflow and [code-review-and-quality](../skills/code-review-and-quality/SKILL.md) for review. This reference changes presentation, not their procedures, completion criteria or merge permissions.

Apply the developer writing guidelines and [Unslop](../skills/unslop/SKILL.md) before drafting and in a final editing pass. Write for a reader who does not know the codebase. Lead with the problem and resulting behaviour, explain unfamiliar terms, and keep material failures and uncertainty visible. Give the title the same care. Adding headings around internal terminology does not make an explanation clear.

## Explain the change and its evidence

Use these sections as the default structure. Preserve intentional project-template requirements. For a small change, keep each section brief or combine related points without losing the information. Link detailed evidence rather than repeating the development log.

### Before and after

Explain the previous problem, its effect on the user and the resulting behaviour. State the actual scope of this PR. A plan or instruction change does not establish that a later application change works.

### Verification

State which checks ran and their results. Name checks not run or still failing. Report existing evidence accurately; rewriting a description is not a new test run.

### Real-surface proof

Name the build and interface exercised, what the user or test did and what was observed. Distinguish simulations, recordings and direct observation. State what remains unproved. For documentation-only changes, explain why an application test was unnecessary and describe the relevant document or workflow check instead.

### Code review

Identify the reviewer, important findings, fixes and remaining blockers. Distinguish author inspection, independent agent review, user feedback and formal GitHub approval. If review has not happened, say so. Do not invent a reviewer or turn positive feedback into proof of an unmeasured requirement.

### Known limitations

Record material limits, unproved behaviour and necessary follow-up. If none are known, say that without implying exhaustive proof. Keep this section current as the PR changes.

## Publish the description where people read it

Use GitHub CLI for these operations. Put the exact Markdown body in a UTF-8 file with real newlines, then use `gh pr create --body-file FILE` or `gh pr edit NUMBER --body-file FILE`, with the explicit repository. Use `--title` for a changed title. Follow the existing authorization for remote changes; this reference grants no new authority.

For an existing PR, read its current title and body before editing. Preserve useful author content and project requirements. Re-read immediately before writing if another contributor may have edited it, and reconcile any change rather than replacing it with a stale draft.

Update the PR body, not a new discussion comment. GitHub may display the description in a card labelled "commented"; that does not make it a separate issue comment. Report an actual CLI or permission failure instead of substituting a comment or assuming authentication is unavailable.

After writing, use `gh pr view NUMBER --repo OWNER/REPO --json title,body,url` and compare the returned title and body with the intended text. Readback verifies persistence, not readability or application correctness. Review the prose separately from the perspective of an unfamiliar reader.

Use readable, verified PR and commit links. For unpublished evidence, link the appropriate local artifact in local handoffs; do not publish private paths or transcripts as though public reviewers can access them. Never fabricate an evidence URL.

## Trial and refine

In the next real PR, check whether the reader can explain what changed, distinguish automated checks from running-app observations, and identify remaining limits. Use that feedback to refine the standard. Installation and template checks alone do not prove clear writing.
