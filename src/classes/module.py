from enums.aura import Aura

class Module:
    def __init__(self, englishName : str, japaneseName : str, aura : Aura) -> None: 
        """A class to represent a song in the Hatsune Miku: Project DIVA series of games

        Args:
            englishName (str): _description_
            japaneseName (str): _description_
            aura (Aura): _description_
        """
        self.englishName: str = englishName
        self.japaneseName: str = japaneseName
        self.aura: Aura = aura