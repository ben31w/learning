"""
A simple function for counting the number of times the string 'the' appears in a 
file. NOTE: It does not count the number of instances of the word 'the'. It
simply counts anytime 'the' (upper or lowercase) appears in a file (whether it
be in the word 'there', 'then', 'bathe', etc.) 
"""

def count_the(filename):
    """Counts every instance of 'the' in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(contents.lower().count('the'))