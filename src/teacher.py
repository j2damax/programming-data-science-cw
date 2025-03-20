# teacher.py

from person import Person

class Teacher(Person):

    """
    Subclass representing a teacher.
    Teacher sub class inhertics common attributes and methods from common class Person
    """

    def __init__(self, name, age, address, teacher_id, subject=None, class_schedule=None, ssn=None):
        super().__init__(name, age, address) # Inhertited attribute for students from Person 
        self.teacher_id = teacher_id # Specialized attribute for teachers
        self.subject = subject  # Subject the teacher specializes in
        self.class_schedule = class_schedule if class_schedule else []  # List to store class schedules
    

    def role_duties(self):
        """
        Describe specific responsibilities for a teacher.

        Returns:
            str: A description of teacher responsibilities.
        """
        return f"{self.name} is a teacher with ID {self.teacher_id}. Their responsibilities include taking classes, preparing lessons, and grading assignments."
    
    
    def schedule_classes(self, schedule):
        """
        Assign a class schedule for the teacher.
        """
        self.class_schedule.extend(schedule)
        return f"Class schedule updated for {self.name}: {', '.join(self.class_schedule)}"    