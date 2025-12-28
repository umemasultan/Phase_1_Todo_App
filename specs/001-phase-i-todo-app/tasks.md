# Tasks: Phase I In-Memory Todo Application

**Input**: Design documents from `/specs/001-phase-i-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), data-model.md (required)

**Tests**: Tests are OPTIONAL per constitutional Principle IV. Tasks below do NOT include tests unless explicitly requested.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story, with a foundational phase for shared infrastructure.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US5, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root (per plan.md)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and directory structure

- [x] **T001** Create project directory structure: `src/models/`, `src/services/`, `src/cli/` directories with `__init__.py` files
  - **Preconditions**: Repository root exists
  - **Expected Output**: Directory structure matches plan.md Section "Project Structure"
  - **Artifacts**: `src/models/__init__.py`, `src/services/__init__.py`, `src/cli/__init__.py`
  - **Reference**: plan.md lines 143-166

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] **T002** [P] [Foundation] Create Task model class in `src/models/task.py`
  - **Preconditions**: T001 completed (directory structure exists)
  - **Expected Output**: Task dataclass with attributes: id (int), title (str), status (str); includes `__post_init__` validation
  - **Artifacts**: `src/models/task.py`
  - **Reference**: data-model.md lines 35-74, plan.md lines 178-190
  - **Implementation**: Use Python dataclass; validate id >= 1, title non-empty trimmed, status in ("Complete", "Incomplete")

- [x] **T003** [P] [Foundation] Create TaskService skeleton class in `src/services/task_service.py`
  - **Preconditions**: T002 completed (Task model exists)
  - **Expected Output**: TaskService class with `__init__` method initializing empty `_tasks` list and `_next_id = 1` counter
  - **Artifacts**: `src/services/task_service.py`
  - **Reference**: plan.md lines 192-206, lines 276-297
  - **Implementation**: Initialize `self._tasks: list[Task] = []` and `self._next_id: int = 1`

- [x] **T004** [P] [Foundation] Create DisplayHelper class in `src/cli/display.py`
  - **Preconditions**: T002 completed (Task model exists)
  - **Expected Output**: DisplayHelper class with method `display_tasks(tasks: list[Task])` that formats and prints task list
  - **Artifacts**: `src/cli/display.py`
  - **Reference**: plan.md lines 209-224, spec.md FR-005
  - **Implementation**: Format as table with columns: ID | Title | Status; show "Your task list is empty" if no tasks (FR-016)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 5 - Menu-Driven Interface (Priority: P1) 🎯 Foundation

**Goal**: Provide menu-driven interface for accessing all features

**Independent Test**: Launch application, verify menu displays with 6 options, test invalid input handling

**Spec Reference**: spec.md lines 77-92 (User Story 5)
**Plan Reference**: plan.md lines 351-359 (Menu Loop Design)

### Implementation for User Story 5

- [x] **T005** [US5] Create MenuHandler skeleton class in `src/cli/menu.py`
  - **Preconditions**: T003 completed (TaskService exists)
  - **Expected Output**: MenuHandler class with `__init__(task_service: TaskService)` and `display_menu()` method
  - **Artifacts**: `src/cli/menu.py`
  - **Reference**: plan.md lines 209-224, spec.md FR-001
  - **Implementation**: Store task_service reference; display_menu() prints numbered menu with 6 options: 1. Add Task, 2. View Tasks, 3. Update Task, 4. Delete Task, 5. Mark Complete/Incomplete, 6. Exit

- [x] **T006** [US5] Implement menu input handling and validation in `src/cli/menu.py`
  - **Preconditions**: T005 completed (MenuHandler skeleton exists)
  - **Expected Output**: MenuHandler method `get_menu_choice()` that reads user input, validates numeric 1-6, returns choice
  - **Artifacts**: `src/cli/menu.py` (modify existing)
  - **Reference**: spec.md FR-015, plan.md lines 341-349 (Input Validation Strategy)
  - **Implementation**: Try converting input to int; catch ValueError for non-numeric; check range 1-6; return error message for invalid input

- [x] **T007** [US5] Implement main menu loop in `src/cli/menu.py`
  - **Preconditions**: T006 completed (menu input handling exists)
  - **Expected Output**: MenuHandler method `run()` with infinite while True loop that displays menu, gets choice, routes to handler methods (stubs), breaks on exit
  - **Artifacts**: `src/cli/menu.py` (modify existing)
  - **Reference**: spec.md FR-013 (return to menu), FR-014 (exit option), plan.md lines 351-359
  - **Implementation**: while True loop; call display_menu(); call get_menu_choice(); if 6, break; else call stub handlers (e.g., `_handle_add_task()`); handle keyboard interrupt (Ctrl+C) gracefully

- [x] **T008** [US5] Create application entry point in `src/main.py`
  - **Preconditions**: T007 completed (menu loop exists), T003 completed (TaskService exists), T004 completed (DisplayHelper exists)
  - **Expected Output**: `src/main.py` with `if __name__ == "__main__"` block that initializes TaskService, DisplayHelper, MenuHandler, and runs menu loop
  - **Artifacts**: `src/main.py`
  - **Reference**: plan.md lines 227-238, spec.md SC-010 (startup < 2 seconds)
  - **Implementation**: Instantiate TaskService, DisplayHelper, MenuHandler(task_service, display_helper), call menu_handler.run(); wrap in try-except for KeyboardInterrupt

**Checkpoint**: At this point, application launches, displays menu, handles input, and exits cleanly. Ready to implement CRUD operations.

---

## Phase 4: User Story 1 - Add and View Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to add tasks and view all tasks (core functionality)

**Independent Test**: Add 3 tasks with different titles, view list showing all tasks with IDs and status

**Spec Reference**: spec.md lines 10-24 (User Story 1)
**Plan Reference**: plan.md lines 192-206 (Services Layer)

### Implementation for User Story 1

- [x] **T009** [P] [US1] Implement add_task method in `src/services/task_service.py`
  - **Preconditions**: T003 completed (TaskService skeleton exists), T002 completed (Task model exists)
  - **Expected Output**: TaskService method `add_task(title: str)` that trims title, validates non-empty, creates Task with next ID and "Incomplete" status, appends to list, increments ID counter, returns (True, task) or (False, error_message)
  - **Artifacts**: `src/services/task_service.py` (modify existing)
  - **Reference**: spec.md FR-002, FR-003, FR-010, FR-017, FR-019; plan.md lines 276-297 (ID Generation Strategy)
  - **Implementation**: `title = title.strip()`; if empty, return `(False, "Task title cannot be empty")`; create `Task(id=self._next_id, title=title, status="Incomplete")`; append to `self._tasks`; increment `self._next_id`; return `(True, task)`

- [x] **T010** [P] [US1] Implement get_all_tasks method in `src/services/task_service.py`
  - **Preconditions**: T003 completed (TaskService skeleton exists)
  - **Expected Output**: TaskService method `get_all_tasks()` that returns list of all tasks
  - **Artifacts**: `src/services/task_service.py` (modify existing)
  - **Reference**: spec.md FR-005
  - **Implementation**: Return `self._tasks` (or copy of it to prevent external modification: `list(self._tasks)`)

- [x] **T011** [US1] Implement add task handler in `src/cli/menu.py`
  - **Preconditions**: T009 completed (add_task service method exists), T007 completed (menu loop exists)
  - **Expected Output**: MenuHandler method `_handle_add_task()` that prompts for title, calls task_service.add_task(), displays success or error message, pauses for Enter
  - **Artifacts**: `src/cli/menu.py` (modify existing)
  - **Reference**: spec.md US1 Acceptance Scenario 1 & 4, plan.md lines 319-337 (Error Handling Strategy)
  - **Implementation**: Read title from input; call `success, result = self.task_service.add_task(title)`; if success, print success message with task details; else print error; wait for Enter press (FR-013)

- [x] **T012** [US1] Implement view tasks handler in `src/cli/menu.py`
  - **Preconditions**: T010 completed (get_all_tasks service method exists), T004 completed (DisplayHelper exists), T007 completed (menu loop exists)
  - **Expected Output**: MenuHandler method `_handle_view_tasks()` that calls task_service.get_all_tasks(), passes to display_helper.display_tasks(), pauses for Enter
  - **Artifacts**: `src/cli/menu.py` (modify existing)
  - **Reference**: spec.md US1 Acceptance Scenario 2 & 3, spec.md FR-016 (empty list message)
  - **Implementation**: Call `tasks = self.task_service.get_all_tasks()`; call `self.display_helper.display_tasks(tasks)`; wait for Enter press (FR-013)

- [x] **T013** [US1] Connect add and view handlers to menu loop in `src/cli/menu.py`
  - **Preconditions**: T011 completed (add handler exists), T012 completed (view handler exists), T007 completed (menu loop exists)
  - **Expected Output**: Menu loop routes choice 1 to `_handle_add_task()` and choice 2 to `_handle_view_tasks()`
  - **Artifacts**: `src/cli/menu.py` (modify existing)
  - **Reference**: spec.md FR-001 (menu-driven interface)
  - **Implementation**: In run() loop, after get_menu_choice(), add if/elif branches: if choice == 1: call `_handle_add_task()`; elif choice == 2: call `_handle_view_tasks()`

**Checkpoint**: At this point, User Story 1 is fully functional - users can add tasks and view the list. This is the MVP baseline.

---

## Phase 5: User Story 2 - Mark Tasks Complete or Incomplete (Priority: P2)

**Goal**: Enable users to toggle task completion status

**Independent Test**: Add tasks, mark some complete, view list showing updated statuses, mark complete tasks incomplete

**Spec Reference**: spec.md lines 27-41 (User Story 2)
**Plan Reference**: plan.md lines 299-307 (Task Status Model)

### Implementation for User Story 2

- [x] **T014** [P] [US2] Implement get_task_by_id helper method in `src/services/task_service.py`
  - **Preconditions**: T003 completed (TaskService skeleton exists)
  - **Expected Output**: TaskService private method `_find_task(task_id: int)` that searches `_tasks` list for task with matching ID, returns Task or None
  - **Artifacts**: `src/services/task_service.py` (modify existing)
  - **Reference**: spec.md FR-011 (ID validation), plan.md lines 192-206
  - **Implementation**: Loop through `self._tasks`; if `task.id == task_id`, return task; return None if not found

- [x] **T015** [P] [US2] Implement mark_complete method in `src/services/task_service.py`
  - **Preconditions**: T014 completed (find_task helper exists), T002 completed (Task model exists)
  - **Expected Output**: TaskService method `mark_complete(task_id: int)` that finds task, sets status to "Complete", returns (True, task) or (False, error_message)
  - **Artifacts**: `src/services/task_service.py` (modify existing)
  - **Reference**: spec.md FR-008, FR-011; plan.md lines 299-307
  - **Implementation**: Call `task = self._find_task(task_id)`; if None, return `(False, f"Task with ID {task_id} not found")`; set `task.status = "Complete"`; return `(True, task)`

- [x] **T016** [P] [US2] Implement mark_incomplete method in `src/services/task_service.py`
  - **Preconditions**: T014 completed (find_task helper exists), T002 completed (Task model exists)
  - **Expected Output**: TaskService method `mark_incomplete(task_id: int)` that finds task, sets status to "Incomplete", returns (True, task) or (False, error_message)
  - **Artifacts**: `src/services/task_service.py` (modify existing)
  - **Reference**: spec.md FR-009, FR-011; plan.md lines 299-307
  - **Implementation**: Call `task = self._find_task(task_id)`; if None, return `(False, f"Task with ID {task_id} not found")`; set `task.status = "Incomplete"`; return `(True, task)`

- [x] **T017** [US2] Implement mark status handler in `src/cli/menu.py`
  - **Preconditions**: T015 completed (mark_complete exists), T016 completed (mark_incomplete exists), T007 completed (menu loop exists)
  - **Expected Output**: MenuHandler method `_handle_mark_status()` that prompts for task ID (validates numeric), prompts for 'c' or 'i', calls appropriate service method, displays result
  - **Artifacts**: `src/cli/menu.py` (modify existing)
  - **Reference**: spec.md US2 Acceptance Scenarios 1-3, plan.md lines 341-349 (Input Validation)
  - **Implementation**: Read ID input; try converting to int (catch ValueError); read choice ('c' or 'i'); validate choice; call mark_complete or mark_incomplete; display success or error; wait for Enter

- [x] **T018** [US2] Connect mark status handler to menu loop in `src/cli/menu.py`
  - **Preconditions**: T017 completed (mark status handler exists), T013 completed (menu loop routes choices)
  - **Expected Output**: Menu loop routes choice 5 to `_handle_mark_status()`
  - **Artifacts**: `src/cli/menu.py` (modify existing)
  - **Reference**: spec.md FR-001
  - **Implementation**: In run() loop, add elif branch: if choice == 5: call `_handle_mark_status()`

**Checkpoint**: At this point, User Story 2 is fully functional - users can mark tasks complete or incomplete.

---

## Phase 6: User Story 3 - Update Task Title (Priority: P3)

**Goal**: Enable users to edit task titles

**Independent Test**: Add task, update its title to new value, view list showing updated title

**Spec Reference**: spec.md lines 44-57 (User Story 3)
**Plan Reference**: plan.md lines 319-337 (Error Handling Strategy)

### Implementation for User Story 3

- [x] **T019** [US3] Implement update_task method in `src/services/task_service.py`
  - **Preconditions**: T014 completed (find_task helper exists)
  - **Expected Output**: TaskService method `update_task(task_id: int, new_title: str)` that finds task, trims and validates new title, updates title, returns (True, task) or (False, error_message)
  - **Artifacts**: `src/services/task_service.py` (modify existing)
  - **Reference**: spec.md FR-006, FR-010, FR-011, FR-017; plan.md lines 319-337
  - **Implementation**: Trim new_title; if empty, return error; call _find_task; if None, return error; set `task.title = new_title.strip()`; return success

- [x] **T020** [US3] Implement update task handler in `src/cli/menu.py`
  - **Preconditions**: T019 completed (update_task service method exists), T007 completed (menu loop exists)
  - **Expected Output**: MenuHandler method `_handle_update_task()` that prompts for task ID (validates numeric), prompts for new title, calls task_service.update_task(), displays result
  - **Artifacts**: `src/cli/menu.py` (modify existing)
  - **Reference**: spec.md US3 Acceptance Scenarios 1-3, plan.md lines 341-349 (Input Validation)
  - **Implementation**: Read ID input; try converting to int (catch ValueError); read new title; call `success, result = self.task_service.update_task(id, title)`; display success or error; wait for Enter

- [x] **T021** [US3] Connect update handler to menu loop in `src/cli/menu.py`
  - **Preconditions**: T020 completed (update handler exists), T018 completed (menu loop routes choices)
  - **Expected Output**: Menu loop routes choice 3 to `_handle_update_task()`
  - **Artifacts**: `src/cli/menu.py` (modify existing)
  - **Reference**: spec.md FR-001
  - **Implementation**: In run() loop, add elif branch: if choice == 3: call `_handle_update_task()`

**Checkpoint**: At this point, User Story 3 is fully functional - users can update task titles.

---

## Phase 7: User Story 4 - Delete Tasks (Priority: P4)

**Goal**: Enable users to remove tasks from the list

**Independent Test**: Add tasks, delete specific task by ID, view list showing task removed

**Spec Reference**: spec.md lines 60-74 (User Story 4)
**Plan Reference**: plan.md lines 192-206 (Services Layer)

### Implementation for User Story 4

- [x] **T022** [US4] Implement delete_task method in `src/services/task_service.py`
  - **Preconditions**: T014 completed (find_task helper exists)
  - **Expected Output**: TaskService method `delete_task(task_id: int)` that finds task, removes from list, returns (True, deleted_task) or (False, error_message)
  - **Artifacts**: `src/services/task_service.py` (modify existing)
  - **Reference**: spec.md FR-007, FR-011; plan.md lines 192-206
  - **Implementation**: Call _find_task; if None, return error; remove task from `self._tasks` list; return success with deleted task (for display)

- [x] **T023** [US4] Implement delete task handler in `src/cli/menu.py`
  - **Preconditions**: T022 completed (delete_task service method exists), T007 completed (menu loop exists)
  - **Expected Output**: MenuHandler method `_handle_delete_task()` that prompts for task ID (validates numeric), calls task_service.delete_task(), displays result
  - **Artifacts**: `src/cli/menu.py` (modify existing)
  - **Reference**: spec.md US4 Acceptance Scenarios 1-3, plan.md lines 341-349 (Input Validation)
  - **Implementation**: Read ID input; try converting to int (catch ValueError); call `success, result = self.task_service.delete_task(id)`; display success message with deleted task details or error; wait for Enter

- [x] **T024** [US4] Connect delete handler to menu loop in `src/cli/menu.py`
  - **Preconditions**: T023 completed (delete handler exists), T021 completed (menu loop routes choices)
  - **Expected Output**: Menu loop routes choice 4 to `_handle_delete_task()`
  - **Artifacts**: `src/cli/menu.py` (modify existing)
  - **Reference**: spec.md FR-001
  - **Implementation**: In run() loop, add elif branch: if choice == 4: call `_handle_delete_task()`

**Checkpoint**: At this point, User Story 4 is fully functional - users can delete tasks.

---

## Phase 8: Polish & Validation

**Purpose**: Final validation, error handling improvements, and user experience polish

- [x] **T025** [P] Add error message for invalid menu choices in `src/cli/menu.py`
  - **Preconditions**: T006 completed (menu input validation exists)
  - **Expected Output**: get_menu_choice() displays "Invalid choice. Please enter a number between 1 and 6." for invalid input
  - **Artifacts**: `src/cli/menu.py` (modify existing)
  - **Reference**: spec.md FR-015, quickstart.md "Invalid Menu Choice" section
  - **Implementation**: In get_menu_choice(), if choice out of range or ValueError caught, print error message and re-display menu

- [x] **T026** [P] Add graceful keyboard interrupt handling in `src/main.py`
  - **Preconditions**: T008 completed (application entry point exists)
  - **Expected Output**: Pressing Ctrl+C displays "Application interrupted. Exiting..." and exits cleanly
  - **Artifacts**: `src/main.py` (modify existing)
  - **Reference**: spec.md Edge Case "keyboard interrupts", plan.md lines 370-374 (Error Handling)
  - **Implementation**: Wrap menu_handler.run() in try-except KeyboardInterrupt block; print exit message on interrupt

- [x] **T027** [P] Add application startup message in `src/main.py`
  - **Preconditions**: T008 completed (application entry point exists)
  - **Expected Output**: Application prints "=== Todo Application - Phase I ===" on startup before menu
  - **Artifacts**: `src/main.py` (modify existing)
  - **Reference**: quickstart.md "Expected Output" section
  - **Implementation**: Print banner message before calling menu_handler.run()

- [x] **T028** [P] Add exit message in `src/cli/menu.py`
  - **Preconditions**: T007 completed (menu loop with exit exists)
  - **Expected Output**: Selecting exit option (6) displays "Thank you for using Todo Application! Goodbye!" before exiting
  - **Artifacts**: `src/cli/menu.py` (modify existing)
  - **Reference**: spec.md FR-014 (exit option), quickstart.md "6. Exit" section
  - **Implementation**: In run() loop, when choice == 6, print exit message before breaking

- [x] **T029** Validate all functional requirements covered
  - **Preconditions**: All T001-T028 completed
  - **Expected Output**: Manual verification that all 20 functional requirements (FR-001 through FR-020) are implemented
  - **Artifacts**: None (validation task)
  - **Reference**: spec.md lines 107-129 (all FRs)
  - **Implementation**: Test each FR by running application: FR-001 (menu), FR-002 (add), FR-003 (IDs), FR-004 (in-memory), FR-005 (view), FR-006 (update), FR-007 (delete), FR-008/009 (mark status), FR-010/017 (validation), FR-011 (ID validation), FR-012/016 (error messages), FR-013 (return to menu), FR-014 (exit), FR-015 (invalid menu), FR-018/019 (status model), FR-020 (no persistence)

- [x] **T030** Validate all acceptance scenarios pass
  - **Preconditions**: T029 completed (all FRs validated)
  - **Expected Output**: Manual testing confirms all 20+ acceptance scenarios from spec.md pass
  - **Artifacts**: None (validation task)
  - **Reference**: spec.md User Story Acceptance Scenarios (US1: 4 scenarios, US2: 4 scenarios, US3: 3 scenarios, US4: 4 scenarios, US5: 5 scenarios)
  - **Implementation**: Test each acceptance scenario manually; verify Given-When-Then conditions

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: No dependencies - start immediately
- **Phase 2 (Foundational)**: Depends on Phase 1 completion - BLOCKS all user stories
- **Phase 3 (User Story 5 - Menu)**: Depends on Phase 2 (T002, T003, T004) - must complete before other user stories
- **Phase 4 (User Story 1 - Add/View)**: Depends on Phase 2 + Phase 3 (menu infrastructure)
- **Phase 5 (User Story 2 - Mark Status)**: Depends on Phase 2 + Phase 3 (can run parallel with Phase 4 service layer tasks)
- **Phase 6 (User Story 3 - Update)**: Depends on Phase 2 + Phase 3 (can run parallel with Phase 4-5 service layer tasks)
- **Phase 7 (User Story 4 - Delete)**: Depends on Phase 2 + Phase 3 (can run parallel with Phase 4-6 service layer tasks)
- **Phase 8 (Polish)**: Depends on all user story implementations complete

### Critical Path

```
T001 → T002/T003/T004 (parallel) → T005 → T006 → T007 → T008 → T009/T010 (parallel) → T011 → T012 → T013 → [US2-US4 can proceed in parallel] → T025-T028 (parallel) → T029 → T030
```

### Parallel Opportunities

**Phase 2 (Foundation)**:
- T002, T003, T004 can run in parallel (different files, no dependencies)

**Phase 4-7 (User Stories Service Layer)**:
- T009/T010 (US1), T014/T015/T016 (US2), T019 (US3), T022 (US4) can run in parallel (all modify task_service.py but implement different methods)

**Phase 8 (Polish)**:
- T025, T026, T027, T028 can run in parallel (different files or different methods)

### Sequential Requirements

- T001 MUST complete before T002, T003, T004
- T002 MUST complete before any service methods (T009, T010, T014, T015, T016, T019, T022)
- T003 MUST complete before menu handler creation (T005)
- T007 (menu loop) MUST complete before any menu handlers (T011, T012, T017, T020, T023)
- Each user story's service methods MUST complete before their corresponding CLI handlers
- CLI handlers MUST complete before connecting to menu loop

---

## Implementation Strategy

### MVP First (User Story 1 + Menu Foundation)

1. Complete Phase 1: Setup (T001)
2. Complete Phase 2: Foundational (T002, T003, T004 in parallel)
3. Complete Phase 3: Menu Infrastructure (T005 → T006 → T007 → T008 sequentially)
4. Complete Phase 4: Add and View Tasks (T009, T010 parallel → T011 → T012 → T013)
5. **STOP and VALIDATE**: Test adding and viewing tasks - this is the functional MVP

### Incremental Delivery (Add Features One at a Time)

1. After MVP validated, add User Story 2 (Phase 5: T014-T018)
   - **Test independently**: Mark tasks complete/incomplete
2. Add User Story 3 (Phase 6: T019-T021)
   - **Test independently**: Update task titles
3. Add User Story 4 (Phase 7: T022-T024)
   - **Test independently**: Delete tasks
4. Complete Phase 8 (Polish: T025-T030)
   - Final validation and UX improvements

### Parallel Team Strategy (If Multiple Developers)

After completing Phase 1-3 (Foundation + Menu):

- **Developer A**: Phase 4 (User Story 1 - Add/View) - T009, T010, T011, T012, T013
- **Developer B**: Phase 5 (User Story 2 - Mark Status) - T014, T015, T016, T017, T018
- **Developer C**: Phase 6 (User Story 3 - Update) - T019, T020, T021
- **Developer D**: Phase 7 (User Story 4 - Delete) - T022, T023, T024

Then all developers collaborate on Phase 8 (Polish).

---

## Task Summary

**Total Tasks**: 30

**By Phase**:
- Phase 1 (Setup): 1 task
- Phase 2 (Foundational): 3 tasks (T002-T004)
- Phase 3 (Menu - US5): 4 tasks (T005-T008)
- Phase 4 (Add/View - US1): 5 tasks (T009-T013)
- Phase 5 (Mark Status - US2): 5 tasks (T014-T018)
- Phase 6 (Update - US3): 3 tasks (T019-T021)
- Phase 7 (Delete - US4): 3 tasks (T022-T024)
- Phase 8 (Polish): 6 tasks (T025-T030)

**Parallelizable Tasks**: 11 tasks marked with [P]

**Critical Path Length**: ~20 tasks (sequential dependencies)

**Estimated Completion**: All user stories independently completable and testable after their respective phases

---

## Notes

- All tasks include exact file paths for clarity
- Tasks reference specific spec sections (FR-XXX) and plan sections for traceability
- Each task specifies preconditions, expected output, and artifacts
- Service layer methods use (success, data_or_error) tuple pattern per plan
- Input validation split between CLI (type) and service (business rules) layers
- No tests included (optional per constitution Principle IV)
- Each user story can be independently tested after its phase completes
- Menu-driven interface (US5) is foundational for all other user stories
- Add/View (US1) is the MVP baseline; other user stories build on this foundation

**Constitutional Compliance**:
- ✅ Phase I only (no files, databases, APIs)
- ✅ Python 3.13+ standard library only
- ✅ Clean architecture (models, services, CLI separation)
- ✅ YAGNI (no unnecessary abstractions)
- ✅ All tasks derived from approved spec and plan
