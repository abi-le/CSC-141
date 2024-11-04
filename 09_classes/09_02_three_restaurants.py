class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        '''initialize restaurant name and cuisine type'''
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
    #print two pieces of information from a method
        print(f"{self.name.title()}, is a five star restaurant.")
        print(f"{self.type} is being served.")

    #print message indicating restaurant is open
    def open_restaurant(self):
            print (f"{self.name.title()} is now open.")
    

#make three instances and call describe_restaurant() for each instance
restaurant = Restaurant('Remys place', 'Ratatouille')
restaurant.describe_restaurant()
print('\n')

restaurant = Restaurant ('austins', 'Chicken pesto pasta')
restaurant.describe_restaurant()
print('\n')

restaurant = Restaurant ('texas roadhouse', 'New york strip')
restaurant.describe_restaurant()
print('\n')

