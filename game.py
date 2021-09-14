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

        #?game_continue is set to continue by default
        game_continue = "1"
        while game_continue == "1":

            #?clear terminal
            os.system('cls')

            #?display welcome msg
            self.display_rules()

            #?prompt user to select game mode (sp/mp)
            self.game_mode()

            #?generate players based on game-mode
            self.generate_players()

            #?determine how many rounds will be played and the min num of wins
            self.round_count_option()

            self.start_round()
            self.display_winner()

            #prompt user to see if they want to restart the game and clr terminal
            game_continue = input("Would you like to play again? Please enter - 1: Yes or 2: No\n")

    #*import the variable from the rules_art.py and displays welcome msg
    def display_rules(self):
        print(rules_art)
    
    #*takes int input from game_made to determine which players to generate (human vs AI / human vs human)
    def generate_players (self):
        self.Win_Condition.player_list.create_player(self.mode)

    #*used to select the game mode   
    def game_mode(self):
        self.mode = int(input('''\n
Select a game mode:
1 - Single Player 
2 - Multiplayer
Please select your game mode! 1 or 2:\n'''))
        return self.mode

    def round_count_option(self):
        self.round_count = int(input("Enter the number of rounds you'd like to play:\n"))
        self.Win_Condition.how_many_wins(self.round_count)

    def start_round(self):
        game_over = False
        self.Win_Condition.how_many_wins(self.round_count)
        current_round = 1
        while not game_over:

            #display the current round
            print("___________________________________________________________")
            print(f"ROUND: {current_round}/{self.round_count}")

            self.gesture_selection() #prompt user to select gestures
            self.round_result() #compare gesture to determine round winner
            self.display_score()

            current_round += 1
            #checks to see if the game is over based on the wins needed/rounds played
            game_over = self.Win_Condition.win_condition_check()

    #*loop through the list of players and prompts them to pick a gesture
    def gesture_selection(self):
        for players in self.Win_Condition.player_list.players:
            players.pick_gesture()

    #*determines who won the round and +1 to their score
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
        #Player One Score: 0/10 | Player Two Score: 0/10
        print(f"Player One score: {self.Win_Condition.player_list.players[0].score}/{self.Win_Condition.wins_needed} | "\
        f"Player Two score: {self.Win_Condition.player_list.players[1].score}/{self.Win_Condition.wins_needed}!\n")

    def display_winner(self):
        if self.Win_Condition.player_list.players[0].score > self.Win_Condition.player_list.players[1].score:
            print("Player One is the Winner!\n")
        if self.Win_Condition.player_list.players[1].score > self.Win_Condition.player_list.players[0].score:
            print("Player Two is the Winner!\n")