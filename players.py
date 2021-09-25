class Player:  # Parent
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.gestures = ("rock", "paper", "scissors", "lizard", "spock")
        self.choice = ""

    # *user picks gesture from gestures tuple
    def pick_gesture(self):
        invalid = True
        while invalid:
            print(f"\nRock | Paper | Scissors | Lizard | Spock\n")
            self.choice = input(
                f"{self.name} please pick a gesture:\n"
            ).lower()
            if self.gesture_validation():
                invalid = False
                return self.choice

    # *checks to see if user choice is in gestures if not re-prompts user
    def gesture_validation(self):
        if self.choice in self.gestures:
            return True
        else:
            return False
