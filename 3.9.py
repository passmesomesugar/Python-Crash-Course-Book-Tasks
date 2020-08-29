# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 14:19:36 2020

@author: passmesomesugar~git
"""

# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
# through 3-7 (page 42), use len() to print a message indicating the number
# of people you are inviting to dinner.

list = ["Jun'ichirō Tanizaki", "Kōbō Abe", "akutagawa ryunosuke"]
print("Guest list contains" ,len(list) , "people")


message = "I would love to see you at my dinner, mr." + list[0]
print(message)
message = "I would love to see you at my dinner, mr." + list[1]
print(message)
message = "I would love to see you at my dinner, mr." + list[2].title()
print(message)
print("Guest list contains" ,len(list) , "people")

print("New larger table has is available")

list.insert(0,"Yasunari Kawabata")
list.insert(round(len(list)/2),"Sunao Tokunaga")
list.append("Isamu Yoshii")
print("Guest list contains" ,len(list) , "people")
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
print("Guest list contains" ,len(list) , "people")
popped_guests = []
print("Our table cannot be delivered")

popped_guest = list.pop()
print(popped_guests)
message = "I would love to see you at my dinner, mr." + popped_guest + " but I can't."
print(message)

popped_guest = list.pop()
message = "I would love to see you at my dinner, mr." + popped_guest + " but I can't."
print(message)

popped_guest = list.pop()
message = "I would love to see you at my dinner, mr." + popped_guest + " but I can't."
print(message)

popped_guest = list.pop()
message = "I would love to see you at my dinner, mr." + popped_guest + " but I can't."
print(message)

print("Guest list contains" ,len(list) , "people")
print(list)

