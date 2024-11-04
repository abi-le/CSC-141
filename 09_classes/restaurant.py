class Restaurant:
#create an attribute called number served
    def __init__(self, restaurant_name, cuisine_type, number_served):
        '''initialize restaurant name and cuisine type'''
        self.name = restaurant_name
        self.type = cuisine_type
        self.number = number_served

    def describe_restaurant(self):
    #print two pieces of information from a method
        print(f"{self.name.title()}, is a French cuisine restaurant.")
        print(f"{self.type.title()} is being served.")

    #print message indicating restaurant is open
    def open_restaurant(self):
            print (f"{self.name.title()} is now open.")

    #print message indicating how many customers were served
    def number_served(self):
        '''print a statement telling how many people were served'''
        print (f"{self.number} people have been served.")

    #method called set_number_served
    def set_number_served(self, people):
        '''set number served to the given value'''
        self.number_served = people
        print (f"{people} people have been served.")
    
    #method called increment_number_served()
    def increment_number_served(self, guests):
        '''add the given amount of people to the existing amount'''
        self.number_served += guests
        print (f"{self.number_served} people have been served today.")