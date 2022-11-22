from enum import Enum, auto

class GameState(Enum):
    """Game State"""
    INITIALIZING = auto()
    IN_PROGRESS = auto()
    WIN = auto()
    LOST = auto()

