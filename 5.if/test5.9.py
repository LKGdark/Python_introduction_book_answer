names=['111','admin']
if names:
    for name in names:
        if name == 'admin':
            print(f"Hello {name},would you like to see a status report?\n")
        else:
            print(f"Hello {name},thank you for logging in again.\n")
else :
    print("No body!\n")