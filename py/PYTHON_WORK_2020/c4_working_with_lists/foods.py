my_foods = ['pizza', 'falafel', 'carrot cake']

# To create a copy of a list, use splices!
# If you ommit the splice ([:]), both variables (my_foods and friend_foods)
# will point to the same list, which can cause logic errors.
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)