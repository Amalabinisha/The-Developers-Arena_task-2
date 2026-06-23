# The-Developers-Arena_task-2
# Student Grade Calculator

## Project Overview

The Student Grade Calculator is a Python-based application that calculates a student's academic performance using marks obtained in five subjects. The program validates user input, calculates total and average marks, assigns a grade, determines performance status, and provides encouraging feedback.

This project demonstrates fundamental Python concepts such as functions, conditional statements, loops, input validation, lists, and formatted output.

---

## Objectives

- Collect marks for five subjects.
- Validate marks entered by the user.
- Calculate total and average marks.
- Assign grades automatically based on average marks.
- Display performance status and feedback.
- Practice Python programming concepts through a real-world application.

---

## Technologies Used

- Python 3.x

No external libraries or packages are required.

---

## Project Structure

```text
Student-Grade-Calculator/
│
├── README.md
├── grade_calculator.py
├── requirements.txt
├── test_cases.txt
└── screenshots/
    └── output.png
```

---

## Features

- Student name input
- Five subject marks input
- Input validation (0–100 range)
- Total marks calculation
- Average marks calculation
- Grade assignment
- Performance classification
- Encouraging feedback messages
- Professional and structured output

---

## Grading Logic

| Grade | Marks Range |
|--------|------------|
| A | 90 – 100 |
| B | 80 – 89 |
| C | 70 – 79 |
| D | 60 – 69 |
| F | Below 60 |

---

## Functions Used

### `calculate_grade()`
Calculates the student's grade and feedback message based on average marks.

### `performance_status()`
Determines the student's overall performance category.

---

## Setup Instructions

### Prerequisites

- Python 3.x installed on your system

### Running the Program

1. Download or clone the repository.
2. Open a terminal or command prompt.
3. Navigate to the project folder.
4. Run the program:

```bash
python grade_calculator.py
```

5. Enter the student name and marks when prompted.

---

## Sample Output

```text
=========================================================
               STUDENT GRADE CALCULATOR
=========================================================

Enter Student Name: Atchaya V

Enter Marks for Mathematics (0-100): 99
Enter Marks for Science (0-100): 92
Enter Marks for English (0-100): 89
Enter Marks for Social Science (0-100): 94
Enter Marks for Computer Science (0-100): 90

Total Marks       : 464/500
Average Marks     : 92.80/100
Grade             : A
Performance       : Outstanding
```

## Learning Outcomes

Through this project, I learned:

- Functions in Python
- Conditional statements (`if`, `elif`, `else`)
- Loops (`for` and `while`)
- Input validation techniques
- List operations
- Mathematical calculations
- Project testing and documentation

---

## Conclusion

The Student Grade Calculator successfully evaluates student performance by calculating total marks, average marks, grades, and performance status. This project strengthened my understanding of core Python programming concepts and demonstrated how programming can be used to solve practical academic evaluation problems.
