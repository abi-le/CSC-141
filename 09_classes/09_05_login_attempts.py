class User:
    def __init__ (self, first_name, last_name, hobby, age, login_attemps):
        '''initialize info on user'''
        self.name = first_name
        self.last = last_name
        self.hobby = hobby
        self.age = age
        self.login_attempts = 0

#make a method called describe_user that prints a summary of the user's information
    def describe_user(self):
        print (f"The user's name is {self.name.title()} {self.last.title()} and they are {self.age} years old. {self.name.title()}'s favorite hobby is {self.hobby}")
        
#make another greet_user that prints a personalized greeting to the user
    def greet_user(self):
        print (f"Hello {self.name.title()} {self.last.title()}! ")
        print("\n")

#method called increment_login_attempts()
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0 


#create several instances representing different users and call both methods

user = User ('jenna', 'cordelle', 'drawing', 19, 1)
user.describe_user()
user.greet_user()

user = User ('jarred', 'smith', 'snowboarding', 22, 1)
user.describe_user()
user.greet_user()

user = User ('billie', 'westland', 'baketball', 19, 1)
user.describe_user()
user.greet_user()

#call increment login attempts several times
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

print(f"\nLogin attempts: {user.login_attempts}")

#call reset login attempts
user.reset_login_attempts()

#print login attempts to make sure it was reset to zero
print(f"\nLogin attempts after reset {user.login_attempts}")

