print("Give me two numbers, and I'll subtract them.")
print("(enter 'q' to quit.)")

while True:
    # Ask for two numbers.
    minuend = input("\nFirst number: ")
    if minuend == 'q':
        break
    subtrahend = input("Second number: ")
    if subtrahend == 'q':
        break

    # Add the two numbers (if possible).
    try:
        answer = float(minuend) - float(subtrahend)
    except ValueError:
        print("You can't subtract those! Please enter numbers!")
    else:
        print(f"Answer: {answer}")