from plotly import express as px

# Example 1, uses a Pandas dataframe. Found from this site:
#  https://matteoguzzo.com/blog/embed-html-graphs-plotly/

gapminder = px.data.gapminder()

fig = px.scatter(
    gapminder.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
    height=600,
    width=975,
)
fig.show()

with open('gdpPerCapVsLifeExpGraph.html', 'w') as f:
    f.write(fig.to_html(include_plotlyjs='cdn'))


# Example 2, uses lists.
#  Looks like date needs to be serialized before trendline will work.
#  https://stackoverflow.com/questions/61644142/plotly-how-to-show-trendline-for-time-series-data-using-plotly-express
x = ['2023-10-22', 
    '2023-10-23', 
    '2023-10-24', 
    '2023-10-26',
    '2023-10-27',
    '2023-10-28',
    '2023-10-29',
    '2023-10-30',
    '2023-11-04',
    '2023-11-06',
    '2023-11-07',
    '2023-11-08',
    '2023-11-12',
    '2023-11-13',
    '2023-11-14',
]
y = [166.8, 167.0, 168.0, 166.0, 167.9, 168.1, 167.4, 168.0, 166.1, 168.2, 167.7, 168.1, 168.2, 168.8, 168.9]
fig = px.scatter(x=x, y=y, labels={'x': 'date', 'y': 'weight'})
with open('dateVsWeight.html', 'w') as f:
    f.write(fig.to_html(include_plotlyjs='cdn'))