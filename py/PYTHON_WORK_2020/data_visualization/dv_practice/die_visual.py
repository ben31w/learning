"""This program graphs the results of rolling a specified number of dice."""
import matplotlib.pyplot as plt

from die import Die

# Make some dice.
die_1 = Die()
die_2 = Die()

# Roll the dice 1000 times, and store the results.
results = []
for i in range(1000):
    results.append(die_1.roll() + die_2.roll())

# Count the number of times each result appeared, and store the frequencies.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for i in range(2, max_result+1):
    frequencies.append(results.count(i))

# Graph the results.
plt.style.use('ggplot')
labels = list(range(2, max_result+1))
fig, ax = plt.subplots()
ax.bar(labels, frequencies)

# Format the plot.
plt.title('Results of rolling two D6 1000 times', fontsize=24)
plt.xlabel('Result', fontsize=16)
plt.ylabel('Frequency of Result', fontsize=16)
plt.xticks(labels)

plt.show()