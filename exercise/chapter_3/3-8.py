# Seeing the World
#   Make of list of at least 5 places you would like to visit. Store those 
#   locations in the list (not in alphabetical order), and print it. Sort the 
#   list temporarily and print it, then print the original list. Print the list
#   in reversed order, and then change it back to its original order. Sort the
#   list in alphabetical order permanately, then print it, then sort in reverse
#   alphabetical order and print the list again.
places_of_interest = ['japan', 'dubai', 'europe', 'mexico', 'hong kong', 'taiwan']

print("Here is the original list:")
print(places_of_interest)

print("\nHere is the list sorted:")
print(sorted(places_of_interest))
print("Here is the original list once again:")
print(places_of_interest)

places_of_interest.reverse()
print("\nHere is the list in reverse order:")
print(places_of_interest)
places_of_interest.reverse()
print("Here is the original list once again:")
print(places_of_interest)

places_of_interest.sort()
print("\nHere is the list sorted:")
print(places_of_interest)
places_of_interest.sort(reverse=True)
print("Here is the list sorted in reverse:")
print(places_of_interest)
