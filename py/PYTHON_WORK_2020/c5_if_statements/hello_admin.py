users = ['admin', 'ben', 'kyle', 'brian', 'nathan', 'stuart']

if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would like to see if a status report?")
        else:
            print(f"Hello {user}, thank you for logging in.")
else:
    print("We need to find some users!")