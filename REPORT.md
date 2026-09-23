# Assignment 1: Mini Project – Console Record-Management Application

## Assignment Report

**Student Name:** Tushar  
**Date:** September 2026  
**Subject:** Python for Data Analytics (PYDA)  
**Project Title:** Student Record Management System

---

## 1. Introduction

This report documents the development of a **Console Record-Management Application** as part of Assignment 1 for the PYDA course. The application is a **Student Record Management System** that allows users to manage student academic records through an interactive, menu-driven console interface.

The application demonstrates the practical integration of six core Python concepts: data types and variables, conditional statements and loops, functions, exception handling, file I/O, and menu-driven console application design.

---

## 2. Objective

To develop a fully functional, console-based record-management application in Python that:

- Provides a clean, menu-driven user interface
- Supports complete CRUD operations (Create, Read, Update, Delete)
- Uses structured functions for modularity and readability
- Handles errors gracefully through exception handling
- Persists data to disk using file I/O (JSON format)
- Demonstrates proper use of Python data types and data structures

---

## 3. System Design

### 3.1 Architecture

The application follows a **single-module architecture** with a clear separation of concerns through functions:

```
main.py
├── Constants & Configuration
├── File I/O Functions        (load_records, save_records)
├── Helper/Utility Functions  (generate_id, get_valid_int, print_record_table, ...)
├── Core CRUD Functions       (add_record, view_all_records, search_record, update_record, delete_record)
├── Statistics Function       (display_statistics)
├── Menu & Main Function      (display_menu, main)
└── Entry Point               (__name__ == "__main__")
```

### 3.2 Data Structure

Each student record is represented as a **Python dictionary** with the following fields:

| Field | Data Type | Description | Validation |
|-------|-----------|-------------|------------|
| `id` | `int` | Unique student identifier | Auto-generated (starts at 1001) |
| `name` | `str` | Student's full name | Non-empty, title-cased |
| `age` | `int` | Student's age | Integer between 5 and 120 |
| `course` | `str` | Enrolled course name | Non-empty, title-cased |
| `grade` | `str` | Academic grade | Must be one of: A+, A, B+, B, C+, C, D, F |
| `phone` | `str` | Contact number | Exactly 10 digits |

All records are stored in a **list of dictionaries** (`list[dict]`), which is serialized to/from a JSON file.

### 3.3 Data Flow

```
User Input → Validation → In-Memory List → JSON File (students.json)
                                    ↑
                              Program Start
                                    ↑
                              JSON File → In-Memory List
```

---

## 4. Python Concepts Demonstrated

### 4.1 Data Types and Variables

The application uses a variety of Python data types:

- **`str`**: Student names, courses, grades, phone numbers, file paths
- **`int`**: Student IDs, ages, menu choices
- **`float`**: Average age calculation in statistics
- **`bool`**: Confirmation results, save success flags
- **`list`**: Collection of all student records; list of ages for statistics
- **`dict`**: Individual student records; menu options mapping; grade/course counts
- **Type Hints**: Used throughout for documentation (e.g., `list[dict]`, `int | None`)

**Example from code:**
```python
MENU_OPTIONS: dict[int, str] = {
    1: "Add a New Student Record",
    2: "View All Student Records",
    ...
}

VALID_GRADES: list[str] = ["A+", "A", "B+", "B", "C+", "C", "D", "F"]
```

### 4.2 Conditional Statements and Loops

- **`if/elif/else`**: Used for menu routing, input validation, search type selection, and field update logic
- **`while True`** loops: Used for the main menu loop and input validation loops (re-prompting on invalid input)
- **`for`** loops: Used for iterating over records to display, search, and calculate statistics

**Example from code:**
```python
while True:
    display_menu()
    choice = get_valid_int("\n  Enter your choice (1-7): ", min_val=1, max_val=7)

    if choice == 1:
        add_record(records)
    elif choice == 2:
        view_all_records(records)
    ...
    elif choice == 7:
        print("Goodbye!")
        sys.exit(0)
```

### 4.3 Functions

The application is built entirely with functions — **15+ named functions** covering:

| Category | Functions |
|----------|-----------|
| File I/O | `load_records()`, `save_records()` |
| Input Validation | `get_valid_int()`, `get_non_empty_string()`, `get_valid_phone()`, `get_valid_grade()` |
| Display Helpers | `print_separator()`, `print_record()`, `print_record_table()`, `display_menu()` |
| Utility | `generate_id()`, `find_record_by_id()`, `confirm_action()` |
| Core CRUD | `add_record()`, `view_all_records()`, `search_record()`, `update_record()`, `delete_record()` |
| Analytics | `display_statistics()` |
| Entry Point | `main()` |

