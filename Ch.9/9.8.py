# 9-8. Privileges: Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use your
# method to show its privileges.

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


class Privilege:

    def __init__(self, privileges=['can ban', 'can remove posts', 'always right']):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = Privilege()


admin_101 = Admin('Mr', 'Anon', 88)
admin_101.privileges.show_privileges()
