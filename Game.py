
import DeckHandler
import Player
import random
import copy

class Game(object):

    def __init__(self):
        D = DeckHandler.DeckHandler()
        D.shuffle()
        self.deck = D.getDeck()
        
        
    def start(self):
        #for player in self.players:
        P = Player.StrategicPlayer(self.deck)
        sets = P.playGame()
        completeGames = 0
        if len(sets) == 27:
            completeGames += 1
        print('Number of complete games: ' + str(completeGames))


def goNuts(howmany):
    #This is where I'll test shit eventually 
    completeGreedy = 0
    averageGreedy = 0
    
    completeLeastCard = 0
    averageLeastCard = 0
    
    completeMostCard = 0
    averageMostCard = 0
    
    completeLeastSet = 0
    averageLeastSet = 0
    
    completeMostSet = 0
    averageMostSet = 0
    
    for i in range (howmany):
        #create deck
        deck = DeckHandler.DeckHandler()
        deck.shuffle()
        
        #Play Greedy
        Greedy = Player.GreedyPlayer(copy.deepcopy(deck.getDeck()))
        sets = Greedy.playGame()
        if len(sets) == 27:
            completeGreedy += 1
        averageGreedy += len(sets)
        
        #Play Strategy: getLeastCard
        S1 = Player.StrategicPlayer(copy.deepcopy(deck.getDeck()), Player.getLeastCard)
        sets = S1.playGame()
        if len(sets) == 27:
            completeLeastCard += 1
        averageLeastCard += len(sets)
        
        #Play Strategy: getMostCard
        S2 = Player.StrategicPlayer(copy.deepcopy(deck.getDeck()), Player.getMostCard)
        sets = S2.playGame()
        if len(sets) == 27:
            completeMostCard += 1
        averageMostCard += len(sets)
        
        #Play Strategy: getLeastSet
        S3 = Player.StrategicPlayer(copy.deepcopy(deck.getDeck()), Player.getLeastSet)
        sets = S3.playGame()
        if len(sets) == 27:
            completeLeastSet += 1
        averageLeastSet += len(sets)
        
        #Play Strategy: getMostSet
        S4 = Player.StrategicPlayer(copy.deepcopy(deck.getDeck()), Player.getMostSet)
        sets = S4.playGame()
        if len(sets) == 27:
            completeMostSet += 1
        averageMostSet += len(sets)
        
    #Statistics
    print "Completed Greedy: \t" + str(completeGreedy)
    print "Average Greedy: \t" + str(averageGreedy/howmany)
    print "Completed Least Card: \t" + str(completeLeastCard)
    print "Average Least Card: \t" + str(averageLeastCard/howmany)
    print "Completed Most Card: \t" + str(completeMostCard)
    print "Average Most Card: \t" + str(averageMostCard/howmany)
    print "Completed Least Set: \t" + str(completeLeastSet)
    print "Average Least Set: \t" + str(averageLeastSet/howmany)
    print "Completed Most Set: \t" + str(completeMostSet)
    print "Average Most Set: \t" + str(averageMostSet/howmany)
    

if __name__ == '__main__':
    goNuts(10)