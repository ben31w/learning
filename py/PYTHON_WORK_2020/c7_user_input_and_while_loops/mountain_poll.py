responses = {}

# Flag to indicate polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the responses in the dictionary.
    responses[name] = response

    #Find out if anyone alse is going to take the poll.
    repeat = input("Would you like to submit another response? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Display results.
print("\n----Poll Results----")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")