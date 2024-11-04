from user import User

from privileges_admin_classes import Admin, Privileges

#create an admin instance and call show_privileges() to show everything is still working correctly
privilege = Admin('Tony', 'Stark')
privilege.show_privileges()
