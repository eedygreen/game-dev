from game.schemas.villians import Villian

class VilliansModel:
    """Base class for all villians"""

    def __init__(self) -> None:
        self.all = self._get_all_villians()

    def __str__(self) -> str:
        name: list[Villian] = []
        for villian in self.all:
            name.append(villian.name)
        return f"{name}"

    def _get_all_villians(self) -> list[Villian]:
        """Get All villians"""
        thanos = Villian(name="Thanos", attack_power=400, life=1500)
        redskull = Villian(name="Redskull", attack_power=350, life=1300)
        poxima = Villian(name="Poxima", attack_power=320, life=1200)
        super_villians: list[str] = [thanos, redskull, poxima]

        return super_villians

    def _get_villian(self, index: int) -> Villian | None:
        """Get a random villian"""
        if index < len(self.all):
            return self.all[index]
        else:
            return None
