# Checking Usernames
#   Create a program that simulates how websites ensure that everyone has a 
#   unique username. Have a list of usernames labeled 'current_users', and 
#   another list labeled 'new_users' that contains more usernames, with 1 or 2 
#   being from current_users. Loop through the new_users list to see if the 
#   username has been used (make sure the comparison is case insensitive). If it
#   is the case, print a message telling the user to create a new username; 
#   else, print that the username is available.
current_users = ['Jaden', 'Katie', 'Marie', 'admin', 'Josh', 'Aaron', 
                     'Tyler']
new_users = ['Kyle', 'ADMIN', 'Joshua', 'aaron', 'maddie']

current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower())

for user in new_users:
    if user.lower() in current_users_lower:
        print("This username is already in use, please create a new one.")
    else:
        print("This username is available.")
