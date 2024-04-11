from classes.song import Song
import os
import csv



def load_songs() -> list[Song]:

    songList: list = []

    with open(os.getcwd() + f"\csv\songs.csv", "r", encoding="UTF-8") as file:
        
        read: csv._reader = csv.reader(file)
            
        for line in read:
            songList.append(Song(line[0], line[1], line[2], line[3], line[4], line[5], line[6]))

    return songList

