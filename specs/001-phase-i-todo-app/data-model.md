# Data Model: Phase I In-Memory Todo Application

**Feature**: Phase I In-Memory Todo Application
**Branch**: `001-phase-i-todo-app`
**Created**: 2025-12-28
**Purpose**: Define the data structures and entities for Phase I todo application

## Overview

Phase I uses a simple in-memory data model with a single entity: **Task**. The model is intentionally minimal to satisfy Phase I requirements without introducing unnecessary complexity (constitutional Principle IX: YAGNI).

## Entity: Task

### Purpose

Represents a single todo item that a user wants to track.

### Attributes

| Attribute | Type    | Required | Default      | Constraints | Description |
|-----------|---------|----------|--------------|-------------|-------------|
| `id`      | int     | Yes      | Auto-assigned| > 0, unique | Unique sequential integer identifier starting from 1 |
| `title`   | str     | Yes      | None         | Non-empty after trimming, max ~500 chars | Text description of what needs to be done |
| `status`  | str     | Yes      | "Incomplete" | Must be "Complete" or "Incomplete" | Completion state of the task |

### Attribute Details

#### `id` (Task Identifier)

- **Type**: Integer
- **Generation**: Sequential, auto-assigned by TaskService starting from 1
- **Uniqueness**: Guaranteed unique within the application session
- **Immutability**: Never changes after task creation
- **Reuse**: IDs are NOT reused after task deletion (simpler logic for Phase I)
- **Specification Reference**: FR-003

**Examples**:
- First task created: `id = 1`
- Second task created: `id = 2`
- If task 1 is deleted, next new task: `id = 3` (not reused)

#### `title` (Task Description)

- **Type**: String
- **Required**: Yes - cannot be empty
- **Validation**: Must have at least 1 character after trimming whitespace
- **Whitespace Handling**: Leading and trailing whitespace automatically trimmed (FR-017)
- **Length**: Reasonable length expected (under 500 characters is acceptable; no explicit limit enforced)
- **Mutability**: Can be updated via update operation (FR-006)
- **Specification Reference**: FR-002, FR-010, FR-017

**Valid Examples**:
- `"Buy groceries"`
- `"Call dentist for appointment"`
- `"   Finish project report   "` → stored as `"Finish project report"` (trimmed)

**Invalid Examples** (rejected with error):
- `""` (empty string)
- `"   "` (whitespace only, becomes empty after trimming)
- `None` (null/undefined)

#### `status` (Completion State)

- **Type**: String enum
- **Valid Values**: Exactly two states (FR-018):
  - `"Complete"` - Task has been finished
  - `"Incomplete"` - Task has not been finished (default)
- **Default**: `"Incomplete"` for new tasks (FR-019)
- **Mutability**: Can be changed via mark_complete/mark_incomplete operations (FR-008, FR-009)
- **Specification Reference**: FR-018, FR-019

**State Transitions**:
```
"Incomplete" --[mark_complete]--> "Complete"
"Complete"   --[mark_incomplete]--> "Incomplete"
```

## Data Structure Implementation

### Python Representation

```python
from dataclasses import dataclass

@dataclass
class Task:
    """
    Represents a single todo item.

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
```

### Storage Strategy

**Phase I**: Simple Python list in TaskService class

```python
class TaskService:
    def __init__(self):
        self._tasks: list[Task] = []      # In-memory list
        self._next_id: int = 1             # ID counter
```

**Characteristics**:
- **Type**: Python list (mutable, ordered sequence)
- **Lifecycle**: Exists only while application is running
- **Persistence**: None - data lost when application exits (Phase I constraint)
- **Capacity**: Limited by available memory (100+ tasks expected, thousands possible)
- **Access Pattern**: Sequential iteration for most operations (O(n) lookup)

**Rationale**: Simplest data structure for Phase I; no premature optimization. List provides adequate performance for expected scale (100 tasks). Easy to replace with file storage in Phase II or database in Phase IV without changing public API of TaskService.

