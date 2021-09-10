from win_conditions import WinConditions

class Game:
    def __init__(self) -> None:
        self.round_count = 0
        self.max_rounds = 0
        self.mode = 0
        self.run_game()
        self.Win_Condition = WinConditions()


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
        game_over = False
        self.WinConditions.how_many_wins(self.round_count)
        while not game_over:
            for players in self.Win_Condition.player_list.players:
                players.pick_gesture()
            player_one_result = self.Win_Condition.gesture_comparison(self.Win_Condition.player_list.players[0],self.Win_Condition.player_list.players[1])
            if player_one_result:
                self.Win_Condition.player_list.players[0].score += 1
            else:
                self.Win_Condition.player_list.players[1].score += 1
            game_over = self.Win_Condition.win_condition_check()  

    def display_winner(self):
        pass