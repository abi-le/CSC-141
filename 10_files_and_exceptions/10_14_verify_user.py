#difficulty 6/10
#modify remember_me.py in case the current user is not the person who last used the program
from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
 
def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")

    else:
        username = get_new_username(path)
    print(f"We'll remember you when you come back, {username}!")

#ask the user if this is the correct username
def correct():
    '''ask if the username is correct'''
    path = Path('username.json')
    username = get_stored_username(path)
    print (f"Is {username} the correct username?")
    question = input ("type 'yes' or 'no':")
    if question == 'yes':
        username = greet_user()
#call get_new_username() to get the correct username
    if question == 'no': 
        username = get_new_username(path)
        greet_user()
        
correct()