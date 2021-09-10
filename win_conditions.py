from player_list import PlayerList


class WinConditions:
    def __init__(self) -> None:
        self.wins_needed = 0

    
    def gesture_comparison(self, player_one, player_two):
        if player_one.choice == "rock":
            if player_two.choice == "scissors" or "lizard":
                return True
            elif player_two.choice == "paper" or "spock":
                return False    
        elif player_one.choice == "paper":
            if player_two.choice == "rock" or "spock":
                return True
            elif player_two.choice == "scissors" or "lizard":
                return False
        elif player_one.choice == "scissors":
            if player_two.choice == "paper" or "lizard":
                return True
            elif player_two.choice == "rock" or "spock":
                return False
        elif player_one.choice == "lizard":
            if player_two.choice == "spock" or "paper":
                return True
            elif player_two.choice == "rock" or "scissors":
                return False
        elif player_one.choice == "spock":
            if player_two.choice == "scissors" or "rock":
                return True
            if player_two.choice == "lizard" or "paper":
                return False

    def how_many_wins(self, rounds):
        if rounds == 3:
            self.wins_needed = 2  

    def win_condition_check(self):
        for player in self.PlayerList.players:
            if player.score == self.wins_needed:
                return True
        else:
            return False
