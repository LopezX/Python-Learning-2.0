# More Conditional Tests
#   Using 5-1, create more conditional tests for each of the following:
#       - Tests for equality and inequality with strings
#       - Tests using the lower method:
#       - numerical tests for equality, inequality, etc.
#       - test using the "and" and "or" word
#       - Test whether an item \nIs on a list
#       - Test whether an item \nIs not on a list
ford_car = 'Mustang'
toyota_car = 'Camry'

print("Is ford_car == 'Mustang'? I predict it's True.")
print(ford_car == 'Mustang')

print("Is ford_car == 'Camry'? I predict it's False.")
print(ford_car == 'Camry')


print("\nIs ford_car != 'Mustang'? I predict it's False.")
print(ford_car != 'Mustang')

print("Is ford_car != 'Camry'? I predict it's True.")
print(ford_car != 'Camry')


print("\nIs ford_car == 'mustang'? I predict it's False.")
print(ford_car == 'mustang')

print("Is ford_car.lower() == 'mustang'? I predict it's True.")
print(ford_car.lower() == 'mustang')


print("\nIs ford_car == 'MUSTANG'? I predict it's False.")
print(ford_car == 'MUSTANG')

print("Is ford_car.upper() == 'MUSTANG'? I predict it's True.")
print(ford_car.upper() == 'MUSTANG')


print("\nIs ford_car == 'mustang'? I predict it's False.")
print(ford_car == 'mustang')

print("Is ford_car.lower() == 'mustang'? I predict it's True.")
print(ford_car.lower() == 'mustang')



ford_cars = ['Bronco', 'Edge', 'Mustang', 'Expedition', 'Ranger', 'F-150']
toyota_cars = ['4Runner', 'Camry', 'Crown', 'GR86', 'Sienna', 'Tundra', 
               'Avalon']

print("\nIs ford_car in ford_cars? I predict it's True.")
print(ford_car in ford_cars)

print("Is ford_car in toyota_cars? I predict it's False.")
print(ford_car in toyota_cars)

print("Is ford_car not in ford_cars? I predict it's False.")
print(ford_car not in ford_cars)

print("Is ford_car not in toyota_cars? I predict it's True.")
print(ford_car not in toyota_cars)



print("\nIs ford_car in ford_cars and toyota_car in ford_cars? I predict it's " 
      "False.")
print(ford_car in ford_cars and toyota_car in ford_cars)

print("Is ford_car in toyota_cars and toyota_car in toyota_cars? I predict "
      "it's False.")
print(ford_car in toyota_cars and toyota_car in toyota_cars)

print("Is ford_car not in ford_cars and toyota_car not in ford_cars? I "
      "predict it's False.")
print(ford_car not in ford_cars and toyota_car not in ford_cars)

print("Is ford_car not in toyota_cars and toyota_car not in toyota_cars? I "
      "predict it's False.")
print(ford_car not in toyota_cars and toyota_car not in toyota_cars)



print("\nIs ford_car in ford_cars or toyota_car in ford_cars? I predict it's " 
      "True.")
print(ford_car in ford_cars or toyota_car in ford_cars)

print("Is ford_car in toyota_cars or toyota_car in toyota_cars? I predict "
      "it's True.")
print(ford_car in toyota_cars or toyota_car in toyota_cars)

print("Is ford_car not in ford_cars or toyota_car not in ford_cars? I "
      "predict it's True.")
print(ford_car not in ford_cars or toyota_car not in ford_cars)

print("Is ford_car not in toyota_cars or toyota_car not in toyota_cars? I "
      "predict it's True.")
print(ford_car not in toyota_cars or toyota_car not in toyota_cars)