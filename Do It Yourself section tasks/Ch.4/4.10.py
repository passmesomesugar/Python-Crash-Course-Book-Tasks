# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 11:53:27 2020

@author: passmesomesugar~git
"""
# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
import math

list_for_ninety_nine = []
for value in range(1, 100):
    list_for_ninety_nine.append(value)

# • Print the message The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
print(list_for_ninety_nine[:3])
print('\n')

# • Print the message Three items from the middle of the list are:. Use a slice to
# print three items from the middle of the list.
print("Three items from the middle of the list are:")
print(list_for_ninety_nine[48:51])
print('\n')

# • Print the message The last three items in the list are:. Use a slice to print the
# last three items in the list.
print("The last three items in the list are:")
print(list_for_ninety_nine[-3:])
