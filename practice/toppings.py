available_toppins = ['mushrooms', 'olives', 'green peppers', 'pepperoni',
                     'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries','extra cheese']

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppins:
            print(f"Adding {requested_topping}.")
        else:
            print(f"Sorry, we don't have {requested_topping}.")
        
print("Finished making your pizza!")
