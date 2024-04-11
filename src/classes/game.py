from song import Song;

class Game:
    def __init__(self, englishname : str, japanesename : str, consoles : list[str], gametype : str, songs : list[Song]) -> None:
        self.EnglishName: str = englishname
        self.JapaneseName : str = japanesename
        self.console: list[str] = consoles
        self.gameType: str = gametype
        self.songs: list[Song] = songs
