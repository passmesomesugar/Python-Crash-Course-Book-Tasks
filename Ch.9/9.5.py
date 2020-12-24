# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 162). Write a method called increment_login
# _attempts() that increments the value of login_attempts by 1. Write another
# method called reset_login_attempts() that resets the value of login_attempts
# to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.

class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name}, {self.last_name}, age: {self.age}")
        print()

    def greet_user(self):
        print(f"Hi, {self.first_name}")
        print()

    def increment_login_attempts(self, value):
        self.login_attempts += value

    def reset_login_attempts(self):
        self.login_attempts = 0


new_user4 = User("Paula", "Patton", 29)
new_user4.describe_user()
new_user4.increment_login_attempts(1)
print(f"{new_user4.login_attempts}")
new_user4.increment_login_attempts(1)
print(f"{new_user4.login_attempts}")
new_user4.increment_login_attempts(1)
print(f"{new_user4.login_attempts}")
new_user4.increment_login_attempts(1)
print(f"{new_user4.login_attempts}")
new_user4.increment_login_attempts(1)
print(f"{new_user4.login_attempts}")
new_user4.increment_login_attempts(1)
new_user4.reset_login_attempts()
print(f"{new_user4.login_attempts}")
