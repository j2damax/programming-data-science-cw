# person.py

class Person:
    
    """
    Base class representing a persin with common attributes and methods 
    """

    """
    Define common attributes 
        name (str): The name of the person.
        age (int): The age of the person.
        address (str): The address of the person.
    """

    """
     Parameters:
        ssn (str, optional): The Social Security Number of the person. Defaults to None.
    """
    
    def __init__(self, name, age, address, ssn=None):
        self.name = name
        self.age = age
        self.address = address
        self.__ssn = ssn  # Private attribute for Social Security Number


    # Getter method for SSN
    def get_ssn(self):
        """
        Get the Social Security Number (SSN) of the person.

        Returns:
            str: The SSN of the person.
        """
        return self.__ssn


    # Setter method for SSN
    def set_ssn(self, ssn):
        """
        Set the Social Security Number (SSN) of the person.

        Parameters:
            ssn (str): The new SSN to set.
        """
        if isinstance(ssn, str) and len(ssn) == 9:  # Basic validation for SSN
            self.__ssn = ssn
        else:
            raise ValueError("SSN must be a 9-digit string.")


    def role_duties(self):
        """
        Describe general responsibilities for a person.

        Returns:
            str: A description of general responsibilities.
        """
        return f"{self.name} has general responsibilities."
