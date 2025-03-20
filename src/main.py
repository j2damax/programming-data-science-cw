from student import Student
from teacher import Teacher
from staff import Staff

def main():
    """
    Main function to prompt the user to select a demonstration option.
    """
    options = {
        "a": demonstrate_inheritance,
        "b": demonstrate_assigning_grades,
        "c": demonstrate_encapsulation,
        "d": demonstrate_role_duties,
        "e": demonstrate_teacher_class,
        "f": demonstrate_attendance_tracking,
        "g": demonstrate_staff_salary_management,
        "h": demonstrate_polymorphism,
        "x": exit_program
    }

    while True:
        # Display the options to the user
        print("\nPlease select an option to demonstrate:")
        print("a) Demonstrate Inheritance")
        print("b) Demonstrate assigning grades")
        print("c) Demonstrate encapsulation")
        print("d) Demonstrate role-specific responsibilities")
        print("e) Demonstrate the specialized Teacher class")
        print("f) Demonstrate attendance tracking for students")
        print("g) Demonstrate staff salary management")
        print("h) Demonstrate polymorphism")
        print("x) Exit the program")

        # Prompt the user for input
        choice = input("Enter your choice (a-h or x to exit): ").strip().lower()
        if choice in options:
            print(f"\nYou selected option '{choice}'.")
            # Call the corresponding function
            options[choice]()
        else:
            print("Invalid choice. Please enter a valid option (a-h or x to exit).")

def main():
    """
    Main function to prompt the user to select a demonstration option.
    """
    options = {
        "a": demonstrate_inheritance,
        "b": demonstrate_assigning_grades,
        "c": demonstrate_encapsulation,
        "d": demonstrate_role_duties,
        "e": demonstrate_teacher_class,
        "f": demonstrate_attendance_tracking,
        "g": demonstrate_staff_salary_management,
        "h": demonstrate_polymorphism,
        "x": exit_program
    }

    while True:
        # Display the options to the user
        print("\nPlease select an option to demonstrate:")
        print("a) Demonstrate Inheritance")
        print("b) Demonstrate assigning grades")
        print("c) Demonstrate encapsulation")
        print("d) Demonstrate role-specific responsibilities")
        print("e) Demonstrate the specialized Teacher class")
        print("f) Demonstrate attendance tracking for students")
        print("g) Demonstrate staff salary management")
        print("h) Demonstrate polymorphism")
        print("x) Exit the program")

        # Prompt the user for input
        choice = input("Enter your choice (a-h or x to exit): ").strip().lower()
        if choice in options:
            print(f"\nYou selected option '{choice}'.")
            # Call the corresponding function
            options[choice]()
        else:
            print("Invalid choice. Please enter a valid option (a-h or x to exit).")

def exit_program():
    """
    Exits the program.
    """
    print("Exiting the program. Goodbye!")
    exit()

def demonstrate_inheritance():
    """
    a. Inheritance in School Classes:
    Demonstrates the use of inheritance in the school management system.
    """
    # Create instances of Student, Teacher, and Staff
    student = Student("Vihas Vinvidu", 10, "300/3, Mankada Road, Kadawatha", "S001")
    teacher = Teacher("Shasi Jayasinghe", 55, "261/3, Temple Road, Kelaniya", "T001", "Mathematics")
    staff = Staff("Achini Udara", 45, "400, New Address, Colombo 04", "ST001", base_salary=35000, years_of_service=5)

    # Display common attributes (inherited from Person)
    print("Common Attributes (Inherited from Person):")
    print(f"Student: Name = {student.name}, Age = {student.age}, Address = {student.address}")
    print(f"Teacher: Name = {teacher.name}, Age = {teacher.age}, Address = {teacher.address}")
    print(f"Staff: Name = {staff.name}, Age = {staff.age}, Address = {staff.address}")
    print("-" * 40)

    # Display specialized attributes and methods
    print("Specialized Attributes and Methods:")
    print(f"Student ID: {student.student_id}")
    print(f"Teacher ID: {teacher.teacher_id}, Subject: {teacher.subject}")
    print(f"Staff ID: {staff.staff_id}, Base Salary: {staff.base_salary}, Years of Service: {staff.years_of_service}")
    print("-" * 40)

    # Call role-specific methods
    print("Role-Specific Duties:")
    print(student.role_duties())
    print(teacher.role_duties())
    print(staff.role_duties())
    print("-" * 40)

def demonstrate_assigning_grades():
    """
    b. Assigning Grades Method for Students:
    Demonstrates the assign_grades() method in the Student class.
    """
    # Create a student instance
    student = Student("Vihas Vinvidu", 10, "300/3, Mankada Road, Kadawatha", "S001")

    # Dictionary of subjects with their corresponding grades
    grades = {
        "Maths": 85,
        "Science": 90,
        "English": 88
    }

    # Assign grades and calculate the average grade
    average_grade = student.assign_grades(grades)

    # Display the assigned grades and the calculated average
    print(f"Grades assigned to {student.name}: {student.grades}")
    print(f"Average grade for {student.name}: {average_grade:.2f}")

