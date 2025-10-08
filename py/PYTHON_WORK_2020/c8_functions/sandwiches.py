""""
The asterisk tells Python to make an empty tuple called ingredients and 
fill it with whatever arguments the function receives when called 
(can be any number of arguments).
""" 
def make_sandwich(*ingredients):
    """Summarize the sandwich we are about to make."""
    if ingredients:
        print("\nMaking a sandwich with the following ingredients:")
        for ingredient in ingredients:
            print(f"- {ingredient}")
    else:
        print("\nMaking a sandwich.")