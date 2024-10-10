sandwich_orders = ['italian', 'tomato ciabatta', 'chicken panini', 'grilled cheese', 'turkey ham']
finished_sandwiches = []
for sandwich in sandwich_orders:
    print (f"I will make your {sandwich.title()}.\n")


while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    
    print (f"{finished_sandwich.title()} sandwich has been made and is ready for pickup\n")
    finished_sandwiches.append(finished_sandwich)

