# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 13:48:26 2020

@author: passmesomesugar~git
"""
# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
Foods_for_Buffet = ('Cold Drinks','Hot drinks','First meal','Second meal','Desert')
# Foods_for_Buffet = ['Cold Drinks','Hot drinks','First meal','Second meal','Desert']
# • Use a for loop to print each food the restaurant offers.
for food in Foods_for_Buffet:
    print(food)
print('\n')
# • Try to modify one of the items, and make sure that Python rejects the
# change.
    # Foods_for_Buffet[2]= "New Value"
# • The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to print
# each of the items on the revised menu.
Foods_for_Buffet = ('Cold Drinks','Hot drinks','Cakes','Business lunch','Desert')
for food in Foods_for_Buffet:
    print(food)

