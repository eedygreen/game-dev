class Life:
    hero_life = 0
    villian_life = 0

    @staticmethod
    def increase_hero_life(life: int) -> None:
        """Increase hero life"""
        Life.hero_life += life

    @staticmethod
    def decrease_hero_life(life: int) -> None:
        """Decrease hero life"""
        Life.hero_life -= life

    @staticmethod
    def increase_villian_life(life: int) -> None:
        """Increase villian life"""
        Life.villian_life += life
    
    @staticmethod
    def decrease_villian_life(life: int) -> None:
        """Decrease villian life"""
        Life.villian_life -= life
#----------------------life---------------------------