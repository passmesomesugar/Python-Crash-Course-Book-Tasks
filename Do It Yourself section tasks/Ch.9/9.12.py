# 9-12. Multiple Modules: Store the User class in one module, and store the
# Privileges and Admin classes in a separate module. In a separate file, create
# an Admin instance and call show_privileges() to show that everything is still
# working correctly.

import admin_and_privileges

super_new_strict_admin = admin_and_privileges.Admin("Bully", "The bad boy", 35)
super_new_strict_admin.privileges.show_privileges()
