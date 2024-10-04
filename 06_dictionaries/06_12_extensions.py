#improving 6-2 by using a for loop
#original
'''favorite_numbers = { 
    'jacob': '29',
    'fatima': '27',
    'paige' : '7',
    'michael' : '1',
    'eric' : '26',
}
number = favorite_numbers['jacob'].title()
print(f"Jacobs's favorite number is {number}.")

number = favorite_numbers['fatima'].title()
print(f"Fatima's favorite number is {number}.")

number = favorite_numbers['paige'].title()
print(f"Paige's favorite number is {number}.")

number = favorite_numbers['michael'].title()
print(f"Michael's favorite number is {number}.")

number = favorite_numbers['eric'].title()
print(f"Eric's favorite number is {number}.")'''

#imporved 
favorite_numbers = { 
    'jacob': '29',
    'fatima': '27',
    'paige' : '7',
    'michael' : '1',
    'eric' : '26',
}
for key, value in favorite_numbers.items():
    print(f"\n{key.title()}'s favorite number is {value}.")
