# Buffet
#   Make a tuple of five basic foods that would be served at a buffet. Print 
#   the tuple using a for loop, then try to modify one of them to make sure
#   that Python rejects the modification. Then, rewrite the tuple with two 
#   items being replaced, and use a for loop to print the new list
buffet_foods = ('spaghetti', 'burgers', 'hot dogs', 'mac and cheese', 'steak fries')

print("The restaurant's buffet has:")
for food in buffet_foods:
    print(food)

# Did not allow for this line to be executed:
# buffet_foods[0] = 'corn dogs'

buffet_foods = ('fried fish', 'burgers', 'steak', 'mac and cheese', 'steak fries')
print("\nThe restaurant changed their buffet menu, now its:")
for food in buffet_foods:
    print(food)
