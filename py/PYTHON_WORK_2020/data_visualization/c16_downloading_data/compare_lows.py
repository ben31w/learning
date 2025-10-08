"""
This program uses Matplotlib to create a graph comparing the low temperatures 
for Sitka, AK; San Francisco, CA; and Death Valley, CA in 2018. It uses data 
from the NOAA's Climate Data Online (CDO) database.
https://www.ncdc.noaa.gov/cdo-web/
"""
import csv
from datetime import datetime

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

# The files.
file_1 = 'data/sitka_weather_2018_simple.csv'
file_2 = 'data/san_francisco_2018.csv'
file_3 = 'data/death_valley_2018_simple.csv'

# The data to be collected.
sitka_dates, sitka_lows = [], []
sf_dates, sf_lows = [], []
dv_dates, dv_lows = [], []

# Collect data for Sitka, AK.
with open(file_1) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Find the row indexes containing the dates and low temperatures.
    for i in range(len(header_row)):
        if header_row[i] == 'DATE':
            date_index = i
        elif header_row[i] == 'TMIN':
            low_index = i

    # Store the data.
    for row in reader:
        date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            low = int(row[low_index])
        except ValueError:
            print(f"Sitka is missing data for {date}.")
        else:
            sitka_dates.append(date)
            sitka_lows.append(low)

# Collect data for San Francisco, CA.
with open(file_2) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Find the row indexes containing the dates and low temperatures.
    for i in range(len(header_row)):
        if header_row[i] == 'DATE':
            date_index = i
        elif header_row[i] == 'TMIN':
            low_index = i

    # Store the data.
    for row in reader:
        date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            low = int(row[low_index])
        except ValueError:
            print(f"San Francisco is missing data for {date}.")
        else:
            sf_dates.append(date)
            sf_lows.append(low)

# Collect data for Death Valley, CA.
with open(file_3) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Find the row indexes containing the dates and low temperatures.
    for i in range(len(header_row)):
        if header_row[i] == 'DATE':
            date_index = i
        elif header_row[i] == 'TMIN':
            low_index = i

    # Store the data.
    for row in reader:
        date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            low = int(row[low_index])
        except ValueError:
            print(f"Death Valley is missing data for {date}.")
        else:
            dv_dates.append(date)
            dv_lows.append(low)

# Plot the data.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(sitka_dates, sitka_lows, c='navy')
ax.plot(sf_dates, sf_lows, c='blue')
ax.plot(dv_dates, dv_lows, c='deepskyblue')

# Create a legend.
patch_1 = mpatches.Patch(color='navy', label='Sitka, AK')
patch_2 = mpatches.Patch(color='blue', label='San Francisco, CA')
patch_3 = mpatches.Patch(color='deepskyblue', label='Death Valley, CA')
ax.legend(handles=[patch_1, patch_2, patch_3])

# Style the plot.
plt.title('Comparing Daily Low Temperatures - 2018', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.ylim(20, 130)
plt.tick_params(axis='both', labelsize=16)

plt.show()