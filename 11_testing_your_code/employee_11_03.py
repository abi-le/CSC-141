class Employee:
    def __init__ (self, first_name, last_name, annual_salary):
        '''initialize firstname lastname and salary'''
        self.name = first_name
        self.last = last_name
        self.salary = annual_salary

    def give_raise(self, default_raise = 5000):
        self.salary += default_raise
        

        


