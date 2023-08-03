#squares = []

# First attempt
# for value in range(1,11):
#     square = value**2
#     squares.append(square)

# Second attempt
# for value in range(1,11):
#     squares.append(value**2)

# Third attempt
squares = [value**2 for value in range(1, 11)]
print(squares)
