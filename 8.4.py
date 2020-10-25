# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.
def make_shirt(size='l', text='I love python'):
    print(f"Shirt has size {size.title()} and following text {text}")


make_shirt('m', 'I love Java')
make_shirt()
