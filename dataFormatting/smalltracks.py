

# Creating a folder with exactly 100,000 tracks to see if it can be hosted on github
# To have everything called for in project outline available.


import os
import shutil



trackslist = os.listdir("tracks")


for i in range(0, 100000) :

    shutil.copy("tracks/" + trackslist[i], "new/" + trackslist[i])
    