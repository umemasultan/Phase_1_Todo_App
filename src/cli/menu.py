"""MenuHandler for Phase I In-Memory Todo Application.

This module handles the menu-driven CLI interface.
"""

from src.services.task_service import TaskService
from src.cli.display import DisplayHelper


class MenuHandler:
    """Handles menu display, input, and routing for the todo application."""

    def __init__(self, task_service: TaskService, display_helper: DisplayHelper):
        """Initialize MenuHandler with service and display dependencies.

        Args:
            task_service: TaskService instance for business logic
            display_helper: DisplayHelper instance for formatting output
        """
        self.task_service = task_service
        self.display_helper = display_helper

    def display_menu(self) -> None:
        """Display the main menu options."""
        print("\nMain Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete/Incomplete")
        print("0. Exit")

    def get_menu_choice(self) -> int:
        """Get and validate user's menu choice.

        Returns:
            Integer between 0-5 representing menu choice, or -1 for invalid input

        Validates:
            - Input must be numeric
            - Input must be 0 (Exit) or in range 1-5
        """
        try:
            choice = int(input("\nEnter your choice (0-5): "))
            if choice == 0 or (1 <= choice <= 5):
                return choice
            else:
                print("Invalid choice. Please enter a number between 0 and 5.")
                return -1
        except ValueError:
            print("Invalid input. Please enter a number.")
            return -1

    def run(self) -> None:
        """Run the main menu loop.

        Displays menu, processes user choices, and routes to appropriate handlers.
        Continues until user selects Exit option (0).
        """
        while True:
            self.display_menu()
            choice = self.get_menu_choice()

            if choice == -1:
                # Invalid input, loop continues
                continue
            elif choice == 0:
                # Exit
                break
            elif choice == 1:
                self._handle_add_task()
            elif choice == 2:
                self._handle_view_tasks()
            elif choice == 3:
                self._handle_update_task()
            elif choice == 4:
                self._handle_delete_task()
            elif choice == 5:
                self._handle_mark_status()

    def _handle_add_task(self) -> None:
        """Handle add task operation.

        Prompts user for task title, validates input, creates task,
        and displays success or error message.
        """
        print("\n--- Add Task ---")
        title = input("Enter task title: ")

        success, result = self.task_service.add_task(title)

        if success:
            print(f"\nTask added successfully!")
            print(f"ID: {result.id}, Title: {result.title}, Status: {result.status}")
        else:
            print(f"\nError: {result}")

        input("\nPress Enter to continue...")

    def _handle_view_tasks(self) -> None:
        """Handle view tasks operation.

        Retrieves all tasks and displays them in formatted table.
        """
        tasks = self.task_service.get_all_tasks()
        self.display_helper.display_tasks(tasks)
        input("Press Enter to continue...")

    def _handle_update_task(self) -> None:
        """Handle update task operation.

        Prompts for task ID and new title, validates input,
        updates task, and displays result.
        """
        print("\n--- Update Task ---")

        # Get task ID
        try:
            task_id = int(input("Enter task ID to update: "))
        except ValueError:
            print("\nError: Invalid input. Please enter a number.")
            input("\nPress Enter to continue...")
            return

        # Get new title
        new_title = input("Enter new title: ")

        # Update task
        success, result = self.task_service.update_task(task_id, new_title)

        if success:
            print(f"\nTask updated successfully!")
            print(f"ID: {result.id}, Title: {result.title}, Status: {result.status}")
        else:
            print(f"\nError: {result}")

        input("\nPress Enter to continue...")

    def _handle_delete_task(self) -> None:
        """Handle delete task operation.

        Prompts for task ID, validates input, deletes task,
        and displays result.
        """
        print("\n--- Delete Task ---")

        # Get task ID
        try:
            task_id = int(input("Enter task ID to delete: "))
        except ValueError:
            print("\nError: Invalid input. Please enter a number.")
            input("\nPress Enter to continue...")
            return

        # Delete task
        success, result = self.task_service.delete_task(task_id)

        if success:
            print(f"\nTask deleted successfully!")
            print(f"ID: {result.id}, Title: {result.title}")
        else:
            print(f"\nError: {result}")

        input("\nPress Enter to continue...")

    def _handle_mark_status(self) -> None:
        """Handle mark task complete/incomplete operation.

        Prompts for task ID and status choice, validates input,
        updates task status, and displays result.
        """
        print("\n--- Mark Task Complete/Incomplete ---")

        # Get task ID
        try:
            task_id = int(input("Enter task ID: "))
        except ValueError:
            print("\nError: Invalid input. Please enter a number.")
            input("\nPress Enter to continue...")
            return

        # Get status choice
        choice = input("Mark as (c)omplete or (i)ncomplete? ").lower()

        if choice not in ('c', 'i'):
            print("\nError: Invalid choice. Please enter 'c' or 'i'.")
            input("\nPress Enter to continue...")
            return

        # Call appropriate service method
        if choice == 'c':
            success, result = self.task_service.mark_complete(task_id)
        else:
            success, result = self.task_service.mark_incomplete(task_id)

        # Display result
        if success:
            status_text = "complete" if choice == 'c' else "incomplete"
            print(f"\nTask marked as {status_text}!")
            print(f"ID: {result.id}, Title: {result.title}, Status: {result.status}")
        else:
            print(f"\nError: {result}")

        input("\nPress Enter to continue...")
