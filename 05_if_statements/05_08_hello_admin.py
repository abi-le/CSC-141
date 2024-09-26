usernames = ['admin', 'snail', 'lalala', 'bolt']

for name in usernames:
    if name == 'admin':
        print("Hello Admin, would you like to see a status report? ")
    else:
        print(f"Hello {name.title()} thank you for logging in.")