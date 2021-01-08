# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 12:03:21 2020

@author: passmesomesugar~git
"""
# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers.
list_for_million=[]
for value in range(1,1000000):
    list_for_million.append(value)    

print("Max value is ", max(list_for_million))    
print("Min value is ", min(list_for_million))   
print(sum(list_for_million))
