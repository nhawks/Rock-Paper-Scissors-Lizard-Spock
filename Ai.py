import random
from players import Player


class Ai (Player):
    def __init__(self, name):
        super().__init__(name)

    
    def pick_gesture(self):
        self.choice = random.choice(self.gestures)
        return self.choice