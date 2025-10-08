# A dictionary in Python is a collection of key-value pairs. Each key is
# connected to a value, and you can use a key to access its associated value.
# A key's value can be a number, a string, a list, or even another dictionary.
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# You can add keys to a dictionary at any time:
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 0, 'speed': 'medium'}
print(f"\nOriginal position: {alien_0['x_position']}")

# Move the alien to the right based on its speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3

# New position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")