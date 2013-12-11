
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


def goNuts(howmany, remove=0, allowReshuffle=False):
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
    
    completePossible = 27 - (remove/3)
    
    for i in range (howmany):
        #create deck
        deck = DeckHandler.DeckHandler()
        deck.dropCards(remove)
        
        #Play Greedy
        Greedy = Player.GreedyPlayer(copy.deepcopy(deck.getDeck()), allowReshuffle)
        sets = Greedy.playGame()
        if len(sets) == completePossible:
            completeGreedy += 1
        averageGreedy += len(sets)
        
        #Play Strategy: getLeastCard
        S1 = Player.StrategicPlayer(copy.deepcopy(deck.getDeck()), Player.getLeastCard, allowReshuffle)
        sets = S1.playGame()
        if len(sets) == completePossible:
            completeLeastCard += 1
        averageLeastCard += len(sets)
        
        #Play Strategy: getMostCard
        S2 = Player.StrategicPlayer(copy.deepcopy(deck.getDeck()), Player.getMostCard, allowReshuffle)
        sets = S2.playGame()
        if len(sets) == completePossible:
            completeMostCard += 1
        averageMostCard += len(sets)
        
        #Play Strategy: getLeastSet
        S3 = Player.StrategicPlayer(copy.deepcopy(deck.getDeck()), Player.getLeastSet, allowReshuffle)
        sets = S3.playGame()
        if len(sets) == completePossible:
            completeLeastSet += 1
        averageLeastSet += len(sets)
        
        #Play Strategy: getMostSet
        S4 = Player.StrategicPlayer(copy.deepcopy(deck.getDeck()), Player.getMostSet, allowReshuffle)
        sets = S4.playGame()
        if len(sets) == completePossible:
            completeMostSet += 1
        averageMostSet += len(sets)
        
    #Statistics
    print("Statistics: Remove(" + str(remove) + ") Reshuffle(" + str(allowReshuffle) + ")")
    print("Completed Greedy: \t" + str(completeGreedy/howmany) + "%")
    print("Average Greedy: \t" + str(averageGreedy/howmany))
    print("Completed Least Card: \t" + str(completeLeastCard/howmany) + "%")
    print("Average Least Card: \t" + str(averageLeastCard/howmany))
    print("Completed Most Card: \t" + str(completeMostCard/howmany) + "%")
    print("Average Most Card: \t" + str(averageMostCard/howmany))
    print("Completed Least Set: \t" + str(completeLeastSet/howmany) + "%")
    print("Average Least Set: \t" + str(averageLeastSet/howmany))
    print("Completed Most Set: \t" + str(completeMostSet/howmany) + "%")
    print("Average Most Set: \t" + str(averageMostSet/howmany))
    print("------------------------------------------")
    
if __name__ == '__main__':
    numGames = 10
#     goNuts(numGames)
#     goNuts(numGames, 6)
#     goNuts(numGames, 12)
#     goNuts(numGames, 0, True)
#     goNuts(numGames, 6, True)
    goNuts(numGames, 12, True)
