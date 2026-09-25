
# ============================================================
# STUDENT MANAGEMENT SYSTEM
# Python Essentials - Evaluated Course Project
# ============================================================
#
# Author: HARSH VARDHAN
# Course: B.Tech CSE (AIML)
#
# SINGLE-FILE VERSION
#
# Features:
# 1. Add Student
# 2. View All Students
# 3. Search Student
# 4. Update Student
# 5. Delete Student
# 6. Enter / Update Marks
# 7. Generate Student Report
# 8. Generate All Performance Reports
# 9. Exit
#
# FIX:
# Student data is stored in a writable folder inside the
# user's account instead of the project folder.
# ============================================================

import json
import os
from pathlib import Path


# ============================================================
# 1. DATA STORAGE LOCATION
# ============================================================

def get_data_file():
    """
    Creates a writable folder for storing student data.

    On Windows:
        C:\\Users\\YourName\\StudentManagementSystemData\\

    This avoids permission problems in protected folders.
    """

    try:
        # Windows local application data folder
        local_app_data = os.environ.get("LOCALAPPDATA")

        if local_app_data:
            data_folder = Path(local_app_data) / "StudentManagementSystem"
        else:
            # Fallback for other operating systems
            data_folder = Path.home() / "StudentManagementSystemData"

        # Create folder if it does not exist
        data_folder.mkdir(parents=True, exist_ok=True)

        return data_folder / "students.json"

    except Exception:
        # Final fallback
        data_folder = Path.home() / "StudentManagementSystemData"
        data_folder.mkdir(parents=True, exist_ok=True)

        return data_folder / "students.json"


DATA_FILE = get_data_file()


# ============================================================
# 2. SUBJECTS
# ============================================================

SUBJECTS = [
    "Python",
    "Mathematics",
    "Computer Fundamentals",
    "Communication Skills"
]


# ============================================================
# 3. FILE HANDLING
# ============================================================

def load_data():
    """
    Load student data from JSON file.

    If the file does not exist, an empty dictionary is returned.
    """

    try:

        if not DATA_FILE.exists():
            return {}

        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Make sure the loaded data is a dictionary
        if isinstance(data, dict):
            return data

        print("\nWarning: Invalid data format.")
        return {}

    except json.JSONDecodeError:

        print("\nWarning: students.json contains invalid data.")
        print("Starting with an empty student database.")

        return {}

    except PermissionError:

        print("\nPermission error while reading student data.")
        print("Please make sure the file is not open in another program.")

        return {}

    except Exception as error:

        print(f"\nError loading data: {error}")

        return {}


def save_data(data):
    """
    Save student data safely to JSON file.

    A temporary file is used first. This reduces the chance
    of corrupting the main JSON file.
    """

    try:

        # Make sure the directory exists
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

        # Temporary file
        temp_file = DATA_FILE.with_suffix(".tmp")

        # Write data to temporary file
        with open(temp_file, "w", encoding="utf-8") as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

            # Make sure everything is written
            file.flush()
            os.fsync(file.fileno())

        # Replace old file with new file
        os.replace(temp_file, DATA_FILE)

        return True

    except PermissionError:

        print("\n" + "=" * 60)
        print("PERMISSION ERROR")
        print("=" * 60)

        print("Python does not have permission to save the file.")
        print("\nTry these steps:")
        print("1. Close students.json if it is open.")
        print("2. Close the program.")
        print("3. Run the program again.")
        print("4. Make sure the project is not inside a protected folder.")

        return False

    except Exception as error:

        print(f"\nError saving data: {error}")

        return False


# ============================================================
# 4. VALIDATION FUNCTIONS
# ============================================================

def validate_student_id(student_id):
    """
    Validate student ID.
    """

    student_id = student_id.strip()

    if student_id == "":
        return False

    if " " in student_id:
        return False

    return True


def validate_name(name):
    """
    Validate student name.

    Only alphabets and spaces are allowed.
    """

    name = name.strip()

    if name == "":
        return False

    if not all(
        character.isalpha() or character.isspace()
        for character in name
    ):
        return False

    return True


