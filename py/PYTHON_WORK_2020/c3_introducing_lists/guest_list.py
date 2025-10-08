guests = ['steve jobs', 'bill gates', 'jeff bezos']

print(f"Please welcome our first guest, {guests[0].title()}, one of the founders of Apple Inc.!")
print(f"Please welcome our second guest, {guests[1].title()}, one of the founders of Microsoft!")
print(f"Please welcome our third guest, {guests[2].title()}, founder and CEO of Amazon!")

print(f"\nUnforunately, {guests[0].title()} couldn't make it because he's dead.")
guests[0] = 'steve wozniak'
print(f"So, please welcome his replacement guest and fellow co-founder of Apple: {guests[0].title()}!")

print("\nGreat news: we have received a bigger dinner table and can invite more guests!")
guests.insert(0, 'mark zuckerberg')
guests.insert(3, 'paul allen')
guests.append('larry page')
print(f"Please welcome {guests[0].title()}, {guests[3].title()}, and {guests[-1].title()}!")

print("\nUnforunately, our new table will not arrive in time for the dinner, and we only have room for two guests now.")
removed_guest1 = guests.pop()
print(f"Sorry, {removed_guest1.title()}!")
removed_guest2 = guests.pop()
print(f"Sorry, {removed_guest2.title()}!")
removed_guest3 = guests.pop()
print(f"Sorry, {removed_guest3.title()}!")
removed_guest4 = guests.pop()
print(f"Sorry, {removed_guest4.title()}!")

print(f"\nCongratulations to our {len(guests)} remaining guests: {guests[0].title()} and {guests[1].title()}!")

del guests[1]
del guests[0]
print(guests)