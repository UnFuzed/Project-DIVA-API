from classes.song import Song
from classes.module import Module
from enums.gametype import GameType
from enums.console import Console
from datetime import date

class Game:

    def __init__(self, englishName : str, japaneseName : str, consoles : list[Console], gameType : GameType, songs : list[Song], modules : list[Module], releaseDate : date) -> None:
        """A class to represent a game in the Hatsune Miku: Project DIVA series of games

        Args:
            englishName (str): The english name of the game
            japaneseName (str): The japanese name of the game 
            consoles (list[Console]): A list of consoles the game can be played on
            gameType (GameType): The type of gameplay that the game uses
            songs (list[Song]): A list of songs in the game
            modules (list[Module]): A list of modules in the game
            releaseDate (datetime)): The release date of the game
        """

        self.englishName: str = englishName
        self.japaneseName : str = japaneseName
        self.Console: list[Console] = consoles
        self.gameType: GameType = gameType
        self.songs: list[Song] = songs
        self.modules: list[Module] = modules
        self.releaseDate: date = releaseDate


