# student.py

from person import Person

class Student(Person):

    """
    Sub class representing a Student
    Student sub class inhertics common attributes and methods from common class Person
    """

    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address) # Inhertited attribute for students from Person 
        self.student_id = student_id # Specialized attribute for Student
        self.grades = {}  # Dictionary to store grades for subjects

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








