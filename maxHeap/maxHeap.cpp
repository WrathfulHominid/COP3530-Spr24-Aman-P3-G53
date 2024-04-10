#include <iostream>
#include <map>
#include <vector>
#include "../dataFormatting/songnode.cpp"
using namespace std;

class MaxHeap{
private:
    vector<pair<string, int>> heap; // max heap storing ALL song name and num shared playlists.
    int k = 5; // max size of heap;
    int size = 0; // initial size, can change.
    vector<pair<string, int>> topK; // heap of only top k songs.

public:
    void insertNode(string name, int num){ // insert a song into the heap.
        size += 1; // increase size.
        heap.push_back(make_pair(name, num)); // add element to end of heap.
        heapifyUp(size-1); // heapify from that index.
    }

    void heapifyUp(int i) { // heapify up for insertion.

        if (i > 0){ // avoid out of bounds.
            int parent = (i-1)/2; // array bounds.
            int child = i;

            if (heap[child].second > heap[parent].second){ // if child playlists greater than parent.
                swap(heap[child], heap[parent]); // swap.

                heapifyUp(parent); // recursively move up.
            }
        }
    }

    pair<string, int> deleteMax(){ // remove the root/max element from the heap.
        pair<string, int> max = heap[0];
        swap(heap[0], heap[heap.size()-1]); // swap last element with max.
        size -= 1;
        heap.pop_back(); // delete max
        heapifyDown(0); // heapify down new root.
        return max;
    }

    void heapifyDown(int i){ //heapify down for deletion.

        int parent = i; // indices
        int left = 2*i + 1;
        int right = 2*i + 2;

        if (left < size && right < size){ // if node has two children.
            if (heap[left].second > heap[parent].second && heap[left].second > heap[right].second){
                parent = left; // if left is greater than parent and right, swap parent and left.
            }

            else if (heap[right].second > heap[parent].second && heap[right].second > heap[left].second){
                parent = right; // if right is greater than parent and left, swap parent and right.
            }

            else if (heap[left].second == heap[right].second && heap[left].second > heap[parent].second){
                parent = left; // if left and right are same size, but still bigger than parent.
            }
        }

        else if (left < size && right >= size){ // if only left child
            if (heap[left].second > heap[parent].second){
                parent = left;
            }
        }

        if (parent != i){ // update values based on index.
            swap(heap[parent], heap[i]); //
            heapifyDown(parent);
        }
    }

    vector<pair<string, int>>& getHeap(){ // getter function.
        return this->heap;
    }

    void kthLargest(){ // creates heap with just top 5 elements.
        for (int i=k-1; i>=0; i--){ // for the top k elements
            topK.push_back(deleteMax()); // add to topK heap (already sorted due to nature of heaps).
        }
    }

    map<string, int> getMap(string songName, SongNode& node){ // gets all common songs.
        node = SongNode::load(songName);
//        node.printSongs();
        return node.getSongs();

    }

    void printMap(map<string, int>& songs){ // prints all common songs.
        for (auto i: songs){
            cout << i.first << " " << i.second << endl;
        }
    }

    void printTopK(){ // prints top k songs.
        kthLargest();
        for (auto i: topK){
            cout << i.first << " " << i.second << endl;
        }
    }

    void printHeap(){
        for (auto i: heap){
            cout << i.first << " " << i.second << endl;
        }
    }

};

int main() {

    map<string, int> songs; // for testing.

    MaxHeap max; // class object.
    SongNode song;

    songs = max.getMap("!AST", song);


    for (auto i: songs){ // for every song in my map, insert into the heap.
        SongNode::parseReverse(i.first);
        max.insertNode(i.first, i.second);
    }

    max.printTopK();

    return 0;
}
