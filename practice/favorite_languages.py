# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorit language is {language.title()}.")

# print()
# for name in favorite_languages.keys():
#     print(name.title())

# for name in sorted(favorite_languages.keys()):
#     print(f"Greetings, {name.title()}.")

# print("Languages mentioned:")
# for language in set(favorite_languages.values()):
#     print(language.title())

favorite_languages = {
    'jen':['python', 'ruby'],
    'sarah':['c'],
    'edward':['ruby', 'go'],
    'phil':['python', 'haskell']
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
