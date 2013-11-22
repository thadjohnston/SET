
import Deck
import Player
import random

class Game(object):

    def __init__(self):
        self.players = ['greedy player']
        self.board = []
        D = Deck.Deck()
        self.deck = D.getDeck()
        random.shuffle(self.deck)
        
    def start(self):
        for player in self.players:
            P = Player.Player(self.deck)
            P.playGame()


if __name__ == '__main__':
    g = Game()
    g.start()