

#ifndef SONGNODE_CPP
#define SONGNODE_CPP


#include <regex>
#include <map>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <utility>
#include <vector>
#include <unordered_set>

using namespace std;


struct SongNode
{



string _name;
string _artist;
string _album;

map<string, int> _shared;



//
string getName()
{

	return this->_name;

}


//
void printName()
{

	cout << this->_name << '\n';

}


//
string getArtist()
{

	return this->_artist;

}


//
void printArtist()
{

	cout << this->_artist << '\n';

}


//
string getAlbum()
{

	return this->_album;

}


//
void printAlbum()
{

	cout << this->_album << '\n';

}


//
map<string, int> getSongs()
{

	return this->_shared;

}


//
void printSongs()
{

	cout << "\nSong : Count\n\n";


	for (auto iter = this->_shared.begin(); iter != this->_shared.end(); iter++)
	{

		cout << get<0>(*iter) << " : " << get<1>(*iter) << endl;

	}


}


//
bool findSong(string song)
{

	auto found = this->_shared.find(song);


	if (found == this->_shared.end())
	{

		return false;

	}

	else
	{
		return true;
	}

}


//
int getCount(string songname)
{

	auto found = this->_shared.find(songname);

	if (found != this->_shared.end())
	{
		return get<1>(*found);
	}
	else
	{
		return 0;
	}

}


//
static bool valueCompare(pair<string, int>& lhs, pair<string, int>& rhs)
{

	return lhs.second < rhs.second;

}


//
unordered_set<string> getHighest(int num = 1)
{


	vector<pair<string, int>> list;

	unordered_set<string> output;


	for (auto iter = this->_shared.begin(); iter != this->_shared.end(); iter++)
	{

		list.push_back(pair(*iter));

	}

	sort(list.begin(), list.end(), valueCompare);

	
	if ( list.size() < num)
	{
		num = list.size();
	}


	for (int index = list.size() - num; index < list.size(); index++)
	{

		output.insert(get<0>(list[index]));

	}


	return output;

}


void addShared(string shared)
{

	if (this->findSong(shared))
	{
		this->_shared[shared]++;
	}
	else
	{
		this->_shared[shared] = 1;
	}

}


static string parseName(string name)
{


	regex next("\\\\");
	
	name = regex_replace(name, next, "!BSL");


	next = "/";

	name = regex_replace(name, next, "!FSL");


	next = ",";

	name = regex_replace(name, next, "!CMA");


	next = "\"";

	name = regex_replace(name, next, "`");


	next = "'";

	name = regex_replace(name, next, "`");


	next = "\\?";

	name = regex_replace(name, next, "!QST");


	next = "\\*";

	name = regex_replace(name, next, "!AST");


	next = "\\|";

	name = regex_replace(name, next, "!BAR");


	next = ":";

	name = regex_replace(name, next, "!SMI");


	next = "<";

	name = regex_replace(name, next, "!LNG");


	next = ">";

	name = regex_replace(name, next, "!RNG");


	next = "\\.";

	name = regex_replace(name, next, "!PRD");


	// Trailing whitespace
	next = "\\s+$";

	name = regex_replace(name, next, "");


	if (251 > name.size())
	{

		name = rmvPunct(name);

	}


	return name;


}


static string parseReverse(string name)
{

	regex next("!BSL");

	name = regex_replace(name, next, "\\");

	next = "!FSL";

	name = regex_replace(name, next, "/");

	next = "!CMA";

	name = regex_replace(name, next, ",");

	next = "`";

	name = regex_replace(name, next, "'");

	next = "!QST";

	name = regex_replace(name, next, "?");

	next = "!AST";

	name = regex_replace(name, next, "*");

	next = "!BAR";

	name = regex_replace(name, next, "|");

	next = "!SMI";

	name = regex_replace(name, next, ":");

	next = "!LNG";

	name = regex_replace(name, next, "<");

	next = "!RNG";

	name = regex_replace(name, next, ">");

	next = "!PRD";

	name = regex_replace(name, next, ".");


	return name;


}


static string rmvCommas(string input)
{

	regex next("\\\\");

	input = regex_replace(input, next, "/");

	next = ",";

	input = regex_replace(input, next, ";");

	next = "'";

	input = regex_replace(input, next, "`");

	next = "\"";

	input = regex_replace(input, next, "`");


	return input;

}


void readCsv(string songname)
{

	this->_name = songname;

	string filepath = "tracks/" + songname + ".csv";


	ifstream file;

	file.open(filepath);


	string line_string;

	getline(file, line_string, '\n');


	istringstream line_stream(line_string);

	string next;

	getline(line_stream, next, ',');


	this->_artist = next;


	getline(line_stream, next);

	this->_album = next;


	getline(file, line_string, '\n');

	string count;


	while (!line_string.empty())
	{
	
		line_stream = istringstream(line_string);

		getline(line_stream, next, ',');

		getline(line_stream, count);

		if (!count.empty())
		{
			this->_shared[next] = stoi(count);
		}


		getline(file, line_string, '\n');
		

	}

	file.close();


}


void toCsv(bool testing = false)
{

	string filepath = this->_name + ".csv";


	if (!testing)
	{

		filepath = "tracks/" + filepath;

	}


	ofstream file(filepath, ios::out | ios::trunc);

	file << this->_artist << ',' << this->_album << endl;

	
	for (auto iter = this->_shared.begin(); iter != this->_shared.end(); iter++)
	{

		file << get<0>(*iter) << ',' << get<1>(*iter) << endl;

	}


	file.close();


}


static string rmvPunct(string name)
{

	regex next("!BSL");

	name = regex_replace(name, next, "");

	next = "!FSL";

	name = regex_replace(name, next, "");

	next = "!CMA";

	name = regex_replace(name, next, "");

	next = "`";

	name = regex_replace(name, next, "");

	next = "!QST";

	name = regex_replace(name, next, "");

	next = "!AST";

	name = regex_replace(name, next, "");

	next = "!BAR";

	name = regex_replace(name, next, "");

	next = "!SMI";

	name = regex_replace(name, next, "");

	next = "!LNG";

	name = regex_replace(name, next, "");

	next = "!RNG";

	name = regex_replace(name, next, "");

	next = "!PRD";

	name = regex_replace(name, next, "");


	return name;


}


static SongNode load(string songname)
{

	SongNode rhs;

	rhs.readCsv(songname);

	return rhs;

}




};



#endif // SONGNODE_CPP
