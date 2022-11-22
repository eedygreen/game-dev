from __future__ import annotations
from random import randint
from .models.superheros import SuperHeroModel
from .models.villians import VilliansModel
from .schemas.superhero import SuperHero
from .schemas.villians import Villian
from .schemas.life import Life
from .schemas.game_state import GameState
from .schemas.player import Player
from .constants import NUM_ATTEMPTS, WIN_MSG, LOST_MSG

#-----------------------Game---------------------------

class Game:

    def __init__(self, player: Player) -> None:
        self.player = player
        self.state = GameState.INITIALIZING
        self.superhero = SuperHeroModel()
        self.villian = VilliansModel()

    def __repr__(self) -> str:
        return f"<class of 'Game'>"

    def __str__(self) -> str:
        return f"Player: {self.player},\nState: {self.state},\nSuperHero: {self.superhero},\nVillian: {self.villian}"


    def win_or_lost_msg(self) -> Game:
        """Win or Lose Message"""
        print("=" * 45)
        if Life.hero_life >= Life.villian_life:
            self.state = GameState.WIN
            print(WIN_MSG)
        else:
            self.state = GameState.LOST
            print(LOST_MSG)
        return self
        
    #-----------------------------Attack--------------------------------

    def attack(self) -> Game:
        """The Attack"""
        self.state = GameState.IN_PROGRESS
        print("Starting Attack....")
        print(f"{self.state}")

        for attack_num in range(NUM_ATTEMPTS):
            hero_index = randint(0, len(self.superhero.all) - 1)
            villian_index = randint(0, len(self.villian.all) - 1)
            # current fighters
            current_superhero = self.superhero._get_superhero(hero_index)
            current_villian = self.villian._get_villian(villian_index)
            if current_superhero and current_villian:
                self.__do_attack(attack_num, current_superhero, current_villian)
            else:
                print("Error, No attack -> No Superhero nor villian")

        return self



    def __do_attack(self, attack: str, superhero: SuperHero, villian: Villian) -> None:
            # increase life
            """Simulate The Attack"""
            Life.increase_hero_life(superhero.life)
            Life.increase_villian_life(villian.life)

            print(
                f"Attack: {attack} => {superhero.name} is attacking  {villian.name}"
            )

            # attack
            Life.decrease_hero_life(villian.attack_power)
            Life.decrease_villian_life(superhero.attack_power)
