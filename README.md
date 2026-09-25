# Smart Student Performance Analyzer

A menu-driven individual Python project for **CSE1021 - Introduction to Problem Solving and Programming**. It is an expanded, command-line version of official sample project title **#31, “Smart Student Performance Analyzer Using Python.”** It runs in VS Code with Python 3 and uses no third-party packages.

## Why this is the right scope

The supplied material teaches a 45-hour fundamentals course: problem solving and top-down design; algorithms, pseudocode, flowcharts, verification and analysis; Python values, variables, expressions, statements, modules and functions; conditionals and loops; fundamental numerical algorithms; factoring, PRNGs and Fibonacci; then array techniques, lists, tuples, sets and dictionaries. The project is deliberately a clear terminal program, not a database, GUI, web, AI, or face-recognition system that the PDFs do not teach.

The modest extensions are JSON saving/loading and a deterministic study-plan generator. They use only the standard library and are isolated in small functions, so every line remains explainable in a viva.

## Features

- Add, search, update, delete, save and reload student records.
- Calculate average, classification, strongest/weakest subject and a ranked leaderboard.
- Demonstrate linear search and binary search explicitly.
- Produce class analysis with maximum, counting, partitioning, sorted duplicate removal and kth-smallest average.
- Offer a per-subject score distribution, two-pointer array reversal and a live comparison-count demonstration for linear versus binary search.
- Use dictionaries for records/marks, a fixed subject tuple, lists for records, and sets for unique recommendations.
- Generate a reproducible, randomised study plan; apply GCD, prime factorisation and Fibonacci meaningfully as planning demonstrations.
- Include input validation and a standard-library unit-test suite.

## Submission documents

- [`statement.md`](statement.md): problem, scope, users and high-level features required by the instruction document.
- [`docs/compliance_checklist.md`](docs/compliance_checklist.md): requirement-to-evidence mapping and non-functional requirements.
- [`docs/design_diagrams.md`](docs/design_diagrams.md): architecture, workflow, use case, component, sequence and JSON-storage diagrams.
- `project_report.pdf`: upload this PDF separately on the course portal after replacing the cover-page placeholders with your own details.

## Folder layout

```text
smart-student-performance-analyzer/
├── src/performance_analyzer.py  # main program
├── src/config.py                # fixed settings
├── src/algorithms.py            # reusable numerical/array algorithms
├── src/storage.py               # JSON loading and saving
├── src/demo_data.py             # reproducible sample records
├── tests/test_analyzer.py       # automated checks
├── docs/
│   ├── course_review.md         # evidence-based syllabus review
│   ├── design_and_algorithms.md # IPO, pseudocode, flowchart and complexity
│   ├── test_cases.md            # manual test cases
│   └── viva_points.md           # presentation and viva prep
├── data/                        # created automatically; JSON is ignored by Git
├── README.md
├── statement.md
├── project_report.pdf
└── .gitignore
```

## Run in VS Code

1. Open this folder in VS Code.
2. Install Python 3.10 or newer if it is not already installed, then select that interpreter in VS Code.
3. No package installation or configuration file is required because the project uses only the Python standard library.
4. In the integrated terminal run:

```bash
python3 src/performance_analyzer.py
```

Choose `9` once for reproducible demonstration data, explore the features, then choose `0` to save. The program creates `data/students.json`; it is ignored so sample private marks are not uploaded accidentally.

## Test

```bash
python3 -m unittest discover -s tests -v
```

## GitHub checklist

```bash
git init
git add .
git commit -m "Build Smart Student Performance Analyzer"
```

Create an empty GitHub repository, add its remote URL, then push the default branch. Do not commit `data/students.json` unless your teacher specifically wants demonstration data included.

Before submission, set the repository to **Public** and submit only its root URL in the form `https://github.com/your-username/your-repository-name`. Do not submit a `/tree/` or `/blob/` URL. Upload `project_report.pdf` separately on the course portal.

See [the project design](docs/design_and_algorithms.md), [test cases](docs/test_cases.md), and [viva notes](docs/viva_points.md).