Each function has a **docstring** explaining its purpose, parameters, and return value.

### 4.4 Exception Handling

Exception handling is implemented throughout the application:

| Exception | Where Handled | Purpose |
|-----------|---------------|---------|
| `ValueError` | `get_valid_int()`, `update_record()` | Invalid integer input from user |
| `json.JSONDecodeError` | `load_records()` | Corrupted or malformed JSON data file |
| `PermissionError` | `load_records()`, `save_records()` | File access permission issues |
| `OSError` | `load_records()`, `save_records()` | General file system errors |

**Example from code:**
```python
try:
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)
except json.JSONDecodeError:
    print("[WARNING] Data file is corrupted. Starting with empty records.")
    return []
except PermissionError:
    print(f"[ERROR] Permission denied when reading '{filepath}'.")
    return []
```

The application also implements **rollback logic** — if saving fails after adding or deleting a record, the in-memory change is reverted.

### 4.5 File I/O

- **Format**: JSON (human-readable, structured)
- **Library**: Python's built-in `json` module
- **Read**: `json.load()` reads the file at program startup
- **Write**: `json.dump()` writes after every add, update, or delete operation
- **Encoding**: UTF-8 (`encoding="utf-8"`)
- **Formatting**: Pretty-printed with `indent=4`

### 4.6 Menu-Driven Console Application Design

- A numbered menu is displayed after every action
- The user selects an option by entering a number (1–7)
- Invalid choices are rejected with a helpful error message
- A "Press Enter to continue" prompt keeps the console readable
- Box-drawing characters (`╔`, `║`, `╚`) are used for visual structure

---

## 5. Features Summary

1. **Add Record**: Collects validated input, auto-assigns ID, saves to file
2. **View All Records**: Displays records in a formatted table with column headers
3. **Search Records**: Search by exact ID or partial name match (case-insensitive)
4. **Update Record**: Selectively update fields; press Enter to keep existing value
5. **Delete Record**: Confirmation required before deletion; rollback on save failure
6. **Statistics Dashboard**: Total count, average/min/max age, grade and course distribution with bar charts
7. **Persistent Storage**: Data survives program restarts via JSON file

---

## 6. Testing

The application was tested for the following scenarios:

| Test Case | Input | Expected Result | Status |
|-----------|-------|-----------------|--------|
| Add valid record | Name, age, course, grade, phone | Record added with new ID | ✓ Pass |
| Add with invalid age | "abc" | Error message, re-prompt | ✓ Pass |
| Add with invalid phone | "12345" | Error message, re-prompt | ✓ Pass |
| View empty database | (no records) | "No records found" message | ✓ Pass |
| Search by existing ID | 1001 | Record displayed | ✓ Pass |
| Search by non-existent ID | 9999 | "Not found" message | ✓ Pass |
| Search by partial name | "pri" | Matching records shown | ✓ Pass |
| Update with Enter (skip) | Press Enter | Field unchanged | ✓ Pass |
| Delete with confirmation | "y" | Record removed | ✓ Pass |
| Delete cancelled | "n" | Record kept | ✓ Pass |
| Invalid menu choice | 0 or 8 | Error, re-prompt | ✓ Pass |
| Corrupted JSON file | Malformed JSON | Warning, empty list used | ✓ Pass |
| Statistics on data | 5 records | Correct averages & counts | ✓ Pass |

---

## 7. Limitations and Future Enhancements

### Current Limitations
- Single-user, single-machine application
- No sorting or filtering of records in the view
- Phone validation is India-specific (10 digits)

### Possible Enhancements
- Export records to CSV or PDF format
- Add sorting (by name, age, grade, ID)
- Add pagination for large datasets
- Implement a login/authentication system
- Migrate to a database (SQLite) for better data management

---

## 8. Conclusion

This project successfully demonstrates the integration of core Python programming concepts into a practical, working application. The Student Record Management System provides a clean user interface, robust input validation, comprehensive error handling, and persistent data storage. The modular design using functions ensures readability, maintainability, and extensibility.

---

## 9. References

- Python Official Documentation: [https://docs.python.org/3/](https://docs.python.org/3/)
- Python `json` Module: [https://docs.python.org/3/library/json.html](https://docs.python.org/3/library/json.html)
- Python File I/O: [https://docs.python.org/3/tutorial/inputoutput.html](https://docs.python.org/3/tutorial/inputoutput.html)
