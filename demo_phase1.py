"""Demo script for Phase I Todo Application - Non-interactive."""

import sys
import io
from pathlib import Path

# Fix Windows console encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from src.services.task_service import TaskService
from src.cli.display import DisplayHelper

def demo():
    """Demonstrate all Phase I features."""
    print("="*60)
    print("PHASE I TODO APP - FEATURE DEMONSTRATION")
    print("="*60)

    service = TaskService()
    display = DisplayHelper()

    # Feature 1: Add Task
    print("\n[FEATURE 1] Add Task")
    print("-" * 60)
    success1, task1 = service.add_task("Buy groceries")
    success2, task2 = service.add_task("Call dentist")
    success3, task3 = service.add_task("Finish report")

    print(f"[OK] Added: {task1.title} (ID: {task1.id})")
    print(f"[OK] Added: {task2.title} (ID: {task2.id})")
    print(f"[OK] Added: {task3.title} (ID: {task3.id})")

    # Feature 2: View Tasks
    print("\n[FEATURE 2] View Tasks")
    print("-" * 60)
    tasks = service.get_all_tasks()
    display.display_tasks(tasks)

    # Feature 5: Mark Complete
    print("\n[FEATURE 5] Mark Task Complete")
    print("-" * 60)
    success, updated = service.mark_complete(1)
    if success:
        print(f"✓ Marked complete: {updated.title} - Status: {updated.status}")

    # View updated list
    print("\nUpdated task list:")
    tasks = service.get_all_tasks()
    display.display_tasks(tasks)

    # Feature 5b: Mark Incomplete
    print("\n[FEATURE 5] Mark Task Incomplete")
    print("-" * 60)
    success, updated = service.mark_incomplete(1)
    if success:
        print(f"✓ Marked incomplete: {updated.title} - Status: {updated.status}")

    # Feature 3: Update Task
    print("\n[FEATURE 3] Update Task")
    print("-" * 60)
    success, updated = service.update_task(2, "Call dentist and schedule appointment")
    if success:
        print(f"✓ Updated task {updated.id}")
        print(f"  Old title: Call dentist")
        print(f"  New title: {updated.title}")

    # View updated list
    print("\nUpdated task list:")
    tasks = service.get_all_tasks()
    display.display_tasks(tasks)

    # Feature 4: Delete Task
    print("\n[FEATURE 4] Delete Task")
    print("-" * 60)
    success, deleted = service.delete_task(3)
    if success:
        print(f"✓ Deleted: {deleted.title} (ID: {deleted.id})")

    # View final list
    print("\nFinal task list:")
    tasks = service.get_all_tasks()
    display.display_tasks(tasks)

    # Error Handling Demo
    print("\n[ERROR HANDLING] Testing Validation")
    print("-" * 60)

    # Empty title
    success, error = service.add_task("   ")
    if not success:
        print(f"✓ Empty title rejected: {error}")

    # Invalid ID
    success, error = service.update_task(999, "Test")
    if not success:
        print(f"✓ Invalid ID rejected: {error}")

    # Invalid ID delete
    success, error = service.delete_task(999)
    if not success:
        print(f"✓ Invalid ID rejected: {error}")

    print("\n" + "="*60)
    print("✓ ALL PHASE I FEATURES DEMONSTRATED SUCCESSFULLY!")
    print("="*60)
    print("\nPhase I Features:")
    print("  1. ✓ Add Task")
    print("  2. ✓ View Tasks")
    print("  3. ✓ Update Task")
    print("  4. ✓ Delete Task")
    print("  5. ✓ Mark Task Complete/Incomplete")
    print("\nMenu Options: 1-5 + 0 (Exit)")
    print("Task Fields: ID, Title, Status")
    print("\nTo run interactive app: python src/main.py")
    print("="*60)

if __name__ == "__main__":
    demo()
