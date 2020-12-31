# 10-12. Favorite Number Remembered: Combine the two programs from
# Exercise 10-11 into one file. If the number is already stored, report the favorite
# number to the user. If not, prompt for the user’s favorite number and store it in a
# file. Run the program twice to see that it works.
import json


def get_stored_favorite_number():
    filename = 'user_favorite_number.json'
    try:
        with open(filename) as file:
            stored_favorite_number = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return stored_favorite_number


def get_favorite_number_from_user():
    favorite_number = get_stored_favorite_number()
    if favorite_number:
        print(f"I know your favorite number is {favorite_number}")
    else:
        favorite_number = input("What is your favorite number?\n")
        filename = 'user_favorite_number.json'
        with open(filename, 'w') as file:
            json.dump(favorite_number, file)


get_favorite_number_from_user()
