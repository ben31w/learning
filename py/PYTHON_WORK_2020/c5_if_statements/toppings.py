available_toppings = ['extra cheese', 'pepperoni', 'mushrooms', 'green peppers',
                      'sausage', 'olives', 'pineapple', 'ham', 'anchovies']

requested_toppings = ['pepperoni', 'green peppers', 'sausage', 'french fries']

# if statement checks if there are requested_toppings
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            if requested_topping == 'green peppers':
                print("Sorry, we are out of green peppers right now.")
            else:
                print(f"Adding {requested_topping}.")
        else:
            print(f"Sorry, we don't serve {requested_topping}.")

print("\nFinished making pizza.")