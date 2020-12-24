# 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and
# five letters. Randomly select four numbers or letters from the list and print a
# message saying that any ticket matching these four numbers or letters wins a
# prize.
import random

numbers = ['1', '2', '565', '56', '79', '41', '69', '151', '1', '3']
letters = ['a', 'b', 'z', 'm']
random_number = numbers[random.randint(0, len(numbers))]
random_letter = letters[random.randint(0, len(letters))]
prize_number = random_letter + random_number
print(f"Price goes to {prize_number}")
