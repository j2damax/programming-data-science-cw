# staff.py

from person import Person

class Staff(Person):
    """
    Sub class representing a Staff member
    Staff sub class inhertics common attributes and methods from common class Person
    """

    def __init__(self, name, age, address, staff_id, base_salary=30000, years_of_service=0, ssn=None):
        super().__init__(name, age, address) # Inhertited attribute for students from Person 
        self.staff_id = staff_id # Specialized attribute for Staff
        self.base_salary = base_salary  # Base salary for the staff member
        self.years_of_service = years_of_service  # Number of years the staff member has worked
        self.calculated_salary = 0  # Placeholder for the calculated salary


    def role_duties(self):
        """
        Describe specific responsibilities for a staff member.

        Returns:
            str: A description of staff responsibilities.
        """
        return f"{self.name} is a staff member with ID {self.staff_id}. Their responsibilities include managing logistics, maintaining facilities, and supporting school operations."


    def calculate_salary(self, bonus_per_year=1000):
        """
        Calculates the salary of the staff member based on their base salary and years of service.

        Parameters:
            bonus_per_year (int): The bonus amount added to the base salary for each year of service.

        Returns:
            float: The calculated salary.
        """
        self.calculated_salary = self.base_salary + (self.years_of_service * bonus_per_year)
        return self.calculated_salary


    def get_salary(self):
        """
        Returns the calculated salary of the staff member.

        Returns:
            float: The calculated salary.
        """
        if self.calculated_salary == 0:
            raise ValueError("Salary has not been calculated yet. Please call calculate_salary() first.")
        return self.calculated_salary