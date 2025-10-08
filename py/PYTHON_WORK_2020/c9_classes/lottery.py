from random import choice

lottery_characters = [1, 2, 3, 4, 5, 6, 7, 8, 9,
    'a', 'b', 'c', 'd', 'e']

winning_ticket = []

for value in range(1, 5):
    char = choice(lottery_characters)
    winning_ticket.append(char)

print(f"Any ticket matching these four numbers or letters wins!")
print(winning_ticket)

your_ticket = []

for value in range(1, 5):
    char = choice(lottery_characters)
    your_ticket.append(char)

print(f"\nYour ticket:")
print(your_ticket)

if your_ticket == winning_ticket:
    print("\nYOU WON!!!")
else:
    print("\nBetter luck next time!")