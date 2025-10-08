import json

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    # If there's a username stored in username.json, print a message asking the
    #  current user if their name is the username.
    if username:
        answer = input(f"Are you {username}? (yes/no) ")
        not_answered = True
        while not_answered:
            # If they answer yes, greet them.
            if answer.lower() == 'yes':
                print(f"Welcome back, {username}!")
                not_answered = False
            # If they answer no, call get_new_username()
            elif answer.lower() == 'no':
                username = get_new_username()
                print(f"We'll remember you when you come back, {username}!")
                not_answered = False
            else:
                answer = input("Please enter 'yes' or 'no'. ")
    # If username.json doesn't exist, call get_new_username()
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()