my_pizzas = ['cheese', 'pepperoni', 'sausage']
friend_pizzas = my_pizzas[:]

my_pizzas.append('hawaiian')
friend_pizzas.append('anchovy')

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

print("\nPizza is our favorite food!")