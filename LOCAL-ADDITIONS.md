# Isaac's additions

The upstream skill files are preserved at aeac41d4d005999432bb7312f7ff06383a91d59d. The four discovery skills and their evidence were adopted at e38d2dae7b496a838cf18b4718f2aaa9be3c1fcf.

On 21 October 2026 Isaac retired design-interview for a trial of upstream idea-refine. Its skill and evaluation are preserved in ~/Archive/skills/design-interview-20261021, with restoration instructions, and in Git history. The active catalog contains three discovery additions. The upstream idea-refine, interview-me and code-review-and-quality skills are unchanged.

The spring-clean release adds working-docs and voyager-orchestration. working-docs owns output placement and authority, while documentation-and-adrs owns the content of documentation and decisions. voyager-orchestration transports an existing workflow through the installed service; it does not replace planning, project instructions or the upstream personas.

Both additions were approved by Isaac on 21 October 2026. Their execution fixtures describe behavioral checks. Structural and lexical checks are recorded separately from actual agent execution; passing those checks does not prove live routing or Voyager operation.

Isaac subsequently narrowed the output-format policy in working-docs. HTML remains the default for human-facing explainers and research. Specifications and plans retain their owning skill's format; HTML copies are produced only on explicit request. Historical documents are not automatically converted or removed.

Source lives in ~/agent-skills. Setup edits use ~/the-workshop/.worktrees. Home discovery points to a fixed release under ~/.local/share/agent-skills/releases. Publication to the fork is a separate action from local activation. Do not edit installed release files.

On 22 October 2026 Isaac requested the original Unslop for a comparison with the existing writing guidance. Lauren Tan’s original pstack skill is preserved unchanged in `external-skills/unslop/`, with its MIT license and pinned source/hash. It is installed alongside the 30 catalog skills. The existing catalog, validators and global writing instructions are unchanged. The upstream invocation setting remains intact; proactive and reactive use are explicit trial conditions, not a changed automatic default.

On 22 October 2026 Isaac approved `screenshots/` beneath the canonical folder containing the supported documents. working-docs now keeps screenshot evidence there, with identifiable filenames and relative links, so document listings remain easy to scan. Existing screenshot moves preserve content and update references.

On 22 October 2026 Isaac adopted Unslop as a second check alongside developer writing instructions, for proactive drafting and reactive editing. The local `skills/unslop` entry reads the preserved original and allows automatic selection. Both engines discover this entry instead of the external source directory, retaining 31 shared skills. Isaac also approved readable PR and commit links in both the local skill and global developer writing instructions. The original import remains byte-identical. Structural and lexical checks do not prove model invocation or writing quality.

On 22 October 2026 the user confirmed a single-layer build-and-verify fleet workflow: one captain assigns workers, independent verification combines systematic review and real-user journeys, each verification allows one correction attempt, and verified slices produce nonblocking user updates. The candidate section in voyager-orchestration is for explicit trials, preserves the installed service authority contract, and excludes shipping and recursive delegation. It remains unreleased pending review and behavioral evidence; deterministic validation is not proof of workflow effectiveness.

The subsequent modularity review separates that candidate procedure into references/voyager-build-verification.md. The core skill requires explicit Voyager selection and consumes the user's own workflow and evidence criteria. It does not require Osmani's review skill or impose the build workflow on ordinary coordination. Fleet grouping remains separate from responsibility and permissions. This revision is also an unreleased draft.

The optional build reference now distinguishes single-task build, build-auto and explicitly selected delegated build-and-verify. It includes triggers, exclusions, permission/input checks, single-owner task state, slice-bounded builder assignments and the catalog promotion criteria. The pre-verification cohesion retry limit is a proposed trial default, not a previously confirmed requirement.

The workflow reference now separates its build/verification procedure from the selected coordination provider. Its explicit Voyager binding preserves current capability and delivery constraints. The setup proposal remains outside the skill package; no runtime adapter, user configuration or installed discovery was changed.
