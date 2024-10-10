pizza = ("\nEnter a pizza topping:")
pizza += ("\nEnter 'quit' when you are finished:")

while True:
    topping = input(pizza)

    if topping == 'quit':
        break
    else: 
        print (f"I'll add {topping} to your pizza.")
  