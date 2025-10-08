# Store file's lines in a list called lines.
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

# Combine lines into one long string.
pi_string = ''
for line in lines:
    pi_string += line.strip()

# Check is user's birthday in is in the first million decimal digits of pi.
birthday = input("\nEnter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("\nYour birthday is in the first million decimal digits of pi!")
else:
    print("\nYour birthday is not in the first million decimal digits of pi...")