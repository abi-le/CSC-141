from random import randint
#make a class Die
class Die:
#one attribute called sides
    def __init__(self, sides=6):
        '''make sides have a default value of 6'''
        self.sides = sides
#write  method called roll_die()
    def roll_die (self):
        '''print a random number between 1 and the number of sides the die has'''
        print (f"{randint (1, self.sides)}")
        

#make a 6-sided die and roll it 10 times
thing = Die()

#roll die 10 times
for i in range(10):
    thing.roll_die()
print ("\n\n")

#make a 10 sided die
side_10 = Die(10)
for i in range(10):
    side_10.roll_die()

print ("\n\n")
#make a 20 sided die
side_20 = Die(20)
for i in range(10):
    side_20.roll_die()
