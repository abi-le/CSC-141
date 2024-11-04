class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        '''initialize restaurant name and cuisine type'''
        self.name = restaurant_name
        self.cuisine = cuisine_type
        

    def describe_restaurant(self):
    #print two pieces of information from a method
        print(f"{self.name.title()}")
        print(f"{self.cuisine.title()}")

    #print message indicating restaurant is open
    def open_restaurant(self):
            print (f"{self.name.title()} is now open.")

#write a class that inherits from the restaurant class
class IceCreamClass(Restaurant):
     '''add ice cream flavors'''
    #add an attribute called flavors that stores a list of ice cream flavors  
     def __init__(self, restaurant_name, cuisine_type):
        '''initialize attributes of the parent class'''
        super().__init__(restaurant_name, cuisine_type)
        self.flavor = ['chocolate', 'vanilla', 'strawberry', 'caramel']
        print (f"At {restaurant_name} which serves {cuisine_type}:")

#write a method that displays these flavors
     def display_flavors(self):
        print(f"Ice cream flavors provided are: {self.flavor}")

#create an instance of IceCreamStand and call this method
ice_cream = IceCreamClass('coldstone', 'ice cream')
ice_cream.display_flavors()



         



