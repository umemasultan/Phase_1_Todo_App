# Quickstart Guide: Phase I In-Memory Todo Application

**Feature**: Phase I In-Memory Todo Application
**Branch**: `001-phase-i-todo-app`
**Created**: 2025-12-28
**Purpose**: Guide for running and using the Phase I todo application

## Prerequisites

- **Python**: Version 3.13 or higher
- **Operating System**: Windows, macOS, or Linux
- **Terminal**: Any terminal/console that supports text input/output

**Check Python Version**:
```bash
python --version
# or
python3 --version
```

Expected output: `Python 3.13.x` or higher

## Installation

### 1. Clone or Download Repository

```bash
git clone <repository-url>
cd Todo_App
```

### 2. Switch to Feature Branch

```bash
git checkout 001-phase-i-todo-app
```

### 3. Verify Project Structure

```bash
ls src/
# Expected: models/ services/ cli/ main.py
```

## Running the Application

### Basic Usage

```bash
python src/main.py
```

or on some systems:

```bash
python3 src/main.py
```

### Expected Output

When the application starts, you should see:

```
=== Todo Application - Phase I ===

Main Menu:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete/Incomplete
6. Exit

Enter your choice (1-6):
```

## Using the Application

### Menu Navigation

The application uses a numbered menu system. Select an option by typing its number and pressing Enter.

### 1. Add Task

**Steps**:
1. Select option `1` from the main menu
2. Enter task title when prompted
3. Task is created with status "Incomplete"
4. Application returns to main menu

**Example**:
```
Enter your choice (1-6): 1

Enter task title: Buy groceries

Task added successfully!
ID: 1, Title: Buy groceries, Status: Incomplete

Press Enter to continue...
```

**Tips**:
- Task titles are automatically trimmed (leading/trailing spaces removed)
- Empty titles are rejected with an error message
- Each task gets a unique sequential ID starting from 1

### 2. View Tasks

**Steps**:
1. Select option `2` from the main menu
2. All tasks are displayed with ID, Title, and Status
3. Application returns to main menu

**Example with tasks**:
```
Enter your choice (1-6): 2

=== Your Tasks ===

ID  | Title                    | Status
----|--------------------------|------------
1   | Buy groceries            | Incomplete
2   | Call dentist             | Complete
3   | Finish project report    | Incomplete

Total tasks: 3

Press Enter to continue...
```

**Example with no tasks**:
```
Enter your choice (1-6): 2

Your task list is empty. Add a task to get started!

Press Enter to continue...
```

### 3. Update Task

**Steps**:
1. Select option `3` from the main menu
2. Enter the ID of the task you want to update
3. Enter the new title
4. Task title is updated
5. Application returns to main menu

**Example**:
```
Enter your choice (1-6): 3

Enter task ID to update: 1
Enter new title: Buy organic groceries

Task updated successfully!
ID: 1, Title: Buy organic groceries, Status: Incomplete

Press Enter to continue...
```

**Error Handling**:
- Non-existent ID: "Task with ID X not found"
- Empty new title: "Task title cannot be empty"
- Non-numeric ID: "Invalid input. Please enter a number"

### 4. Delete Task

**Steps**:
1. Select option `4` from the main menu
2. Enter the ID of the task you want to delete
3. Task is permanently removed
4. Application returns to main menu

**Example**:
```
Enter your choice (1-6): 4

Enter task ID to delete: 2

Task deleted successfully!
ID: 2, Title: Call dentist

Press Enter to continue...
```

**Error Handling**:
- Non-existent ID: "Task with ID X not found"
- Non-numeric ID: "Invalid input. Please enter a number"

**Note**: Deleted task IDs are NOT reused. If you delete task 2, the next new task will have the next sequential ID (not 2).

### 5. Mark Task Complete/Incomplete

**Steps**:
1. Select option `5` from the main menu
2. Enter the ID of the task you want to toggle
3. Enter `c` to mark complete or `i` to mark incomplete
4. Task status is updated
5. Application returns to main menu

**Example (mark complete)**:
```
Enter your choice (1-6): 5

Enter task ID: 1
Mark as (c)omplete or (i)ncomplete? c

Task marked as complete!
ID: 1, Title: Buy groceries, Status: Complete

Press Enter to continue...
```

**Example (mark incomplete)**:
```
Enter your choice (1-6): 5

Enter task ID: 1
Mark as (c)omplete or (i)ncomplete? i

Task marked as incomplete!
ID: 1, Title: Buy groceries, Status: Incomplete

Press Enter to continue...
```

**Error Handling**:
- Non-existent ID: "Task with ID X not found"
- Invalid choice (not 'c' or 'i'): "Invalid choice. Please enter 'c' or 'i'"

### 6. Exit

**Steps**:
1. Select option `6` from the main menu
2. Application exits cleanly

**Example**:
```
Enter your choice (1-6): 6

Thank you for using Todo Application!
Goodbye!
```

**Important**: All data is lost when you exit. Tasks are stored in memory only and are NOT persisted to files or databases in Phase I.

## Common Usage Patterns

### Daily Workflow Example

