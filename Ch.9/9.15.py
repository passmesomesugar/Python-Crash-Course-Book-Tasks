# 9-15. Lottery Analysis: You can use a loop to see how hard it might be to win
# the kind of lottery you just modeled. Make a list or tuple called my_ticket.
# Write a loop that keeps pulling numbers until your ticket wins. Print a message
# reporting how many times the loop had to run to give you a winning ticket.
import random

numbers = ['1', '2', '565', '56', '79', '41', '69', '151', '1', '3']
letters = ['a', 'b', 'z', 'm']
my_prize_number = 'a56'
random_number = numbers[random.randint(0, len(numbers))]
random_letter = letters[random.randint(0, len(letters))]


def roll():
    prize_number = random_letter + random_number
    return prize_number


while my_prize_number != prize_number:
    prize_number = random_letter + random_number
    print("Current prize number is:")
    print(prize_number)
else:
    print("You finally won")
