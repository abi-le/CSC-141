
def city_country(city, country):
    '''return a city and its countries name'''
    city_country = (f"{city}, {country}")
    return city_country.title()
name = city_country ('sacramentio', 'california')
print(name)
name = city_country ('philidephia', 'pennsylvania')
print(name)
name = city_country ('dustin', 'florida')
print(name)