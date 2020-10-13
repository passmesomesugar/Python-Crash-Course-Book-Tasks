# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 13:56:35 2020

@author: passmesomesugar~git
"""

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.


list = ["Einstein", "John the builder", "akutagawa ryunosuke"]

message = "I would love to see you at my dinner, mr." + list[0]
print(message)
message = "I would love to see you at my dinner, mr." + list[1]
print(message)
message = "I would love to see you at my dinner, mr." + list[2].title()
print(message)
