import matplotlib.pyplot as plt

# The data
x_values = range(1, 1001)
y_values = [x**3 for x in x_values]

# The style and figure to be used
plt.style.use('seaborn')
fig, ax = plt.subplots()

# Plot the points.
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.hot, s=10)

# Set figure and axis titles, and tick mark sizes.
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)
ax.tick_params(axis='both', labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1_100_000_000])

# Save and show the figure.
plt.savefig('cubes_plot.png', bbox_inches='tight')
plt.show()