magicians = ['alice', 'david', 'carolina']

# For loop tells Python to pull a name from the list magicians, and associate it
# with the variable magician
for magician in magicians:
    print(magician)
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't want to see your next trick, {magician.title()}.\n")

print("Thank you everyone. That was a great magic show!")