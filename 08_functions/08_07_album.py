def name_album (name, album, songs):
    '''return dictionary about artist'''
    artist = {'artist name': name, 'album': album}

#using none
    if songs : None
    if songs:
        artist ['songs'] = songs
    return artist

album = name_album ('def leppard', 'pyromania', songs = 14)
print (album)

album = name_album ('bruno mars', 'an evening with silk sonic', songs = 10)
print (album)

album = name_album ('jordan ward', 'forward', songs = 9)
print (album)