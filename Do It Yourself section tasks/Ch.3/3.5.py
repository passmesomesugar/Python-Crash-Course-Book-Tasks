# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 14:02:49 2020

@author: passmesomesugar~git
"""

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end
# of your program stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still
# in your list.


list = ["Jun'ichirō Tanizaki", "Kōbō Abe", "akutagawa ryunosuke"]

message = "I would love to see you at my dinner, mr." + list[0]
print(message)
message = "I would love to see you at my dinner, mr." + list[1]
print(message)
message = "I would love to see you at my dinner, mr." + list[2].title()
print(message)
list.pop()
list.append("Isamu Yoshii")
print("Second invitation list")
message = "I would love to see you at my dinner, mr." + list[0]
print(message)
message = "I would love to see you at my dinner, mr." + list[1]
print(message)
message = "I would love to see you at my dinner, mr." + list[2].title()
print(message)