def validate_course(course):
    """
    Validate course.
    """

    if course.strip() == "":
        return False

    return True


def get_valid_mark(subject):
    """
    Get valid marks between 0 and 100.
    """

    while True:

        try:

            mark = float(
                input(f"Enter marks for {subject} (0-100): ")
            )

            if 0 <= mark <= 100:
                return mark

            print("Marks must be between 0 and 100.")

        except ValueError:

            print("Please enter a valid number.")


# ============================================================
# 5. MARKS FUNCTIONS
# ============================================================

def calculate_total(marks):
    """
    Calculate total marks.
    """

    return sum(marks.values())


def calculate_percentage(marks):
    """
    Calculate percentage.
    """

    if not marks:
        return 0

    total = calculate_total(marks)

    maximum_marks = len(marks) * 100

    percentage = (total / maximum_marks) * 100

    return percentage


def calculate_grade(percentage):
    """
    Calculate grade.

    90 and above = A
    75-89        = B
    60-74        = C
    50-59        = D
    Below 50     = F
    """

    if percentage >= 90:
        return "A"

    elif percentage >= 75:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 50:
        return "D"

    else:
        return "F"


def calculate_result(marks):
    """
    Calculate Pass/Fail.

    Minimum 40 marks are required in every subject.
    """

    if not marks:
        return "Not Available"

    for mark in marks.values():

        if mark < 40:
            return "Fail"

    return "Pass"


def performance_message(percentage):
    """
    Display performance message.
    """

    if percentage >= 90:
        return "Excellent Performance"

    elif percentage >= 75:
        return "Very Good Performance"

    elif percentage >= 60:
        return "Good Performance"

    elif percentage >= 50:
        return "Average Performance"

    else:
        return "Needs Improvement"


# ============================================================
# 6. ADD STUDENT
# ============================================================

def add_student(data):

    print("\n" + "=" * 60)
    print("                    ADD STUDENT")
    print("=" * 60)

    # Student ID
    student_id = input("Enter Student ID: ").strip()

    if not validate_student_id(student_id):

        print("\nInvalid Student ID.")
        print("Student ID cannot be empty or contain spaces.")

        return

    # Check duplicate ID
    if student_id in data:

        print("\nStudent ID already exists.")

        return

    # Student Name
    name = input("Enter Student Name: ").strip()

    if not validate_name(name):

        print("\nInvalid name.")
        print("Name should contain alphabets and spaces only.")

        return

    # Course
    course = input("Enter Course: ").strip()

    if not validate_course(course):

        print("\nCourse cannot be empty.")

        return

    # Year
    year = input("Enter Year/Semester: ").strip()

    if year == "":
        year = "Not Specified"

    # Create student
    student = {

        "student_id": student_id,

        "name": name,

        "course": course,

        "year": year,

        "marks": {}

    }

    # Add to dictionary
    data[student_id] = student

    # Save
    if save_data(data):

        print("\n" + "-" * 60)
        print("Student added successfully!")
        print("-" * 60)

        print("Student ID :", student_id)
        print("Name       :", name)
        print("Course     :", course)
        print("Year       :", year)


# ============================================================
# 7. VIEW ALL STUDENTS
# ============================================================

def view_all_students(data):

    print("\n" + "=" * 80)
    print("                       ALL STUDENTS")
    print("=" * 80)

    if not data:

        print("No students found.")

        return

    print(
        f"{'ID':<12}"
        f"{'Name':<25}"
        f"{'Course':<25}"
        f"{'Year':<15}"
    )

    print("-" * 80)

    for student in data.values():

        print(
            f"{student['student_id']:<12}"
            f"{student['name']:<25}"
            f"{student['course']:<25}"
            f"{student['year']:<15}"
        )


# ============================================================
# 8. SEARCH STUDENT
# ============================================================

