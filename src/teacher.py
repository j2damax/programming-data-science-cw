# teacher.py

from person import Person

class Teacher(Person):

    """
    Subclass representing a teacher.
    Teacher sub class inhertics common attributes and methods from common class Person
    """

    def __init__(self, name, age, address, teacher_id, ssn=None):
        super().__init__(name, age, address) # Inhertited attribute for students from Person 
        self.teacher_id = teacher_id # Specialized attribute for teachers
    

    def role_duties(self):
        """
        Describe specific responsibilities for a teacher.

        Returns:
            str: A description of teacher responsibilities.
        """
        return f"{self.name} is a teacher with ID {self.teacher_id}. Their responsibilities include taking classes, preparing lessons, and grading assignments."
    