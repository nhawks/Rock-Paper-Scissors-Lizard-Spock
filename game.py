from win_conditions import WinConditions
from rules_art import rules_art
import os

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
            os.system('cls')
            self.display_rules()
            self.game_mode()
            self.generate_players()
            self.round_count_option()
            self.start_round()
            self.display_winner()
            game_continue = input("Would you like to play again? Please enter - 1 (yes) or 2 (no):\n")


    def display_rules(self):
        print(rules_art)
    
    def generate_players (self):
        self.Win_Condition.player_list.create_player(self.mode)
        
    def game_mode(self):
        self.mode = int(input('''\n
Select a game mode:
1 - Single Player 
2 - Multiplayer
Please enter one number from above:\n'''))
        return self.mode

    def round_count_option(self):
        self.round_count = int(input("Enter the number of rounds you'd like to play:\n"))
        self.Win_Condition.how_many_wins(self.round_count)

    def start_round(self):
        game_over = False
        self.Win_Condition.how_many_wins(self.round_count)
        current_round = 1
        while not game_over:
            print("___________________________________________________________")
            print(f"ROUND: {current_round}/{self.round_count}")
            self.gesture_selection()
            self.round_result()
            self.display_score()
            current_round += 1
            game_over = self.Win_Condition.win_condition_check()

    def gesture_selection(self):
        for players in self.Win_Condition.player_list.players:
            players.pick_gesture()

    def round_result(self):
        player_one_result = self.Win_Condition.gesture_comparison(self.Win_Condition.player_list.players[0],self.Win_Condition.player_list.players[1])
        if player_one_result:
            self.Win_Condition.player_list.players[0].score += 1
            print(f"\nPlayer One's {self.Win_Condition.player_list.players[0].choice} beats Player Two's {self.Win_Condition.player_list.players[1].choice} this round! \n")
        elif player_one_result == False:
            self.Win_Condition.player_list.players[1].score += 1
            print(f"\nPlayer Two's {self.Win_Condition.player_list.players[1].choice} beats Player One's {self.Win_Condition.player_list.players[0].choice} this round! \n")
        else:
            print("\nThis round is a draw! \n")   

    def display_score(self):
        print(f"Player One score: {self.Win_Condition.player_list.players[0].score}/{self.Win_Condition.wins_needed} | "\
        f"Player Two score: {self.Win_Condition.player_list.players[1].score}/{self.Win_Condition.wins_needed}!")

    def display_winner(self):
        if self.Win_Condition.player_list.players[0].score > self.Win_Condition.player_list.players[1].score:
            print("Player One is the Winner!\n")
        if self.Win_Condition.player_list.players[1].score > self.Win_Condition.player_list.players[0].score:
            print("Player Two is the Winner!\n")