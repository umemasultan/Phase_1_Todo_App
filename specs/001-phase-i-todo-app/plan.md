# Implementation Plan: Phase I In-Memory Todo Application

**Branch**: `001-phase-i-todo-app` | **Date**: 2025-12-28 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-phase-i-todo-app/spec.md`

**Note**: This plan defines the technical implementation strategy for Phase I of the Evolution of Todo project.

## Summary

Build an in-memory Python console todo application that provides menu-driven CRUD operations on tasks without any persistence beyond runtime. The application follows clean architecture principles with separation between data models, business logic, and user interface. All functionality is accessible through a numbered menu system that validates inputs and provides clear error messages.

**Primary Requirement**: Single-user console application for managing tasks in memory with add, view, update, delete, and completion tracking capabilities.

**Technical Approach**: Python 3.13+ using standard library only, with a three-layer architecture (models, services, CLI) and simple in-memory list storage with sequential ID generation.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: Python standard library only (no external packages)
**Storage**: In-memory list data structure (no persistence)
**Testing**: pytest (if tests are requested; tests are optional per constitution)
**Target Platform**: Cross-platform console (Windows, macOS, Linux with Python 3.13+ installed)
**Project Type**: Single project (console application)
**Performance Goals**:
- Application startup < 2 seconds
- All operations (add, view, update, delete, mark complete) < 10-15 seconds
- Support 100+ tasks without performance degradation

**Constraints**:
- No file I/O (Phase I constraint)
- No database access (Phase I constraint)
- No external libraries beyond Python standard library
- No web frameworks or networking
- No persistence mechanism
- Single-user only (no authentication or multi-user support)

**Scale/Scope**:
- Single-user local application
- Support for 100+ tasks in memory
- Console-only interface
- 5 core operations (Add, View, Update, Delete, Mark Complete/Incomplete)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### ✅ Principle I: Spec-Driven Development (MANDATORY)
- **Status**: PASS
- **Evidence**: Specification created and approved before planning; plan follows approved spec
- **Action**: None required

### ✅ Principle II: Agent Autonomy with Human Oversight
- **Status**: PASS
- **Evidence**: All implementation decisions derived from approved specification; no feature invention
- **Action**: None required

### ✅ Principle III: Phase Boundary Enforcement
- **Status**: PASS
- **Evidence**: Plan strictly adheres to Phase I constraints:
  - ✅ No file persistence (Phase II feature)
  - ✅ No database (Phase IV feature)
  - ✅ No REST API or web interface (Phase III feature)
  - ✅ No authentication (Phase IV feature)
  - ✅ No event streaming, containerization, or cloud concepts (Phase V features)
- **Action**: None required

### ✅ Principle IV: Test-Driven Development (CONDITIONAL)
- **Status**: PASS
- **Evidence**: Tests are optional per constitutional principle; TDD will be applied only if user requests tests
- **Action**: None required (tests optional unless requested)

### ✅ Principle V: Clean Architecture and Separation of Concerns
- **Status**: PASS
- **Evidence**: Three-layer architecture planned:
  - **Models**: Task data structure (`src/models/task.py`)
  - **Services**: Business logic for CRUD operations (`src/services/task_service.py`)
  - **CLI**: User interface and menu system (`src/cli/menu.py`, `src/main.py`)
- **Action**: None required

### ✅ Principle VI: Stateless Services and Cloud-Native Readiness
- **Status**: N/A for Phase I
- **Evidence**: Phase I is single-user local application; statelessness applies from Phase III onward
- **Action**: None required

### ✅ Principle VII: Observability and Operational Excellence
- **Status**: PASS
- **Evidence**: Error handling and console output specified; structured logging not required for Phase I
- **Action**: None required

### ✅ Principle VIII: Security by Design
- **Status**: PASS
- **Evidence**: Input validation specified for:
  - Task titles (non-empty after trimming) - FR-010, FR-017
  - Task IDs (existence validation) - FR-011
  - Menu choices (numeric validation) - FR-015
- **Action**: None required

### ✅ Principle IX: Simplicity and YAGNI
- **Status**: PASS
- **Evidence**:
  - Using simple Python list for storage (no premature database abstraction)
  - Sequential integer IDs (no UUID or complex ID generation)
  - No repository pattern (direct service layer access to list)
  - No dependency injection framework
  - No design patterns beyond basic layering
- **Action**: None required

### ✅ Principle X: Versioning and Breaking Changes
- **Status**: N/A for Phase I
- **Evidence**: No public APIs in Phase I; versioning applies from Phase III onward
- **Action**: None required

### ✅ Technology Constraints
- **Status**: PASS
- **Evidence**:
  - ✅ Python 3.13+ as specified
  - ✅ Standard library only (no external dependencies)
  - ✅ No databases
  - ✅ No files
  - ✅ No web frameworks
  - ✅ No premature technology from future phases
- **Action**: None required

**Constitution Check Result**: ✅ ALL GATES PASS - Proceed to Phase 0

## Project Structure

### Documentation (this feature)

```text
specs/001-phase-i-todo-app/
├── plan.md              # This file (/sp.plan command output)
├── spec.md              # Feature specification
├── research.md          # Phase 0 output - architecture decisions
├── data-model.md        # Phase 1 output - Task entity definition
├── quickstart.md        # Phase 1 output - how to run the application
├── checklists/
│   └── requirements.md  # Specification quality validation
└── tasks.md             # Phase 2 output (/sp.tasks command)
```

### Source Code (repository root)

```text
src/
├── models/
│   ├── __init__.py
│   └── task.py          # Task data class with id, title, status
├── services/
│   ├── __init__.py
│   └── task_service.py  # CRUD operations, ID generation, validation
├── cli/
│   ├── __init__.py
│   ├── menu.py          # Menu display and user input handling
│   └── display.py       # Task list formatting and output
└── main.py              # Application entry point

