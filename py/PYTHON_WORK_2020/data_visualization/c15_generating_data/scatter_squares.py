import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# Plotting the points.
# c is the color of the points (can use strings like 'red' or a tuple with RGB 
#  values 0-1). You can initialize c as a list of numbers, and the points will 
#  be colored in a gradient when a colormap (cmap) argument is defined.
# s is the size of the points.
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
#  x-axis runs from 0 to 1100. y-axis runs from 0 to 1,100,000.
ax.axis([0, 1100, 0, 1_100_000])

# Save the figure as an image with trimmed whitespace, then show the figure.
plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()