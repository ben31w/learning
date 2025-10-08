import json

# Explore the structure of the data.
# Load the file.
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# List of all earthquakes in the data set. Each EQ is a dictionary.
all_eq_dicts = all_eq_data['features']

# Find the magnitude, longitude, and latitude of each EQ.
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag'] # properties is a nested dictionary
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])