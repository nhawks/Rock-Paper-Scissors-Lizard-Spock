import random
from players import Player


class Ai(Player):
    def __init__(self, name):
        super().__init__(name)

    # method override to randonmly select an item from the gestures list
    def pick_gesture(self):
        self.choice = random.choice(self.gestures)
        print("\nPlayer Two has made their choice...")
        return self.choice
