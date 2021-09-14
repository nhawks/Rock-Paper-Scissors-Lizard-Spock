from Ai import Ai
from players import Player


class PlayerList:
    def __init__(self):
        self.players = []


    #*based on int input from game.game_mode determine if single/multi-player
    def create_player(self, mode):
        #Single-Player: Human vs AI(calls child class Parent)
        if mode == 1:
         player_one = Player("Player One")
         player_ai = Ai("Player Two")
         self.players = [player_one, player_ai]
        
        #Multiplayer: Human vs Human
        elif mode == 2:
         player_one = Player("Player One")
         player_two = Player("Player Two")
         self.players = [player_one, player_two]