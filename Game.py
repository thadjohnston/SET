
import DeckHandler
import Player
import random

class Game(object):

    def __init__(self):
        self.players = ['greedy player']
        self.board = []
        D = DeckHandler.DeckHandler()
        self.deck = D.getDeck()
        self.shuffle()
        
    def start(self):
        for player in self.players:
            P = Player.LeastConflict(self.deck)
            P.playGame()

#def goNuts():
    #This is where I'll test shit eventually 

if __name__ == '__main__':
    g = Game()
    g.start()