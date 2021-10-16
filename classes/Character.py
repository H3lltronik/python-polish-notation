from enum import Enum

class CharacterType(Enum):
    Operator = 1
    Operand = 2
    OpenGroup = 3
    CloseGroup = 4

class Character:
    symbol = ''
    type = None

    def __init__(self, symbol: str, type: CharacterType):
        self.type = type
        self.symbol = symbol

    def __str__(self) -> str:
        return self.symbol

    def __add__(self, other):
        return str(self) + other
        
    def __radd__(self, other):
        return other + str(self)

class Operator(Character):
    priority: int

    def __init__(self, symbol: str, priority: int):
        super().__init__(symbol, CharacterType.Operand)
        self.priority = priority
