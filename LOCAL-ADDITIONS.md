# Isaac's additions

The upstream skill files are preserved at aeac41d4d005999432bb7312f7ff06383a91d59d. The four discovery skills and their evidence were adopted at e38d2dae7b496a838cf18b4718f2aaa9be3c1fcf.

On 21 October 2026 Isaac retired design-interview for a trial of upstream idea-refine. Its skill and evaluation are preserved in ~/Archive/skills/design-interview-20261021, with restoration instructions, and in Git history. The active catalog contains three discovery additions. The upstream idea-refine, interview-me and code-review-and-quality skills are unchanged.

The spring-clean release adds working-docs and voyager-orchestration. working-docs owns output placement and authority, while documentation-and-adrs owns the content of documentation and decisions. voyager-orchestration transports an existing workflow through the installed service; it does not replace planning, project instructions or the upstream personas.

Both additions were approved by Isaac on 21 October 2026. Their execution fixtures describe behavioral checks. Structural and lexical checks are recorded separately from actual agent execution; passing those checks does not prove live routing or Voyager operation.

Isaac subsequently narrowed the output-format policy in working-docs. HTML remains the default for human-facing explainers and research. Specifications and plans retain their owning skill's format; HTML copies are produced only on explicit request. Historical documents are not automatically converted or removed.

Source lives in ~/agent-skills. Setup edits use ~/the-workshop/.worktrees. Home discovery points to a fixed release under ~/.local/share/agent-skills/releases. Publication to the fork is a separate action from local activation. Do not edit installed release files.

On 22 October 2026 Isaac requested the original Unslop for a comparison with the existing writing guidance. Lauren Tan’s original pstack skill is preserved unchanged in `external-skills/unslop/`, with its MIT license and pinned source/hash. It is installed alongside the 30 catalog skills. The existing catalog, validators and global writing instructions are unchanged. The upstream invocation setting remains intact; proactive and reactive use are explicit trial conditions, not a changed automatic default.
