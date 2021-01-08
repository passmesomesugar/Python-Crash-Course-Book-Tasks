# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.
sandwich_orders = ['sandwich', 'pastrami', 'sandmich', 'pastrami', 'max3000', 'pastrami', 'quick fix', '50sent',
                   'double tuna', 'quick mix']
finished_sandwiches = []
print("deli has run out of pastrami")
while sandwich_orders:
    current_order = sandwich_orders.pop()
    if current_order != 'pastrami':
        finished_sandwiches.append(current_order)
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
