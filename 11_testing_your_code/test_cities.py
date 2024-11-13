

#create a file called tests_cities.py that tests the function you just wrote
import pytest 
from city_functions import city_country

#test the function
def test_city_country ():
    result = city_country("paris", "france")
    assert result == 'Paris, France'