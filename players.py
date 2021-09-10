

class Player:
    def __init__ (self, name):
        self.name = name
        self.score = 0
        self.gestures = ("rock", "paper", "scissors", "lizard", "spock")
        self.choice = ""


    def pick_gesture(self):
        print(self.gestures)
        self.choice = input(f'{self.name} please pick a gesture! \n')
        if self.gesture_validation():
            return self.choice

    def gesture_validation(self):
        if self.choice in self.gestures:
            return True
        else:
            return False   