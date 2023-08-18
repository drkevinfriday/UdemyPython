from nested_data import albums

SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1


while True:
    print(f"Please select album to listen to: (invalid choice exits)")
    # for index, (album, artist , year, songs) in enumerate(albums):
    #     print(album)

    #prints the index plus 1 and the albums title.
    for index, (title, artist, year,songs) in enumerate(albums):
        print(f"{index +1} {title}")
    
    choice =  int(input())
    if 1 <= choice <len(albums):
        songs_list = albums[choice-1][SONGS_LIST_INDEX]

    else:
        break

    print(f"Please select a song to listen to: (invalid choice exits)")
    for index, (track_number, song_title) in enumerate(songs_list):
    
        print(f"{track_number} \t{song_title}")
    
    choice =  int(input())
    if 1 <= choice <len(albums):
        song_choice = songs_list[choice-SONG_TITLE_INDEX][SONG_TITLE_INDEX]

        print(f"Playing {song_choice}\n\n")
    else:
        break


