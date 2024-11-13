#difficulty = 6
#replace the word python with c, print each modified line to the screen
from pathlib import Path
#print the contents once by reading in the entire file
path = Path ("10_files_and_exceptions\learning_python.txt")
contents = path.read_text()
print(contents)
print('\n')
C = contents.replace('Python', 'C++')
print(C)