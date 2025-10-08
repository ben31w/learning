print("Give me two numbers, and I'll add them.")
print("(enter 'q' to quit.)")

while True:
    # Ask for two numbers.
    addend_1 = input("\nFirst number: ")
    if addend_1 == 'q':
        break
    addend_2 = input("Second number: ")
    if addend_2 == 'q':
        break

    # Add the two numbers (if possible).
    try:
        answer = float(addend_1) + float(addend_2)
    except ValueError:
        print("You can't add those! Please enter numbers!")
    else:
        print(f"Answer: {answer}")