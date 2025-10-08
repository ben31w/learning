print("Give me two numbers, and I'll multiply them.")
print("(enter 'q' to quit.)")

while True:
    # Ask for two numbers.
    factor_1 = input("\nFirst number: ")
    if factor_1 == 'q':
        break
    factor_2 = input("Second number: ")
    if factor_2 == 'q':
        break

    # Add the two numbers (if possible).
    try:
        answer = float(factor_1) * float(factor_2)
    except ValueError:
        print("You can't multiply those! Please enter numbers!")
    else:
        print(f"Answer: {answer}")