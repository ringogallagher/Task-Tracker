# Task Tracker CLI Usage

Run the script from the terminal:

```bash
python task_tracker.py <command> [arguments]
```

## Commands

### 1. Add a new task

```bash
python task_tracker.py add "Your task description"
```

**Example:**

```bash
python task_tracker.py add "Finish Python project"
```

Output:

```
Task success added (ID: 1, status: to-do)
```

---

### 2. List all tasks

```bash
python task_tracker.py list
```

**Example Output:**

```
['⏳'] 1: Finish Python project (to-do)
  Created: 15 Nov 2025, 04 16 PM
  Updated: 15 Nov 2025, 04 16 PM
```

---

### 3. Update task status

```bash
python task_tracker.py status <id> <new_status>
```

**Valid statuses:** `to-do`, `in-progress`, `done`

**Example:**

```bash
python task_tracker.py status 1 in-progress
```

Output:

```
Task 1 status update to 'in-progress'.
```

---

### 4. Delete a task

```bash
python task_tracker.py delete <id>
```

**Example:**

```bash
python task_tracker.py delete 1
```

Output:

```
Task 1 deleted.
```
