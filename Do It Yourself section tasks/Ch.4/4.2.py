# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 11:42:25 2020

@author: passmesomesugar~git
"""
# Animals: Think of at least three different animals that have a common characteristic.
# Store the names of these animals in a list, and then use a for loop to
# print out the name of each animal.

animals = ['Tiger', 'Lepard', 'Cat']
for animal in animals:
    print(animal.title())
print('\n')

# • Modify your program to print a statement about each animal, such as
# A dog would make a great pet.
for animal in animals:
    print(animal.title() + " would make a great pet.")
print('\n')

# • Add a line at the end of your program stating what these animals have in
# common. You could print a sentence such as Any of these animals would
# make a great pet!
for animal in animals:
    print(animal.title() + " would make a great pet.")
    print("All these animals meow")
print('\n')
