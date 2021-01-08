# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
# function send_messages() with a copy of the list of messages. After calling the
# function, print both of your lists to show that the original list has retained its
# messages.
messages = ['Message one ', 'Please close the doors', 'Use linux for the sake of humanity', 'NO smoking area']
sent = []
print("Messages: ", messages)
print("Sent:", sent)


def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


send_messages(messages[:], sent)
print("Messages: ", messages)
print("Sent:", sent)
