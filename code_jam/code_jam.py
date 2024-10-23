import random
import os

characters = {'Mario': 32, 'Luigi': 40, 'Peach': 35, 'Wario': 38, 'Toad': 40, 'Yoshi': 30, 'Bowser': 37, 'Daisy': 33, 'Dry Bones' : 40}
number_of_characters = len(characters)


character_names = list(characters.keys())
print(character_names)

character_times = list(characters.values())
print (character_times)

your_character_time = 37
print ('These are the characters you are racing against.')
for character in character_names:
    print (character.title())
print('\n')

random_number = random.randint(0, number_of_characters - 1)
character = character_names[random_number]
character_time = character_times[random_number]
character_race = (1, 2, 3, 4, 5)
random_number = random.choice(character_race)


choice =''
change_character = True
print_line_once = True

GameOn = True

while GameOn:
    if(len(characters) != 0 and change_character):
        random_key = random.choice(list(characters.keys()))

    if(print_line_once):
        print (f"You are in the track with {random_key.title()}, who has a race time of {character_time} seconds.")
        print_line_once = False

    if choice == 'c':
        change_character = True
        # print(len(characters))
        print (f"Next racer is {random_key.title()}.\n")
        if(random_key.title() in characters):
            value = characters.pop(random_key.title())

    if(len(characters) == 0):
        choice = input("Last character press (r) to race:")
    else:
        choice = input("Are you (r)acing, or (c)hosing another racer?:")


    if choice == 'r':
        change_character = False
        #you race
        your_race = random.randint(0, your_character_time)
        for i in range(1):
            random_number = random.randint(1, 5)
        if your_race == 0:
            print (f"Your car broke down, and it was an automatic win for {random_key.title()}")
            break
        else:
            print (f"You race {random_key.title()}, and are {random_number} seconds ahead")
            character_time = character_time - random_number
        
        if character_time <= 0:
            print (f"You beat {random_key.title()} and won the tournament!")
            characters.pop(character)
            break
        
            
        characters_race = random.randint(0, your_character_time)
        for i in range(1):
             random_number = random.randint(1, 5)
        if characters_race == 0:
            print (f"{random_key.title()}'s car broke down and it is an automatic win for you!")
            break
        else:
            print (f'{random_key.title()} races you and is ahead by {random_number}.')
            your_race = your_race - random_number

            if your_race <= 0:
                print (f"You have lost the race.")
                break

print ("Hope you had fun playing!")
    
