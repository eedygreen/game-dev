from game.schemas.superhero import SuperHero

class SuperHeroModel:
    """Base Class Super Hero"""
    def __init__(self) -> None:
        self.all: list[SuperHero] = self._get_all_superheros()
    
    def __str__(self) -> str:
        name: list[SuperHero] = []
        for hero in self.all:
            name.append(hero.name)
        return f"{name}"
    
    def _get_all_superheros(self) -> list[SuperHero]:
        """Get All Super Heros"""
        ironman = SuperHero(name="Ironman", attack_power=300, life=1200)
        blackwidow = SuperHero(name="Blackwidow", attack_power=200, life=1000)
        spiderman = SuperHero(name="Spiderman", attack_power=250, life=1100)
        hulk = SuperHero(name="Hulk", attack_power=350, life=1350)
        superheros: list[str] = [ironman, blackwidow, spiderman, hulk]
        return superheros

    def _get_superhero(self, index: int) -> SuperHero | None:
        """Get a random super hero"""
        if index < len(self.all):
            return self.all[index]
        else:
            return None