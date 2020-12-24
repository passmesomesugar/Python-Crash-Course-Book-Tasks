# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.

class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"{self.first_name}, {self.last_name}, age: {self.age}")
        print()

    def greet_user(self):
        print(f"Hi, {self.first_name}")
        print()


new_user1 = User("Jack", "Jones", 28)
new_user1.describe_user()
new_user1.greet_user()

new_user2 = User("John", "Doe", 26)
new_user2.describe_user()
new_user2.greet_user()

new_user3 = User("Gerald", "Fielding", 33)
new_user3.describe_user()
new_user3.greet_user()

new_user4 = User("Paula", "Patton", 29)
new_user4.describe_user()
new_user4.greet_user()
