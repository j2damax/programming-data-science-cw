# staff.py

from person import Person

class Staff(Person):
    """
    Sub class representing a Staff member
    Staff sub class inhertics common attributes and methods from common class Person
    """

    def __init__(self, name, age, address, staff_id, ssn=None):
        super().__init__(name, age, address) # Inhertited attribute for students from Person 
        self.staff_id = staff_id # Specialized attribute for Staff

    def role_duties(self):
        """
        Describe specific responsibilities for a staff member.

        Returns:
            str: A description of staff responsibilities.
        """
        return f"{self.name} is a staff member with ID {self.staff_id}. Their responsibilities include managing logistics, maintaining facilities, and supporting school operations."
