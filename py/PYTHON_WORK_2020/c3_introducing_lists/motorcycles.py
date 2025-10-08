motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Modifying elements in a list:
motorcycles[0] = 'ducati'
print(motorcycles)

# Appending elements to the end of a list:
motorcycles.append('honda')
print(motorcycles)

# Inserting elements into a list:
motorcycles.insert(2, 'harley-davidson')
print(motorcycles)

# Removing elements from a list using a del statement:
del motorcycles[2]
print(motorcycles)

# Removing elements from a list using remove() allows you to remove an item w/o knowing its index:
motorcycles.remove('suzuki')
print(motorcycles)

# Removing elements from a list using pop() allows you to use the removed element:
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Note: pop() still removes the elements from the list.
print(motorcycles)

#Adding the popped elements back to the list:
motorcycles.append(last_owned)
motorcycles.insert(0, first_owned)
print(motorcycles)