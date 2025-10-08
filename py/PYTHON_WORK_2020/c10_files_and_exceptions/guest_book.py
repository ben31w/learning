filename = 'guest_book.txt'

prompt = "\nEnter a name, and I'll add it to my guest book."
prompt += "\n(enter 'quit' when you are done adding names.) "

while True:
    guest = input(prompt)

    if guest == 'quit':
        break
    
    with open(filename, 'a') as file_object:
        file_object.write(f"{guest}\n")
        print(f"\nAdded {guest}.")

print("\nPlease check guest_book.txt to see the new additions.")