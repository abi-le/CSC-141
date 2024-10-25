def name_album (name, album):
    '''return dictionary about artist and their album'''
    artist = {'artist name': name, 'album': album}
    return artist

while True:
    print ("Please enter artists name:")
    print("(enter'q' at any time to quit)")

    name = input("name: ")
    if name == 'q':
        break
    
    print("Please enter artists album: ")
    print("(enter'q' at any time to quit)")
    album = input("album: ")
    if album == 'q':
        break

    album = name_album(name, album)
    print(f"{name} {album}")