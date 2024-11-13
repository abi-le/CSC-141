
#test file for Employee with two test functions
import pytest
from employee_11_03 import Employee

#write a fixture
@pytest.fixture

#default raise
def test_give_default_raise():
    '''test that a single response is stored properly'''
    employee = Employee('Abi', 'Le', 70000)
    employee.give_raise()
    assert employee.annual_salary == 75000

#custom raise
def test_give_custom_raise():
    '''test that a single response is stored properly'''
    employee = Employee('Abi', 'Le', 70000)
    employee.give_raise(1000)
    assert employee.annual_salary == 71000