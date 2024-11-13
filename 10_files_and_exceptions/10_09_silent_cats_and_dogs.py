#diffculty 2/10
#modify your except block in Excercise 10_08 to fail silently if either file is missing

#write a program that tries to read these files and print the contents of the file to the screen
from pathlib import Path

def print_contents(path):
    '''print contents of the files'''
#wrap code in try-except block to catch FileNotFoundError
    try:
        contents = path.read_text('cats.txt', 'dogs.txt')
    except FileNotFoundError:
#print a friendly message if the file is missing
        pass
    else:
    #print the contents of the file
        print(f"{path}")

files = ['cats.txt', 'dogs.txt']
for file in files:
    path = Path(file)
    print_contents(path)