# School Management System (OOP in Python)

This project is a **School Management System** developed using **Object-Oriented Programming (OOP)** principles in Python. It is part of the **Programming for Data Science** coursework for the MSc Data Science program at Coventry University.

## Features
- **Student Management**: 
  - Track grades, attendance, and other student-related information.
  - Assign grades for subjects and calculate average grades.
  - Track attendance and calculate attendance percentage.
- **Teacher Management**: 
  - Manage class schedules and subject assignments.
  - Assign and update class schedules.
- **Staff Management**: 
  - Handle administrative tasks and salary calculations.
  - Calculate salaries based on years of service and bonuses.
- **Encapsulation**: 
  - Secure sensitive information like Social Security Numbers (SSN) using getter and setter methods.
- **Polymorphism**: 
  - Unified handling of students, teachers, and staff roles while respecting their unique responsibilities.
- **Inheritance**: 
  - Reuse common attributes and methods across different roles (students, teachers, staff).
- **Data Handling**: 
  - Perform grade calculations, attendance tracking, and salary management.

## Project Structure
```
programming-data-science-cw/
├── src/
│   ├── __init__.py      # Package initialization
│   ├── main.py          # Main program entry point
│   ├── student.py       # Student class implementation
│   ├── teacher.py       # Teacher class implementation
│   ├── staff.py         # Staff class implementation
│   └── person.py        # Base Person class
├── README.md            # Project documentation
└── requirements.txt     # Dependencies (if any)
```

## Environment Requirements
To run this project, ensure you have the following:
- **Python Version**: Python 3.8 or higher.
- **Operating System**: The project is platform-independent and can run on Windows, macOS, or Linux.
- **Dependencies**: No external libraries are required for this project. It uses only Python's standard library.

## How to Clone and Run the Project
Follow these steps to clone and run the project:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd programming-data-science-cw
   ```

2. **Set Up the Environment**:
   - Ensure you have Python 3.8 or higher installed.
   - Optionally, create a virtual environment to isolate the project:
     ```bash
     python3 -m venv venv
     source venv/bin/activate  # On macOS/Linux
     venv\Scripts\activate     # On Windows
     ```

3. **Run the Program**:
   - Navigate to the `src` directory and execute the main program:
     ```bash
     python src/main.py
     ```

## Demonstration Options
When you run the program, you will be prompted to select one of the following options to demonstrate the system's functionality:
- **a)** Demonstrate Inheritance
- **b)** Demonstrate Assigning Grades
- **c)** Demonstrate Encapsulation
- **d)** Demonstrate Role-Specific Responsibilities
- **e)** Demonstrate the Specialized Teacher Class
- **f)** Demonstrate Attendance Tracking for Students
- **g)** Demonstrate Staff Salary Management
- **h)** Demonstrate Polymorphism
- **x)** Exit the program

## How to Run
1. Clone the repository:
   ```bash
   HTTP: git clone https://github.com/j2damax/programming-data-science-cw.git
   SSH: git@github.com:j2damax/programming-data-science-cw.git
   GitHub CLI: gh repo clone j2damax/programming-data-science-cw
   cd programming-data-science-cw
   ```

2. Run the program:
   ```bash
   python src/main.py
   ```

## Demonstration Options
When you run the program, you will be prompted to select one of the following options to demonstrate the system's functionality:
- **a)** Demonstrate Inheritance
- **b)** Demonstrate Assigning Grades
- **c)** Demonstrate Encapsulation
- **d)** Demonstrate Role-Specific Responsibilities
- **e)** Demonstrate the Specialized Teacher Class
- **f)** Demonstrate Attendance Tracking for Students
- **g)** Demonstrate Staff Salary Management
- **h)** Demonstrate Polymorphism
- **x)** Exit the program

## Author
**Jayampathy Balasuriya**  
Student No: COMScDS242P-009  
MSc Data Science, Coventry University