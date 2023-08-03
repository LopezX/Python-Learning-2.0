# My Pizzas, Your Pizzas
#   Using the program from 4-1, make a copy of your pizza list and call it
#   "friend_pizzas". Then, add a new pizza to the original list and new list,
#   and print each list to prove that you have separate lists
favorite_pizzas = ['pepperoni', 'meat supreme', 'cheese', 'chicken alfredo', 'steak']
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append('Barbeque')
friend_pizzas.append('mushroom')

print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print(pizza)
    
print()

print("My friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)
    