def display_message():
    """Prints a sentence about Python Crash Course Chapter 8."""
    print("I'm learning about functions.")

def greet_user(username):
    """Display a simple greeting."""
    print(f"\nHello, {username.title()}!")

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

greet_user('reader')
display_message()

while True:
    print("\nPlease tell me your name.")
    print("(Enter 'quit' at any time to quit.)\n")
    
    f_name = input("First name: ")
    if f_name == 'quit':
        break

    l_name = input("Last name: ")
    if l_name == 'quit':
        break

    person = get_formatted_name(f_name, l_name)
    greet_user(person)