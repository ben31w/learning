from die import Die

d1 = Die()
print("Rolling a six-sided die ten times:")
for value in range(1, 11):
    print(d1.roll())

d2 = Die(10)
print("\nRolling a ten-sided die ten times:")
for value in range(1, 11):
    print(d2.roll())

d3 = Die(20)
print("\nRolling a twenty-sided die ten times:")
for value in range(1, 11):
    print(d3.roll())