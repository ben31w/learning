import json

def find_favorite_number():
    """Ask user what their favorite number is and return it."""
    no_favorite_number = True
    while no_favorite_number:
        try:
            favorite_number = int(input("What is your favorite number? "))
        except ValueError:
            print("Please enter an integer.")
        else:
            return favorite_number

def print_favorite_number():
    """
    Prints the user's 'favorite number' stored in favorite_number.json.
    If that file does not exist, call find_favorite_number() to find the user's
    favorite number, then store it in favorite_number.json and print a message
    saying it's been 'remembered.'
    """
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            fav_num = json.load(f)
    except FileNotFoundError:
        fav_num = find_favorite_number()
        with open(filename, 'w') as f:
            json.dump(fav_num, f)
            print(f"So your favorite number is {fav_num}. I'll remember that!")
    else:
        print(f"Your favorite number is {fav_num}.")

print_favorite_number()