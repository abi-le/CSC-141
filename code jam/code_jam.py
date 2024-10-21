import random
import os

characters = {'Mario': 32, 'Luigi': 40, 'Peach': 35, 'Wario': 38, 'Toad': 40, 'Yoshi': 30}
number_of_characters = len(characters)
#random_key = random.choice(list(characters.keys()))

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


print (f"You are in the track with {character.title()}, who has a race time of {character_time} seconds.")

choice =''

GameOn = True

while GameOn:
    
    random_key = random.choice(list(characters.keys()))

    if choice == 'c':
        print (f"Next racer is {random_key.title()}.\n")
    #value = characters.pop(random_key)

    choice = input("Are you (r)acing, or (c)hosing another racer?:")


    if choice == 'r':
    
        #you race
        your_race = random.randint(0, your_character_time)
        for i in range(1):
            random_number = random.randint(1, 5)
        if your_race == 0:
            print (f"Your car broke down, and it was an automatic win for {character.title()}")
            break
        else:
            print (f"You race {character.title()}, and are {random_number} seconds ahead")
        character_time = character_time - random_number
        
        if character_time <= 0:
            print (f"You beat {character.title()} and won the tournament!")
            characters.pop(character)
            break
        
            
        characters_race = random.randint(0, your_character_time)
        for i in range(1):
             random_number = random.randint(1, 5)
        if characters_race == 0:
            print (f"{character.title()}'s car broke down and it is an automatic win for you!")
            break
        else:
            print (f'{character.title()} races you and is ahead by {random_number}.')
            your_race = your_race - random_number

            if your_race <= 0:
                print (f"You have lost the race.")
                break

print ("Hope you had fun playing!")
    
