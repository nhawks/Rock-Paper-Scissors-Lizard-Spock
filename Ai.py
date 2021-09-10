from players import Player
import random


class Ai (Player):
    def __init__(self, name):
        super().__init__(name)

    
    def random_choice(self):
        self.choice = random.choice(self.gestures())
        return self.choice