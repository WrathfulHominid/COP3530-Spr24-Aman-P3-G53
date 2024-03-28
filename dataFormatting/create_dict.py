
import pandas
import os
import time
import multiprocessing

from songnode import SongNode



class NodeConstructor :


    node_dict = {}

    num_finished = 0
    avg_time = 0
    total_time = 0



    @classmethod
    def Construct(cls, iterable) :

        filenames = [str(x) + ".csv" for x in iterable ]


        for playlist in filenames :

            #print( "File : " + playlist + " ; Number of nodes : " + str(len(cls.node_dict)) )

            #start_time = time.perf_counter()


            current_playlist = pandas.read_csv("parsed_playlists/" + playlist)

            song_dict = {}
            song_list = []




            for index in current_playlist.index :

                song = SongNode.parse_name( current_playlist.iloc[index]["track_name"] )
                album = SongNode.rmv_commas( current_playlist.iloc[index]["album_name"] )
                artist = SongNode.parse_name( current_playlist.iloc[index]["artist_name"] )

                song_dict[song] = (artist, album)
                song_list.append(song)



            for track in song_dict.keys() :


                if track not in cls.node_dict.keys() :

                    #track_filename = SongNode.parse_name(track)

                    if  track + '.csv' in os.listdir('tracks') :

                        node = SongNode.load(track)

                        cls.node_dict[track] = node

                    else :

                        cls.node_dict[track] = (SongNode(track, song_dict[track][0], song_dict[track][1]))




            i = 0

            while (i < len(song_list)) : 

                current_song = song_list[i]


                j = i + 1

                while j < len(song_list) :

                    cls.node_dict[current_song].add_shared(song_list[j])

                    cls.node_dict[song_list[j]].add_shared(current_song)

                    j += 1


                i += 1



        for j in cls.node_dict.values() :

            j.to_csv()





            #end_time = time.perf_counter()
            #run_time = end_time - start_time


            #if not 0 == cls.num_finished :

                #cls.avg_time = (cls.avg_time + run_time)/float(2)
            
            #else :
                #cls.avg_time = run_time

            #cls.num_finished += 1
            #cls.total_time += run_time

            #print( "Finished : " + str(cls.num_finished) + " ; Run time : " + str( '%.5f' % run_time ) + " ; Collective average time : " + str( '%.5f' % cls.avg_time ) )
            #print( "Total run time : " + str(cls.total_time) + " ; Estimated time to completion : " + str( (1000000 - cls.num_finished) * cls.avg_time / 60 ) + " minutes" )
            #print()




if __name__ == "__main__" :


    if not ("playlist_index.txt" in os.listdir()) :

        current = str(0)

        file = open("playlist_index.txt", mode = 'w')
        file.write( current )
        file.close()

    file = open("playlist_index.txt", mode = 'r')
    num = file.read()
    playlist_index = int( num )
    file.close()

    playlist_increment = 100

    num_cores = 8


    playlists_finished = 0

    avg_time = 0

    total_time = 0

    #manager = multiprocessing.Manager() 
    #node_dict = manager.dict()
    


    # TODO ---------- Allow shared node_dict across processes
    # TODO ---------- Ensure child processes complete on keyboard interrupt
    # TODO ---------- Find source of non-critical errors; corrupted data? memory mismanagement? (Extra fields in dataframes; int values of 'count' turning into string of dataframe object information)
    # TODO ---------- Go through current data, and rectify any corruption



    while len( os.listdir("parsed_playlists") ) > playlist_index :


        start_time = time.perf_counter()


        P_one = multiprocessing.Process( target = NodeConstructor.Construct, args = (range(playlist_index, playlist_index + playlist_increment), ) )
        P_one.start()
        playlist_index += playlist_increment


        P_two = multiprocessing.Process( target = NodeConstructor.Construct, args = (range(playlist_index, playlist_index + playlist_increment), ) )
        P_two.start()
        playlist_index += playlist_increment


        P_three = multiprocessing.Process( target = NodeConstructor.Construct, args = (range(playlist_index, playlist_index + playlist_increment), ) )
        P_three.start()
        playlist_index += playlist_increment


        P_four = multiprocessing.Process( target = NodeConstructor.Construct, args = (range(playlist_index, playlist_index + playlist_increment), ) )
        P_four.start()
        playlist_index += playlist_increment


        P_five = multiprocessing.Process( target = NodeConstructor.Construct, args = (range(playlist_index, playlist_index + playlist_increment), ) )
        P_five.start()
        playlist_index += playlist_increment


        P_six = multiprocessing.Process( target = NodeConstructor.Construct, args = (range(playlist_index, playlist_index + playlist_increment), ) )
        P_six.start()
        playlist_index += playlist_increment


        P_seven = multiprocessing.Process( target = NodeConstructor.Construct, args = (range(playlist_index, playlist_index + playlist_increment), ) )
        P_seven.start()
        playlist_index += playlist_increment


        P_eight = multiprocessing.Process( target = NodeConstructor.Construct, args = (range(playlist_index, playlist_index + playlist_increment), ) )
        P_eight.start()
        playlist_index += playlist_increment


        P_one.join()
        P_two.join()
        P_three.join()
        P_four.join()
        P_five.join()
        P_six.join()
        P_seven.join()
        P_eight.join()

    
        
        #for j in node_dict.values() :

            #j.to_csv()



        end_time = time.perf_counter()

        run_time = end_time - start_time

        playlists_finished += playlist_increment * num_cores

        file = open("playlist_index.txt", mode = 'w')
        file.write( str(playlist_index) )
        file.close()

        total_time += run_time

        avg_time = total_time / (playlists_finished)

        print( "Playlists finished : " + str(playlists_finished) + " ; Batch time : " + str('%.2f' % run_time) + " seconds" + " ; Time per playlist : " + str( '%.2f' % avg_time ) + " seconds" )
        print( "Total playlists finished : " + str(playlist_index) + " ; Total run time (minutes) : " + str('%.2f' % (total_time / 60)) + " ; Estimated time to completion : " + str( '%.2f' % (( (1000000 - (playlist_index) ) * avg_time) / 60 ) ) + " minutes" )
        print()




