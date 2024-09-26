#see if username is avaliable or not
current_users = ['George_Washington', 'PVZ', 'Sebastian_the_crab', 'Little_bird', 'Tweedledee']

new_users = ['Pinky', 'Oompa_Loompa', 'Tweedledee', 'Fish_fried', 'PVZ']
for user in new_users:
    if user in current_users:
        print (f"{user.title()} enter a new username.")

    else:
        print(f"{user.title()} username is avaliable")


#case sensitive
current_users = ['George_Washington', 'Pvz', 'Sebastian_the_crab', 'Little_bird', 'Tweedledee']

new_users = ['pinky', 'oompa_loompa', 'tweedledee', 'fish_fried', 'pvz']
for user in new_users:
    if user.title() in current_users:
        print (f"{user} enter a new username.")

    else:
        print(f"{user} username is avaliable")
    