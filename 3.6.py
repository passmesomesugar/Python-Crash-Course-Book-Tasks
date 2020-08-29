# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 14:09:02 2020

@author: passmesomesugar~git
"""


# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
# call to the end of your program informing people that you found a bigger
# dinner table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.


list = ["Jun'ichirō Tanizaki", "Kōbō Abe", "akutagawa ryunosuke"]

message = "I would love to see you at my dinner, mr." + list[0]
print(message)
message = "I would love to see you at my dinner, mr." + list[1]
print(message)
message = "I would love to see you at my dinner, mr." + list[2].title()
print(message)

print("New larger table has is available")

list.insert(0,"Yasunari Kawabata")
list.insert(round(len(list)/2),"Sunao Tokunaga")
list.append("Isamu Yoshii")
print("Second round of invitations")

message = "I would love to see you at my dinner, mr." + list[0]
print(message)
message = "I would love to see you at my dinner, mr." + list[1]
print(message)
message = "I would love to see you at my dinner, mr." + list[2].title()
print(message)
message = "I would love to see you at my dinner, mr." + list[3]
print(message)
message = "I would love to see you at my dinner, mr." + list[4].title()
print(message)
message = "I would love to see you at my dinner, mr." + list[5]
print(message)


