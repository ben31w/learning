"""A class for ice cream stands, which are treated as types of restaurants."""

from restaurant import Restaurant

class IceCreamStand(Restaurant):
    """A simple attempt to model an ice cream stand."""

    def __init__(self, restaurant_name, number_served=0):
        """
        Initialize attributes from parent class.
        Add new attribute 'flavors'.
        """
        super().__init__(restaurant_name=restaurant_name, 
                         cuisine_type='ice cream', 
                         number_served=number_served)
        self.flavors = ['chocolate', 'vanilla', 'strawberry']

    def describe_restaurant(self):
        """Prints a message about the ice cream stand."""
        print(f"{self.restaurant_name.title()} is an ice cream stand. "
            f"It has served {self.number_served} people.")

    def display_flavors(self):
        """Print the list of flavors."""
        print("This ice cream stand serves the following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

    def add_flavors(self, *flavors):
        """
        Given a list of new flavors, add them to the existing list.
        Since self.flavors is defined as a list (not a tuple), you 
        don't need to convert it using the list() and tuple() functions.
        """
        for flavor in flavors:
            if flavor not in self.flavors:
                self.flavors.append(flavor)