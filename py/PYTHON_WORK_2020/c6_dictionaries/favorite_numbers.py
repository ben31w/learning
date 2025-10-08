favorite_numbers = {
    'ben': [13, 31],
    'kyle': [13],
    'lamar': [8, 7],
    'tom': [12],
}

for name, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print(f"{name.title()}'s favorite number is:")
    else:
        print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")
    print()