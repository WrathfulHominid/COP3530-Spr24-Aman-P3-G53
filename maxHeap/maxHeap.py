'''
This is an example of how I used the MaxHeap class: I based this off of your structure. 

rootSong = SongNode.load(name)
sharedSongs = rootSong.get_songs()
maxHeap = MaxHeap(rootSong.get_name(), rootSong.get_Artist(), rootSong.get_Album())
for song, shared in sharedSongs.items():
   maxHeap.insertNode(song, shared)
data = maxHeap.createJson()
'''


class MaxHeap:
    def __init__(self, songName, songArtist, songAlbum):  # initialize
        self.size = 0
        self.k = 5
        self.heap = []
        self.topK = []
        self.songName = songName
        self.songArtist = songArtist
        self.songAlbum = songAlbum

    def insertNode(self, name, num):  # inserts a node to max heap
        self.size += 1
        self.heap.append([name, num])
        self.heapifyUp(self.size - 1)

    def heapifyUp(self, i):  # heapify up
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i][1] > self.heap[parent][1]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def deleteMax(self):  # deletes and returns max element
        max = self.heap[0]
        self.heap[0], self.heap[self.size - 1] = self.heap[self.size - 1], self.heap[0]
        self.size -= 1
        self.heap.pop()
        self.heapifyDown(0)
        return max

    def heapifyDown(self, i):  # heapify down after deletion
        while True:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < len(self.heap) and self.heap[left][1] > self.heap[largest][1]:
                largest = left
            if right < len(self.heap) and self.heap[right][1] > self.heap[largest][1]:
                largest = right
            if largest != i:
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                i = largest
            else:
                break

    def getHeap(self):  # returns full heap
        return self.heap

    def kthLargest(self):  # creates a max heap of just the top k elements
        for _ in range(self.k):
            self.topK.append(self.deleteMax())

    def createJson(self, time): # creates top k max heap and organizes in json.
        self.kthLargest()
        songs = self.topK

        data = {
            'song_data_max': {
                self.getSongName(): [{song[0]: song[1]} for song in songs]
            },
            'exec_time_max': time
        }

        return data

    def printTopK(self):  # prints top k elements
        self.kthLargest()
        for i in self.topK:
            print(i[0], i[1])

    def printHeap(self):  # prints whole heap
        for i in self.heap:
            print(i[0], i[1])

    def getSongName(self): # get song name
        return self.songName
