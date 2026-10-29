import { createTask } from './tasks.mjs';
const title = process.argv[2];
try {
  const task = createTask(title);
  console.log(JSON.stringify(task));
} catch (error) {
  console.error(error.message);
  process.exitCode = 1;
}
