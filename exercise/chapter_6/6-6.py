# Polling
#   Make a list of people who should take the favorite languages poll. Include 
#   some names that are already in the dictionary and some that aren't. Loop 
#   through the list, and if they've already taken the poll, print a message 
#   thanking them for responding. Else, invite them to respond.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

favorite_languages_next_poll = [
    'daryl',
    'sarah',
    'bobby',
    'evelyn',
    'alex',
    'edward',
    'ethan',
    'joshua',
]

for name in favorite_languages_next_poll:
    if name in favorite_languages.keys():
        print(f"Thank you for taking the poll earlier today, {name.title()}.")
    else:
        print(f"{name.title()}, I would like to invite you to take this poll about your favorite programming language.")
