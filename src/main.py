from student import Student
from teacher import Teacher
from staff import Staff

def main():
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

if __name__ == "__main__":
    main()
