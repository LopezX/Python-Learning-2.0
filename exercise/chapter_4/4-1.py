# Pizzas
#   Make a list of your favorite pizzas. Print the list using a for loop. Add
#   each pizza you like to a sentence and use a for loop to print it out. At 
#   the end, print a statement about how much you like pizza.
favorite_pizzas = ['pepperoni', 'meat supreme', 'cheese', 'chicken alfredo', 'steak']

for pizza in favorite_pizzas:
    print(f"{pizza.title()}")
    
print("")

for pizza in favorite_pizzas:
    print (f"I like to eat {pizza.title()} pizza.")

print("I like to eat pizza every now and then.")