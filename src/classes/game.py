from song import Song
from enums.gametype import GameType
from enums.console import Console

class Game:

    def __init__(self, englishName : str, japaneseName : str, consoles : list[Console], gameType : GameType, songs : list[Song], releaseDate : str) -> None:
        """A class to represent a game in the Hatsune Miku: Project DIVA series of games

        Args:
            englishName (str): The english name of the game
            japaneseName (str): The japanese name of the game 
            consoles (list[Console]): A list of consoles the game can be played on
            gameType (GameType): The type of gameplay that the game uses
            songs (list[Song]): A list of songs in the game
            releaseDate (str): The release date of the game
        """

        self.englishName: str = englishName
        self.japaneseName : str = japaneseName
        self.Console: list[str] = consoles
        self.gameType: GameType = gameType
        self.songs: list[Song] = songs
        self.releaseDate: str = releaseDate
