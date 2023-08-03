cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

# sort cars in order (least to greatest)
# cars.sort()
# print(cars)

# sort cars in reverse order (greatest to least)
# cars.sort(reverse=True)
# print(cars)

# TEMPORARILY sort a list
# print("Here is the original list:")
# print(cars)

# print("Here is the sorted list:")
# print(sorted(cars))

# print("Here is the original list again:")
# print(cars)

# printing the reverse order of the list
# cars.reverse()
# print(cars)

# Using an if-statement
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
