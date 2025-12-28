"""Main entry point for Phase I In-Memory Todo Application.

This module initializes and runs the todo application.
"""

import sys
from pathlib import Path

# Add parent directory to path so imports work from anywhere
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.services.task_service import TaskService
from src.cli.display import DisplayHelper
from src.cli.menu import MenuHandler


def main():
    """Initialize and run the todo application."""
    # T027: Startup banner
    print("=== Todo Application - Phase I ===")

    # Initialize services
    task_service = TaskService()
    display_helper = DisplayHelper()
    menu_handler = MenuHandler(task_service, display_helper)

    # Run application
    try:
        menu_handler.run()
        # T028: Exit message (normal exit)
        print("\nThank you for using Todo Application!")
        print("Goodbye!")
    except KeyboardInterrupt:
        # T026: Handle Ctrl+C gracefully
        print("\n\nApplication interrupted. Exiting...")


if __name__ == "__main__":
    main()
