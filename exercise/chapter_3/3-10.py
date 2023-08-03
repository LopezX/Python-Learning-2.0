# Every function
#   Make a list of something (city names, mountains, languages, etc.) and use
#   all of the list functions that you've learned so far
countries = ['united states of america', 'mexico', 'japan', 'china', 'russia',
             'france', 'spain', 'italy', 'united kingdom', 'switzerland',
             'netherland', 'finland', 'brazil', 'colombia', 'cuba', 'peru',
             'dominican republic', 'thailand', 'australia', 'portugal', 
             'ireland', 'greenland', 'canada', 'chile', 'iraq', 'iran', 
             'syria', 'afghanistan', 'turkey', 'egypt', 'south africa']

print("Here is a list of countries that I could think of:")
print(countries)

print(f"\nI could remember, off the top of my head, {len(countries)} countries.")
print(f"The first country I thought of was {countries[1].title()}.")
print(f"The last country I thought of was {countries[-1].title()}.")

print("\nHere is the list temporarily sorted:")
print(sorted(countries))
print("Here is the list in it original state:")
print(countries)

print("\nHere is the list in reverse order:")
countries.reverse()
print(countries)
print("Let's change it back to it's original list:")
countries.reverse()
print(countries)

print("\nLet's sort the countries permanately:")
countries.sort()
print(countries)
print("Here is the list in reverse order:")
countries.sort(reverse=True)
print(countries)
print("From now on, the list will be sorted in alphabetical order.")
countries.sort(reverse=False)

print("\nLet's remove some countries off the list:")
print(f"The first one removed from the end of the list is {countries.pop().title()}.")
print(f"The first one removed from the front of the list is {countries.pop(0).title()}.")
print(f"The second one removed from the end of the list is {countries.pop().title()}.")
print(f"The second one removed from the front of the list is {countries.pop(0)}.")
print("The list is now:")
print(countries)

print("\nLet's delete the list")
del countries[26]
del countries[25]
del countries[24]
del countries[23]
del countries[22]
del countries[21]
del countries[20]
del countries[19]
del countries[18]
del countries[17]
del countries[16]
del countries[15]
del countries[14]
del countries[13]
del countries[12]
del countries[11]
del countries[10]
del countries[9]
del countries[8]
del countries[7]
del countries[6]
del countries[5]
del countries[4]
del countries[3]
del countries[2]
del countries[1]
del countries[0]
print("The list is now empty:")
print(countries)
