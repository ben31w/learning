"""
This program uses Plotly to create a world map that displays where earthquakes
with 1.0+ magnitudes have occured within a specified time interval. It uses data
from GeoJSON files provided by the USGS.
https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
"""
import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Load the file.
filename = 'data/05_31_2020_eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# List of all earthquakes in the data set. Each EQ is a dictionary.
all_eq_dicts = all_eq_data['features']

# Collect data on each EQ.
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]
layout = Layout(title=f'{all_eq_data["metadata"]["title"]} - May 31, 2020')

fig = {'data': data, 'layout': layout}
offline.plot(fig, filename='html_files/global_earthquakes_30_day.html')