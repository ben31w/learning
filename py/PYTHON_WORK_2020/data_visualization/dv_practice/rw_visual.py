from plotly.graph_objs import Scatter, Layout, Figure
from plotly import offline

from random_walk import RandomWalk

# Make a random walk.
rw = RandomWalk(50_000)
rw.fill_walk()

# Create the visualization.
data = [
    Scatter(
        x=rw.x_values, y=rw.y_values, mode='markers',
        marker=dict(
            color=list(range(rw.num_points)),
            colorscale='Plotly3',
            size=1
        )
    )
]
layout = Layout(
    xaxis=dict(visible=False),
    yaxis=dict(visible=False)
)

fig = Figure(data=data, layout=layout)
offline.plot(fig, filename='rw_visual.html')