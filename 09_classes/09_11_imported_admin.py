#store the classes User, Admin, Privileges in one module

from classes import User, Admin, Privileges

#make an Admin instance and call show_privileges to show everything is working correctly
privilege = Admin('Jack', 'Le')
privilege.show_privileges()