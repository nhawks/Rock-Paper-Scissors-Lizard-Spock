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
            self.display_rules()
            self.game_mode()
            self.generate_players()
            self.round_count_option()
            self.start_round()
            self.display_winner()
            game_continue = input("Would you like to play again? 1: Yes 2: No \n")


    def display_rules(self):
        print(
'''Welcome to: ROCK vs PAPER vs SCISSORS vs LIZARD vs SPOCK\n
The rules are simple pick an item from the list at start of each round.
Depending on your choice and your opponent's choice will decide who wins!
You can play against AI or a friend and pick how many rounds you'd like to play.\n

GESTURE BREAKDOWN\n
________________________________________________________
Rock crushes Scissors       | Scissors cuts Paper\n
Paper covers Rock           | Rock crushes Lizard\n
Lizard poisons Spock        | Spock smashes Scissors\n
Scissors decapitates Lizard | Lizard eats Paper\n
Paper disproves Spock       | Spock vaporizes Rock
_________________________________________________________\n''')
    
    def generate_players (self):
        self.Win_Condition.player_list.create_player(self.mode)
        
    def game_mode(self):
        self.mode = int(input("How many players: 1 or 2 \n"))
        return self.mode

    def round_count_option(self):
        self.round_count = int(input("How many rounds would you like to play? \n"))
        self.Win_Condition.how_many_wins(self.round_count)

    def start_round(self):
        game_over = False
        self.Win_Condition.how_many_wins(self.round_count)
        while not game_over:
            self.gesture_selection()
            self.round_result()
            self.display_score()
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
        print(f"Player One score: {self.Win_Condition.player_list.players[0].score}/{self.Win_Condition.wins_needed}!\n")
        print(f"Player Two score: {self.Win_Condition.player_list.players[1].score}/{self.Win_Condition.wins_needed}!\n")

    def display_winner(self):
        if self.Win_Condition.player_list.players[0].score > self.Win_Condition.player_list.players[1].score:
            print("Player One is the Winner!\n")
        if self.Win_Condition.player_list.players[1].score > self.Win_Condition.player_list.players[0].score:
            print("Player Two is the Winner!\n")