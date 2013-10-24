
import Deck
import random

class Game(object):

    def __init__(self):
        self.players = []
        self.board = []
        D = Deck()
        shuffledDeck = D.getDeck()
        D.shuffle(shuffledDeck)


if __name__ == '__main__':
    #SK = Game()
    for i in range(10):
        print(i)