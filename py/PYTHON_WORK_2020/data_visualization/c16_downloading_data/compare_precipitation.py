"""
This program uses Matplotlib to create a graph comparing the precipitation 
levels for Sitka, AK; Death Valley, CA; and San Francisco, CA in 2018. It uses 
data from the NOAA's Climate Data Online (CDO) database.
https://www.ncdc.noaa.gov/cdo-web/
"""
import csv
from datetime import datetime

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

# The files.
file_1 = 'data/sitka_weather_2018_simple.csv'
file_2 = 'data/death_valley_2018_simple.csv'
file_3 = 'data/san_francisco_2018.csv'

# The data to be collected.
sitka_dates, sitka_prcp = [], []
dv_dates, dv_prcp = [], []
sf_dates, sf_prcp = [], []

# Collect data for Sitka.
with open(file_1) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Find the row indexes containing the dates and precipitations.
    for i in range(len(header_row)):
        if header_row[i] == 'DATE':
            date_index = i
        elif header_row[i] == 'PRCP':
            prcp_index = i

    # Store the data.
    for row in reader:
        date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            prcp = float(row[prcp_index])
        except ValueError:
            print(f"Sitka has no precipitation data for {date}.")
        else:
            sitka_dates.append(date)
            sitka_prcp.append(prcp)

# Collect data for Death Valley.
with open(file_2) as f:
    reader = csv.reader(f)
    header_row = next(f)

    # Find the row indexes containing the dates and precipitations.
    for i in range(len(header_row)):
        if header_row[i] == 'DATE':
            date_index = i
        elif header_row[i] == 'PRCP':
            prcp_index = i

    # Store the data.
    for row in reader:
        date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            prcp = float(row[prcp_index])
        except ValueError:
            print(f"Death Valley has no precipitation data for {date}.")
        else:
            dv_dates.append(date)
            dv_prcp.append(prcp)

# Collect data for San Francisco.
with open(file_3) as f:
    reader = csv.reader(f)
    header_row = next(f)

    # Find the row indexes containing the dates and precipitations.
    for i in range(len(header_row)):
        if header_row[i] == 'DATE':
            date_index = i
        elif header_row[i] == 'PRCP':
            prcp_index = i

    # Store the data.
    for row in reader:
        date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            prcp = float(row[prcp_index])
        except ValueError:
            print(f"San Francisco has no precipitation data for {date}.")
        else:
            sf_dates.append(date)
            sf_prcp.append(prcp)

# Plot the data.
# plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(sitka_dates, sitka_prcp, c='blue')
ax.plot(sf_dates, sf_prcp, c='green')
ax.plot(dv_dates, dv_prcp, c='red')

# Create a legend.
patch_1 = mpatches.Patch(color='blue', label='Sitka, AK')
patch_2 = mpatches.Patch(color='red', label='Death Valley, CA')
patch_3 = mpatches.Patch(color='green', label='San Francisco, CA')
ax.legend(handles=[patch_1, patch_2, patch_3])

# Format the plot.
plt.title('Comparing Precipation Levels - 2018', fontsize=22)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Precipitation (in.)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()