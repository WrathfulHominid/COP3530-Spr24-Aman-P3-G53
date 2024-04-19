import boto3
import pandas as pd
from io import StringIO
import re
import os
import json

class SongNode :


    def __init__(self, name = "", artist = "", album = ""):

        self._name = name
        self._artist = artist
        self._album = album
        self._shared = dict()


    def get_name(self):

        return self._name


    def print_name(self) :

        print(self.get_name())


    def get_artist(self) :

        return self._artist


    def print_artist(self) :

        print(self.get_artist())


    def get_album(self) :
    
        return self._album


    def print_album(self) :

        print(self.get_album())


    def get_songs(self):

        return self._shared


    def print_songs(self) :

        print(self.get_songs())


    def find_song(self, song) :

        return song in self._shared.keys()


    def get_count(self, song) :


        if self.find_song(song) :
    
            return self._shared[song]

        else :

            return 0

    

    def get_highest(self, num=1) :

        return [x[0] for x in reversed(sorted(self.get_songs().items(), key = lambda y : y[1]))][0 : num]
        

    def add_shared(self, shared):
    

        if self.find_song(shared) :

            self._shared[shared] = int(self._shared[shared]) + 1

        else :

            self._shared[shared] = 1


    @staticmethod
    def parse_name(name) :

        
        # Parsing out illegal filename characters


        replacements = {
                        '\\' : '!BSL',
                        '/' : '!FSL',
                        ',' : '!CMA',
                        "'" : '`',
                        '"' : '`',
                        '?' : '!QST',
                        '*' : '!AST',
                        '|' : '!BAR',
                        ':' : '!SMI',
                        '<' : '!LNG',
                        '>' : '!RNG',
                        '.' : '!PRD'
                        }

        regex = re.compile("%s" % "|".join( map( re.escape, replacements.keys() ) ) )
                        
        output = regex.sub( lambda found : str( replacements[found.group()] ), str( name ) )
        output = output.strip()


        if len(output) > 251 :

            output = SongNode.rmv_punct(output)


        return output

    @staticmethod
    def parse_reverse(name) :

        replacements = {
                        '!BSL' : '\\',
                        '!FSL' : '/',
                        '!CMA' : ',',
                        '`' : "'",
                        '!QST' : '?',
                        '!AST' : '*',
                        '!BAR' : '|',
                        '!SMI' : ':',
                        '!LNG' : '<',
                        '!RNG' : '>',
                        '!PRD' : '.'
                        }

        regex = re.compile("%s" % "|".join( replacements.keys() ) )
                        
        return  regex.sub( lambda found : replacements[found.group()], name )
       

    
    @staticmethod
    def rmv_commas(string) :


        replacements = {
                        '\\' : '/',
                        ',' : ';',
                        '"' : '`',
                        "'" : '`'
                        }

        regex = re.compile("%s" % "|".join( map(re.escape, replacements) ) )
        return regex.sub( lambda found : replacements[found.group()], string )



    def read_csv(self, songname, testing = False) :

        print("Current working directory:", os.getcwd())
        
        with open('../config.json', 'r') as config_file:
            config = json.load(config_file)

        session = boto3.Session(
            aws_access_key_id=config['aws_access_key_id'],
            aws_secret_access_key=config['aws_secret_access_key'],
            region_name=config['region_name']
        )

        s3 = session.client('s3')
        client = boto3.client('s3')
        
        bucket_name = 'tracksdataset'
        paginator = s3.get_paginator('list_objects_v2')
        pages = paginator.paginate(Bucket=bucket_name)
        objKeys = []
        
        found = False
        
        for page in pages:
            for obj in page.get('Contents', []):
                if(obj["Key"].replace('.csv', '') == songname):
                    objKeys.append(obj["Key"])
                    found = True
                    break
            if found:
                break
        
        csv_obj = client.get_object(Bucket=bucket_name, Key=objKeys[0])
        
        body = csv_obj['Body']
        csv_string = body.read().decode('utf-8')

        df = pd.DataFrame(StringIO(csv_string))

        columns = list(df)
            
        for i, j in df.iterrows():
            if(i == 0):
                continue
            s = ""
            for k in columns:
                s += df[k][i]
            p = s.split(",")
            self._shared[p[0]] = int(p[1].replace('\r\n', ''))
        


    def to_csv(self, filepath = None, testing = False) :

        name = self.get_name()

        #name = SongNode.parse_name(name)


        if (False == testing) and (None == filepath) :

            filepath = 'tracks/' + name + '.csv'

        elif (True == testing) and (None == filepath) :

            filepath = name + '.csv'

        
        
        file = open(filepath, mode='w', encoding='utf-8')

        file.write(self._artist + "," + self._album + '\n')

        
        for song, count in self._shared.items() :

            file.write(song + ',' + str( count ) + '\n')

        file.close()


    @staticmethod
    def rmv_punct(self, string) :

 
        replacements = {
                        '!BSL' : '',
                        '!FSL' : '',
                        '!CMA' : '',
                        '`' : "",
                        '!QST' : '',
                        '!AST' : '',
                        '!BAR' : '',
                        '!SMI' : '',
                        '!LNG' : '',
                        '!RNG' : '',
                        '!PRD' : ''
                        }

        regex = re.compile("%s" % "|".join( map(re.escape, replacements) ) )

        return regex.sub( lambda found : replacements[found.group()], string )
        


    @staticmethod
    def load(songname, testing = False) :

        lhs = SongNode()

        lhs.read_csv(songname, testing = testing)

        return lhs



