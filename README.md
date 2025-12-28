# Phase I Todo Application 📝

> A clean, minimal, in-memory todo application built with Python

[![Python Version](https://img.shields.io/badge/python-3.13%2B-blue.svg)](https://www.python.org/downloads/)
[![Phase](https://img.shields.io/badge/phase-I%20Basic-brightgreen.svg)](PHASE_I_COMPLETE.md)

---

## 🎯 About

**Phase I** of the "Evolution of Todo" project - A simple console-based todo app demonstrating clean code and Spec-Driven Development.

### Features

- ✅ Add tasks
- ✅ View all tasks
- ✅ Update task title
- ✅ Delete tasks
- ✅ Mark complete/incomplete
- ✅ Menu-driven interface

---

## 🚀 Quick Start

### Prerequisites
- Python 3.13+

### Run

```bash
# Clone the repo
git clone https://github.com/umemasultan/Phase_1_Todo_App.git
cd Phase_1_Todo_App

# Run the app
python src/main.py
```

**Windows:** Double-click `run.bat`

---

## 📖 Usage

```
Main Menu:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete/Incomplete
0. Exit
```

### Example

```bash
$ python src/main.py

=== Todo Application - Phase I ===

Main Menu:
1. Add Task
...

Enter your choice (0-5): 1
Enter task title: Buy groceries

Task added successfully!
ID: 1, Title: Buy groceries, Status: Incomplete
```

---

## 🏗️ Project Structure

```
Phase_1_Todo_App/
├── src/
│   ├── models/task.py         # Task model
│   ├── services/task_service.py   # Business logic
│   ├── cli/menu.py            # Menu interface
│   └── main.py                # Entry point
├── specs/                     # Documentation
├── test_basic_functionality.py    # Tests
└── README.md
```

---

## 🧪 Testing

```bash
# Run tests
python test_basic_functionality.py

# Run demo
python demo_phase1.py
```

---

## 💡 Technical Highlights

- **Clean Architecture** - Models / Services / CLI separation
- **In-Memory Storage** - No database, no files
- **Input Validation** - All user inputs validated
- **Error Handling** - Graceful error messages
- **Pure Python** - No external dependencies

---

## 🗺️ Roadmap

- **Phase I** ✅ - Basic CRUD (Current)
- **Phase II** 🔜 - Priority, categories, search
- **Phase III** 🔮 - Database, statistics, undo
- **Phase IV** 🌐 - Web interface, multi-user

---

## 📚 Documentation

- [PHASE_I_COMPLETE.md](PHASE_I_COMPLETE.md) - Full documentation
- [specs/](specs/001-phase-i-todo-app/) - Detailed specifications

---

## 👤 Author

**Umema Sultan**

[![GitHub](https://img.shields.io/badge/GitHub-umemasultan-181717?style=for-the-badge&logo=github)](https://github.com/umemasultan)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/umema-sultan-385797341/)
[![TikTok](https://img.shields.io/badge/TikTok-@codedremer-000000?style=for-the-badge&logo=tiktok)](https://www.tiktok.com/@codedremer?lang=en)
[![WhatsApp](https://img.shields.io/badge/WhatsApp-Join-25D366?style=for-the-badge&logo=whatsapp)](https://whatsapp.com/channel/0029Vb25yCO7dmeTzYnD7p0M)

**Connect:**
- 💼 [LinkedIn](https://www.linkedin.com/in/umema-sultan-385797341/)
- 🎥 [TikTok @codedremer](https://www.tiktok.com/@codedremer?lang=en) - Coding tutorials
- 💬 [WhatsApp Channel](https://whatsapp.com/channel/0029Vb25yCO7dmeTzYnD7p0M)

---

## 📄 License

MIT License

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ by [Umema Sultan](https://github.com/umemasultan)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/umema-sultan-385797341/)
[![TikTok](https://img.shields.io/badge/TikTok-Follow-000000?style=flat-square&logo=tiktok)](https://www.tiktok.com/@codedremer?lang=en)
[![WhatsApp](https://img.shields.io/badge/WhatsApp-Join-25D366?style=flat-square&logo=whatsapp)](https://whatsapp.com/channel/0029Vb25yCO7dmeTzYnD7p0M)

**Follow for more coding projects! 🚀**

[Documentation](PHASE_I_COMPLETE.md) · [Report Bug](https://github.com/umemasultan/Phase_1_Todo_App/issues) · [Request Feature](https://github.com/umemasultan/Phase_1_Todo_App/issues)

</div>
