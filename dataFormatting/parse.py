
import pandas
import json
import os


file_index = 0


for filename in os.listdir("spotify_million_playlist_dataset/data/"):

    file = json.load(open("spotify_million_playlist_dataset/data/" + filename))


    index = 0

    while index <= 999 :

        data = pandas.DataFrame(file["playlists"][index]["tracks"])


        data = data.drop(columns = ['pos', 'track_uri', 'album_uri', 'artist_uri'])

        print(str(file_index * 1000 + index))
        data.to_csv("parsed_playlists/" + str(file_index * 1000 + index) + ".csv", index=False)


        index += 1


    file_index += 1

