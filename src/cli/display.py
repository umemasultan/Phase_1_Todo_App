"""DisplayHelper for Phase I In-Memory Todo Application.

This module handles formatting and displaying task lists.
"""

from typing import List
from src.models.task import Task


class DisplayHelper:
    """Helper class for displaying tasks in console format."""

    def display_tasks(self, tasks: List[Task]) -> None:
        """Display list of tasks in formatted table.

        Args:
            tasks: List of Task objects to display

        Displays:
            - Formatted table with ID, Title, Status columns if tasks exist
            - "Your task list is empty" message if no tasks
        """
        if not tasks:
            print("\nYour task list is empty. Add a task to get started!\n")
            return

        print("\n=== Your Tasks ===\n")
        print(f"{'ID':<4} | {'Title':<40} | {'Status':<12}")
        print("-" * 60)

        for task in tasks:
            print(f"{task.id:<4} | {task.title:<40} | {task.status:<12}")

        print(f"\nTotal tasks: {len(tasks)}\n")
