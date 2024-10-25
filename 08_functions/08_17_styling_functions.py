#three programs that follow the styling guidelines
#first 08_01
def display_message():
    '''display a message about what you are learning in this chapter'''
    print ("I am learing about functions in this chapter.")

display_message()

#second 08_05
def describe_city(city, country='Italy'):
    '''print the city and the country it is in'''
    print (f"{city.title()} is in {country}.")
#cities in the country
describe_city (city='venice')
describe_city (city='florence')
#city not in country
describe_city (city= 'paris')

#third 08_14
def make_car (
    manufacturer, model, color, **arguements):
    '''print car and its details'''
    arguements['manufacturer'] = manufacturer
    arguements ['model'] = model
    arguements ['color'] = color
    return arguements
car = make_car('toyota', 'corolla', 'grey', tires='michelin')
print(car)