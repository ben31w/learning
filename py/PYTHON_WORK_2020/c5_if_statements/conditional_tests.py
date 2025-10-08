car = 'subaru'
print(f"car = {car}")

print("Is car == 'audi'? I predict False.")
print(car == 'audi')

print("\nIs car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'Subaru'? I predict False.")
print(car == 'Subaru')

print("\nIs car.title() == 'Subaru'? I predict True.")
print(car.title() == 'Subaru')

age_0 = 19
age_1 = 22
print(f"\nage_0 = {age_0}")
print(f"age_1 = {age_1}")

print("\nIs age_0 >= 18? I predict True.")
print(age_0 >= 18)

print("\nIs age_0 >= 21? I predict False.")
print(age_0 >= 21)

print("\nIs age_0 >= 21 or age_1 >=21? I predict True.")
print(age_0 >= 21 or age_1 >=21)

print("\nIs age_0 >= 21 and age_1 >=21? I predict False.")
print(age_0 >= 21 and age_1 >= 21)

books = ['harry potter', 'percy jackson', 'the other wes moore']
print(f"\nbooks: {books}")

print("\nIs 'Percy Jackson'.lower in books? I predict True.")
print('Percy Jackson'.lower() in books)

print("\nIs 'the outsiders' not in books? I predict True.")
print('the outsiders' not in books)