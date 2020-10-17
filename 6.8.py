# 6-8. Pets: Make several dictionaries, where each dictionary represents a different
# pet. In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets. Next, loop through your list and as
# you do, print everything you know about each pet.

pet_1 = {'name': 'Charley', 'breed': 'pug', 'size': 'small', 'tail': 'short', 'owner': 'Jackie'}
pet_2 = {'name': 'Louie', 'breed': 'frug', 'size': 'small', 'tail': 'short', 'owner': 'Hu Jintao'}
pet_3 = {'name': 'Frankie', 'breed': 'smug', 'size': 'small', 'tail': 'short', 'owner': 'Maggy'}
pet_4 = {'name': 'Vincent', 'breed': 'pepe', 'size': 'small', 'tail': 'short', 'owner': 'Shaggy'}

pets_list = (pet_1, pet_2, pet_3, pet_4)

for pet in pets_list:
    print(pet)
