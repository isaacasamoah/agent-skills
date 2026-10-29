import { appendFileSync } from 'node:fs';
export function appendTask(task) {
  appendFileSync('tasks.jsonl', JSON.stringify(task) + '\n', { mode: 0o600 });
}
