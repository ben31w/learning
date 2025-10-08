"""A class that can be used to represent an employee."""

class Employee:
    """A simple attempt to model an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        """Initialize attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def change_last_name(self, last_name):
        """Changes an employee's last name."""
        self.last_name = last_name

    def change_name(self, first_name, last_name=''):
        """
        Changes an employee's first name if one argument is given.
        Changes an employee's first and last name if two arguments are given.
        """
        self.first_name = first_name
        if last_name:
            self.last_name = last_name

    def give_raise(self, increase=5000):
        """
        Increase an employee's annual salary by a specified amount or by $5000
        if no specified amount is given.
        """
        self.annual_salary += increase