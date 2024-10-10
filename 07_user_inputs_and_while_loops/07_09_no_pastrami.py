sandwich_orders = ['italian', 'pastrami', 'tomato ciabatta', 'chicken panini', 'pastrami', 'grilled cheese', 'turkey ham', 'pastrami']
finished_sandwiches = []
for sandwich in sandwich_orders:
    print (f"I will make your {sandwich.title()}.\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print ("The deli has run out of pastrami.\n")

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    
    print (f"{finished_sandwich.title()} sandwich has been made and is ready for pickup\n")
    finished_sandwiches.append(finished_sandwich)