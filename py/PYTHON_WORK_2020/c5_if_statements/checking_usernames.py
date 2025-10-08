current_users = ['admin', 'ben', 'kyle', 'brian', 'nathan', 'stuart']
new_users = ['ben31w', 'KyleM', 'Brian', 'nAtHaN', 'stuart5555']

print("Current users:")
print(current_users)
print()

username_taken = False

for new_user in new_users:
    for current_user in current_users:
        if new_user.lower() == current_user.lower():
            print(f"Sorry, the username '{new_user}' is taken.")
            username_taken = True
    if username_taken == False:
        print(f"Added {new_user}.")
        current_users.append(new_user)
    else:
        username_taken = False

print("\nCurrent users:")
print(current_users)