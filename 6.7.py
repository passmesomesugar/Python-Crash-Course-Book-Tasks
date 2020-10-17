# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 99).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.

person_one = {'name': 'Wim', 'surname': 'Hof', 'nickname': 'Ice Man', 'place of birth': 'Sittard'}
person_two = {'name': 'Dennis', 'surname': 'Ritchie', 'nickname': '', 'place of birth': 'New York'}
person_three = {'name': 'Bjarne ', 'surname': 'Stroustrup', 'nickname': '', 'place of birth': 'Aarhus'}
people = (person_one, person_two, person_three)
for person in people:
    print(person)
