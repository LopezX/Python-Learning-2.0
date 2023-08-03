# Rivers
#   Make a dictionary containg three major rivers and the country each river 
#   runs through. Use a loop to print a sentence, use a loop to print the name 
#   of each river, and use a loop to print the name of each country
rivers = {
    'nile':'egypt',
    'mississippi':'united states',
    'amazon':'brazil',
    'yangtze':'china',
    'ganges':'india',
}

for country, river in rivers.items():
    print(f"The {river.title()} river flows through {country.title()}.")
    
print("\nRivers of the world:")
for river in rivers.keys():
    print(river.title())
    
print("\nCountries that have rivers:")
for country in rivers.values():
    print(country.title())
