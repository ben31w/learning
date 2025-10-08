filename = 'learning_python.txt'

# Print by reading the entire file.
with open(filename) as file_object:
    contents = file_object.read().replace('Python', 'C')

print(contents + "\n")

# Print by looping through the file object.
with open(filename) as file_object:
    for line in file_object:
        print(line.replace('Python', 'C').rstrip())

print()

# Print by storing lines in a list.
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.replace('Python', 'C').rstrip())

print()