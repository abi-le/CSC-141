#diffculty 6/10
#combine the two programs written in exercise 10-11
from pathlib import Path
import json

#if the number is stored report the favorite number to the user
path = Path('favorite.json')
if path.exists():
    contents = path.read_text()
    favorite = json.loads(contents)
    print (f"I remembered that your favorite number is {favorite}")

#if the number is not stored, prompt the user's favorite number and store it in a file
else: 
    favorite = input ("Please enter favorite number:")
    contents = json.dumps(favorite)
    path.write_text(contents)
    print (f"I'll remember your favorite number is {contents}")