"""
This program uses Matplotlib to create a graph comparing the high and low 
temperatures for Sitka, AK and Death Valley, CA in 2018. It uses data from the
NOAA's Climate Data Online (CDO) database.
https://www.ncdc.noaa.gov/cdo-web/
"""
import csv
from datetime import datetime

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

# The files.
file_1 = 'data/sitka_weather_2018_simple.csv'
file_2 = 'data/death_valley_2018_simple.csv'

# The data to be collected.
sitka_dates, sitka_highs, sitka_lows = [], [], []
dv_dates, dv_highs, dv_lows = [], [], []

# Collect data for Sitka, AK.
with open(file_1) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Find the row indexes containing the dates, and high and low temperatures.
    for i in range(len(header_row)):
        if header_row[i] == 'DATE':
            date_index = i
        elif header_row[i] == 'TMAX':
            high_index = i
        elif header_row[i] == 'TMIN':
            low_index = i

    # Store the data.
    for row in reader:
        date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            print(f"Sitka is missing data for {date}.")
        else:
            sitka_dates.append(date)
            sitka_highs.append(high)
            sitka_lows.append(low)

# Collect data for Death Valley, CA.
with open(file_2) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Find the row indexes containing the dates, and high and low temperatures.
    for i in range(len(header_row)):
        if header_row[i] == 'DATE':
            date_index = i
        elif header_row[i] == 'TMAX':
            high_index = i
        elif header_row[i] == 'TMIN':
            low_index = i

    # Store the data.
    for row in reader:
        date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            print(f"Death Valley is missing data for {date}.")
        else:
            dv_dates.append(date)
            dv_highs.append(high)
            dv_lows.append(low)

# Plot the data.
# plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(sitka_dates, sitka_highs, c='red', alpha=0.5)
ax.plot(sitka_dates, sitka_lows, c='blue', alpha=0.5)
plt.fill_between(sitka_dates, sitka_highs, sitka_lows, facecolor='blue', 
    alpha=0.1)
ax.plot(dv_dates, dv_highs, c='indianred', alpha=0.5)
ax.plot(dv_dates, dv_lows, c='steelblue', alpha=0.5)
plt.fill_between(dv_dates, dv_highs, dv_lows, facecolor='steelblue', alpha=0.1)

# Create a legend.
patch_1 = mpatches.Patch(color='red', alpha=0.5, label='Sitka H')
patch_2 = mpatches.Patch(color='blue', alpha=0.5, label='Sitka L')
patch_3 = mpatches.Patch(color='indianred', alpha=0.5, label='Death Valley H')
patch_4 = mpatches.Patch(color='steelblue', alpha=0.5, label='Death Valley H')
plt.legend(handles=[patch_1, patch_2, patch_3, patch_4])

# Format the plot.
plt.title('Sitka vs. Death Valley H&L Temperatures - 2018', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.ylim(0, 130)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()