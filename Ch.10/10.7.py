# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
# so the user can continue entering numbers even if they make a mistake and
# enter text instead of a number.

user_input_number = input("Please enter a number\n")
while True:
    try:
        a = int(user_input_number)
    except ValueError:
        pass