def search_student(data):

    print("\n" + "=" * 60)
    print("                    SEARCH STUDENT")
    print("=" * 60)

    search = input(
        "Enter Student ID or Name: "
    ).strip().lower()

    if search == "":

        print("Search cannot be empty.")

        return

    found = False

    for student in data.values():

        student_id = student["student_id"].lower()

        student_name = student["name"].lower()

        if search in student_id or search in student_name:

            print("\nStudent Found")
            print("-" * 40)

            print("Student ID :", student["student_id"])
            print("Name       :", student["name"])
            print("Course     :", student["course"])
            print("Year       :", student["year"])

            found = True

    if not found:

        print("\nNo student found.")


# ============================================================
# 9. UPDATE STUDENT
# ============================================================

def update_student(data):

    print("\n" + "=" * 60)
    print("                    UPDATE STUDENT")
    print("=" * 60)

    student_id = input("Enter Student ID: ").strip()

    if student_id not in data:

        print("\nStudent not found.")

        return

    student = data[student_id]

    print("\nPress ENTER to keep the existing value.")

    # Update name
    name = input(
        f"Enter new name [{student['name']}]: "
    ).strip()

    if name != "":

        if validate_name(name):

            student["name"] = name

        else:

            print("Invalid name.")
            return

    # Update course
    course = input(
        f"Enter new course [{student['course']}]: "
    ).strip()

    if course != "":

        if validate_course(course):

            student["course"] = course

        else:

            print("Invalid course.")
            return

    # Update year
    year = input(
        f"Enter new year/semester [{student['year']}]: "
    ).strip()

    if year != "":
        student["year"] = year

    # Save
    if save_data(data):

        print("\nStudent updated successfully!")


# ============================================================
# 10. DELETE STUDENT
# ============================================================

def delete_student(data):

    print("\n" + "=" * 60)
    print("                    DELETE STUDENT")
    print("=" * 60)

    student_id = input("Enter Student ID: ").strip()

    if student_id not in data:

        print("\nStudent not found.")

        return

    student = data[student_id]

    print("\nStudent Details")
    print("-" * 40)

    print("Student ID :", student["student_id"])
    print("Name       :", student["name"])
    print("Course     :", student["course"])

    confirm = input(
        "\nAre you sure you want to delete this student? (y/n): "
    ).strip().lower()

    if confirm == "y":

        del data[student_id]

        if save_data(data):

            print("\nStudent deleted successfully!")

    else:

        print("\nDeletion cancelled.")


# ============================================================
# 11. ENTER / UPDATE MARKS
# ============================================================

def enter_marks(data):

    print("\n" + "=" * 60)
    print("                 ENTER / UPDATE MARKS")
    print("=" * 60)

    student_id = input("Enter Student ID: ").strip()

    if student_id not in data:

        print("\nStudent not found.")

        return

    student = data[student_id]

    print("\nStudent:", student["name"])

    print("-" * 40)

    marks = {}

    for subject in SUBJECTS:

        marks[subject] = get_valid_mark(subject)

    student["marks"] = marks

    if save_data(data):

        print("\nMarks saved successfully!")


# ============================================================
# 12. GENERATE STUDENT REPORT
# ============================================================

def generate_student_report(data):

    print("\n" + "=" * 60)
    print("                  STUDENT REPORT")
    print("=" * 60)

    student_id = input("Enter Student ID: ").strip()

    if student_id not in data:

        print("\nStudent not found.")

        return

    student = data[student_id]

    print("\n")
    print("=" * 60)
    print("            STUDENT PERFORMANCE REPORT")
    print("=" * 60)

    print("Student ID :", student["student_id"])
    print("Name       :", student["name"])
    print("Course     :", student["course"])
    print("Year       :", student["year"])

    print("\nMarks")
    print("-" * 60)

    marks = student["marks"]

    if not marks:

        print("Marks have not been entered yet.")

        print("=" * 60)

        return

    for subject, mark in marks.items():

        print(
            f"{subject:<35} : {mark:.2f}"
        )

    total = calculate_total(marks)

    percentage = calculate_percentage(marks)

    grade = calculate_grade(percentage)

    result = calculate_result(marks)

    performance = performance_message(percentage)

    print("-" * 60)

    print(f"Total Marks : {total:.2f}")
    print(f"Percentage  : {percentage:.2f}%")
    print(f"Grade       : {grade}")
    print(f"Result      : {result}")
    print(f"Performance : {performance}")

    print("=" * 60)


