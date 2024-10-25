def make_sandwich(*ingredients):
    '''print the ingredients for the sandwhich'''
    print ("These are the ingredients for the sandwich:")
    for ingredient in ingredients:
        print(f"- {ingredient}")
    
make_sandwich('ham', 'cheese', 'lettuce', 'tomato')

make_sandwich ('chicken', 'pesto', 'mozzarella')

make_sandwich ('cheese', 'steak')