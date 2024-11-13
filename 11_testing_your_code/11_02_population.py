#difficulty 7/10
#modify function so it requires a third perameter, population
from city_functions import city_country


def test_city_country ():
    result = city_country("Santiago", "Chile", "5,000,000")
    print (f"{result}")

#modify the function so the population parameter is optional
def city_country(city, country, population=''):
    '''return a single string'''
    if population:
        title = (f"{city.title()}, {country.title()}, {population}")
    else:
        title = (f"{city.title()}, {country.title()}")
    return title.title()

#write a second test that verifies you can call the function with all three values
def test_city_country_population():
    '''return all three'''
    results = city_country("Santiago", "Chile", "5,000,000")
    assert results == 'Santiago Chile 5,000,000'
