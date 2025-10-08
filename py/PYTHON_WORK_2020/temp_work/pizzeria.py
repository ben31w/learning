# Welcome customer, and ask how many pizzas they will order.
welcome_prompt = "\nWelcome to Paisano's Pizzeria!"
welcome_prompt += "\nHow many pizzas will you be ordering today? "
number_valid = False

while not number_valid:
    try:
        num_pizzas = int(input(welcome_prompt))
    except ValueError:
        welcome_prompt = "\nPlease enter a valid number." 


size_prompt += "\nWhat size pizza would you like? (small/medium/large) "

size_response = input(size_prompt)
size_valid = False

while size_valid == False:
    if size_response.strip().lower() == 'small' or size_response.strip().lower() == 's':
        size = 'small'
        size_valid = True
    elif size_response.strip().lower() == 'medium' or size_response.strip().lower() == 'm':
        size = 'medium'
        size_valid = True
    elif size_response.strip().lower() == 'large' or size_response.strip().lower() =='l':
        size = 'large'
        size_valid = True
    else:
        size_prompt = "\nPlease enter a valid size. "
        size_response = input(size_prompt)

# Ask customer for crust thickness.
crust_prompt = "\nWhat type of crust would you like? (thick/thin) "
crust_response = input(crust_prompt)
crust_valid = False

while crust_valid == False:
    if crust_response.strip().lower() == 'thick':
        crust = 'thick'
        crust_valid = True
    elif crust_response.strip().lower() == 'thin':
        crust = 'thin'
        crust_valid = True
    else:
        crust_prompt = "Please specify if you want a thick or thin crust. "
        crust_response = input(crust_prompt)

# Ask for any toppings.
available_toppings = ['pepperoni', 'sausage', 'anchovies', 'pineapple', 
    'green peppers', 'mushrooms', 'olives', 'onions', 'extra cheese']
requested_toppings = []
print("\nWe serve the following toppings:")
print(sorted(available_toppings))

toppings_prompt = "\nWould you like any toppings? "
requesting_toppings = True


while requesting_toppings:
    toppings_response = input(toppings_prompt)
    if toppings_response.strip().lower() == 'no':
        requesting_toppings = False
    elif toppings_response.strip().lower() in available_toppings:
        requested_toppings.append(toppings_response.strip().lower())
        print(f"Adding {toppings_response.strip().lower()}.")
        toppings_prompt = "\nAnything else? "
    else:
        print(f"Sorry, we don't serve {toppings_response.strip().lower()}.")
        toppings_prompt = "\nAnything else? "

# Print their order.
if len(requested_toppings) == 0:
    print(f"\nYou ordered a {size}, {crust}-crust pizza.")
else:
    print(f"\nYou ordered a {size}, {crust}-crust pizza with the following toppings:")
    for topping in requested_toppings:
        print("- " + topping)
print("\nEnjoy!")