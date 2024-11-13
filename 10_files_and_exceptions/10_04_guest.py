from pathlib import Path

#write a program thar prompts the user for their name
name = input ("Enter name: ")

#when they respond write their name to a file called guest.txt
path = Path('final_guest.txt')
path.write_text(name)

print("You have been added to the guest list.")
    
