print("Give me two numbers, and I'll divide them.")
print("(enter 'q' to quit.)")

while True:
    # Ask for two numbers.
    dividend = input("\nFirst number: ")
    if dividend == 'q':
        break
    divisor = input("Second number: ")
    if divisor == 'q':
        break

    # Divide the two numbers (if possible).
    try:
        quotient = float(dividend)/float(divisor)
    except ValueError:
        print("You can't divide those! Please enter numbers!")
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(f"Answer: {quotient}")