def demonstrate_encapsulation():
    """
    c. Encapsulation for Sensitive Information:
    Demonstrates encapsulation for the 'ssn' attribute in the Person class.
    """
    # Create a student instance
    student = Student("Vihas Vinvidu", 10, "300/3, Mankada Road, Kadawatha", "S001", ssn="200512345V")
    # Create a teacher instance
    teacher = Teacher("Shasi Jayasinghe", 55, "261/3, Temple Road, Kelaniya", "T001", subject="Mathematics", ssn="550123456V")

    # Access the SSN using the getter method
    print(f"Student {student.name}'s SSN (via getter): {student.get_ssn()}")
    print(f"Teacher {teacher.name}'s SSN (via getter): {teacher.get_ssn()}")

    # Modify the SSN using the setter method
    student.set_ssn("200512346V")
    teacher.set_ssn("550123457V")

    # Access the updated SSN using the getter method
    print(f"Updated Student {student.name}'s SSN (via getter): {student.get_ssn()}")
    print(f"Updated Teacher {teacher.name}'s SSN (via getter): {teacher.get_ssn()}")

def demonstrate_role_duties():
    """
    d. Class-Specific Responsibilities with Method Overriding:
    Demonstrates the role_duties() method and its overriding in the Student, Teacher, and Staff classes.
    """
    # Create instances of Student, Teacher, and Staff
    student = Student("Vihas Vinvidu", 10, "300/3, Mankada Road, Kadawatha", "S001")
    teacher = Teacher("Shasi Jayasinghe", 55, "261/3, Temple Road, Kelaniya", "T001", subject="Mathematics")
    staff = Staff("Achini Udara", 45, "400, New Address, Colombo 04", "ST001", base_salary=35000, years_of_service=5)

    # Call the role_duties() method for each instance
    print("Role-Specific Responsibilities:")
    print(f"Student: {student.role_duties()}")
    print(f"Teacher: {teacher.role_duties()}")
    print(f"Staff: {staff.role_duties()}")


def demonstrate_teacher_class():
    """
    e. Specialized Teacher Class:
    Demonstrates the specialized Teacher class with attributes and methods.
    """
    # Create a teacher instance
    teacher = Teacher("Mr. Smith", 45, "456 Oak St", "T001", subject="Mathematics")

    # Display teacher's basic information and subject specialization
    print(f"Teacher Name: {teacher.name}")
    print(f"Teacher Age: {teacher.age}")
    print(f"Teacher Address: {teacher.address}")
    print(f"Teacher ID: {teacher.teacher_id}")
    print(f"Subject Specialization: {teacher.subject}")

    # Assign a class schedule to the teacher
    schedule = ["Monday 9 AM - Maths", "Wednesday 11 AM - Science", "Friday 1 PM - English"]
    updated_schedule = teacher.schedule_classes(schedule)

    # Display the updated class schedule
    print(f"Updated Class Schedule for {teacher.name}:")
    print(updated_schedule)

    # Display teacher's role-specific duties
    print(f"Role Duties: {teacher.role_duties()}")


def demonstrate_attendance_tracking():
    """
    f. Attendance Tracking for Students:
    Demonstrates the attendance() method in the Student class.
    """
    # Create a student instance
    student = Student("Vihas Vinvidu", 20, "300/3, Mankada Road, Kadawatha", "S001")

    # Mark attendance for classes
    print(student.attendance("Math", True))  # Alice attended Math
    print(student.attendance("Science", False))  # Alice missed Science
    print(student.attendance("English", True))  # Alice attended English

    # Display the overall attendance summary
    print("Overall Attendance Summary:")
    print(student.get_attendance_summary())


def demonstrate_staff_salary_management():
    """
    g. Staff Salary Management:
    Demonstrates the calculate_salary() and get_salary() methods in the Staff class.
    """
    # Create a staff instance
    staff = Staff("Achini Udara", 45, "400, New Address, Colombo 04", "ST001", base_salary=35000, years_of_service=5)

    # Display staff's basic information
    print(f"Staff Name: {staff.name}")
    print(f"Staff Age: {staff.age}")
    print(f"Staff Address: {staff.address}")
    print(f"Staff ID: {staff.staff_id}")
    print(f"Base Salary: Rs.{staff.base_salary}")
    print(f"Years of Service: {staff.years_of_service}")

    # Calculate the salary
    calculated_salary = staff.calculate_salary(bonus_per_year=2000)
    print(f"Calculated Salary for {staff.name}: Rs.{calculated_salary}")

    # Retrieve the salary using get_salary()
    print(f"Retrieved Salary for {staff.name}: Rs.{staff.get_salary()}")


def demonstrate_polymorphism():
    """
    h. Polymorphism in School System:
    Demonstrates polymorphism by handling different roles (Student, Teacher, Staff) uniformly.
    """
    # Create instances of Student, Teacher, and Staff
    student = Student("Vihas Vinvidu", 10, "300/3, Mankada Road, Kadawatha", "S001")
    teacher = Teacher("Shasi Jayasinghe", 55, "261/3, Temple Road, Kelaniya", "T001", subject="Mathematics")
    staff = Staff("Achini Udara", 45, "400, New Address, Colombo 04", "ST001", base_salary=35000, years_of_service=5)

    # Store all individuals in a list
    individuals = [student, teacher, staff]

    # Display information for all individuals using polymorphism
    print("Displaying Information for All Individuals:")
    for individual in individuals:
        print(f"Name: {individual.name}, Age: {individual.age}, Address: {individual.address}")
        print(f"Role Duties: {individual.role_duties()}")
        print("-" * 40)

if __name__ == "__main__":
    main()
