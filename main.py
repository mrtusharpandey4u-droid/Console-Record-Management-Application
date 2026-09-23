"""
Student Record Management System
=================================
A console-based record-management application that allows users to
add, view, search, update, and delete student records.

Concepts Demonstrated:
    - Data Types and Variables
    - Conditional Statements and Loops
    - Functions
    - Exception Handling
    - File I/O (JSON persistence)
    - Menu-driven Console Application Design

Author : Tushar
Date   : 2026-09-23
"""

import json
import os
import sys

# Ensure the console uses UTF-8 encoding on Windows so that
# box-drawing characters and symbols render correctly.
if sys.platform == "win32":
    os.system("")  # Enable ANSI/VT100 escape sequences on Windows 10+
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

# ──────────────────────────────────────────────
# Constants
# ──────────────────────────────────────────────
DATA_FILE: str = "students.json"

MENU_OPTIONS: dict[int, str] = {
    1: "Add a New Student Record",
    2: "View All Student Records",
    3: "Search for a Student Record",
    4: "Update a Student Record",
    5: "Delete a Student Record",
    6: "Display Statistics",
    7: "Exit",
}

VALID_GRADES: list[str] = ["A+", "A", "B+", "B", "C+", "C", "D", "F"]


# ──────────────────────────────────────────────
# File I/O Functions
# ──────────────────────────────────────────────
def load_records(filepath: str = DATA_FILE) -> list[dict]:
    """
    Load student records from a JSON file.

    Parameters
    ----------
    filepath : str
        Path to the JSON data file.

    Returns
    -------
    list[dict]
        A list of student record dictionaries.
        Returns an empty list if the file does not exist or is empty.
    """
    try:
        if not os.path.exists(filepath):
            return []
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                print("[WARNING] Data file format is invalid. Starting with empty records.")
                return []
    except json.JSONDecodeError:
        print("[WARNING] Data file is corrupted or empty. Starting with empty records.")
        return []
    except PermissionError:
        print(f"[ERROR] Permission denied when reading '{filepath}'.")
        return []
    except OSError as e:
        print(f"[ERROR] Could not read data file: {e}")
        return []


def save_records(records: list[dict], filepath: str = DATA_FILE) -> bool:
    """
    Save student records to a JSON file.

    Parameters
    ----------
    records : list[dict]
        The list of student record dictionaries to persist.
    filepath : str
        Path to the JSON data file.

    Returns
    -------
    bool
        True if saved successfully, False otherwise.
    """
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(records, file, indent=4, ensure_ascii=False)
        return True
    except PermissionError:
        print(f"[ERROR] Permission denied when writing to '{filepath}'.")
        return False
    except OSError as e:
        print(f"[ERROR] Could not save data file: {e}")
        return False


# ──────────────────────────────────────────────
# Helper / Utility Functions
# ──────────────────────────────────────────────
def generate_id(records: list[dict]) -> int:
    """Generate the next unique student ID."""
    if not records:
        return 1001
    return max(record["id"] for record in records) + 1


def get_valid_int(prompt: str, min_val: int | None = None, max_val: int | None = None) -> int:
    """
    Prompt the user for a valid integer within an optional range.

    Keeps asking until a valid integer is entered.
    """
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"  ✗ Value must be at least {min_val}. Try again.")
                continue
            if max_val is not None and value > max_val:
                print(f"  ✗ Value must be at most {max_val}. Try again.")
                continue
            return value
        except ValueError:
            print("  ✗ Invalid input. Please enter a whole number.")


def get_non_empty_string(prompt: str) -> str:
    """Prompt the user for a non-empty string."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  ✗ This field cannot be empty. Try again.")


def get_valid_phone(prompt: str) -> str:
    """Prompt the user for a valid 10-digit phone number."""
    while True:
        value = input(prompt).strip()
        if value.isdigit() and len(value) == 10:
            return value
        print("  ✗ Please enter a valid 10-digit phone number.")


def get_valid_grade(prompt: str) -> str:
    """Prompt the user for a valid grade from the allowed list."""
    while True:
        value = input(prompt).strip().upper()
        if value in VALID_GRADES:
            return value
        print(f"  ✗ Invalid grade. Choose from: {', '.join(VALID_GRADES)}")


def print_separator(char: str = "─", length: int = 60) -> None:
    """Print a visual separator line."""
    print(char * length)


def print_record(record: dict) -> None:
    """Display a single student record in a formatted manner."""
    print(f"  ID      : {record['id']}")
    print(f"  Name    : {record['name']}")
    print(f"  Age     : {record['age']}")
    print(f"  Course  : {record['course']}")
    print(f"  Grade   : {record['grade']}")
    print(f"  Phone   : {record['phone']}")


def print_record_table(records: list[dict]) -> None:
    """Display multiple student records in a table format."""
    header = f"{'ID':<8} {'Name':<22} {'Age':<6} {'Course':<20} {'Grade':<8} {'Phone':<12}"
    print_separator("═", len(header))
    print(header)
    print_separator("─", len(header))
    for record in records:
        print(
            f"{record['id']:<8} "
            f"{record['name']:<22} "
            f"{record['age']:<6} "
            f"{record['course']:<20} "
            f"{record['grade']:<8} "
            f"{record['phone']:<12}"
        )
    print_separator("═", len(header))


def find_record_by_id(records: list[dict], student_id: int) -> dict | None:
    """
    Find and return a record matching the given student ID.

    Returns None if not found.
    """
    for record in records:
        if record["id"] == student_id:
            return record
    return None


def confirm_action(prompt: str = "Are you sure? (y/n): ") -> bool:
    """Ask the user for a yes/no confirmation."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in ("y", "yes"):
            return True
        elif choice in ("n", "no"):
            return False
        else:
            print("  ✗ Please enter 'y' or 'n'.")


