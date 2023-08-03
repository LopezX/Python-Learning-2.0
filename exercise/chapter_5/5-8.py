# Hello Admin
#   Make a list of 5 or more usernames, including the name 'admin'. Loop through
#   the list, and print a greeting to each user. If the user is 'admin', print a
#   special greeting; else, print a generic greeting to the user.
usernames = ['Jaden', 'Katie', 'Marie', 'admin', 'Josh', 'Aaron', 'Tyler']

for username in usernames:
    if username == 'admin':
        print(f"Greetings, {username}. What would you like to view today?")
    else:
        print(f"Hello {username}, thanks for logging in.")
