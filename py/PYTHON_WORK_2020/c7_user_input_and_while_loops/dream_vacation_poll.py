responses = {}

# Welcome users with message.
print("Thank you for taking the dream vacation poll.")

# Flag to indicate polling is active.
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("What is your dream vacation place? ")

    # Store user's name and response in dictionary.
    responses[name] = response

    # Ask for more results.
    print("\nYour response has been recorded.")
    repeat = input("Would you like to submit another response? (yes/no) ")

    if repeat == 'no':
        polling_active = False

# Display results.
for name, response in responses.items():
    print(f"{name} wants to visit {response}.")