# ──────────────────────────────────────────────
# Core CRUD Functions
# ──────────────────────────────────────────────
def add_record(records: list[dict]) -> None:
    """
    Add a new student record.

    Collects student details from the user, assigns a unique ID,
    appends the record to the list, and saves to file.
    """
    print("\n╔══════════════════════════════════════╗")
    print("║      ADD A NEW STUDENT RECORD        ║")
    print("╚══════════════════════════════════════╝")

    name   = get_non_empty_string("  Enter student name  : ")
    age    = get_valid_int("  Enter student age   : ", min_val=5, max_val=120)
    course = get_non_empty_string("  Enter course name   : ")
    grade  = get_valid_grade(f"  Enter grade {VALID_GRADES} : ")
    phone  = get_valid_phone("  Enter phone (10 digits) : ")

    student_id = generate_id(records)

    new_record: dict = {
        "id": student_id,
        "name": name.title(),
        "age": age,
        "course": course.title(),
        "grade": grade,
        "phone": phone,
    }

    records.append(new_record)

    if save_records(records):
        print(f"\n  ✓ Student record added successfully! (ID: {student_id})")
    else:
        # Rollback in-memory change if save failed
        records.pop()
        print("\n  ✗ Failed to save the record. Please try again.")


def view_all_records(records: list[dict]) -> None:
    """
    Display all student records in a formatted table.
    """
    print("\n╔══════════════════════════════════════╗")
    print("║      ALL STUDENT RECORDS             ║")
    print("╚══════════════════════════════════════╝\n")

    if not records:
        print("  (No records found. Add some students first!)")
        return

    print(f"  Total Records: {len(records)}\n")
    print_record_table(records)


def search_record(records: list[dict]) -> None:
    """
    Search for student records by ID or name (partial match).
    """
    print("\n╔══════════════════════════════════════╗")
    print("║      SEARCH STUDENT RECORDS          ║")
    print("╚══════════════════════════════════════╝")

    if not records:
        print("\n  (No records to search. Add some students first!)")
        return

    print("\n  Search by:")
    print("    1. Student ID")
    print("    2. Student Name")
    choice = get_valid_int("  Enter choice (1-2): ", min_val=1, max_val=2)

    if choice == 1:
        student_id = get_valid_int("  Enter Student ID: ")
        result = find_record_by_id(records, student_id)
        if result:
            print(f"\n  ✓ Record found:\n")
            print_record(result)
        else:
            print(f"\n  ✗ No student found with ID {student_id}.")

    elif choice == 2:
        search_name = get_non_empty_string("  Enter name to search: ").lower()
        results: list[dict] = [
            r for r in records if search_name in r["name"].lower()
        ]
        if results:
            print(f"\n  ✓ Found {len(results)} matching record(s):\n")
            print_record_table(results)
        else:
            print(f"\n  ✗ No student found matching '{search_name}'.")


def update_record(records: list[dict]) -> None:
    """
    Update an existing student record by ID.

    Allows the user to selectively update individual fields
    or keep the existing values by pressing Enter.
    """
    print("\n╔══════════════════════════════════════╗")
    print("║      UPDATE A STUDENT RECORD         ║")
    print("╚══════════════════════════════════════╝")

    if not records:
        print("\n  (No records to update. Add some students first!)")
        return

    student_id = get_valid_int("\n  Enter Student ID to update: ")
    record = find_record_by_id(records, student_id)

    if record is None:
        print(f"\n  ✗ No student found with ID {student_id}.")
        return

    print(f"\n  Current record:")
    print_record(record)
    print("\n  (Press Enter to keep the current value for any field)\n")

    # Name
    new_name = input(f"  New name [{record['name']}]: ").strip()
    if new_name:
        record["name"] = new_name.title()

    # Age
    age_input = input(f"  New age [{record['age']}]: ").strip()
    if age_input:
        try:
            new_age = int(age_input)
            if 5 <= new_age <= 120:
                record["age"] = new_age
            else:
                print("  ✗ Age out of range (5-120). Keeping old value.")
        except ValueError:
            print("  ✗ Invalid age. Keeping old value.")

    # Course
    new_course = input(f"  New course [{record['course']}]: ").strip()
    if new_course:
        record["course"] = new_course.title()

    # Grade
    new_grade = input(f"  New grade [{record['grade']}]: ").strip().upper()
    if new_grade:
        if new_grade in VALID_GRADES:
            record["grade"] = new_grade
        else:
            print(f"  ✗ Invalid grade. Keeping old value.")

    # Phone
    new_phone = input(f"  New phone [{record['phone']}]: ").strip()
    if new_phone:
        if new_phone.isdigit() and len(new_phone) == 10:
            record["phone"] = new_phone
        else:
            print("  ✗ Invalid phone number. Keeping old value.")

    if save_records(records):
        print(f"\n  ✓ Record ID {student_id} updated successfully!")
    else:
        print("\n  ✗ Failed to save changes.")


