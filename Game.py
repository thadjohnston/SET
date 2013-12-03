
import DeckHandler
import Player
import random

class Game(object):

    def __init__(self):
        D = DeckHandler.DeckHandler()
        D.shuffle()
        self.deck = D.getDeck()
        
        
    def start(self):
        for i in range(1000):
            D = DeckHandler.DeckHandler()
            D.shuffle()
            self.deck = D.getDeck()
            P = Player.StrategicPlayer(self.deck, Player.getLeastSet, False)
            sets = P.playGame()
            completeGames = 0
            if len(sets) == 27:
                completeGames += 1
        print('Number of complete games: ' + str(completeGames))


def goNuts():
    #This is where I'll test shit eventually 
    #Play Greedy
    
    #Play Strategy: getLeastCard
    
    
    #Play Strategy: getMostCard
    
    
    #Play Strategy: getLeastSet
    
    
    #Play Strategy: getMostSet
    
    return
    

if __name__ == '__main__':
    g = Game()
    g.start()