# Favorite Places
#   Make a dictionary called 'favorite places'. Think of at least 3 places and 
#   store one to three for each person. Print each person's favorite places in 
#   an ordered fashion.
favorite_places = {
    'xavier':[
        'hawaii',
        'texas',
        'colorado',
    ],
    'angie':[
        'hawaii',
        'colorado',
        'kansas',
    ],
    'alexander':[
        'south korea',
        'dubai',
        'california',
    ],
    'nathan':[
        'hawaii',
        'texas',
        'kansas'
    ]
}

for person, favorite_place in favorite_places.items():
    print(f"\n{person.title()}'s favorite places are:")
    for place in favorite_place:
        print(f"\t{place.title()}")
