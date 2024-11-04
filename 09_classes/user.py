#for 09_12 store the user class in one module
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