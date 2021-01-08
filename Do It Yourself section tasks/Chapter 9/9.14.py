# 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and
# five letters. Randomly select four numbers or letters from the list and print a
# message saying that any ticket matching these four numbers or letters wins a
# prize.
import random

numbers = ['11', '22', '33', '44', '55', '66', '77', '88', '99', '00']
letters = ['a', 'b', 'x', 'y']
random_number = numbers[random.randint(0, len(numbers))]
random_letter = letters[random.randint(0, len(letters))]
prize_number = random_letter + random_number
print(f"Price goes to {prize_number}")
