# 📚 Student Record Management System

A console-based **Student Record Management System** built with Python. This application provides a fully interactive, menu-driven interface for managing student records with persistent file storage.

---

## 📋 Project Description

This project is a **Console Record-Management Application** developed as part of the Python for Data Analytics (PYDA) course. It demonstrates core Python programming concepts through a practical, working application that manages student academic records.

The system allows users to perform complete CRUD (Create, Read, Update, Delete) operations on student data, with all records persisted to a JSON file so data is retained between sessions.

---

## ✨ Features

| Feature | Description |
|---|---|
| **Add Records** | Add new student records with auto-generated unique IDs |
| **View All Records** | Display all records in a formatted table layout |
| **Search Records** | Search by Student ID or by Name (partial match supported) |
| **Update Records** | Update individual fields of a record (press Enter to skip) |
| **Delete Records** | Delete records with confirmation prompt |
| **Statistics Dashboard** | View total count, average age, grade & course distributions |
| **Data Persistence** | All data saved to/loaded from `students.json` automatically |
| **Input Validation** | Comprehensive validation for all user inputs |
| **Error Handling** | Graceful handling of file errors, invalid data, and edge cases |

---

## 🧠 Technologies & Concepts Used

| Concept | How It's Used |
|---|---|
| **Data Types & Variables** | `str`, `int`, `float`, `bool`, `list`, `dict` used throughout |
| **Conditional Statements** | `if/elif/else` for menu routing, validation, and search logic |
| **Loops** | `while` loops for menu, input validation; `for` loops for iteration |
| **Functions** | 15+ functions with clear separation of concerns (CRUD, I/O, helpers) |
| **Exception Handling** | `try/except` for `ValueError`, `JSONDecodeError`, `PermissionError`, `OSError` |
| **File I/O** | JSON-based read/write for persistent storage with `open()`, `json.load()`, `json.dump()` |
| **Menu-Driven Design** | Numbered menu with continuous loop until user exits |

---

## 📂 Project Structure

```
PYDA - 1/
├── main.py            # Main application source code
├── students.json      # Data file (auto-created, sample data included)
├── README.md          # Project documentation (this file)
└── REPORT.md          # Detailed assignment report
```

---

## 🚀 How to Run the Application

### Prerequisites
- Python 3.10 or higher installed on your system

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mrtusharpandey4u-droid/Console-Record-Management-Application.git
   ```

2. **Run the application:**
   ```bash
   python main.py
   ```

3. **Follow the on-screen menu** to interact with the system.

> **Note:** No external libraries are required. The application uses only Python standard library modules (`json`, `os`, `sys`).

---

## 📸 Sample Input/Output

### Main Menu
```
══════════════════════════════════════════
   WELCOME TO THE STUDENT RECORD
       MANAGEMENT SYSTEM
══════════════════════════════════════════

  ℹ Loaded 5 existing record(s) from 'students.json'.

╔══════════════════════════════════════╗
║   STUDENT RECORD MANAGEMENT SYSTEM   ║
╠══════════════════════════════════════╣
║   1. Add a New Student Record        ║
║   2. View All Student Records        ║
║   3. Search for a Student Record     ║
║   4. Update a Student Record         ║
║   5. Delete a Student Record         ║
║   6. Display Statistics              ║
║   7. Exit                            ║
╚══════════════════════════════════════╝

  Enter your choice (1-7):
```

### Adding a Record
```
╔══════════════════════════════════════╗
║      ADD A NEW STUDENT RECORD        ║
╚══════════════════════════════════════╝
  Enter student name  : Ananya Verma
  Enter student age   : 21
  Enter course name   : Machine Learning
  Enter grade ['A+', 'A', 'B+', 'B', 'C+', 'C', 'D', 'F'] : A
  Enter phone (10 digits) : 9001234567

  ✓ Student record added successfully! (ID: 1006)
```

### Viewing All Records
```
╔══════════════════════════════════════╗
║      ALL STUDENT RECORDS             ║
╚══════════════════════════════════════╝

  Total Records: 5

══════════════════════════════════════════════════════════════════════════════
ID       Name                   Age    Course               Grade    Phone
──────────────────────────────────────────────────────────────────────────────
1001     Aarav Sharma           20     Computer Science     A+       9876543210
1002     Priya Patel            21     Data Science         A        9123456789
1003     Rohan Mehta            19     Computer Science     B+       9988776655
1004     Sneha Gupta            22     Artificial Intelligence A     8877665544
1005     Vikram Singh           20     Data Science         B        7766554433
══════════════════════════════════════════════════════════════════════════════
```

### Searching by Name
```
╔══════════════════════════════════════╗
║      SEARCH STUDENT RECORDS          ║
╚══════════════════════════════════════╝

  Search by:
    1. Student ID
    2. Student Name
  Enter choice (1-2): 2
  Enter name to search: priya

  ✓ Found 1 matching record(s):

══════════════════════════════════════════════════════════════════════════════
ID       Name                   Age    Course               Grade    Phone
──────────────────────────────────────────────────────────────────────────────
1002     Priya Patel            21     Data Science         A        9123456789
══════════════════════════════════════════════════════════════════════════════
```

### Statistics
```
╔══════════════════════════════════════╗
║      RECORD STATISTICS               ║
╚══════════════════════════════════════╝

  Total Students    : 5
  Average Age       : 20.4
  Youngest Student  : 19
  Oldest Student    : 22

  Grade Distribution:
──────────────────────────────
    A+   :   1  █
    A    :   2  ██
    B+   :   1  █
    B    :   1  █
──────────────────────────────

  Course Distribution:
────────────────────────────────────────
    Artificial Intelligence  :   1  █
    Computer Science         :   2  ██
    Data Science             :   2  ██
────────────────────────────────────────
```

---

## 📄 Data File Format

Records are stored in `students.json` using the following structure:

```json
[
    {
        "id": 1001,
        "name": "Aarav Sharma",
        "age": 20,
        "course": "Computer Science",
        "grade": "A+",
        "phone": "9876543210"
    }
]
```

---

## 🔗 GitHub Repository

**Repository URL:** `(https://github.com/mrtusharpandey4u-droid/Console-Record-Management-Application)`

---

## 👤 Author

- **Name:** Tushar Pandey
- **Course:** Python for Data Analytics (PYDA)
- **Date:** 23rd September 2026
