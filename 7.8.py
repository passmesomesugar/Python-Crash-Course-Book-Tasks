# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various
# sandwiches. Then make an empty list called finished_sandwiches. Loop
# through the list of sandwich orders and print a message for each order, such
# as I made your tuna sandwich. As each sandwich is made, move it to the list
# of finished sandwiches. After all the sandwiches have been made, print a
# message listing each sandwich that was made.
sandwich_orders = ['sandwich', 'sandmich', 'max3000', 'quick fix', '50sent', 'double tuna', 'quick mix']
finished_sandwiches = []
while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"I made you a {current_order} sandwich")
    finished_sandwiches.append(current_order)
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
