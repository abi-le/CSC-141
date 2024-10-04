glossary = { 'for_loop': 'A programming construct that executes a block of code repeatedly until a condition is met',
            'value': 'A piece of data that a program works with',
            'list' : 'Store multiple items in a single variable',
            'variable' : 'Contains the memory location of an object',
            'tuple' : 'Used to store multiple items in a single variable and are written with round brackets',
            'function': 'Blocks of reusable code that perform a specific task',
            'keys' : 'method to return a view object of the dictionary keys as a list',
            'dictionary': 'used to store data values in key:value pairs',
            'range' : 'used to generate a sequence of numbers. It is commonly used in for-loops to iterate over a sequence of numbers',
            'integers' : 'one of the basic data types available for representing whole numbers, both positive and negative',
            }
for name, term in glossary.items():
    print(f"\n{name.title()}: {term.lower()}.")