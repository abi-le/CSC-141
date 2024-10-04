jessica = {'first_name': 'jessica', 'last_name': 'le', 'age': '27'}
david = {'first_name': 'david', 'last_name': 'le', 'age': '29'}
auroarah = {'first_name': 'auroarah', 'last_name': 'le', 'age':'29'}

people = [jessica, david, auroarah]
for info in people:
    print (f"Information on {info['first_name'].title()} {info['last_name'].title()}, is her age {info['age']}.\n")
    

