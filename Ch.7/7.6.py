# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
# that do each of the following at least once:

# • Use a conditional test in the while statement to stop the loop.
prompt = "Please enter your age "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        if int(message) <= 3:
            price = 0
        if 3 < int(message) <= 12:
            price = 10
        if int(message) > 12:
            price = 15
        print(f"Your ticket price is {price}$")

# • Use an active variable to control how long the loop runs.
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        if int(message) <= 3:
            price = 0
        if 3 < int(message) <= 12:
            price = 10
        if int(message) > 12:
            price = 15
        print(f"Your ticket price is {price}$")

# • Use a break statement to exit the loop when the user enters a 'quit' value.
while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        if int(message) <= 3:
            price = 0
        if 3 < int(message) <= 12:
            price = 10
        if int(message) > 12:
            price = 15
        print(f"Your ticket price is {price}$")
