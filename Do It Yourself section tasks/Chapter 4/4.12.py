# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 13:38:21 2020

@author: passmesomesugar~git
"""
# 4-12. More Loops: All versions of foods.py in this section have avoided using
# for loops when printing to save space. Choose a version of foods.py, and
# write two for loops to print each list of foods.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My foods list:")
for food in my_foods:
    print(food)
print('\n')
print("Friends foods list:")
for food in friend_foods:
    print(food)
print('\n')
