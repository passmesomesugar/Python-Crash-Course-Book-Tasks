# 9-15. Lottery Analysis: You can use a loop to see how hard it might be to win
# the kind of lottery you just modeled. Make a list or tuple called my_ticket.
# Write a loop that keeps pulling numbers until your ticket wins. Print a message
# reporting how many times the loop had to run to give you a winning ticket.
import random

numbers = ['11', '22', '33', '44', '55', '66', '77', '88', '99', '00']
letters = ['a', 'b', 'x', 'y']
my_ticket = 'y55'
counter = 0
win_ticket = ''


def generate_ticket():
    random_number = numbers[random.randint(0, len(numbers) - 1)]
    random_letter = letters[random.randint(0, len(letters) - 1)]
    return random_letter + random_number


while True:
    win_ticket = generate_ticket()
    print(f"Currently win ticket is: {win_ticket}")
    counter += 1
    if win_ticket == my_ticket:
        print(f"It took {counter} attempts")
        break
