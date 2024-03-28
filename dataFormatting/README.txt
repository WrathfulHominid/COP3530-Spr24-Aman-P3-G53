

Each song has it's own file in csv format, with the file name as the song name given in the json from spotify, but run through a parsing function to replace problematic characters.
I.E. "F*ck, it's good to be a gangsta'", would be replaced, using the regex-based methods parse_name()(py), or parseName()(cpp), into "F!ASTck!CMA it`s good to be a gangsta`" Note the '`' instead of normal quotes.
If the filename was too long (over 251 characters, plus four for '.csv') Then I removed the punctuation.

There are static methods for reversing the parsing, which returns a new string:
	py: SongNode.parse_reverse(name-to-be-reversed)
	cpp: SongNode::parseReverse(name-to-be-reversed);

To load a SongNode from file, you can use the static methods:
	py: SongNode.load(parsed-songname)
	cpp: SongNode::load(parsed-songname);

These return a SongNode object. So, you would write:
	py: node = SongNode.load(parsed-songname)
	cpp: SongNode node = SongNode::load(parsed-songname); 

This method automatically goes into the ./tracks/ subdirectory using for py the "os" library, and for cpp the <fstream> library.


Note that you can iterate over the subdirectory to find all song names in python:
	py: os.listdir("tracks") (yielding a list of strings)
	cpp: ???? (std::filesystem in c++17; this course specifies c++14 standard) (Maybe getenv() and system() from the <cstdlib>; here are some links)

		https://www.quora.com/How-do-you-create-a-folder-in-C#:~:text=In%20C%2B%2B%2C%20you%20cannot,or%20mkdir%20on%20Linux%2FUnix
		https://cplusplus.com/reference/cstdlib/system/
		https://cplusplus.com/reference/cstdlib/getenv/
		https://stackoverflow.com/questions/143174/how-do-i-get-the-directory-that-a-program-is-running-from
		https://cplusplus.com/forum/beginner/10292/
		https://www.geeksforgeeks.org/cpp-program-to-get-the-list-of-files-in-a-directory/


There's already over 300 thousand files, though, so you might want to use some fraction of them while developing.

**I can also run a python program to just get a master list of all the current track names, and write them to files (one for a, one for b...); then, a c++ program to read them all into a set.
That way you can just read out of the file on program startup. It'd be an easy way to subdivide the tracklist during development, too.


I removed commas, slashes, and quotes, from artist and album names.

You can get and print values utilizing the first bunch of methods in each file:
	py: node.(get | print)_name() ; node.(get | print)_artist() ; node.(get | print)_album() ; node.(get | print)_songs() ("get" returns a python dict)
	cpp: node.(get | print)Name() ; node.(get | print)Artist() ; node.(get | print)Album() ; node.(get | print)Songs() ("get" returns an ordered map)

There's also:
	py: node-object.get_count(parsed-songname)
	cpp: node-object.getCount(parsed-songname);
Which just returns the number of playlists that are shared between the node, and the argument song.

The reason the signatures for methods in each language is different is because I was trying to copy the pandas conventions, but when I went to cpp I decided I hated those.






