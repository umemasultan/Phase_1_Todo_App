"""Task model for Phase I In-Memory Todo Application.

This module defines the Task entity with validation.
"""

from dataclasses import dataclass


@dataclass
class Task:
    """Represents a single todo item.

    Attributes:
        id: Unique sequential integer identifier (>= 1)
        title: Non-empty text description (trimmed)
        status: Completion state - "Complete" or "Incomplete"
    """

    id: int
    title: str
    status: str  # "Complete" or "Incomplete"

    def __post_init__(self):
        """Validate task data after initialization."""
        if self.id < 1:
            raise ValueError("Task ID must be positive integer >= 1")
        if not self.title or not self.title.strip():
            raise ValueError("Task title cannot be empty")
        if self.status not in ("Complete", "Incomplete"):
            raise ValueError(f"Invalid status: {self.status}")
