# Python refers to values that cannot be changed as immutable, and an immutable 
#  list is called a tuple. Tuples look just like lists, but the are initialized 
#  using parentheses instead of square brackets.
dimensions = (200, 50)
print(dimensions[0]) # Item indexes, however, still uses square brackets.
print(dimensions[1])

# Although you can't modify the items in a tuple, you can still change them by 
#  redefining the entire tuple.
dimensions = (400, 100)
print(dimensions[0])
print(dimensions[1])


# Note: Tuples are technically defined by the presence of a comma, not 
#  parentheses. If for some reason, you wanted to create a tuple with only one 
#  element, you would need to include a trailing comma.

my_t = (3,) # Without the trailing comma, this variable would just be an int.

print()
print(my_t)

# You can't modify the elements of a tuple or append items unless you convert 
#  the tuple to a list using the list() function.
my_t = list(my_t)
my_t[0] = 1
my_t.append(2)
my_t = tuple(my_t)

print(my_t)