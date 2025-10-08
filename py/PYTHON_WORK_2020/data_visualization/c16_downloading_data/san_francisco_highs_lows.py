
"""
This program uses Matplotlib to create a graph displaying the daily high and low 
temperatures for San Francisco Valley, CA in 2018. It uses data from the NOAA's 
Climate Data Online (CDO) database.
https://www.ncdc.noaa.gov/cdo-web/
"""
import csv
from datetime import datetime

import matplotlib.pyplot as plt

# Collect the data.
filename = 'data/san_francisco_2018.csv'
with open(filename) as f:
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
    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            print(f"Missing data for {date}.")
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

# Plot the data.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format the plot.
plt.title('Daily high and low temperatures - 2018\nSan Francisco, CA', 
    fontsize=22)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.ylim(0, 130)
plt.tick_params(axis='both', labelsize=16)

plt.show()