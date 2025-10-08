"""
A set of classes that can be used to represent electric cars.
Includes Battery and ElectricCar (a child class of Car).
"""

from car import Car

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size # Battery size in kWh

    def describe_battery(self):
        """Print a statement describing the car's battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrades a battery size less than 100 kWH to 100 kWh."""
        if self.battery_size < 100:
            self.battery_size = 100

class ElectricCar(Car):
    """Represents aspects of a car, specific to elecric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
        """
        ^^^Whenever you instantiate an ElectricCar, the __init__() method will
        also instantiate a Battery called 'battery', which acts as an attribute
        of ElectricCar.
        """