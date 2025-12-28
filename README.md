# Phase I Todo Application 📝

> **Evolution of Todo - Hackathon II**
> A clean, minimal, in-memory todo application demonstrating Spec-Driven Development

[![Python Version](https://img.shields.io/badge/python-3.13%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Phase](https://img.shields.io/badge/phase-I%20Basic-brightgreen.svg)](PHASE_I_COMPLETE.md)

---

## 🎯 Project Overview

This is **Phase I** of the "Evolution of Todo" project - a multi-phase journey building a todo application from basic console app to advanced web application. Phase I focuses on **core CRUD operations** with an in-memory data store.

### Phase I Scope: Basic Level ✅

**What's Included:**
- ✅ Add tasks (with title)
- ✅ View all tasks
- ✅ Update task title
- ✅ Delete tasks
- ✅ Mark tasks complete/incomplete
- ✅ Menu-driven CLI interface

**What's NOT Included (Future Phases):**
- ❌ Priority levels
- ❌ Categories/tags
- ❌ Due dates
- ❌ Search/filter/sort
- ❌ File/database persistence
- ❌ Bulk operations
- ❌ Undo/redo

---

## ✨ Features

### Core Operations
| Feature | Description | Status |
|---------|-------------|--------|
| **Add Task** | Create new task with title | ✅ |
| **View Tasks** | Display all tasks in table format | ✅ |
| **Update Task** | Modify existing task title | ✅ |
| **Delete Task** | Remove task by ID | ✅ |
| **Mark Complete** | Toggle task completion status | ✅ |

### Technical Highlights
- 🎨 Clean architecture (Models / Services / CLI)
- 🔒 Input validation & error handling
- 📊 Simple table-based display
- 💾 In-memory storage (no persistence)
- 🐍 Python 3.13+ standard library only
- 🧪 Comprehensive test coverage

---

## 🚀 Quick Start

### Prerequisites
- Python 3.13 or higher
- No external dependencies required!

### Installation

```bash
# Clone the repository
git clone https://github.com/umemasultan/Phase_1_Todo_App.git
cd Phase_1_Todo_App

# Run the application
python src/main.py
```

### Alternative: Windows Quick Launch
```bash
# Double-click or run:
run.bat
```

---

## 📖 Usage

### Menu Interface

```
Main Menu:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete/Incomplete
0. Exit
```

### Example Session

```bash
$ python src/main.py

=== Todo Application - Phase I ===

Main Menu:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete/Incomplete
0. Exit

Enter your choice (0-5): 1

--- Add Task ---
Enter task title: Buy groceries

Task added successfully!
ID: 1, Title: Buy groceries, Status: Incomplete

Press Enter to continue...
```

### View Tasks Output

```
=== Your Tasks ===

ID   | Title                                    | Status
------------------------------------------------------------
1    | Buy groceries                            | Incomplete
2    | Call dentist                             | Complete
3    | Finish report                            | Incomplete

Total tasks: 3
```

---

## 🏗️ Project Structure

```
Phase_1_Todo_App/
├── src/
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py              # Task data model (ID, Title, Status)
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_service.py      # Business logic (CRUD operations)
│   ├── cli/
│   │   ├── __init__.py
│   │   ├── display.py           # Output formatting
│   │   └── menu.py              # Menu handling & user input
│   └── main.py                  # Application entry point
├── specs/
│   └── 001-phase-i-todo-app/
│       ├── spec.md              # Feature specification
│       ├── plan.md              # Implementation plan
│       ├── tasks.md             # Task breakdown
│       └── data-model.md        # Data model documentation
├── history/
│   └── prompts/                 # Development history (PHR logs)
├── test_basic_functionality.py  # Automated tests
├── demo_phase1.py               # Feature demonstration
├── run.bat                      # Windows launcher
├── PHASE_I_COMPLETE.md          # Detailed documentation
└── README.md                    # This file
```

---

## 🧪 Testing

### Run Automated Tests

```bash
python test_basic_functionality.py
```

**Expected Output:**
```
============================================================
Phase I Todo Application - Validation Tests
============================================================
Testing Task model...
[PASS] Task model tests passed

Testing TaskService...
[PASS] TaskService tests passed

Testing DisplayHelper...
[PASS] DisplayHelper tests passed

============================================================
[SUCCESS] ALL TESTS PASSED!
============================================================
```

### Run Feature Demo

```bash
python demo_phase1.py
```

Demonstrates all 5 core features with sample data.

---

## 📊 Technical Details

### Data Model

```python
@dataclass
class Task:
    id: int          # Unique sequential ID (auto-assigned)
    title: str       # Task description (required, non-empty)
    status: str      # "Complete" or "Incomplete"
```

### Architecture

**Clean Architecture Layers:**

1. **Models Layer** (`src/models/`)
   - Data structures with validation
   - No business logic

2. **Services Layer** (`src/services/`)
   - Business logic (CRUD operations)
   - Input validation
   - Error handling
   - Returns `(success: bool, result: Task | error_message)`

3. **CLI Layer** (`src/cli/`)
   - User interaction (menu, input)
   - Output formatting
   - Display logic

4. **Main Entry** (`src/main.py`)
   - Application initialization
   - Dependency wiring
   - Graceful error handling

### Key Design Decisions

- **In-Memory Storage**: Python list for simplicity
- **Sequential IDs**: Auto-incrementing counter
- **Menu-Driven**: Standard CLI pattern (0-5 options)
- **Error Handling**: Tuple returns `(bool, data|error)`
- **No External Dependencies**: Pure Python standard library

---

## 📋 Requirements Checklist

### Functional Requirements (20/20) ✅

- [x] FR-001: Menu-driven console interface
- [x] FR-002: Add tasks with title
- [x] FR-003: Unique sequential IDs
- [x] FR-004: In-memory storage
- [x] FR-005: View all tasks
- [x] FR-006: Update task title
- [x] FR-007: Delete task by ID
- [x] FR-008: Mark task complete
- [x] FR-009: Mark task incomplete
- [x] FR-010: Validate non-empty titles
- [x] FR-011: Validate task IDs exist
- [x] FR-012: Clear error messages
- [x] FR-013: Return to menu after operations
- [x] FR-014: Exit option (0)
- [x] FR-015: Handle invalid menu selections
- [x] FR-016: Empty list message
- [x] FR-017: Trim whitespace from titles
- [x] FR-018: Two states: Complete/Incomplete
- [x] FR-019: New tasks default to Incomplete
- [x] FR-020: In-memory only (no persistence)

### Success Criteria (10/10) ✅

- [x] SC-001: Add task in < 10 seconds
- [x] SC-002: View list in < 3 seconds
- [x] SC-003: Update task in < 15 seconds
- [x] SC-004: Mark/delete in < 10 seconds
- [x] SC-005: Handles 100+ tasks
- [x] SC-006: Clear error messages
- [x] SC-007: 100% error handling (no crashes)
- [x] SC-008: Usable without documentation
- [x] SC-009: Correct status display
- [x] SC-010: Startup < 2 seconds

---

## 🛠️ Development

### Methodology

This project follows **Spec-Driven Development (SDD)**:

1. **Constitution** → Project principles & constraints
2. **Specification** → WHAT to build (user stories, requirements)
3. **Plan** → HOW to build (architecture, design decisions)
4. **Tasks** → Step-by-step implementation breakdown
5. **Implementation** → Code following the plan
6. **Validation** → Tests matching specification

### Development History

All development decisions are recorded in:
- `specs/` - Specifications and planning artifacts
- `history/prompts/` - Prompt History Records (PHRs)

### Code Quality Standards

- ✅ Python 3.13+ type hints
- ✅ Comprehensive docstrings
- ✅ PEP 8 style compliance
- ✅ Single Responsibility Principle
- ✅ No hardcoded values
- ✅ Input validation everywhere
- ✅ Graceful error handling

---

## 🗺️ Roadmap

### Phase I: Basic Level ✅ (Current)
- In-memory CRUD operations
- Menu-driven CLI
- Simple task management

### Phase II: Intermediate Level 🔜 (Next)
- Priority levels (High/Medium/Low)
- Categories and tags
- Due dates
- Search and filter
- File persistence (JSON/CSV)

### Phase III: Advanced Level 🔮 (Future)
- Database integration (SQLite)
- Statistics dashboard
- Bulk operations
- Undo/Redo
- Import/Export

### Phase IV: Web Application 🌐 (Future)
- REST API (Flask/FastAPI)
- Web UI (HTML/CSS/JS)
- Multi-user support
- Authentication

---

## 📚 Documentation

- **[PHASE_I_COMPLETE.md](PHASE_I_COMPLETE.md)** - Full Phase I documentation
- **[specs/001-phase-i-todo-app/spec.md](specs/001-phase-i-todo-app/spec.md)** - Feature specification
- **[specs/001-phase-i-todo-app/plan.md](specs/001-phase-i-todo-app/plan.md)** - Implementation plan
- **[specs/001-phase-i-todo-app/tasks.md](specs/001-phase-i-todo-app/tasks.md)** - Task breakdown

---

## 🤝 Contributing

This is a learning project following a phased approach. Contributions for **Phase II+** features are welcome after Phase I is complete.

### Guidelines
1. Follow Spec-Driven Development process
2. Maintain phase boundaries (no Phase II features in Phase I)
3. Write tests for all new features
4. Follow existing code style
5. Update documentation

---

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details

---

## 👤 Author

**Umema Sultan**
- GitHub: [@umemasultan](https://github.com/umemasultan)
- Project: [Phase_1_Todo_App](https://github.com/umemasultan/Phase_1_Todo_App)

---

## 🙏 Acknowledgments

- Built with **Claude Code** (Spec-Driven Development)
- Follows **Clean Architecture** principles
- Inspired by **The Evolution of Software** concept

---

## 📞 Support

If you encounter issues:
1. Check [PHASE_I_COMPLETE.md](PHASE_I_COMPLETE.md) for detailed docs
2. Run tests: `python test_basic_functionality.py`
3. Open an issue on GitHub

---

## 🎓 Learning Resources

This project demonstrates:
- ✅ Spec-Driven Development (SDD)
- ✅ Clean Architecture
- ✅ SOLID principles
- ✅ Test-Driven Validation
- ✅ Menu-driven CLI design
- ✅ Python best practices

Perfect for learning **software engineering fundamentals**!

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ using Python | Phase I Complete ✅

[View Full Documentation](PHASE_I_COMPLETE.md) | [Report Bug](https://github.com/umemasultan/Phase_1_Todo_App/issues) | [Request Feature](https://github.com/umemasultan/Phase_1_Todo_App/issues)

</div>
