from player_list import PlayerList


class WinConditions:
    def __init__(self) -> None:
        self.wins_needed = 0
        self.player_list = PlayerList()

    
    #*compares choices and returns true/false to determine round winner
    def gesture_comparison(self, player_one, player_two):
        if player_one.choice == player_two.choice:
            return "This is a Draw!"
        elif player_one.choice == "rock":
            if player_two.choice == "scissors" or player_two.choice == "lizard":
                return True
            elif player_two.choice == "paper" or player_two.choice == "spock":
                return False    
        elif player_one.choice == "paper":
            if player_two.choice == "rock" or player_two.choice == "spock":
                return True
            elif player_two.choice == "scissors" or player_two.choice == "lizard":
                return False
        elif player_one.choice == "scissors":
            if player_two.choice == "paper" or player_two.choice == "lizard":
                return True
            elif player_two.choice == "rock" or player_two.choice == "spock":
                return False
        elif player_one.choice == "lizard":
            if player_two.choice == "spock" or player_two.choice == "paper":
                return True
            elif player_two.choice == "rock" or player_two.choice == "scissors":
                return False
        elif player_one.choice == "spock":
            if player_two.choice == "scissors" or player_two.choice == "rock":
                return True
            if player_two.choice == "lizard" or player_two.choice == "paper":
                return False

    #*determines how many wins are needed based on num of rounds 
    def how_many_wins(self, rounds):
        self.wins_needed = int(rounds / 2) + 1

    #*check to see if the req num of wins have been met
    def win_condition_check(self):
        for player in self.player_list.players:
            if player.score == self.wins_needed:
                return True
        else:
            return False
