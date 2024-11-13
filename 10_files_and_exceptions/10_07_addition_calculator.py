#difficulty 2/10
#Wrap your code from exercise 10-6 in a while loop so the user can continue entering numbers
print ("Please enter 2 numbers and they will be added together.")
print("enter 'q' to quit.")

while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break

    second_number = input("Second number:")
    if second_number == 'q':
        break
#write a friendly error message
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print(f"The value input was not a number.")
    else: 
        print(answer)