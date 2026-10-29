from pathlib import Path
import json
import subprocess

base = Path("completed-example").resolve()
repo, vault = base / "repo", base / "vault"
files = {
    "repo/AGENTS.md": "This synthetic project uses untracked worktree-local specifications and tasks/ under the approved completed-work convention. The canonical Obsidian project is ../vault from this primary checkout, or ../../../vault from either worktree. Only Export is accepted complete. Import is active. No network, merge or installation is authorized.\n",
    "repo/README.md": "# Synthetic project\nExport is already integrated. Do not change this tracked file.\n",
    "vault/status.md": "# Demo\n[Export design](explainer/design/export.html)\n[Export build](explainer/walkthroughs/export.html)\n[Export research](research/export.html)\n[Import](explainer/walkthroughs/import.html)\n",
    "vault/explainer/design/export.html": '<html><h1>Export design</h1><a href="../walkthroughs/export.html">Build</a></html>',
    "vault/explainer/walkthroughs/export.html": '<html><h1>Export accepted</h1><a href="evidence/export.txt">Export evidence</a><a href="evidence/shared.json">Shared evidence</a></html>',
    "vault/explainer/walkthroughs/import.html": '<html><h1>Import active</h1><a href="evidence/shared.json">Shared evidence</a></html>',
    "vault/explainer/walkthroughs/evidence/export.txt": "Synthetic completed Export evidence.\n",
    "vault/explainer/walkthroughs/evidence/shared.json": '{"synthetic":true,"used_by":["export","import"]}\n',
    "vault/research/export.html": '<html><h1>Export research</h1><a href="../explainer/design/export.html">Design</a></html>',
}
for name, text in files.items():
    p = base / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)
subprocess.run(["git", "init", "-q", "-b", "main", str(repo)], check=True)
for args in [["add", "."], ["-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "commit", "-qm", "Synthetic accepted Export baseline"]]:
    subprocess.run(["git", "-C", str(repo), *args], check=True)
subprocess.run(["git", "-C", str(repo), "worktree", "add", "-qb", "feature/export", str(repo / ".worktrees/feature-export")], check=True)
subprocess.run(["git", "-C", str(repo), "worktree", "add", "-qb", "feature/import", str(repo / ".worktrees/feature-import")], check=True)
exclude = repo / ".git/info/exclude"
exclude.write_text(exclude.read_text() + "\n/.worktrees/\n/SPEC.md\n/SPEC-export.md\n/tasks/plan.md\n/tasks/todo.md\n")
local = {
    "repo/.worktrees/feature-export/SPEC.md": "# Export\nAccepted complete. [Module](SPEC-export.md). [Plan](tasks/plan.md).\n",
    "repo/.worktrees/feature-export/SPEC-export.md": "# Export module\nAccepted behavior. Preserve this record.\n",
    "repo/.worktrees/feature-export/tasks/plan.md": "# Export plan\nAll acceptance checks and owner review passed. [Spec](../SPEC.md).\n",
    "repo/.worktrees/feature-export/tasks/todo.md": "# Export tasks\n- [x] Implement and verify export\n",
    "repo/.worktrees/feature-import/SPEC.md": "# Import\nActive specification. Preserve byte-identical.\n",
    "repo/.worktrees/feature-import/tasks/plan.md": "# Import plan\nActive and incomplete. Preserve byte-identical.\n",
    "repo/.worktrees/feature-import/tasks/todo.md": "# Import tasks\n- [ ] Build import\n",
    "vault/spec-history/earlier-feature-spec.md": "# Earlier completed feature\nKeep this archived record unchanged.\n",
}
for name, text in local.items():
    p = base / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)
files.update(local)
(base / "original.json").write_text(json.dumps(files, indent=2))
print("Created synthetic completed-example. Export is integrated and accepted; Import is active. Task documents are untracked and locally ignored.")
