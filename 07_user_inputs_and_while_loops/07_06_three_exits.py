prompt = "\nPlease enter age of person:"
prompt += "\n(Enter 'done' when you are finished): "
#active variable
active = True
while active: 
    age = input(prompt)
    if age == 'done':
    #break statement
        break 

    if int(age) < 1:
        term = 'infant'
        print (f"\nPerson is an {term}")

    if int(age) >=1 and int(age) <=3:
        term = 'toddler'
        print (f"\nPerson is an {term}")

    if int(age) >3 and int(age) <=12:
        term = 'child'
        print (f"\nPerson is an {term}")

    if int(age) >12 and int(age) <18:
        term = 'adolescent'
        print (f"\nPerson is an {term}")
    #conditional statement
    if int(age) >=18:
        term = 'adult'
        print (f"\nPerson is an {term}")

   
    
