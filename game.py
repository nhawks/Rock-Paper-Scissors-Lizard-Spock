from win_conditions import WinConditions

class Game:
    def __init__(self) -> None:
        self.round_count = 0
        self.max_rounds = 0
        self.mode = 0
        self.Win_Condition = WinConditions()
        self.run_game()



    def run_game(self):
        game_continue = "1"
        while game_continue == "1":
            self.game_mode()
            self.generate_players()
            self.round_count_option()
            self.display_rules()
            self.start_round()
            self.display_winner()
            game_continue = input("Would you like to play again? 1: Yes 2: No \n")


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
        self.Win_Condition.player_list.create_player(self.mode)
        
    def game_mode(self):
        self.mode = int(input("How many players: 1 or 2 \n"))
        return self.mode

    def round_count_option(self):
        # self.round_count = 3
        self.round_count = int(input("How many rounds would you like to play? \n"))
        self.Win_Condition.how_many_wins(self.round_count)

    def start_round(self):
        game_over = False
        self.Win_Condition.how_many_wins(self.round_count)
        while not game_over:
            for players in self.Win_Condition.player_list.players:
                players.pick_gesture()
            player_one_result = self.Win_Condition.gesture_comparison(self.Win_Condition.player_list.players[0],self.Win_Condition.player_list.players[1])
            if player_one_result:
                self.Win_Condition.player_list.players[0].score += 1
                print(f"Player One's {self.Win_Condition.player_list.players[0].choice} beats Player Two's {self.Win_Condition.player_list.players[1].choice} this round!")
            else:
                self.Win_Condition.player_list.players[1].score += 1
                print(f"Player Two's {self.Win_Condition.player_list.players[1].choice} beats Player One's {self.Win_Condition.player_list.players[0].choice} this round!")
            game_over = self.Win_Condition.win_condition_check()

    def display_winner(self):
        if self.Win_Condition.player_list.players[0].score > self.Win_Condition.player_list.players[1].score:
            print("Player One is the Winner!")
        if self.Win_Condition.player_list.players[1].score > self.Win_Condition.player_list.players[0].score:
            print("Player Two is the Winner!")