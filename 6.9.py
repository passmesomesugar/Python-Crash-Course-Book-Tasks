# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
# names to use as keys in the dictionary, and store one to three favorite places
# for each person. To make this exercise a bit more interesting, ask some friends
# to name a few of their favorite places. Loop through the dictionary, and print
# each person’s name and their favorite places.
favorite_places = {'Sally': {'first': 'Montana', 'second': 'Pasadena',
                             'third': 'Chicago'},
                   'Samir': {'first': 'Beijing', 'second': 'Moscow',
                             'third': 'Warsaw'},
                   'Saurong': {'first': 'Shire', 'second': 'Mordor',
                               'third': 'Starbucks'}
                   }
for person, favorite_place in favorite_places.items():
    print(f"{person} favourite places:")
    for number, place in favorite_place.items():
        print(f"{number} is {place}")
