"""
While a single asterisk tells Python to create an empty tuple,
double asterisks tell Python to create an empty dictionary.
They allow the function to accept an arbitrary number of keyword arguments.
"""

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info