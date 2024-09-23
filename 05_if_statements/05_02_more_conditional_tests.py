#test for equality and inequality with strings
#equality
#true
dog = 'Jack'
print("Is dog == 'Jack'? I predict True.")
print(dog == 'Jack')
#false
print("Is dog == 'Duke'? I predict False")
print(dog == 'Duke')

 #inequality 
if dog != 'Duke':
    print("\nDog is Duke\n")
if dog != 'Jack':
    print("\nDog is Jack\n")


#tests using lower() method
dog = 'Jack'
dog.lower() == 'Jack'
print(dog == 'Jack')

dog.lower() == 'duke'
print(dog =='duke')
print("\n\n")

#numerical tests involving equality and inequality
age = 21
age == 21
print (age == 21)

age == 13
print (age == 13)
print("\n")

number = 3
if number != 5:
    print("Incorrect")

if number != 3:
    print("correct")

print("\n")

#greater than and less than
#true
age_greater_less = 20
print(age_greater_less < 22)
#false
print (age_greater_less < 2)
print("\n")
#true
age_greater_less > 12
print(age_greater_less > 12)
#false
print(age_greater_less > 30)
print("\n")

#greater than or equal 
#true
age_greater_equal = 5
print (age_greater_equal > 2)
print (age_greater_equal >= 5)
print("\n")

#false
print (age_greater_equal > 7)
print (age_greater_equal >= 9)
print("\n")

#less than or equal to
#true
age_less_than = 5
print(age_less_than < 10)
print (age_less_than<= 5)
print("\n")

#false 
print(age_less_than < 3)
print (age_less_than <= 4)
print("\n")

#tests using the and keyword and the or keyword
#true (and)
age_1 = 30
age_2 = 20
print(age_1 >= 30 and age_2 >= 20)

#false (and)
age_1 = 30
age_2 = 20
print(age_1 >= 20 and age_2 >= 30)
print("\n")

#true (or)
age_1 = 35
age_2 = 25
print(age_1 >= 35 or age_2 >= 25)

#false (or)
age_1 = 35
age_2 = 25
print(age_1 >= 55 or age_2 >= 65)
print("\n")

#test whether an item is in a list
#true
list = ['Switzerland', 'Thailand', 'Cabo', 'Montana', 'Autralia']
print('Thailand' in list)
#false
print('Vietnam' in list)
print("\n")

#test whether an item is not in a list
#false
list_country = ['Switzerland', 'Thailand', 'Cabo', 'Montana', 'Autralia']
country = 'chile'
if country not in list_country:
    print(f"{country.title()}, if not on list, add yourself.")

#false
list_country = ['Switzerland', 'Thailand', 'Cabo', 'Montana', 'Autralia']
country = 'Switzerland'
if country not in list_country:
    print(f"{country.title()}, if not on list, add yourself.")





