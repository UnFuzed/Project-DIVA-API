from enums.difficulty import Difficulty

class Chart:
    def __init__(self, difficulty : Difficulty, starlevel : float):
        self.difficulty: Difficulty = difficulty
        self.starlevel: float = starlevel
