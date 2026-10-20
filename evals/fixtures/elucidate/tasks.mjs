import { randomUUID } from 'node:crypto';
import { appendTask } from './store.mjs';
export function createTask(title) {
  if (typeof title !== 'string' || !title.trim()) throw new Error('Title required');
  const task = { id: randomUUID(), title: title.trim() };
  appendTask(task);
  return task;
}
