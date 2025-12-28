"""TaskService for Phase I In-Memory Todo Application.

This module provides business logic for CRUD operations on tasks.
"""

from typing import List, Tuple
from src.models.task import Task


class TaskService:
    """Service class for managing tasks in memory.

    Attributes:
        _tasks: In-memory list of Task objects
        _next_id: Counter for generating sequential task IDs
    """

    def __init__(self):
        """Initialize TaskService with empty task list and ID counter."""
        self._tasks: List[Task] = []
        self._next_id: int = 1

    def add_task(self, title: str) -> Tuple[bool, any]:
        """Add a new task with given title.

        Args:
            title: Task title (will be trimmed)

        Returns:
            Tuple of (success: bool, result: Task or error_message: str)
            - (True, Task) if task created successfully
            - (False, error_message) if validation fails

        Validates:
            - Title must be non-empty after trimming (FR-010, FR-017)
        """
        title = title.strip()
        if not title:
            return (False, "Task title cannot be empty")

        task = Task(id=self._next_id, title=title, status="Incomplete")
        self._tasks.append(task)
        self._next_id += 1
        return (True, task)

    def get_all_tasks(self) -> List[Task]:
        """Get all tasks.

        Returns:
            List of all Task objects (returns copy to prevent external modification)
        """
        return list(self._tasks)

    def _find_task(self, task_id: int) -> Task:
        """Find task by ID (helper method).

        Args:
            task_id: Task ID to search for

        Returns:
            Task if found, None otherwise
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def mark_complete(self, task_id: int) -> Tuple[bool, any]:
        """Mark task as complete.

        Args:
            task_id: ID of task to mark complete

        Returns:
            Tuple of (success: bool, result: Task or error_message: str)
        """
        task = self._find_task(task_id)
        if not task:
            return (False, f"Task with ID {task_id} not found")

        task.status = "Complete"
        return (True, task)

    def mark_incomplete(self, task_id: int) -> Tuple[bool, any]:
        """Mark task as incomplete.

        Args:
            task_id: ID of task to mark incomplete

        Returns:
            Tuple of (success: bool, result: Task or error_message: str)
        """
        task = self._find_task(task_id)
        if not task:
            return (False, f"Task with ID {task_id} not found")

        task.status = "Incomplete"
        return (True, task)

    def update_task(self, task_id: int, new_title: str) -> Tuple[bool, any]:
        """Update task title.

        Args:
            task_id: ID of task to update
            new_title: New title (will be trimmed)

        Returns:
            Tuple of (success: bool, result: Task or error_message: str)

        Validates:
            - New title must be non-empty after trimming
            - Task ID must exist
        """
        new_title = new_title.strip()
        if not new_title:
            return (False, "Task title cannot be empty")

        task = self._find_task(task_id)
        if not task:
            return (False, f"Task with ID {task_id} not found")

        task.title = new_title
        return (True, task)

    def delete_task(self, task_id: int) -> Tuple[bool, any]:
        """Delete task by ID.

        Args:
            task_id: ID of task to delete

        Returns:
            Tuple of (success: bool, result: Task or error_message: str)
            Returns deleted task on success for confirmation display
        """
        task = self._find_task(task_id)
        if not task:
            return (False, f"Task with ID {task_id} not found")

        self._tasks.remove(task)
        return (True, task)
