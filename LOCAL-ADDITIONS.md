# Isaac's additions

The upstream skill files are preserved at aeac41d4d005999432bb7312f7ff06383a91d59d. The four discovery skills and their evidence were adopted at e38d2dae7b496a838cf18b4718f2aaa9be3c1fcf.

The spring-clean release adds working-docs and voyager-orchestration. working-docs owns output placement and authority, while documentation-and-adrs owns the content of documentation and decisions. voyager-orchestration transports an existing workflow through the installed service; it does not replace planning, project instructions or the upstream personas.

Both additions were approved by Isaac on 21 October 2026. Their execution fixtures describe behavioral checks. Structural and lexical checks are recorded separately from actual agent execution; passing those checks does not prove live routing or Voyager operation.

Source lives in ~/agent-skills. Setup edits use ~/the-workshop/.worktrees. Home discovery points to a fixed release under ~/.local/share/agent-skills/releases. Publication to the fork is a separate action from local activation. Do not edit installed release files.
