'''
This is an example of how I used the MinHeap class

rootSong = SongNode.load(name) #create a SongNode object loading the song name
sharedSongs = rootSong.get_songs() #get the shared songs for the song loaded
mh = MinHeap(rootSong.get_name(), rootSong.get_artist(), rootSong.get_album()) #create MinHeap object 
for song, shared in sharedSongs.items(): #insert the songs and the shared values into the min heap 
    mh.insertSong(song, shared)
data = mh.createJson() #this is the json data for the top 5 songs
'''

class MinHeap:
    
    '''
    MinHeap is constructed using a list [] where:
    
        list[(i -1) / 2] parent node.
        list[(2 * i) + 1] left child node.
        list[(2 * i) + 2] right child node.
        
    The items in the list are lists themselves with the songname and its value. Example of a list for the song 'Ivy'
    
    [['Self Control', 23], ['Location', 24], ['Nights', 28], ['Thinkin Bout You', 25], ['Pink + White', 26]]
    '''
    def __init__(self, songName, songArtist, songAlbum):
        self.songName = songName
        self.songArtist = songArtist
        self.songAlbum = songAlbum
        self.playlist = []
        self.size = 0
        
    #heapifyUp for inserting songs
    def heapifyUp(self):   
        index = self.size
        while index > 0:
            parentIndex = (index - 1) // 2
            if self.playlist[index][1] < self.playlist[parentIndex][1]:
                self.playlist[index], self.playlist[parentIndex] = self.playlist[parentIndex], self.playlist[index]
                index = parentIndex
            else:
                break
            
    #heapifyDown for deleting songs
    def heapifyDown(self):
        index = 0
        
        while index < self.size:
            smallest = index
            leftChildIndex = (index * 2) + 1
            rightChildIndex = (index * 2) + 2
            
            if leftChildIndex < self.size and self.playlist[leftChildIndex][1] < self.playlist[smallest][1]:
                smallest = leftChildIndex
            
            if rightChildIndex < self.size and self.playlist[rightChildIndex][1] < self.playlist[smallest][1]:
                smallest = rightChildIndex
            
            if smallest != index:
                self.playlist[index], self.playlist[smallest] = self.playlist[smallest], self.playlist[index]
                index = smallest
            else:
                break 
  
    def insertSong(self, title, shared):
        self.playlist.append([title, shared])
        self.heapifyUp()
        self.size += 1
        #holds the heap to 5 songs
        if self.size == 6:
            self.removeMin()
        
    def removeMin(self):
        index = self.size - 1
        self.size -= 1
        self.playlist[0] = self.playlist[index]
        self.playlist.pop()
        self.heapifyDown()
        
    #helper method for debugging
    def printPlaylist(self):
        for songs in self.playlist:
            print(songs[0], songs[1])
    
    def printOrdered(self):
        for _ in range(0, self.size):
            print(self.getMin())
            self.removeMin()
           
    #create json from the 5 songs in the heap to send to frontend
    def createJson(self):
        songs = []
        
        #get the 5 songs in the minheap and add them to songs[]
        for _ in range(0, self.size):
            songs.append(self.getMin())
            self.removeMin()
        
        #create the json object to return
        
        '''
        Example of the json for the song Ivy with list [['Self Control', 23], ['Location', 24], ['Nights', 28], ['Thinkin Bout You', 25], ['Pink + White', 26]]
        
        {'song_data': 
            {'Ivy': 
                [
                    {'Self Control': 23}, 
                    {'Location': 24}, 
                    {'Thinkin Bout You': 25}, 
                    {'Pink + White': 26}, 
                    {'Nights': 28}
                ]
            }
        }
        
        '''
        data = {
            'song_data': {
            self.getSongName(): [{song[0]: song[1]} for song in songs]
            }
        }
        
        return data;
    
    
    #getter methods
    def getPlaylist(self):
        return self.playlist
    
    def getSize(self):
        return self.size
    
    def getSongName(self):
        return self.songName
    
    def getArtistName(self):
        return self.songArtist
    
    def getAlbumName(self):
        return self.songAlbum
    
    def getMin(self):
        return self.getPlaylist()[0]