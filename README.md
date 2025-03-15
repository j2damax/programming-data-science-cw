COURSE WORK: PROGRAMMING FOR DATA SCIENCE
2024.2 BATCH
MSc Data Science: Coventry University UK
Author: Jayampathy Balasuriya
Student NO: COMScDS242P-009

# Question 1 – OOP for School Management System (40 Marks) – [word count: 800 words]
Imagine you're tasked with creating a management system for a school. The system should
handle various roles like students, teachers, and staff, while also tracking grades, classes,
schedules, and other key information. Using Object-Oriented Programming (OOP) principles,
you'll develop a system that can handle multiple responsibilities, track different entities, and
perform actions specific to each role.

Below are the tasks to guide you through the system development. Your responses should
demonstrate a solid understanding of OOP concepts, including inheritance, encapsulation,
polymorphism, and method overriding, applied to the school context.

## 🎓 School Management System (OOP in Python)
This project is a **School Management System** developed using **Object-Oriented Programming (OOP)** principles in Python. It is part of the **Programming for Data Science** coursework and demonstrates concepts such as **inheritance, encapsulation, polymorphism, and method overriding**.

### 📌 Features
- 👨‍🎓 **Student Management** (Track grades, attendance, etc.)
- 👨‍🏫 **Teacher Management** (Class scheduling, subject assignments)
- 🏢 **Staff Management** (Salary calculation, administrative tasks)
- 🔒 **Encapsulation** (Secure sensitive information like SSN)
- 🔁 **Polymorphism** (Unified handling of students, teachers, and staff)
- 📊 **Data Handling** (Grade calculation, attendance tracking)

### 📌 Project Structure
programming-data-science-cw/
├── src/
│   ├── __init__.py      # Indicates src is a package
│   ├── main.py
│   └── models/
│       ├── __init__.py  # Indicates models is a package
│       ├── person.py    # Person - Main Class
    │       ├── student.py   # Student - Sub Class  
│           ├── teacher.py   # Teacher - Sub Class
│           └── staff.py     # Staff - Sub Class
├── .gitignore
├── README.md
└── requirements.txt
