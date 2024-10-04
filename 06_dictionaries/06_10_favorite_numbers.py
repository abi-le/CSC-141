favorite_numbers = { 
    'jacob': ['29', '35'],
    'fatima': ['27', '52'],
    'paige' : ['7', '31'],
    'michael' : ['1', '21'],
    'eric' : ['26', '72'],
}
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"{number.title()}")

