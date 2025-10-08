def describe_pet(animal_type, pet_name):
    """Displays information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# For positional arguments, the order matters.
describe_pet('cat', 'sweetie')
describe_pet('dog', 'georgia')

# For keyword arguments, the order doesn't matter since you specify each
# variable's value.
describe_pet(animal_type='cat', pet_name='sweetie')
describe_pet(pet_name='georgia', animal_type='dog')

# When you use a default value for a parameter, it must come after all
# non-default parameters. This is because Python still maintains positional
# arguments when you omit the argument with a default parameter.
def describePet(pet_name, animal_type='cat'):
    """Same as describe_pet(), but has a default animal_type parameter."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describePet('sweetie')
describePet('georgia', 'dog')