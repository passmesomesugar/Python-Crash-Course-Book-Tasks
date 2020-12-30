# 10-4. Guest Book: Write a while loop that prompts users for their name. When
# they enter their name, print a greeting to the screen and add a line recording
# their visit in a file called guest_book.txt. Make sure each entry appears on a
# new line in the file.

output_file_name = 'guest_book.txt'
guest_book = []
keep_going = True
while keep_going:
    name = input('Enter your name, or input empty  (press Enter) line to quit\n')
    guest_book.append(name)
    if name == '':
        keep_going = False
with open(output_file_name, 'w') as file_handler:
    for item in guest_book:
        file_handler.write("{}\n".format(item))
