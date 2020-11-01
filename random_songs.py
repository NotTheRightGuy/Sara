import random

def give_me_random_song():
    """

    :return: A random song name fetched from songs.txt
    """

    with open('songs.txt','r') as file:
        song_names = file.read()
    song_list = song_names.split('\n')[2:]
    index = random.randint(0,len(song_list))

    return (song_list[index])

