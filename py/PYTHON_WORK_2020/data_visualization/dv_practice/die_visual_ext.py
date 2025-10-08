"""
This uses Plotly to create a bar graph comparing the results of rolling two D6
and three D4 (types of dice) 1000 times.
"""
from plotly.graph_objs import Bar, Layout, Figure
from plotly import offline

from die import Die

# Make the dice.
d6_1, d6_2 = Die(), Die()
d4_1, d4_2, d4_3 = Die(4), Die(4), Die(4)

# Make some rolls, and store the results.
d6_results = []
d4_results = []
for i in range(5000):
    d6_results.append(d6_1.roll() + d6_2.roll())
    d4_results.append(d4_1.roll() + d4_2.roll() + d4_3.roll())

# Count the number of times each result appeared, and store the frequencies.
d6_frequencies = []
d4_frequencies = []
max_result = max(d6_1.num_sides + d6_2.num_sides, 
    d4_1.num_sides + d4_2.num_sides, d4_3.num_sides)
for i in range(2, max_result+1):
    d6_frequencies.append(d6_results.count(i))
    d4_frequencies.append(d4_results.count(i))

# Create a visualization.
x_values = list(range(2, max_result+1))
data = [
    Bar(name='D6 Results', x=x_values, y=d6_frequencies, hoverinfo='y', marker=dict(color='blue')),
    Bar(name='D4 Results', x=x_values, y=d4_frequencies, hoverinfo='y', marker=dict(color='red'))
]
layout = Layout(
    title='Results of rolling two D6 and three D4 5000 times',
    titlefont=dict(size=24),
    xaxis=dict(title='Result', dtick=1),
    yaxis=dict(title='Frequency of Result')
)

fig = Figure(data=data, layout=layout)
offline.plot(fig, filename='d6_d6_vs_d4_d4_d4.html')