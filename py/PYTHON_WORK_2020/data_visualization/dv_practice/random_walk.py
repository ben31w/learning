"""
A class for modeling random walks on a simple 2D grid.
A random walk is a path where each step is random.
"""

from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # Create lists to store x- and y-values. All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Perform a step in a random direction and over a random distance."""
        direction = choice([-1, 1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            
            # Decide which direction to go and how to go in that direction.
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject and redo steps that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position, and add the new values to the lists.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)