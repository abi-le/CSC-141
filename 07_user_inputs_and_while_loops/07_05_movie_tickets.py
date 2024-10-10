# prompt = input("Please enter your age:")

while True:
    prompt = input("Please enter your age:")
    age = int(prompt)

    if age < 3:
        price = 0
        print (f"Your ticket is ${price}")

    if age >= 3 and age <= 12:
        price = 10
        print (f"Your ticket is ${price}")
        
    elif age >12:
        price = 15
        print (f"Your ticket is ${price}")
        