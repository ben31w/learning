# If file is in the same directory as current program
filename = 'pi_digits.txt'
with open(filename) as file_object:
    contents = file_object.read()
print(contents)

# If file isn't in the same directory as current program
file_path = '/Users/ben31/OneDrive/Desktop/python_work/text_files/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
print(contents)