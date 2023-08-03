# Favorite Numbers
#   # Favorite Number
#   Use a dictionary to store people's favorite numbers. Print each person's 
#   name and their favorite number.
favorite_numbers = {
    'jason':[13, 8, 27],
    'rachel':[1, 99, 0],
    'tom':[23, 15],
    'nate':[7],
    'daniel':[60, 88],
}

for person, numbers in favorite_numbers.items():
    print(f"\n{person.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")
