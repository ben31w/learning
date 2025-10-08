from random import choice

lottery_characters = [1, 2, 3, 4, 5, 6, 7, 8, 9,
    'a', 'b', 'c', 'd', 'e']
# Stores the number of times it takes to pull a winning ticket.
count = 0

# Create a winning ticket.
winning_ticket = []

for value in range(1, 5):
    char = choice(lottery_characters)
    winning_ticket.append(char)

print(f"Any ticket matching these four numbers or letters wins!")
print(winning_ticket)
print()

# Keep generating random tickets until one matches.
your_ticket = []

while your_ticket != winning_ticket:
    your_ticket = [choice(lottery_characters), choice(lottery_characters),
        choice(lottery_characters), choice(lottery_characters)]
    count += 1
    print(f"{count}: {your_ticket}")

print(f"It took you {count} tries to win.")