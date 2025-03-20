# student.py

from person import Person

class Student(Person):

    """
    Sub class representing a Student
    Student sub class inhertics common attributes and methods from common class Person
    """

    def __init__(self, name, age, address, student_id, ssn=None):
        super().__init__(name, age, address, ssn) # Inhertited attribute for students from Person 
        self.student_id = student_id # Specialized attribute for Student
        self.grades = {}  # Dictionary to store grades for subjects
        self.attendance_record = []  # List to track attendance for each class


    def assign_grades(self, grades):

        """
        Assigns grades for subjects and calculates the average grade.

        Parameters:
            grades (dict): A dictionary where the keys are subject names and the values are numeric grades.
        Returns:
            float: The average grade calculated from the provided grades.
        """

        # Validate when data not recived in expected format
        if not isinstance(grades, dict):
            raise ValueError("Grades must be provided as a dictionary of subject: grade pairs.") 

        self.grades = grades  # Store the provided grades

        if grades:  # Ensure there is at least one grade
            total = sum(grades.values())
            average = total / len(grades)
        else:
            average = 0  # If no grades are provided, default the average to 0

        return average


    def role_duties(self):
        """
        Describe specific responsibilities for a student.

        Returns:
            str: A description of student responsibilities.
        """
        return f"{self.name} is a student with ID {self.student_id}. Their responsibilities include attending classes, completing assignments, and taking exams."
   

    def attendance(self, class_name, attended):
        """
        Tracks attendance for a specific class.

        Parameters:
            class_name (str): The name of the class.
            attended (bool): True if the student attended, False if absent.

        Returns:
            str: A message indicating the updated attendance record.
        """
        status = "Present" if attended else "Absent"
        self.attendance_record.append((class_name, status))
        return f"Attendance for {class_name} marked as {status} for {self.name}."


    def get_attendance_summary(self):
        """
        Provides a summary of the student's overall attendance.

        Returns:
            str: A summary of the attendance record.
        """
        total_classes = len(self.attendance_record)
        attended_classes = sum(1 for _, status in self.attendance_record if status == "Present")
        attendance_percentage = (attended_classes / total_classes) * 100 if total_classes > 0 else 0

        summary = f"{self.name} has attended {attended_classes}/{total_classes} classes ({attendance_percentage:.2f}%)."
        return summary






