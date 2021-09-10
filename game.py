from player_list import PlayerList
from win_conditions import WinConditions

class Game:
    def __init__(self) -> None:
        self.round_count = 0
        self.max_rounds = 0
        self.mode = 0
        self.run_game()
        WinConditions()
        PlayerList()
        


    def run_game(self):
        self.game_mode()
        self.generate_players()
        self.round_count_option()
        self.display_rules()
        self.start_round()


    def display_rules(self):
        print('''
        \nRock crushes Scissors
        \nScissors cuts Paper
        \nPaper covers Rock
        \nRock crushes Lizard
        \nLizard poisons Spock
        \nSpock smashes Scissors
        \nScissors decapitates Lizard
        \nLizard eats Paper
        \nPaper disproves Spock
        \nSpock vaporizes Rock\n
        ''')
    
    def generate_players (self):
        self.PlayerList.create_player(self.mode)
        
    def game_mode(self):
        self.mode = int(input("How many players: 1 or 2"))
        return self.mode

    def round_count_option(self):
        self.round_count = 3
        # self.round_count = int(input("How many rounds would you like to play?"))

    def start_round(self):
        self.how_many_wins(self.round_count)

    def display_winner(self):
        pass