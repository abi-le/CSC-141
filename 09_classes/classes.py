class User:
    def __init__ (self, first_name, last_name):
        '''initialize info on user'''
        self.name = first_name
        self.last = last_name
        
#make a method called describe_user that prints a summary of the user's information
    def describe_user(self):
        print (f"The user's name is {self.name.title()} {self.last.title()} and they are {self.age} years old. {self.name.title()}'s favorite hobby is {self.hobby}")
        
#make another greet_user that prints a personalized greeting to the user
    def greet_user(self):
        print (f"Hello {self.name.title()} {self.last.title()}! ")
        print("\n")

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