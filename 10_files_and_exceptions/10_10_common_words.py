#difficulty 
#visit project Gutenberg and find a few texts to analyze
from pathlib import Path

def count(path):
    try: 
        contents = path.read_text()
    except FileNotFoundError:
        print (f"Sorry the file {path} could not be found.")
#find out how many times 'the' appears in each text
    else:
        word = contents
        count = word.count('the')
        print(f"In the file {path}, 'the' appears {count} times.")


path = Path('gutenberg.txt')
count(path)
