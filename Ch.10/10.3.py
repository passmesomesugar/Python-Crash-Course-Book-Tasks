# 10-3. Guest: Write a program that prompts the user for their name. When they
# respond, write their name to a file called guest.txt.
filename = 'guest.txt'
name = input("Please enter your name\n")
with open(filename, 'a+') as file_object:
    file_object.write(name)
