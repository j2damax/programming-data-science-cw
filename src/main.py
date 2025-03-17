from student import Student
from teacher import Teacher
from staff import Staff

def main():

    # Demonstrate inheritance
    #demonstrate_inheritance()

    # Demonstrate assigning grades
    demonstrate_assigning_grades()
    
    return
    # Create a student instance
    student = Student("Alice", 20, "123 Maple St", "S001")
    
    # Dictionary of subjects with their corresponding grades
    grades = {
        "Math": 90,
        "Science": 85,
        "English": 88
    }
    
    # Assign grades and calculate the average grade
    average_grade = student.assign_grades(grades)
    
    # Display the assigned grades and the calculated average
    print("Grades assigned:", student.grades)
    print("Average grade:", average_grade)

    # Access the SSN using the getter method
    print("Student SSN:", student.get_ssn())

    # Create instances of Student, Teacher, and Staff
    teacher = Teacher("Mr. Smith", 45, "456 Oak St", "T001")
    staff = Staff("Ms. Johnson", 35, "789 Pine St", "ST001")

    # Display role-specific duties
    print(student.role_duties())
    print(teacher.role_duties())
    print(staff.role_duties())

 # Demonstrate the usage of subject and class_schedule for Teacher
    print(f"Teacher {teacher.name} specializes in {teacher.subject}.")
    
    # Assign a class schedule to the teacher
    schedule = ["Monday 9 AM - Algebra", "Wednesday 11 AM - Geometry", "Friday 1 PM - Calculus"]
    updated_schedule = teacher.schedule_classes(schedule)
    
    # Display the updated class schedule
    print(updated_schedule)    

    # Mark attendance for classes
    print(student.attendance("Math", True))  # Alice attended Math
    print(student.attendance("Science", False))  # Alice missed Science
    print(student.attendance("English", True))  # Alice attended English

    # Display attendance summary
    print(student.get_attendance_summary())    

    # Create a staff instance
    staff = Staff("Ms. Johnson", 35, "789 Pine St", "ST001", base_salary=35000, years_of_service=5)

    # Calculate the salary
    calculated_salary = staff.calculate_salary(bonus_per_year=1200)
    print(f"Calculated Salary for {staff.name}: ${calculated_salary}")

    # Get the salary
    print(f"Retrieved Salary for {staff.name}: ${staff.get_salary()}")

     # Create instances of Student, Teacher, and Staff
    student = Student("Alice", 20, "123 Maple St", "S001")
    teacher = Teacher("Mr. Smith", 45, "456 Oak St", "T001", "Mathematics")
    staff = Staff("Ms. Johnson", 35, "789 Pine St", "ST001", base_salary=35000, years_of_service=5)

    # Store all individuals in a list
    individuals = [student, teacher, staff]

    # Display information for all individuals using polymorphism
    display_individual_info(individuals)

def demonstrate_inheritance():
    """
    a. Inheritance in School Classes:
    Demonstrates the use of inheritance in the school management system.
    """
    # Create instances of Student, Teacher, and Staff
    student = Student("Alice", 20, "123 Maple St", "S001")
    teacher = Teacher("Mr. Smith", 45, "456 Oak St", "T001", "Mathematics")
    staff = Staff("Ms. Johnson", 35, "789 Pine St", "ST001", base_salary=35000, years_of_service=5)

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
    student = Student("Alice", 20, "123 Maple St", "S001")

    # Dictionary of subjects with their corresponding grades
    grades = {
        "Math": 90,
        "Science": 85,
        "English": 88
    }

    # Assign grades and calculate the average grade
    average_grade = student.assign_grades(grades)

    # Display the assigned grades and the calculated average
    print(f"Grades assigned to {student.name}: {student.grades}")
    print(f"Average grade for {student.name}: {average_grade:.2f}")



def display_individual_info(individuals):
    """
    Display basic information for all individuals in the system.

    Args:
        individuals (list): A list of Person objects (students, teachers, staff).
    """
    for individual in individuals:
        print(f"Name: {individual.name}, Age: {individual.age}")
        print(f"Role Duties: {individual.role_duties()}")
        print("-" * 40)

if __name__ == "__main__":
    main()
