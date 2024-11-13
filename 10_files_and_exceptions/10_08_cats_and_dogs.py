#diffculty 6/10
#make two files cats.txt and dogs.txt
#write a program that tries to read these files and print the contents of the file to the screen
from pathlib import Path

def print_contents(path):
    '''print contents of the files'''
#wrap code in try-except block to catch FileNotFoundError
    try:
        contents = path.read_text('cats.txt', 'dogs.txt')
    except FileNotFoundError:
#print a friendly message if the file is missing
        print(f"Sorry the file {path} does not exist.")
    else:
    #print the contents of the file
        print(f"{path}")

files = ['cats.txt', 'dogs.txt']
for file in files:
    path = Path(file)
    print_contents(path)

