# Slices
#   Using a program you made before (in this case, 4-9), for each slice print a
#   message saying what the slice is, followed by the slice. The slices are:
#       - the first three items
#       - the middle of the list
#       - the last three items
cubes = list(value**3 for value in range(1,11))

print(f"The first three items in the list are: {cubes[:3]}.")
print(f"The items from the middle of the list are: {cubes[4:6]}")
print(f"The last three items in the list are: {cubes[7:]}")
