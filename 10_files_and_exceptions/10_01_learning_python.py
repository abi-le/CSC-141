#difficulty = 4
from pathlib import Path
#print the contents once by reading in the entire file
path = Path ("10_files_and_exceptions\learning_python.txt")
contents = path.read_text()
print(contents)
print('\n')
#store the lines in a list and loop over each line
lines = contents.splitlines()
for line in lines:
    print(f"{line}")