cars = ['bmw', 'audi', 'toyota', 'subaru']

# The sort() method alters the order of the list permanently. By default, sort()
# will sort the elements alphabetically. You can pass the argument reverse=True
# to sort them in reverse alphabetical order.
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# To maintain the original order of the list but present in a sorted order, use
# the sorted() function.
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("\nHere are the sorted lists:")
print(sorted(cars))
print(sorted(cars, reverse=True))

print("\nHere is the original list:")
print(cars)

# The reverse() method reverses the order of a list. 
# Like sort(), reverse() changes the order pemanently, but it can easily be 
# reverted by applying reverse() a second time.
cars.reverse()
print("\nHere is the list in reverse order:")
print(cars)

# The len() function returns the length of a list.
print("\nThe length of the list is:")
print(len(cars))