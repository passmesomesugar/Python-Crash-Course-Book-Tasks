# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99)
# so each person can have more than one favorite number. Then print each person’s
# name along with their favorite numbers.

favourite_number_dictionary = {'Michael The Jordan': (13, 1223, 23, 12, 312, 3),
                               'John The Builder': (121, 4545, 5445),
                               'Mickey Mouse': (121, 45445, 5445),
                               'Micky in DaHouse': (13, 14, 15)}
for person, numbers in favourite_number_dictionary.items():
    print(person, "favourite numbers are:")
    print(numbers)
