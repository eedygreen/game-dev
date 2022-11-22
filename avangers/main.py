from game import Game, Player


def main() -> None:
    """Main function"""
    
    player_1 = Player("John", "Doe")
    player_2 = Player("Maryam", "eedy")
    game = Game(player=player_1)
    game_2 = Game(player=player_2)
    print(game.state)
    
    game_on = game.attack().win_or_lost_msg()
    game2_on = game_2.attack().win_or_lost_msg()
    print(game_on.state)
    print(game2_on.state)

main()