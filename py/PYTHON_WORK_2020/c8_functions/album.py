def make_album(artist, album_title, songs=None):
    """Returns a dictionary of info about a music album."""
    album = {'artist': artist, 'album_title': album_title}
    if songs:
        album['songs'] = songs
    return album

while True:
    print("\nAlbum Maker! (kind of)")
    print("(Enter 'quit' at any time to quit.)")

    album_title = input("\nEnter the name of an album: ")
    if album_title == 'quit':
        break

    artist = input("\nWho made this album? ")
    if artist == 'quit':
        break

    songs = input("\nHow many songs are in this album? (type 'n/a' if unsure) ")
    if songs =='quit':
        break
    elif songs == 'n/a':
        album = make_album(artist, album_title)
    else:
        album = make_album(artist, album_title, songs)
    print()
    print(album)
