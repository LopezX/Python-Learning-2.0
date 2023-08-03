# Pers
#   Make several dictionaries, where each dictionary represents a different pet.
#   In each dictionary, include the kind of pet and the owner's name. Store in a
#   list called pets. Loop through your list and print everything you know about
#   the pets.
pet_0 = {
    'type':'dog',
    'name':'milo',
    'owner':{
        'first':'mary',
        'last':'ann'
    },
}

pet_1 = {
    'type':'cat',
    'name':'susie',
    'owner':{
        'first':'mike',
        'last':'johnston'
    },
}

pet_2 = {
    'type':'hamster',
    'name':'mr. squeaks',
    'owner':{
        'first':'luisa',
        'last':'martinez'
    },
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    owner = pet['owner']
    owner_full_name = f"{owner['first']} {owner['last']}"
    
    print(f"\nThis is {owner_full_name.title()}'s pet.")
    print(f"Their name is {pet['name'].title()}. They are a {pet['type']}.")
