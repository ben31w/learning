sandwich_orders = ['pastrami', 'tuna', 'chicken', 'pastrami', 'pastrami', 'ham', 'ham', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich == 'pastrami':
        print("Sorry, we are out of pastrami.")
        while 'pastrami' in sandwich_orders:
            sandwich_orders.remove('pastrami')
    else:
        print(f"I made your {sandwich} sandwich.")
        finished_sandwiches.append(sandwich)

print("\nFinished making all the sandwiches.")