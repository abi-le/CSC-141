#difficulty 5/10

from pathlib import Path
import json

#ask two more pieces of information about the user
username = input("what is your name: ")
hobby = input("what is your favorite hobby: ")
job = input("What is your job: ")


#store the information in a dictionary 
info = {'username': username, 
        'hobby': hobby,
        'job': job}
# write this dictionary into a file using json.dumps()and read it back using json.loads
path = Path('dictionary.json')
contents = json.dumps(info)
path.write_text(contents)

print(f"We'll remember you when you come back {username}!")