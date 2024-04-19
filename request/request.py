from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys
import timeit

parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir)

from dataFormatting.songnode import SongNode
from minHeap.minheap import MinHeap
from maxHeap.maxheap import MaxHeap

directory_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tracks')

app = Flask(__name__)
CORS(app)

def getJson(song):
    start = timeit.default_timer()
    rootSong = SongNode.load(song)
    sharedSongs = rootSong.get_songs()
    playlist = MinHeap(rootSong.get_name(), rootSong.get_artist(), rootSong.get_album())
    for song, shared in sharedSongs.items():
        playlist.insertSong(song, shared)
    end = timeit.default_timer()
    time_exec = end - start
    data = playlist.createJson(time_exec)
    return data
            
def getJson2(song):
    start = timeit.default_timer()
    rootSong = SongNode.load(song)
    sharedSongs = rootSong.get_songs()
    maxHeap = MaxHeap(rootSong.get_name(), rootSong.get_artist(), rootSong.get_album())
    for song, shared in sharedSongs.items():
        maxHeap.insertNode(song, shared)
    end = timeit.default_timer()
    time_exec = end - start
    data = maxHeap.createJson(time_exec)
    return data

@app.route('/frontend', methods=['POST'])
def get_song_data():
    
    data = request.get_json()
    song = data.get('song')
    
    sn = SongNode()
    
    song_data = getJson(sn.parse_name(song))
    song_data2 = getJson2(sn.parse_name(song))
    
    if song_data is None:
        return jsonify({"message": "Song not found"}), 404
    else:
        return jsonify(song_data, song_data2)

if __name__ == '__main__':
    app.run(debug=True, port=5000)