# ============================================================
# 13. ALL PERFORMANCE REPORTS
# ============================================================

def generate_all_reports(data):

    print("\n" + "=" * 85)
    print("                 ALL PERFORMANCE REPORTS")
    print("=" * 85)

    if not data:

        print("No students found.")

        return

    print(
        f"{'ID':<12}"
        f"{'Name':<25}"
        f"{'Percentage':<15}"
        f"{'Grade':<10}"
        f"{'Result':<10}"
    )

    print("-" * 85)

    for student in data.values():

        marks = student["marks"]

        if marks:

            percentage = calculate_percentage(marks)

            grade = calculate_grade(percentage)

            result = calculate_result(marks)

            print(
                f"{student['student_id']:<12}"
                f"{student['name']:<25}"
                f"{percentage:<15.2f}"
                f"{grade:<10}"
                f"{result:<10}"
            )

        else:

            print(
                f"{student['student_id']:<12}"
                f"{student['name']:<25}"
                f"{'Not Available':<15}"
                f"{'-':<10}"
                f"{'-':<10}"
            )

    print("-" * 85)


# ============================================================
# 14. DISPLAY MENU
# ============================================================

def display_menu():

    print("\n")
    print("=" * 60)
    print("             STUDENT MANAGEMENT SYSTEM")
    print("=" * 60)

    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Enter / Update Marks")
    print("7. Generate Student Report")
    print("8. Generate All Performance Reports")
    print("9. Exit")

    print("=" * 60)


# ============================================================
# 15. MAIN FUNCTION
# ============================================================

def main():

    # Load existing student data
    data = load_data()

    print("\n")
    print("=" * 60)
    print("       WELCOME TO STUDENT MANAGEMENT SYSTEM")
    print("=" * 60)

    print("\nData file location:")
    print(DATA_FILE)

    while True:

        display_menu()

        choice = input(
            "Enter your choice (1-9): "
        ).strip()

        # ----------------------------------------------------
        # OPTION 1
        # ----------------------------------------------------

        if choice == "1":

            add_student(data)

        # ----------------------------------------------------
        # OPTION 2
        # ----------------------------------------------------

        elif choice == "2":

            view_all_students(data)

        # ----------------------------------------------------
        # OPTION 3
        # ----------------------------------------------------

        elif choice == "3":

            search_student(data)

        # ----------------------------------------------------
        # OPTION 4
        # ----------------------------------------------------

        elif choice == "4":

            update_student(data)

        # ----------------------------------------------------
        # OPTION 5
        # ----------------------------------------------------

        elif choice == "5":

            delete_student(data)

        # ----------------------------------------------------
        # OPTION 6
        # ----------------------------------------------------

        elif choice == "6":

            enter_marks(data)

        # ----------------------------------------------------
        # OPTION 7
        # ----------------------------------------------------

        elif choice == "7":

            generate_student_report(data)

        # ----------------------------------------------------
        # OPTION 8
        # ----------------------------------------------------

        elif choice == "8":

            generate_all_reports(data)

        # ----------------------------------------------------
        # OPTION 9
        # ----------------------------------------------------

        elif choice == "9":

            print("\n" + "=" * 60)
            print("Thank you for using Student Management System!")
            print("Goodbye!")
            print("=" * 60)

            break

        # ----------------------------------------------------
        # INVALID OPTION
        # ----------------------------------------------------

        else:

            print("\nInvalid choice!")
            print("Please enter a number from 1 to 9.")


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":

    main()







# created by HARSH VARDHAN