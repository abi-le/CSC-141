#for 09_12 store privileges and admin class in a separate module

#import User class

from user import User
#write a class called Admin that inherits from the User class

class Admin(User):
    '''represent admin from user'''
    #add an attribute that stores a list of strings
    def __init__(self, first_name, last_name):
        '''
        Initialize attributes of the parent class
        Then initializ attributes specific to admin'''
        super().__init__(first_name, last_name)
        self.strings = ['can add post', 'can delete post', 'can ban user']
        print (f"Hello {first_name}, {last_name}.")

        #write a method called show_privileges() that lists privileges
    def show_privileges(self):
        print (f"Admin's privileges include: {self.strings}")

        
#write a separate privileges class with one attribute, and stores a list of strings
class Privileges:
    def __init__(self, privileges):
        super().__init__(privileges)
        self.strings = ['can add post', 'can delete post', 'can ban user']
        print (f"Hello Admin.")

#move the show privileges method to this class
    def show_privileges(self):
        print (f"Admin's privileges include: {self.strings}")
#make a privileges instance as an attribute in the Admin class
        self.privelege = Privileges()