countries = ['germany', 'vietnam', 'south africa', 'peru', 'new zealand']

print(f"{len(countries)} countries I want to visit:")
print(countries)

print("\nIn reverse order:")
countries.reverse()
print(countries)

print("\nIn alphabetical order:")
print(sorted(countries))

print("\nIn reverse alphabetical order:")
print(sorted(countries, reverse=True))

print("\nIn alphabetical order again:")
countries.sort()
print(countries)