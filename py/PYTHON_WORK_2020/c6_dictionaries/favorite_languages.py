favorite_languages = {
    'jen': 'python',
    'claire': 'c',
    'robert': 'ruby',
    'phil': 'python', # It's good practice to add a comma after the last
                      # key:value pair in case you want to add more.
}

for k, v in favorite_languages.items():
    print(f"{k.title()}'s favorite language is {v.title()}.")

print("\nThank you to the following respondents for taking the poll:")
# If you omit the keys() method, Python will still loop through the dictionary's
# keys by default.
for k in sorted(favorite_languages.keys()):
    print(k.title())

print("\nThe following languages have been collected:")
# A set is a collection of items in which each item must be unique. Use the
# set() method to retrieve values from a list or dictionary w/o repetition.
for v in set(favorite_languages.values()):
    print(v.title())
# You can also build a set directly using braces and commas, and Python will
# omit repeated items:
languages = {'python', 'ruby', 'c', 'python'}
print(languages)
# Unlike lists and dictionaries, sets do not retain items in any specific order.
# (This is noticeable when you re-build the program over and over again.)