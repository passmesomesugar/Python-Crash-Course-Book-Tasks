# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 10:07:45 2020

@author: passmesomesugar~git
"""
# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name of each pizza.

pizzas = ['Margherita', 'Marinara', 'Quattro Stagioni']
for pizza in pizzas:
    print(pizza.title())
print('\n')
# Modify your for loop to print a sentence using the name of the pizza
# instead of printing just the name of the pizza. For each pizza you should
# have one line of output containing a simple statement like I like pepperoni
# pizza.

for pizza in pizzas:
    print("Popular choice: " + pizza.title())
    
#     Add a line at the end of your program, outside the for loop, that states
# how much you like pizza. The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence, such as
# I really love pizza!
print('\n')    
print("I like pizza a lot")
print("I really can't remember the last time I've ate one")
print("But I really love pizza")    
    