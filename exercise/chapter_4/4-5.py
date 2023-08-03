# Summing a Million
#   Make a list of numbers from one to one million. Use min() and max() to make
#   sure the list actually starts at one and ends at one million. Then use 
#   sum() to add all the numbers up.
values = list(range(1,1000001))

print(f"The minimum value in the list is {min(values)}.")
print(f"The maximum value in the list is {max(values)}.")
print(f"The sum of the values in the list is {sum(values)}.")