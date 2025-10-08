def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    if toppings:
        print(f"\nMaking a {size}-inch pizza with the following toppings:")
        for topping in toppings:
            print(f"- {topping}")
    else:
        print(f"\nMaking a {size}-inch pizza.")