# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 14:19:36 2020

@author: passmesomesugar~git
"""

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
# • Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.

list = ["Jun'ichirō Tanizaki", "Kōbō Abe", "akutagawa ryunosuke"]

message = "I would love to see you at my dinner, mr." + list[0]
print(message)
message = "I would love to see you at my dinner, mr." + list[1]
print(message)
message = "I would love to see you at my dinner, mr." + list[2].title()
print(message)

print("New larger table has is available")

list.insert(0, "Yasunari Kawabata")
list.insert(round(len(list) / 2), "Sunao Tokunaga")
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

print(list)
