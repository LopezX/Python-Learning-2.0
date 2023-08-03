# No Users
#   Adding to 5-9, make a safe check to ensure the list is not empty. If the 
#   list is empty, then print a message.
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Greetings, {username}. What would you like to view today?")
        else:
            print(f"Hello {username}, thanks for logging in.")
else:
    print("We need to find some users!")
