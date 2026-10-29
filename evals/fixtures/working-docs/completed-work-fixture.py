from pathlib import Path
import json
import subprocess

base = Path("completed-example").resolve()
repo, vault = base / "repo", base / "vault"
files = {
    "repo/AGENTS.md": "This synthetic project uses root specifications, tasks/, and the approved completed-work convention. Only Export is accepted complete. Import is active. No network, merge or installation is authorized.\n",
    "repo/SPEC.md": "# Specifications\n[Export](SPEC-export.md)\n[Import](SPEC-import.md)\n",
    "repo/SPEC-export.md": "# Export\nAccepted complete. [Plan](tasks/export-plan.md).\n",
    "repo/SPEC-import.md": "# Import\nActive specification. Preserve byte-identical.\n",
    "repo/tasks/export-plan.md": "# Export plan\nAll acceptance checks and owner review passed.\n",
    "repo/tasks/export-todo.md": "# Export tasks\n- [x] Implement and verify export\n",
    "repo/tasks/plan.md": "# Import plan\nActive and incomplete. Preserve byte-identical.\n",
    "repo/tasks/todo.md": "# Import tasks\n- [ ] Build import\n",
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
(base / "original.json").write_text(json.dumps(files, indent=2))
subprocess.run(["git", "init", "-q", "-b", "main", str(repo)], check=True)
for args in [["add", "."], ["-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "commit", "-qm", "Synthetic accepted Export baseline"]]:
    subprocess.run(["git", "-C", str(repo), *args], check=True)
subprocess.run(["git", "-C", str(repo), "worktree", "add", "-qb", "feature/export", str(repo / ".worktrees/export")], check=True)
print("Created synthetic completed-example. Export is accepted complete; Import is active.")
