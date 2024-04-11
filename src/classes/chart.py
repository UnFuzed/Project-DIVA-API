from enums.difficulty import Difficulty

class Chart:
    def __init__(self, difficulty : Difficulty, starLevel : float):
        self.difficulty: Difficulty = difficulty
        self.starLevel: float = starLevel


