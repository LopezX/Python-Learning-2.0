# Ordinal Numbers
#   Ordinal numbers indicate a position on a list, such as 1st or 2nd. Make a 
#   program that stores the numbers 1 though 9, then loops through the list and 
#   uses an if-elif-else chain to print the proper ordinal number on their own 
#   lines
ordinal_numbers = list(range(1, 10))

for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print (f"{ordinal_number}st")
    elif ordinal_number == 2:
        print(f"{ordinal_number}nd")
    elif ordinal_number == 3:
        print(f"{ordinal_number}rd")
    else:
        print(f"{ordinal_number}th")