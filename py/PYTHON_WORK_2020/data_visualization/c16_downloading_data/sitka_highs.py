"""
This program uses Matplotlib to create a graph displaying the daily high  
temperatures for Sitka, AK in 2018. It uses data from the NOAA's 
Climate Data Online (CDO) database.
https://www.ncdc.noaa.gov/cdo-web/
"""
import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Find the columns containing the dates and high temperatures.
    for i in range(len(header_row)):
        if header_row[i] == 'DATE':
            date_index = i
        elif header_row[i] == 'TMAX':
            high_index = i

    # Store the dates and high temperatures. 
    dates, highs = [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(date)

        high = int(row[5])
        highs.append(high)
    
# Plot the data.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Format the plot.
plt.title("Daily high temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate() # Formats the date labels diagonally.
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()