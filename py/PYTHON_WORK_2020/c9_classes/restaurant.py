"""A class that can be used to represent a restaurant."""

class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        """Assign restaurant name and attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        """Prints the restaurant's name and cuisine type."""
        print(f"The restaurant {self.restaurant_name.title()} serves "
            f"{self.cuisine_type.title()} food. It has served "
            f"{self.number_served} people.")

    def increment_number_served(self, value):
        """Add the given value to the total number of people served."""
        if value >= 0:
            self.number_served += value

    def set_number_served(self, value):
        """Set the total number of people a restaurant has served."""
        if value >= self.number_served:
            self.number_served = value