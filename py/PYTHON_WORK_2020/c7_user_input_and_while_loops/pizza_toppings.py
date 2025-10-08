prompt = "Enter a pizza topping."
prompt += "\n(Enter 'quit' to exit the program.) "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    elif (topping == 'pepperoni') or (topping == 'Pepperoni') or (topping == 'PEPPERONI'):
        print("Sorry, we are out of pepperoni.\n")
    else:
        print(f"Adding {topping}.\n")
