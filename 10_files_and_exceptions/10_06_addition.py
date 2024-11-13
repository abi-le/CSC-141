#difficulty 2/10
#write a program that prompts for two numbers
print ("Please enter 2 numbers and they will be added together.")

first_number = input("\nFirst number:")

second_number = input("Second number:")
#write a friendly error message
try:
        answer = int(first_number) + int(second_number)
except ValueError:
        print(f"The value input was not a number.")
else: 
        print(answer)