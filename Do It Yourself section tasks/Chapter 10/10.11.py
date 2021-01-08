# 10-11. Favorite Number: Write a program that prompts for the user’s favorite
# number. Use json.dump() to store this number in a file. Write a separate program
# that reads in this value and prints the message, “I know your favorite
# number! It’s _____.”
import json

favorite_number = input("What is your favorite number?\n")
filename = 'user_favorite_number.json'
with open(filename, 'w') as file:
    json.dump(favorite_number, file)

try:
    with open(filename) as file:
        favorite_number = json.load(file)
        print(f"I know your favorite number is {favorite_number}")
except FileNotFoundError:
    pass
