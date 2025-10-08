filename = 'programming_poll.txt'

prompt = "\nWhy do you like programming?"
prompt += "\n(enter 'quit' to exit the program) "

while True:
    reason = input(prompt)

    if reason == 'quit':
        break
    
    with open(filename, 'a') as file_object:
        file_object.write(f"{reason}\n")
        print("\nThanks for your input. Care to submit another response?")

print("\nPlease check programming_poll.txt to see all submitted responses!")