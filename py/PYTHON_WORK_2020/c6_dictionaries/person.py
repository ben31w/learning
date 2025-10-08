person_0 = {
    'first_name': 'ben',
    'last_name': 'wright',
    'age': 18,
    'city': 'leesburg',
}
person_1 = {
    'first_name': 'kyle',
    'last_name': 'mcguinness',
    'age': 17,
    'city': 'leesburg',
}
person_2 = {
    'first_name': 'bernie',
    'last_name': 'sanders',
    'age': 78,
    'city': 'burlington',
}
person_3 = {
    'first_name': 'joe',
    'last_name': 'biden',
    'age': 77,
    'city': 'wilmington',
}

people = [person_0, person_1, person_2, person_3]

for person in people:
    print(f"Name: {person['first_name'].title()} {person['last_name'].title()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].title()}\n")