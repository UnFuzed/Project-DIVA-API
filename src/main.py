from classes.song import Song
from classes.game import Game
from classes.module import Module

from enums.gametype import GameType

from load import load_songs

from datetime import date

def Main() -> None:

    
    testsong = Song("Love is War", "恋は戦争", "ryo", "ryo", date(2008, 2, 22), 1, None)
    testmodule = Module("Supreme", "ダミー", None)

    game = Game("F", "F", ["VITA", "PS3"], GameType.Console, [testsong], [testmodule], "Dec test")
    print(game.songs[0].releaseDate)

    songlist: list[Song] = load_songs()
   
    


if __name__ == "__main__":
    Main()  