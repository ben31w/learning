"""
A set of classes used to represent an admin of a computer, website, etc.
Includes Privileges and Admin (a child class of User).
"""
from user import User

class Privileges:
    """A list of admin privileges."""

    def __init__(self, *privileges):
        self.privileges = privileges

    def add_privileges(self, *privileges):
        """Add privileges to an admin."""
        self.privileges = list(self.privileges)
        for privilege in privileges:
            self.privileges.append(privilege)
        self.privileges = tuple(self.privileges)

    def show_privileges(self):
        """Print a list of admin privileges."""
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    """A simple Admin class that extends User."""

    def __init__(self, first_name, last_name, age, location=''):
        """
        Initialize attributes inherited from User.
        Then initialize new attributes.
        """
        super().__init__(first_name, last_name, age, location)
        # Other inherited attributes: login_attempts = 0
        self.privileges = Privileges('can add posts', 'can delete posts',
            'can ban users')
