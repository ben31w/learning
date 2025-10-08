import json

# Explore the structure of the data.
# Load the file.
filename = 'data/eq_data_7_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# Make the file more readable by using json.dump() with an indent argument.
readable_file = 'data/readable_eq_data_7_day.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

# The newly created, more readable file shows the entire thing is a dictionary
#  with 3 keys: "type", "metadata", and "features". "type" and "metadata"
#  contain information about the file itself, while "features" contains a list
#  of all the earthquakes. Each earthquake item is a dictionary, with keys such
#  as "properties" and "geometry" that store info about each earthquake.