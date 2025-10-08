"""A class used to represent a die (singular form of dice)."""

from random import randint

class Die:
    """A simple attempt to model a die."""

    def __init__(self, sides=6):
        """Initialize the number of sides."""
        self.sides = sides

    def roll(self):
        """
        Simulates the roll of a dice by returning a number between 1 and the 
        number of sides, inclusive.
        """
        return randint(1, self.sides)