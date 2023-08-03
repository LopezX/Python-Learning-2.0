# People
#   Starting with the program in 6-1.py, make two new dictionaries representing 
#   different people, and store all three in a list called 'people'. Loop 
#   through the list, printing everything you know about the people
person_0 = {
    'first_name':'Dylan',
    'last_name':'Bogard',
    'age':20,
    'relationship':'best friend',
    'hair_color':'blonde',
}

person_1 = {
    'first_name':'Nathan',
    'last_name':'Lopez',
    'age':18,
    'relationship':'brother',
    'hair_color':'dark brown',
}

person_2 = {
    'first_name':'Evelyn',
    'last_name':'Pan',
    'age':20,
    'relationship':'college friend',
    'hair_color':'black',
}

people = [person_0, person_1, person_2]

for person in people:
    print(f"\nI know of a person named {person['first_name']} {person['last_name']}.")
    print(f"They are my {person['relationship']}.")
    print(f"They are {person['age']} years old and have {person['hair_color']} hair.")
