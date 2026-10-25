---
name: unslop
description: Improve clarity when writing or editing prose for human readers. Use when drafting or revising reviews, explanations, documents or titles, when writing becomes verbose or hard to follow, or when asked to unslop. Apply before drafting and as a final editing pass.
---

# Unslop

## Overview

Use Unslop as a second check alongside the developer writing guidelines. It keeps prose clear when context overload or habitual verbosity makes those guidelines easy to miss. It supports both drafting new text and editing existing text.

Read [Lauren Tan's original Unslop rules](../../external-skills/unslop/SKILL.md) before using either mode. The original is preserved unchanged as a reference. This local entry controls discovery and adds Isaac's usage preferences; the original's explicit-only metadata does not govern this entry.

## When to Use

- Before drafting a substantial human-facing review, explanation or document.
- For every pull request title and description, alongside the developer writing guidelines and the [PR-description standard](../../references/pr-descriptions.md).
- After drafting, or when editing existing prose that sounds inflated, verbose or hard to understand.
- When the user asks to unslop or identifies a confusing title or passage.

For short replies, keep the check proportionate. This skill edits prose; it does not replace factual investigation or technical review.

## Process

### Draft with the rules in mind

Identify what the reader needs to understand or decide. Apply the original rules while writing. Give the title and opening a concrete subject and result, using familiar language. Explain necessary technical terms and keep enough reasoning for the reader to follow.

### Review and revise

Apply the original rules to the title, opening and remaining prose. Rewrite dense or inflated passages in complete sentences. Preserve facts, necessary caveats, evidence, intended tone and the user's requested detail. Do not invent mechanisms or explanations to make a sentence sound concrete. Preserve exact quotations, code and requested exact output formats.

### Make code references useful

In human-facing prose, use readable PR and commit links instead of bare commit hashes. Prefer the PR title linked to the PR. When a specific commit matters, use its title or a short description linked to that commit, within the PR when available, and include the PR link for context. Verify the destination; never invent a PR or URL. For unpublished work, name the change and link to the relevant local file or diff. Keep raw hashes only where required in commands, exact quotations or machine-readable evidence.

Return the requested prose without narrating every editing check. Do not create a separate document just to apply the skill.

## Common Rationalizations

| Rationalization | Response |
|---|---|
| The developer instructions already cover writing | This is the second check when those instructions get lost in context. |
| Shorter always means clearer | Keep the reasoning and connections the reader needs. |
| A commit hash proves the claim | Give the reader a named link to inspect the change. |

## Red Flags

- A title that requires project jargon to decode.
- Prose that sounds impressive but leaves the action or result unclear.
- Bare commit hashes in a human-facing explanation.
- An edit that removes evidence or qualifications to sound more decisive.

## Verification

- The title and opening tell the reader what the document or answer concerns.
- The draft follows the original rules without losing meaning or necessary detail.
- Code references have readable labels and usable destinations, with no invented PR links.
- The final pass checks the whole text, not just the first paragraph.
