from player_list import Player


class PlayerList:
    def __init__(self):
        players = []


    def create_player(self):
         player_one = Player()
         player_two = Player()
         self.players = [player_one, player_two]