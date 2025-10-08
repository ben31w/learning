def build_person(first_name, last_name, age=None):
    """Returns a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', 27)
print(musician)

musician = build_person('john', 'lennon')
print(musician)