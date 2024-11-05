#this was extremely difficult and I wanted to cry the whole time doing this assignment

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        '''initialize restaurant name and cuisine type'''
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
    #print two pieces of information from a method
        print(f"{self.name.title()}, is a French cuisine restaurant.")
        print(f"{self.type.title()} is being served.")

    #print message indicating restaurant is open
    def open_restaurant(self):
            print (f"{self.name.title()} is now open.")
    
#make an instance called restaurant from my class
restaurant = Restaurant('remys place', 'ratatouille')
print(f"{restaurant.name}")
print(f"{restaurant.type}")

#call both methods
restaurant = Restaurant('Remys place', 'ratatouille')
restaurant.describe_restaurant()
restaurant.open_restaurant()
    
            
        
