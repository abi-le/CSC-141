#import restaurant
from restaurant import Restaurant

#make a restaurant instance and call one of restaurant's methods to show that the import statement is working
restaurant = Restaurant('Austins', 'Chicken alfredo', '103')
restaurant.describe_restaurant()
restaurant.open_restaurant()