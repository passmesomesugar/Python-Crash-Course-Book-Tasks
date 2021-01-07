# 10-5. Programming Poll: Write a while loop that asks people why they like
# programming. Each time someone enters a reason, add their reason to a file
# that stores all the responses.

output_file_name = 'responses.txt'
responses_list = []
keep_going = True
while keep_going:
    response = input('Why do you like programming? Enter empty response to leave.\n')
    responses_list.append(response)
    if response == '':
        keep_going = False
with open(output_file_name, 'w') as file_handler:
    for item in responses_list:
        file_handler.write("{}\n".format(item))
