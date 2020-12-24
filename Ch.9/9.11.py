# 9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173).
# Store the classes User, Privileges, and Admin in one module. Create a separate
# file, make an Admin instance, and call show_privileges() to show that
# everything is working correctly.
import admin

new_admin = admin.Admin("Super", "NovaGuy", 35)
new_admin.greet_user()
new_admin.describe_user()
new_admin.privileges.show_privileges()
