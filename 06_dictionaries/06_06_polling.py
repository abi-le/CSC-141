favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
}

poll = {'sally', 'jacob', 'jen', 'sarah', 'edward', 'phil'}
for name in poll: 
    if name in favorite_languages: 
        print(f"{name.title()}, thank you for repsonding.")
    else:
        print(f"{name.title()}, you need to take the poll")