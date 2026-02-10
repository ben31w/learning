# Source - https://stackoverflow.com/a/69741932
# Posted by Rob Raymond, modified by community. See post 'Timeline' for change history
# Retrieved 2026-02-03, License - CC BY-SA 4.0

import plotly.graph_objects as go
import plotly.express as px

x_list = [1, 2, 3, 4, 5, 6]
y_list = [5, 1, 1, 4, 1, 3]
color_list = [0, 2, 0, 2, 2, 1]


go.Figure(
    [
        go.Scatter(
            x=x_list[tn : tn + 2],
            y=y_list[tn : tn + 2],
            # line_shape="hv",
            line_color=px.colors.qualitative.Plotly[color_list[tn]],
            showlegend=False,
        )
        for tn in range(len(x_list))
    ]
).show()
