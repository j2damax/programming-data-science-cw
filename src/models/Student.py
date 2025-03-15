# Student.py
from .person import Person

class Student(Person):

    """
    Sub class representing a Student
    Student sub class inhertics common attributes and methods from common class Person
    """

    def __init__(self, name, age, address, student_id):
        super.__init__(name, age, address) # Inhertited attribute for students from Person 
        self.student_id = student_id # Specialized attribute for Student







