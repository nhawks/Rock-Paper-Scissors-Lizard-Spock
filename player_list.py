from Ai import Ai
from players import Player


class PlayerList:
    def __init__(self):
        self.players = []


    def create_player(self, mode):
        if mode == 1:
         player_one = Player("Player One")
         player_ai = Ai()
         self.players = [player_one, player_ai]
        
        if mode == 2:
         player_one = Player("Player One")
         player_two = Player("Player Two")
         self.players = [player_one, player_two]