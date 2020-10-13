# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 16:37:56 2020

@author: passmesomesugar~git
"""

# 3-10. Every Function: Think of something you could store in a list. For example,
# you could make a list of mountains, rivers, countries, cities, languages, or anything
# else you’d like. Write a program that creates a list containing these items
# and then uses each function introduced in this chapter at least once.

list_of_mountains = ["K-2", "Chogori", "Jamalungma", "Broad Peak", "Gasherbrum-2", "Kanchenjanga", "Manaslu"]
print(len(list_of_mountains))
list_of_mountains.reverse()
print(list_of_mountains)
print(sorted(list_of_mountains))
list_of_mountains.sort(reverse=True)
print(list_of_mountains)
