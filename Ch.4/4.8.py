# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 12:19:25 2020

@author: passmesomesugar~git
"""

# 4-8. Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.
list_of_cubes = []
for value in range(1, 10):
    value_to_append = value ** 3;
    print(value_to_append)
    list_of_cubes.append(value_to_append)
print(list_of_cubes)
