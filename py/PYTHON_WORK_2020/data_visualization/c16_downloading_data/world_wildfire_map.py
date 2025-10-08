"""
This program uses Plotly to create a world map that displays the brightness and
location of all wildfires that have occured within a specified time interval.
It uses data from NASA's Earth Observation Data.
https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data
"""
import csv

from plotly.graph_objs import Scattergeo, Layout, Figure
from plotly import offline

# The file
filename = 'data/MODIS_C6_Global_24h.csv'

# The data to be collected.
lons, lats, brights = [], [], []

# Collect the data.
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Find the row indexes containing the longitudes, latitudes, and brightnesses.
    for i in range(len(header_row)):
        if header_row[i] == 'longitude':
            lon_index = i
        elif header_row[i] == 'latitude':
            lat_index = i
        elif header_row[i] == 'brightness':
            bright_index = i

    # Store the data.
    for row in reader:
        lons.append(float(row[lon_index]))
        lats.append(float(row[lat_index]))
        brights.append(float(row[bright_index]))

# Map the data.
data = [
    Scattergeo(
        lon=lons, 
        lat=lats, 
        hovertext=brights,
        marker=dict(
            size=4,
            color=brights,
            colorscale='Plasma',
            reversescale=True,
            colorbar=dict(title='Brightness Temperature (K)')
        )
    )
]
layout = Layout(title='World Wildfires in the Past 24 Hours (06-06-2020)')

fig = {'data': data, 'layout': layout}
offline.plot(fig, filename='html_files/world_wildfires_1_day.html')