tests/                   # Optional - only if TDD requested
├── contract/            # Not applicable for Phase I (no APIs)
├── integration/
│   └── test_user_flows.py
└── unit/
    ├── test_task.py
    ├── test_task_service.py
    └── test_menu.py
```

**Structure Decision**: Selected "Single project" structure as this is a console application without web or mobile components. The three-layer architecture (models, services, CLI) provides clear separation of concerns as required by constitutional Principle V, while remaining simple enough for Phase I scope per Principle IX (Simplicity and YAGNI).

## Complexity Tracking

> **No constitutional violations** - this section intentionally left empty as all constitutional principles are satisfied.

## Architecture Design

### Layer Responsibilities

#### 1. Models Layer (`src/models/`)

**Purpose**: Define data structures for the domain

**Components**:
- `task.py`: Task data class

**Responsibilities**:
- Define Task attributes (id, title, status)
- Provide immutable data structure
- No business logic (data holder only)

**Dependencies**: None (pure data structures)

#### 2. Services Layer (`src/services/`)

**Purpose**: Implement business logic and operations

**Components**:
- `task_service.py`: TaskService class

**Responsibilities**:
- Maintain in-memory task list
- Generate sequential task IDs
- Implement CRUD operations (add, get_all, get_by_id, update, delete)
- Implement status operations (mark_complete, mark_incomplete)
- Validate task data (non-empty titles, ID existence)
- Trim whitespace from titles (FR-017)

**Dependencies**: Models layer (Task class)

#### 3. CLI Layer (`src/cli/`)

**Purpose**: Handle user interaction and display

**Components**:
- `menu.py`: MenuHandler class - menu display and input processing
- `display.py`: DisplayHelper class - task list formatting and output

**Responsibilities**:
- Display numbered menu options
- Capture and validate user input (menu choices, task IDs, titles)
- Handle input errors gracefully (invalid menu choices, non-numeric IDs)
- Format task lists for console display
- Show success and error messages
- Control application flow (loop until exit)

**Dependencies**: Services layer (TaskService), Models layer (Task)

#### 4. Application Entry Point (`src/main.py`)

**Purpose**: Bootstrap and run the application

**Responsibilities**:
- Initialize TaskService
- Initialize MenuHandler
- Start main menu loop
- Handle keyboard interrupts (Ctrl+C) gracefully
- Exit cleanly

**Dependencies**: All layers

### Data Flow

```
User Input (console)
    ↓
MenuHandler (cli/menu.py) - validates input, routes to service
    ↓
TaskService (services/task_service.py) - executes business logic
    ↓
Task List (in-memory list) - stores/retrieves data
    ↓
TaskService returns result or error
    ↓
DisplayHelper (cli/display.py) - formats output
    ↓
Console Output (user sees result)
    ↓
MenuHandler displays menu again (loop)
```

### Key Design Decisions

#### 1. In-Memory Storage Strategy

**Decision**: Use a simple Python list to store Task objects in TaskService

**Rationale**:
- Simplest data structure for Phase I requirements
- O(n) lookup is acceptable for 100 tasks (performance requirement)
- No need for database or file abstraction per constitutional Principle IX (YAGNI)
- Easy to replace with file storage in Phase II or database in Phase IV

**Alternatives Considered**:
- Dictionary with ID as key: More complex than needed; list is sufficient
- Repository pattern with abstraction: Violates YAGNI principle; premature for Phase I

#### 2. Task ID Generation Strategy

**Decision**: Sequential integer counter starting from 1, incremented on each add operation

**Rationale**:
- Simple and predictable for users (FR-003 specifies sequential IDs)
- No need for complex UUID or hash-based IDs in single-user application
- IDs not reused after deletion (simplifies logic, acceptable for Phase I)

**Implementation**:
```python
class TaskService:
    def __init__(self):
        self._tasks = []
        self._next_id = 1

    def add_task(self, title):
        task = Task(id=self._next_id, title=title.strip(), status="Incomplete")
        self._tasks.append(task)
        self._next_id += 1
        return task
