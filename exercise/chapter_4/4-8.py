# Cubes
#   Make a list of the first ten cubes and use a for loop to print them
cubes = []

for value in range(1,11):
    cube = value**3
    cubes.append(cube)

for cube in cubes:
    print(cube)
    