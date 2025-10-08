import json

filename = 'username.json'

try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    pass
else:
    print(f"Welcome back, {username}!")