```

#### 3. Task Status Model

**Decision**: Two-state string enum: "Complete" and "Incomplete"

**Rationale**:
- FR-018 explicitly requires exactly two states
- Strings are human-readable in console output
- No need for boolean (less clear in display)
- Easy to extend to multiple states in future phases if needed

#### 4. Error Handling Strategy

**Decision**: Service layer returns (success, data_or_error_message) tuples; CLI layer handles display

**Rationale**:
- Keeps error handling logic in service layer (business concern)
- CLI layer remains focused on display and formatting
- Allows for consistent error message format across all operations
- No exceptions for control flow (cleaner code for validation errors)

**Pattern**:
```python
# Service layer
def update_task(self, task_id, new_title):
    if not new_title.strip():
        return (False, "Task title cannot be empty")
    task = self._find_task(task_id)
    if not task:
        return (False, f"Task with ID {task_id} not found")
    task.title = new_title.strip()
    return (True, task)

# CLI layer
success, result = task_service.update_task(id, title)
if success:
    print(f"Task updated: {result.title}")
else:
    print(f"Error: {result}")
```

#### 5. Input Validation Strategy

**Decision**: Multi-layer validation
- CLI layer: Validates input types (numeric for IDs and menu choices)
- Service layer: Validates business rules (non-empty titles, ID existence)

**Rationale**:
- Separation of concerns: UI validation vs. business validation
- CLI catches obvious errors early (non-numeric input)
- Service layer ensures data integrity (business rules)
- Satisfies FR-010, FR-011, FR-015

#### 6. Menu Loop Design

**Decision**: Infinite loop with explicit exit option; each operation returns to menu

**Rationale**:
- FR-013 requires return to menu after each operation
- FR-014 requires explicit exit option
- Simple control flow: while True loop with break on exit choice
- Handles errors without crashing (try-except for keyboard interrupts)

### Non-Functional Architecture Decisions

#### Performance

- **Startup**: Application initializes empty task list (O(1)), displays menu immediately
- **Add/View/Update/Delete**: All operations are O(n) where n = number of tasks
- **Acceptable for Phase I**: 100 tasks → worst case ~100 iterations (negligible on modern hardware)
- **No optimization needed**: Premature optimization violates YAGNI principle

#### Error Handling

- **User Input Errors**: Caught and displayed with clear messages; user can retry
- **Keyboard Interrupts**: Caught gracefully with cleanup message
- **No Crashes**: All error conditions handled per SC-007 (100% error handling)

#### Usability

- **Clear Menu Labels**: Numbered options with descriptive text
- **Visual Formatting**: Task lists formatted with columns for ID, Title, Status
- **Empty List Handling**: Informative message when no tasks exist (FR-016)
- **Consistent Flow**: All operations follow same pattern: input → process → result → menu

## Phase 0: Research (No research needed)

**Status**: ✅ SKIPPED

**Rationale**:
- No unknowns or "NEEDS CLARIFICATION" markers in Technical Context
- Python 3.13+ standard library is well-documented and stable
- Architecture decisions are straightforward for console application
- No external dependencies to evaluate
- All technical choices are clear from specification and constitution

**Conclusion**: Proceed directly to Phase 1 (Design & Contracts)

## Phase 1 Output Artifacts

This section will be completed by generating the following files:

1. **data-model.md** - Detailed Task entity specification
2. **contracts/** - N/A for Phase I (no APIs; this is a console application)
3. **quickstart.md** - How to run the application

**Note**: Contracts directory is not applicable for Phase I as there are no public APIs. Menu interactions are internal to the application and documented in quickstart.md instead.

---

## Next Steps

1. ✅ **Constitution Check**: Passed - all principles satisfied
2. ✅ **Phase 0 (Research)**: Skipped - no unknowns to research
3. ⏳ **Phase 1 (Design)**: Generate data-model.md and quickstart.md
4. ⏳ **Agent Context Update**: Update Claude-specific guidance with Python 3.13+ info
5. ⏳ **Phase 2 (Tasks)**: Run `/sp.tasks` to generate task breakdown after plan approval

**Ready for**: User approval of this plan, then proceed to generate Phase 1 artifacts (data-model.md, quickstart.md) and update agent context.
