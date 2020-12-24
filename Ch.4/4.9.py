# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 12:22:15 2020

@author: passmesomesugar~git
"""
# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the
# first 10 cubes.
list_of_cubes = [value ** 3 for value in range(1, 10)]
for value in list_of_cubes:
    print(value)