def delete_record(records: list[dict]) -> None:
    """
    Delete a student record by ID after user confirmation.
    """
    print("\n╔══════════════════════════════════════╗")
    print("║      DELETE A STUDENT RECORD         ║")
    print("╚══════════════════════════════════════╝")

    if not records:
        print("\n  (No records to delete. Add some students first!)")
        return

    student_id = get_valid_int("\n  Enter Student ID to delete: ")
    record = find_record_by_id(records, student_id)

    if record is None:
        print(f"\n  ✗ No student found with ID {student_id}.")
        return

    print(f"\n  Record to be deleted:")
    print_record(record)

    if confirm_action("\n  Are you sure you want to delete this record? (y/n): "):
        records.remove(record)
        if save_records(records):
            print(f"\n  ✓ Record ID {student_id} deleted successfully!")
        else:
            # Rollback
            records.append(record)
            print("\n  ✗ Failed to delete the record. Please try again.")
    else:
        print("\n  ✗ Deletion cancelled.")


def display_statistics(records: list[dict]) -> None:
    """
    Display summary statistics about the stored records.

    Shows total count, average age, grade distribution,
    and course distribution.
    """
    print("\n╔══════════════════════════════════════╗")
    print("║      RECORD STATISTICS               ║")
    print("╚══════════════════════════════════════╝")

    if not records:
        print("\n  (No records available for statistics.)")
        return

    total: int = len(records)
    ages: list[int] = [r["age"] for r in records]
    avg_age: float = sum(ages) / total

    # Grade distribution
    grade_counts: dict[str, int] = {}
    for record in records:
        grade = record["grade"]
        grade_counts[grade] = grade_counts.get(grade, 0) + 1

    # Course distribution
    course_counts: dict[str, int] = {}
    for record in records:
        course = record["course"]
        course_counts[course] = course_counts.get(course, 0) + 1

    print(f"\n  Total Students    : {total}")
    print(f"  Average Age       : {avg_age:.1f}")
    print(f"  Youngest Student  : {min(ages)}")
    print(f"  Oldest Student    : {max(ages)}")

    print(f"\n  Grade Distribution:")
    print_separator("─", 30)
    for grade in VALID_GRADES:
        count = grade_counts.get(grade, 0)
        if count > 0:
            bar = "█" * count
            print(f"    {grade:<4} : {count:>3}  {bar}")
    print_separator("─", 30)

    print(f"\n  Course Distribution:")
    print_separator("─", 40)
    for course, count in sorted(course_counts.items()):
        bar = "█" * count
        print(f"    {course:<20} : {count:>3}  {bar}")
    print_separator("─", 40)


# ──────────────────────────────────────────────
# Menu & Main Function
# ──────────────────────────────────────────────
def display_menu() -> None:
    """Display the main application menu."""
    print("\n╔══════════════════════════════════════╗")
    print("║   STUDENT RECORD MANAGEMENT SYSTEM   ║")
    print("╠══════════════════════════════════════╣")
    for key, value in MENU_OPTIONS.items():
        print(f"║   {key}. {value:<33}║")
    print("╚══════════════════════════════════════╝")


def main() -> None:
    """
    Main entry point of the application.

    Loads existing records from the data file, displays the menu,
    and routes user choices to the appropriate handler functions
    in a continuous loop until the user chooses to exit.
    """
    print("\n" + "═" * 42)
    print("   WELCOME TO THE STUDENT RECORD")
    print("       MANAGEMENT SYSTEM")
    print("═" * 42)

    # Load existing records from file
    records: list[dict] = load_records()
    print(f"\n  ℹ Loaded {len(records)} existing record(s) from '{DATA_FILE}'.")

    while True:
        display_menu()

        choice: int = get_valid_int("\n  Enter your choice (1-7): ", min_val=1, max_val=7)

        if choice == 1:
            add_record(records)
        elif choice == 2:
            view_all_records(records)
        elif choice == 3:
            search_record(records)
        elif choice == 4:
            update_record(records)
        elif choice == 5:
            delete_record(records)
        elif choice == 6:
            display_statistics(records)
        elif choice == 7:
            print("\n  Thank you for using the Student Record Management System!")
            print("  Goodbye! 👋\n")
            sys.exit(0)

        input("\n  Press Enter to continue...")


# ──────────────────────────────────────────────
# Entry Point
# ──────────────────────────────────────────────
if __name__ == "__main__":
    main()