```
1. Start application
2. Add today's tasks (option 1)
   - "Buy groceries"
   - "Call dentist"
   - "Finish project report"
3. View all tasks (option 2)
4. Complete tasks as you go (option 5)
5. View progress (option 2)
6. Exit when done (option 6)
```

### Correcting Mistakes

```
# Fix a typo in task title
1. View tasks to find the ID (option 2)
2. Update the task title (option 3)

# Remove unwanted task
1. View tasks to find the ID (option 2)
2. Delete the task (option 4)
```

## Troubleshooting

### Application Won't Start

**Problem**: `python src/main.py` gives an error

**Solutions**:
1. Check Python version: `python --version` (must be 3.13+)
2. Try `python3 src/main.py` instead
3. Ensure you're in the project root directory: `ls src/main.py` should show the file
4. Check file permissions: `ls -l src/main.py` (should be readable)

### "Module not found" Error

**Problem**: `ModuleNotFoundError: No module named 'models'` or similar

**Solution**: Make sure you're running from the project root, not from inside `src/`:
```bash
# Wrong (from inside src/)
cd src
python main.py  # ❌ Won't work

# Correct (from project root)
cd Todo_App
python src/main.py  # ✅ Works
```

### Invalid Menu Choice

**Problem**: Entering a number outside 1-6 or non-numeric input

**Expected Behavior**: Error message displayed, menu shown again
```
Invalid choice. Please enter a number between 1 and 6.
```

**Solution**: Enter a valid number (1-6)

### Empty Title Error

**Problem**: Trying to add or update a task with empty title

**Expected Behavior**: Error message displayed, operation cancelled
```
Error: Task title cannot be empty
```

**Solution**: Enter a non-empty title (at least one character after trimming spaces)

### Task Not Found Error

**Problem**: Entering a task ID that doesn't exist

**Expected Behavior**: Error message displayed, operation cancelled
```
Error: Task with ID 999 not found
```

**Solution**:
1. View all tasks (option 2) to see valid IDs
2. Use an existing task ID

### Application Freezes or Hangs

**Problem**: Application becomes unresponsive

**Solution**: Press `Ctrl+C` (Windows/Linux) or `Cmd+C` (macOS) to exit gracefully
```
^C
Application interrupted. Exiting...
```

## Limitations (Phase I)

### No Persistence
- **Issue**: All tasks are lost when you exit the application
- **Workaround**: None in Phase I
- **Fix**: Phase II will add file-based persistence

### No Search or Filter
- **Issue**: Cannot search tasks by keyword or filter by status
- **Workaround**: Use option 2 to view all tasks
- **Fix**: May be added in future phases

### No Task Priority or Due Dates
- **Issue**: All tasks are treated equally; no priority levels or deadlines
- **Workaround**: Use numbering or prefixes in titles (e.g., "URGENT: Buy groceries")
- **Fix**: May be added in future phases

### No Multi-User Support
- **Issue**: Only one person can use the application at a time (single-user)
- **Workaround**: None needed for Phase I (intentional design)
- **Fix**: Phase IV will add multi-user support with authentication

### No Undo
- **Issue**: Deleted or modified tasks cannot be recovered
- **Workaround**: Be careful with delete operations
- **Fix**: May be added in future phases

## Performance Notes

- **Startup Time**: < 2 seconds on standard hardware
- **Operation Time**: All operations (add, view, update, delete, mark) complete in < 10-15 seconds
- **Capacity**: Application handles 100+ tasks without performance degradation
- **Memory Usage**: Minimal (tasks stored in RAM only)

## Getting Help

### In-Application
- Each menu option is self-explanatory
- Error messages provide specific guidance when operations fail
- All operations return to the main menu (safe to experiment)

### Documentation
- **Specification**: See [spec.md](./spec.md) for feature requirements
- **Implementation Plan**: See [plan.md](./plan.md) for architecture details
- **Data Model**: See [data-model.md](./data-model.md) for Task entity details

### Common Questions

**Q: Where are my tasks saved?**
A: Nowhere. Phase I stores tasks in memory only. They are lost when you exit.

**Q: Can I use this on multiple computers?**
A: Each computer runs a separate instance with its own tasks (no sync in Phase I).

**Q: Can I export my tasks?**
A: No export functionality in Phase I. This may be added in future phases.

**Q: What happens if I enter invalid input?**
A: The application displays an error message and lets you try again. It never crashes.

**Q: Can I cancel an operation?**
A: Not explicitly, but you can enter invalid input to trigger an error, then choose a different menu option.

## Next Steps

Once you're comfortable with Phase I:

1. **Review the Implementation**: Check `src/` directory to see how the application is structured
2. **Run Tests** (if implemented): `pytest tests/` to validate functionality
3. **Await Phase II**: File-based persistence coming soon
4. **Provide Feedback**: Report any issues or suggestions

## Summary

Phase I provides a functional, menu-driven todo application that runs entirely in memory. It's intentionally simple, focusing on core CRUD operations without unnecessary complexity. All features work exactly as specified, with robust error handling and a user-friendly interface.

**Remember**: All data is lost on exit. Phase II will add persistence!
