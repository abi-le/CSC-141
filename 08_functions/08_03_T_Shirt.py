#positional arguements
def make_shirt (size, message):
    print (f"The size of the shirt is {size}.")
    print (f"The message on the shirt will be, {message}!")

make_shirt ('M', 'you got this')

#keyword arguments
def make_shirt (size, message):
    print (f"The size of the shirt is {size}.")
    print (f"The message on the shirt will be, {message}!")

make_shirt (size='M', message='you got this')