# 5-10. Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username.
# • Make a list of five or more usernames called current_users.
# • Make another list of five usernames called new_users. Make sure one or
# two of the new usernames are also in the current_users list.
# • Loop through the new_users list to see if each new username has already
# been used. If it has, print a message that the person will need to enter a
# new username. If a username has not been used, print a message saying
# that the username is available.
# • Make sure your comparison is case insensitive. If 'John' has been used,
# 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
# current_users containing the lowercase versions of all existing users.)
current_users = ['admin', 'friend', 'user', 'user2', 'isildur2', 'jessica_parker', 'bear', 'KiTten', 'tom_cr00se',
                 'John']
current_users_copy = []
# copy of current_users list
for current_user in current_users:
    current_users_copy.append(current_user.lower())
print(current_users_copy)

new_users = ['anotherbear', 'Mike_tison', 'mushroom_dad', 'user2', 'ToM_cr00se', 'JOHN']
for new_user in new_users:
    if new_user.lower() in current_users_copy:
        print(f"This '{new_user}' name is already used.")
    else:
        print(F"'{new_user}' is Ok")
print("Checking finished")
