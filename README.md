# Student Management System

A simple, menu-driven **Student Management System built with Python** to practice Object-Oriented Programming (OOP) concepts.

This project allows users to view student information, enroll students, and drop students using a simple command-line interface.

## Features

- View all students and their information
- Enroll a student using their Student ID
- Drop a student using their Student ID
- Check whether a student is already enrolled
- Display a message when a student ID is not found
- Simple menu-driven command-line interface

## Concepts Practiced

- Classes and Objects
- Constructors (`__init__`)
- Instance Attributes and Methods
- Class Attributes
- Class Methods (`@classmethod`)
- Lists and Object Management
- Loops and Conditional Statements
- Searching Objects by ID
- Flags for Tracking Search Results
- Understanding Encapsulation and Private Attributes

## Technologies Used

- Python 3

## Project Structure

```text
student-management-system/
├── main.py
└── README.md
```

*Note: `main.py` is a suggested filename for the Python source code.*

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Clone this repository or download the source code.
3. Open a terminal in the project directory.
4. Run the program:

```bash
python main.py
```

## How to Use

After running the program, choose an option from the menu:

```text
1. View All Students
2. Enroll Student
3. Drop Student
4. Exit
```

- **Option 1:** Display all students and their enrollment status.
- **Option 2:** Enter a Student ID to enroll a student.
- **Option 3:** Enter a Student ID to drop a student.
- **Option 4:** Exit the program.

## Sample Student Data

The program starts with three sample students:

| Student ID | Name | Department | Enrolled |
|---|---|---|---|
| S01 | fury | CST | True |
| S02 | night | EEE | False |
| S03 | dark | Civil | True |

## Future Improvements

- Implement private attributes properly
- Add getters and setters or use Python's `@property`
- Improve input validation and error handling
- Add new students through the menu
- Store student data in a file or database
- Improve the user interface

## Learning Purpose

This project was created for learning and practicing Python OOP. It helped me understand how classes, objects, methods, and conditional logic work together in a practical application.

I'm continuing to learn, practice, and improve my programming skills one project at a time.

---

**Language:** Python

**Project Type:** Beginner OOP Practice Project
