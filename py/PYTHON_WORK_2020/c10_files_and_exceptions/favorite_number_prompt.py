import json

no_favorite_number = True
while no_favorite_number:
    try:
        fav_num = int(input("What is your favorite number? "))
    except ValueError:
        print("Please enter an integer.")
    else:
        filename = 'favorite_number.json'
        with open(filename, 'w') as f:
            json.dump(fav_num, f)
            print(f"So your favorite number is {fav_num}. I'll remember that!")
            no_favorite_number = False