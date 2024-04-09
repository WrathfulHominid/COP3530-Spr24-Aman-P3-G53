#include <iostream>
#include <map>
#include <vector>
using namespace std;

class MaxHeap{
private:
    vector<pair<string, int>> heap; // max heap storing song name and num shared playlists.
    int k = 5; // max size of heap;
    int size = 0; // initial size, can change.

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

    pair<string, int> deleteMax(){
        pair<string, int> max = heap[0];
        swap(heap[0], heap[heap.size()-1]);
        size -= 1;
        heap.pop_back();
        heapifyDown(0);
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

    vector<pair<string, int>> kthLargest(){
        vector<pair<string, int>> topK;
        for (int i=k-1; i>=0; i--){
            topK.push_back(deleteMax());
        }

        return topK;
    }

};

int main() {

    map<string, int> songs; // for testing.

    songs["a"] = 10;
    songs["b"] = 15;
    songs["c"] = 7;
    songs["d"] = 9;
    songs["e"] = 27;
    songs["f"] = 300;
    songs["g"] = 2;

    MaxHeap max; // class object.

    for (auto i: songs){ // for every song in my map, insert into the heap.
        max.insertNode(i.first, i.second);
    }

    vector<pair<string, int>> k = max.kthLargest();

    for (int i=0; i<k.size(); i++){
        cout << k[i].first << " " << k[i].second << endl;
    }

    return 0;
}
