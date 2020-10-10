# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 16:18:49 2020

@author: passmesomesugar~git
"""

# 3-8. Seeing the World: Think of at least five places in the world you’d like to
# visit.


# • Store the locations in a list. Make sure the list is not in alphabetical order.
list = ["Akihabara", "Zanzibar" ,"New York", "Los Angeles","Neverland", "Nevermoreland", "Azeroth" ]

# • Print your list in its original order. Don’t worry about printing the list neatly,
# just print it as a raw Python list.
print("Original order:")
print(list)
print("\n")

# • Use sorted() to print your list in alphabetical order without modifying the
# actual list.
print("Sorted order:")
print(sorted(list))
print("\n")

# • Show that your list is still in its original order by printing it.
print("Original order:")
print(list)
print("\n")

# • Use sorted() to print your list in reverse alphabetical order without changing
# the order of the original list.
print("Reverse alphabetical order")
print(sorted(list,reverse=True))
print("\n")

# • Show that your list is still in its original order by printing it again.
print("Original order:")
print(list)
print("\n")

# • Use reverse() to change the order of your list. Print the list to show that its
# order has changed.
print("reverse() used:")
list.reverse()
print(list)
print("\n")

# • Use reverse() to change the order of your list again. Print the list to show
# it’s back to its original order.
print("reverse() used again:")
list.reverse()
print(list)
print("\n")

# • Use sort() to change your list so it’s stored in alphabetical order. Print the
# list to show that its order has been changed.
print("sort() used, alphab. order now")
list.sort()
print(list)
print("\n")

# • Use sort() to change your list so it’s stored in reverse alphabetical order.
# Print the list to show that its order has changed.
print("sort() with reverse")
list.sort(reverse=True)
print(list)





