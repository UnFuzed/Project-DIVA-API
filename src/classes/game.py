from song import Song
from enums.gametype import GameType

class Game:
    def __init__(self, englishName : str, japaneseName : str, consoles : list[str], gameType : GameType, songs : list[Song]) -> None:
        self.EnglishName: str = englishName
        self.JapaneseName : str = japaneseName
        self.console: list[str] = consoles
        self.gameType: GameType = gameType
        self.songs: list[Song] = songs


