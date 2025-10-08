squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

# List comprehension combines the for loop and the creation of new elements into one line,
# and automatically appends each new element. The following example uses list comprehension
# to build a list of squared numbers:
squares = [value**2 for value in range(1,11)]
print(squares)