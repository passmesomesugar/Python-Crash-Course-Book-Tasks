# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 13:25:26 2020

@author: passmesomesugar~git
"""
# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:


My_favorite_pizzas = ['Margherita', 'Marinara', 'Quattro Stagioni']
friend_pizzas = My_favorite_pizzas[:]
print(friend_pizzas)

# • Add a new pizza to the original list.
My_favorite_pizzas.append('new pizza for pizzas - SundaySpecial')

# • Add a different pizza to the list friend_pizzas.
friend_pizzas.append('Some New Pizza')

# • Prove that you have two separate lists. Print the message My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message
# My friend’s favorite pizzas are:, and then use a for loop to print the second
# list. Make sure each new pizza is stored in the appropriate list.
print("My favorite pizzas are: ")
for pizza in My_favorite_pizzas:
    print(pizza)
print('\n')
print("My friend’s favorite pizzas are:")
for friends_pizza in friend_pizzas:
    print(friends_pizza)
