import matplotlib.pyplot as plt

plt.style.use('seaborn')

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# fig represents the entire figure or collection of plots that are generated.
#  ax represents a single set of axes, or a subplot, in the figure.
#  pyplot.subplots() creates a Figure and an object or array of Axes.
fig, ax = plt.subplots()

# axes.Axes.plot() creates a plot from the data it is given.
# When plot() is given only one set of numbers, the numbers act as the 
#  y-coordinates, and the x-coordinates default to range(len(y)).
# When plot() is given two set of numbers, the first set acts as x-coordinates,
#  while the second set corresponds to the y-axis.
ax.plot(input_values, squares, linewidth=3)

# Set the chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick mark labels on both axes.
ax.tick_params(axis='both', labelsize=14)

plt.show()