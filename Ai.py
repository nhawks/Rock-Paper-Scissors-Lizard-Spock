from players import Player
import random


class Ai (Player):
    def __init__(self):
        
        super().__init__(self)

    
    def random_choice(self):
        self.choice = random.choice(self.gestures())
        return self.choice