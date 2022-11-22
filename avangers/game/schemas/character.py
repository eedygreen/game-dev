class Character:
    """Character"""
    def __init__(self, name: str, attack_power: int, life: int) -> None:
        self.name = name
        self.attack_power = attack_power
        self.life = life

    def __str__(self) -> str:
        print(f"Name: {self.name}, Attack_Power: {self.attack_power}, Life: {self.life}")

#________________________________________Role________________________________________