## Relationships

### Phase I

No relationships exist in Phase I. Task is a standalone entity with no foreign keys, references, or associations to other entities.

**Why**: Single entity model is sufficient for Phase I requirements. Relationships will be introduced in future phases when needed:
- Phase IV: User-Task relationship (multi-user support)
- Phase V: Potentially Task-Category, Task-Project relationships

## Validation Rules

| Rule | Description | Enforced By | Error Message |
|------|-------------|-------------|---------------|
| ID Uniqueness | Each task must have a unique ID | TaskService (auto-generation) | N/A (guaranteed by design) |
| ID Positivity | ID must be >= 1 | Task.__post_init__ | "Task ID must be positive integer >= 1" |
| Title Non-Empty | Title must have at least 1 char after trimming | TaskService (add/update methods) | "Task title cannot be empty" |
| Title Trimmed | Leading/trailing whitespace removed | TaskService (automatic in add/update) | N/A (automatic) |
| Status Values | Status must be "Complete" or "Incomplete" | Task.__post_init__ | "Invalid status: {value}" |
| ID Existence | Task ID must exist for update/delete/status operations | TaskService (validation) | "Task with ID {id} not found" |

**Specification References**: FR-003, FR-010, FR-011, FR-017, FR-018, FR-019

## State Management

### Task Lifecycle

```
[NOT EXISTS]
    |
    | add_task(title) → Task created with status="Incomplete"
    ↓
[EXISTS - Incomplete]
    |
    ├─→ mark_complete() → [EXISTS - Complete]
    |                            |
    |                            ↓
    |                     mark_incomplete() → [EXISTS - Incomplete]
    |
    ├─→ update_task(title) → [EXISTS - Incomplete] (title changed)
    |
    └─→ delete_task() → [NOT EXISTS] (permanently removed)
```

### Invariants

The following must always be true:
1. Every Task in the system has a unique, positive integer ID
2. Every Task has a non-empty trimmed title
3. Every Task has a status of exactly "Complete" or "Incomplete"
4. Task IDs are sequential and never decrease (even after deletions)
5. No two tasks share the same ID at any given time

## Data Model Evolution (Future Phases)

### Phase I (Current)
- **Entities**: Task only
- **Storage**: In-memory list
- **Persistence**: None

### Phase II (Planned)
- **Entities**: Task (same structure)
- **Storage**: JSON file
- **Changes**: Add file I/O, persistence across sessions
- **Migration**: Serialize Task list to JSON on exit, deserialize on startup

### Phase III (Planned)
- **Entities**: Task (same structure)
- **Storage**: In-memory or transitional JSON
- **Changes**: Add REST API exposure of Task data
- **Migration**: No schema changes, add API layer

### Phase IV (Planned)
- **Entities**: Task + User (new)
- **Storage**: PostgreSQL database
- **Changes**: Add user_id foreign key to Task, authentication
- **Migration**: Significant - add User table, Task.user_id, migrate from files to database

### Phase V (Planned)
- **Entities**: Task + User + potentially AI enhancements
- **Storage**: PostgreSQL + event store (Kafka)
- **Changes**: Event sourcing, CQRS patterns, AI features
- **Migration**: Major architectural evolution

**Note**: Each phase's data model evolution will be documented in that phase's plan.md. Phase I plan must NOT implement any Phase II+ features (constitutional Principle III: Phase Boundary Enforcement).

## Summary

Phase I data model consists of a single **Task** entity with three attributes (id, title, status) stored in a simple Python list. The model is intentionally minimal, fully satisfying Phase I requirements without premature abstraction or future-proofing. Validation ensures data integrity at both the Task level (via __post_init__) and the service level (via TaskService methods).

**Constitutional Compliance**:
- ✅ Principle V (Clean Architecture): Model is pure data structure, no business logic
- ✅ Principle IX (YAGNI): No unnecessary attributes, relationships, or abstractions
- ✅ Phase I Constraints: No database schemas, no file formats, no API contracts
