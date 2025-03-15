# Teacher.py

from .person import Person

class Teacher(Person):

    """
    Subclass representing a teacher.
    Teacher sub class inhertics common attributes and methods from common class Person
    """

    def __ini__(self, name, age, address, teacher_id):
        super().__ini__(name, age, address) # Inhertited attribute for students from Person 
        self.teacher_id = teacher_id # Specialized attribute for teachers
    