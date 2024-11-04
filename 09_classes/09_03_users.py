class User:
    def __init__ (self, first_name, last_name, hobby, age):
        '''initialize info on user'''
        self.name = first_name
        self.last = last_name
        self.hobby = hobby
        self.age = age
#make a method called describe_user that prints a summary of the user's information
    def describe_user(self):
        print (f"The user's name is {self.name.title()} {self.last.title()} and they are {self.age} years old. {self.name.title()}'s favorite hobby is {self.hobby}")
        
#make another greet_user that prints a personalized greeting to the user
    def greet_user(self):
        print (f"Hello {self.name.title()} {self.last.title()}! ")
        print("\n")
#create several instances representing different users and call both methods

user = User ('jenna', 'cordelle', 'drawing', 19)
user.describe_user()
user.greet_user()

user = User ('jarred', 'smith', 'snowboarding', 22)
user.describe_user()
user.greet_user()

user = User ('billie', 'westland', 'baketball', 19)
user.describe_user()
user.greet_user()
