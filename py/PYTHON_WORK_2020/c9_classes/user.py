"""A class that can be used to represent a user of a computer, website, etc."""

class User:
    """User class stores information about a person/user."""

    def __init__(self, first_name, last_name, age, location=''):
        """Define names and attributes of user."""
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{self.first_name} {self.last_name}"
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        """Lists a user's attributes."""
        print(f"\nName: {self.full_name.title()}")
        print(f"Age: {self.age}")
        if self.location:
            print(f"Location: {self.location.title()}")
        print(f"Number of login attempts: {self.login_attempts}")

    def greet_user(self):
        """Greets the user."""
        print(f"\nHello, {self.full_name.title()}!")

    def increment_login_attempts(self, value):
        if value > 0:
            self.login_attempts += value

    def reset_login_attempts(self):
        self.login_attempts = 0