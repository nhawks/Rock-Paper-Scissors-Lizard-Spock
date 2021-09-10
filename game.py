class Game:
    def __init__(self) -> None:
        self.round_count = 0
        self.mode = 0
        self.run_game()



    def run_game(self):
        pass

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

    def game_mode(self):
        pass

    def round_count_option(self):
        pass

    def start_round(self):
        pass

    def display_winner(self):
        pass