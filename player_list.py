from Ai import Ai
from player_list import Player


class PlayerList:
    def __init__(self):
        self.players = []


    def create_player(self, mode):
        if mode == 1:
         player_one = Player()
         player_ai = Ai()
         self.players = [player_one, player_ai]
        
        if mode == 2:
         player_one = Player()
         player_two = Player()
         self.players = [player_one, player_two]