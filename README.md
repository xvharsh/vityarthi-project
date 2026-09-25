# Student Management System

## Project Title
**Student Management System using Python**

## Overview
A Python-based console application for managing student records and academic performance. It supports student CRUD operations, marks entry, percentage/grade calculation, and report generation.

## Objectives
- Apply Python programming concepts in a practical project.
- Digitally manage student records.
- Calculate and report academic performance.
- Practice modular programming, JSON file handling, validation, exception handling, testing, Git, and GitHub.

## Problem Statement
Manual student record management can be time-consuming and error-prone. This system provides a simple computerized solution for storing, retrieving, updating, deleting, and reporting student information.

## Functional Modules
1. **Student Management** — add, view, search, update, delete.
2. **Marks & Performance** — enter marks, calculate total, percentage, grade, and result.
3. **Report Generation** — display formatted student performance reports.

## Non-Functional Requirements
- **Usability:** simple menu-driven interface.
- **Reliability:** validation and controlled error handling.
- **Maintainability:** separated Python modules.
- **Performance:** efficient for normal academic datasets.
- **Resource efficiency:** standard-library-only implementation.
- **Error handling:** invalid input is rejected with useful messages.

## Technologies
- Python 3
- Standard library
- JSON
- Git
- GitHub
- `unittest`

## Project Structure
```text
student-management-system/
├── README.md
├── statement.md
├── requirements.txt
├── LICENSE
├── .gitignore
├── main.py
├── student.py
├── marks.py
├── reports.py
├── validation.py
├── file_handler.py
├── menu.py
├── data/
│   └── students.json
├── tests/
│   ├── __init__.py
│   ├── test_student.py
│   ├── test_marks.py
│   └── test_validation.py
└── screenshots/
```

## Requirements
- Python 3.x
- No external Python packages are required.

## Installation & Run
```bash
git clone https://github.com/yourusername/student-management-system.git
cd student-management-system
python main.py
```

## Main Menu
```text
====================================
       STUDENT MANAGEMENT SYSTEM
====================================

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Enter Marks
7. Generate Report
8. Exit
```

## Grade Calculation
| Percentage | Grade |
|---|---|
| 90–100 | A |
| 75–89 | B |
| 60–74 | C |
| 50–59 | D |
| Below 50 | F |

A student passes only when each entered subject mark is at least 40.

## CRUD
| Operation | Feature |
|---|---|
| Create | Add Student |
| Read | View/Search Student |
| Update | Update Student |
| Delete | Delete Student |

## Testing
Run:
```bash
python -m unittest discover tests -v
```

## GitHub
```bash
git init
git add .
git commit -m "Initial project setup"
git branch -M main
git remote add origin <repository-url>
git push -u origin main
```

## Future Enhancements
- Tkinter GUI
- Login and role management
- SQLite database
- Attendance management
- PDF report export
- Data visualization
- Cloud storage

## Learning Outcomes
Variables, data types, operators, conditionals, loops, functions, lists, dictionaries, file handling, JSON, exception handling, modular programming, validation, testing, Git, and GitHub.

## Author
**Pranshu Sinha**  
**Course:** B.Tech CSE / AIML

## License
This project is developed for educational and academic purposes.
