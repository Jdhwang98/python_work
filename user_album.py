def make_album(artist, title):
    album = {
        "artist" : artist.title(),
        "title" : title.title()
    }
    return album


artist_prompt = "please enter artist name: "
title_prompt = "please enter album name: "
print("creating library")

while True:
    artist = input(artist_prompt)
    if artist == "quit":
        break
    title = input(title_prompt)
    if title == "quit":    
        break
    album = make_album(artist,artist)

print("here is all the albums: ")
print(album)

