from enums.aura import Aura

class Song:
    def __init__(self, englishName : str, japaneseName : str, englishArtist : str, japaneseArtist : str, releaseDate : str, pvid : int, aura : Aura) -> None:
        """A class to represent a module in the Hatsune Miku: Project DIVA series of games

        Args:
            englishName (str): The english name of the song
            japaneseName (str): The japanese name of the song
            englishProducer (str): The english name of the producer
            japaneseProducer (str): The japanese name of the producer
            releaseDate (str): The release date of the song
            pvid (int): The PV ID number for the song
            aura (Aura): The aura type in Hatsune Miku: Project DIVA X
        """
        self.englishName: str = englishName
        self.japaneseName: str = japaneseName
        self.englishArtist: str = englishArtist
        self.japaneseArtist: str = japaneseArtist
        self.releaseDate: str = releaseDate
        self.pvid: int = pvid
        self.aura: Aura = aura
        


        
        