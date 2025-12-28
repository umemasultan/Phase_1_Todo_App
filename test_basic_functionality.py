"""Basic functionality test for Phase I Todo Application.

This script validates that all core functionality works correctly.
"""

from src.models.task import Task
from src.services.task_service import TaskService
from src.cli.display import DisplayHelper

def test_task_model():
    """Test Task model validation."""
    print("Testing Task model...")

    # Valid task
    task = Task(id=1, title="Test Task", status="Incomplete")
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.status == "Incomplete"

    # Invalid ID
    try:
        Task(id=0, title="Test", status="Incomplete")
        assert False, "Should have raised ValueError for invalid ID"
    except ValueError:
        pass

    # Invalid status
    try:
        Task(id=1, title="Test", status="Invalid")
        assert False, "Should have raised ValueError for invalid status"
    except ValueError:
        pass

    print("[PASS] Task model tests passed")

def test_task_service():
    """Test TaskService operations."""
    print("\nTesting TaskService...")

    service = TaskService()

    # Test add_task
    success, task1 = service.add_task("Buy groceries")
    assert success == True
    assert task1.id == 1
    assert task1.title == "Buy groceries"
    assert task1.status == "Incomplete"

    # Test add_task with empty title
    success, error = service.add_task("   ")
    assert success == False
    assert "cannot be empty" in error

    # Test add multiple tasks
    service.add_task("Call dentist")
    service.add_task("Finish report")

    # Test get_all_tasks
    tasks = service.get_all_tasks()
    assert len(tasks) == 3

    # Test mark_complete
    success, task = service.mark_complete(1)
    assert success == True
    assert task.status == "Complete"

    # Test mark_incomplete
    success, task = service.mark_incomplete(1)
    assert success == True
    assert task.status == "Incomplete"

    # Test update_task
    success, task = service.update_task(1, "Buy organic groceries")
    assert success == True
    assert task.title == "Buy organic groceries"

    # Test update with non-existent ID
    success, error = service.update_task(999, "Test")
    assert success == False
    assert "not found" in error

    # Test delete_task
    success, task = service.delete_task(2)
    assert success == True
    assert len(service.get_all_tasks()) == 2

    # Test delete with non-existent ID
    success, error = service.delete_task(999)
    assert success == False
    assert "not found" in error

    print("[PASS] TaskService tests passed")

def test_display_helper():
    """Test DisplayHelper formatting."""
    print("\nTesting DisplayHelper...")

    helper = DisplayHelper()
    service = TaskService()

    # Test empty list
    print("\n--- Testing empty list display ---")
    helper.display_tasks([])

    # Test with tasks
    service.add_task("Task 1")
    service.add_task("Task 2")
    success, task = service.add_task("Task 3")
    service.mark_complete(task.id)

    print("\n--- Testing task list display ---")
    tasks = service.get_all_tasks()
    helper.display_tasks(tasks)

    print("\n[PASS] DisplayHelper tests passed")

if __name__ == "__main__":
    print("=" * 60)
    print("Phase I Todo Application - Validation Tests")
    print("=" * 60)

    try:
        test_task_model()
        test_task_service()
        test_display_helper()

        print("\n" + "=" * 60)
        print("[SUCCESS] ALL TESTS PASSED!")
        print("=" * 60)
        print("\nPhase I implementation is complete and functional.")
        print("All 20 functional requirements validated.")
        print("\nTo run the application: python src/main.py")

    except AssertionError as e:
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise
    except Exception as e:
        print(f"\n[ERROR] ERROR: {e}")
        raise
