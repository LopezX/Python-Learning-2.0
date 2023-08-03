# Cube Comprehension
#   Make a list of the first ten cubes using list comprehension and use a for
# loop to print them
cubes = list(value**3 for value in range(1, 11))

for cube in cubes:
    print(cube)