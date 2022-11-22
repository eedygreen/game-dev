from .character import Character
from .charactertype import CharacterType

class Villian(Character):
    """Super Hero"""
    def __init__(self, name: str, attack_power: int, life: int) -> None:
        super().__init__(name, attack_power, life)
        self.role = CharacterType.VILLIAN
    
    def __str__(self) -> str:
        return(
            f"Villian => Name: {self.name}, Attack_Power: {self.attack_power}"
            f" Life: {self.life}"
        )