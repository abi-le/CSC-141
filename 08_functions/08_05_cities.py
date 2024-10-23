def describe_city(city, country='Italy'):
    print (f"{city.title()} is in {country}.")
#cities in the country
describe_city (city='venice')
describe_city (city='florence')
#city not in country
describe_city (city= 'paris')