# The range() function creates a range of ints starting at the first given int
# and ending just before the second. If you give range() only one number, it 
# will start at zero and stop just before the given number.
for value in range(1, 5):
    print(value)

# range() can be used inside the list() function to create a list of numbers:
numbers = list(range(6))
print(numbers)