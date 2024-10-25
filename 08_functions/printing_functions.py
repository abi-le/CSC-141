#printing_functions.py

def make_sandwich(*ingredients):
    '''print the ingredients for the sandwhich'''
    print ("These are the ingredients for the sandwich:")
    for ingredient in ingredients:
        print(f"- {ingredient}")
    
