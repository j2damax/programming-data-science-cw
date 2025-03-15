# Staff.py

from person import Person

class Staff(Person):
    """
    Sub class representing a Staff member
    Staff sub class inhertics common attributes and methods from common class Person
    """

    def __init__(self, name, age, address, staff_id):
        super.__init__(name, age, address) # Inhertited attribute for students from Person 
        self.staff_id = staff_id # Specialized attribute for Staff