# 9-13. Dice: Make a class Die with one attribute called sides, which has a default
# value of 6. Write a method called roll_die() that prints a random number
# between 1 and the number of sides the die has. Make a 6-sided die and roll it
# 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.
import random


class Die:
    sides = 6

    def roll_die(self):
        print(random.randint(1, 6))


die = Die()
i = 0
while i < 10:
    die.roll_die()
    i += 1
