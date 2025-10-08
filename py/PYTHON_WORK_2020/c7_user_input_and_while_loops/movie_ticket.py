prompt = "How old are you?"
prompt += "\nThis will determine the price of your movie ticket. "

age = int(input(prompt))

if age < 3:
    price = 0
elif age < 12:
    price = 10
else:
    price = 15

print(f"\nYour ticket will be ${price}.")