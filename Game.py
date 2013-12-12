
import DeckHandler
import Player
import random
import copy
import math

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
    stdDevGreedy = 0
    averageGreedy = 0
    
    completeLeastCard = 0
    stdDevLeastCard = 0
    averageLeastCard = 0
    
    completeMostCard = 0
    stdDevMostCard = 0
    averageMostCard = 0
    
    completeLeastSet = 0
    stdDevLeastSet = 0
    averageLeastSet = 0
    
    completeMostSet = 0
    stdDevMostSet = 0
    averageMostSet = 0
    
    completeBComb = 0
    stdDevBComb = 0
    averageBComb = 0
    
    completeWComb = 0
    stdDevWComb = 0
    averageWComb = 0
    
    stdDevGreedy = 0
    stdDevLeastCard = 0
    stdDevMostCard = 0
    stdDevLeastSet = 0
    stdDevMostSet = 0
    stdDevBComb = 0
    stdDevWComb = 0
    
    numSetsGreedy = []
    numSetsLeastCard = []
    numSetsMostCard = []
    numSetsLeastSet = []
    numSetsMostSet = []
    numSetsBComb = []
    numSetsWComb = []
    
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
        numSetsGreedy.append(len(sets))
        averageGreedy += len(sets)
        
        #Play Strategy: getLeastCard
        S1 = Player.StrategicPlayer(copy.deepcopy(deck.getDeck()), Player.getLeastCard, allowReshuffle)
        sets = S1.playGame()
        if len(sets) == completePossible:
            completeLeastCard += 1
        numSetsLeastCard.append(len(sets))
        averageLeastCard += len(sets)
        
        #Play Strategy: getMostCard
        S2 = Player.StrategicPlayer(copy.deepcopy(deck.getDeck()), Player.getMostCard, allowReshuffle)
        sets = S2.playGame()
        if len(sets) == completePossible:
            completeMostCard += 1
        numSetsMostCard.append(len(sets))
        averageMostCard += len(sets)
        
        #Play Strategy: getLeastSet
        S3 = Player.StrategicPlayer(copy.deepcopy(deck.getDeck()), Player.getLeastSet, allowReshuffle)
        sets = S3.playGame()
        if len(sets) == completePossible:
            completeLeastSet += 1
        numSetsLeastSet.append(len(sets))
        averageLeastSet += len(sets)
        
        #Play Strategy: getMostSet
        S4 = Player.StrategicPlayer(copy.deepcopy(deck.getDeck()), Player.getMostSet, allowReshuffle)
        sets = S4.playGame()
        if len(sets) == completePossible:
            completeMostSet += 1
        numSetsMostSet.append(len(sets))
        averageMostSet += len(sets)
        
        #Play Strategy: bestCombinatoric
        S5 = Player.StrategicPlayer(copy.deepcopy(deck.getDeck()), Player.bestCombinatoric, allowReshuffle)
        sets = S5.playGame()
        if len(sets) == completePossible:
            completeBComb += 1
        numSetsBComb.append(len(sets))
        averageBComb += len(sets)
        
        #Play Strategy: worstCombinatoric
        S6 = Player.StrategicPlayer(copy.deepcopy(deck.getDeck()), Player.worstCombinatoric, allowReshuffle)
        sets = S6.playGame()
        if len(sets) == completePossible:
            completeWComb += 1
        numSetsWComb.append(len(sets))
        averageWComb += len(sets)
        
    averageGreedy = averageGreedy/float(howmany)
    averageLeastCard = averageLeastCard/float(howmany)
    averageMostCard = averageMostCard/float(howmany)
    averageLeastSet = averageLeastSet/float(howmany)
    averageMostSet = averageMostSet/float(howmany)
    averageBComb = averageBComb/float(howmany)
    averageWComb = averageWComb/float(howmany)
    
    for i in range(howmany):
        stdDevGreedy += (averageGreedy - numSetsGreedy[i]) * (averageGreedy - numSetsGreedy[i])
        stdDevLeastCard += (averageLeastCard - numSetsLeastCard[i]) * (averageLeastCard - numSetsLeastCard[i])
        stdDevMostCard += (averageMostCard - numSetsMostCard[i]) * (averageMostCard - numSetsMostCard[i])
        stdDevLeastSet += (averageLeastSet - numSetsLeastSet[i]) * (averageLeastSet - numSetsLeastSet[i])
        stdDevMostSet += (averageMostSet - numSetsMostSet[i]) * (averageMostSet - numSetsMostSet[i])
        stdDevBComb += (averageBComb - numSetsBComb[i]) * (averageBComb - numSetsBComb[i])
        stdDevWComb += (averageWComb - numSetsWComb[i]) * (averageWComb - numSetsWComb[i])
        
    stdDevGreedy = math.sqrt(stdDevGreedy/float(howmany))
    stdDevLeastCard = math.sqrt(stdDevLeastCard/float(howmany))
    stdDevMostCard = math.sqrt(stdDevMostCard/float(howmany))
    stdDevLeastSet = math.sqrt(stdDevLeastSet/float(howmany))
    stdDevMostSet = math.sqrt(stdDevMostSet/float(howmany))
    stdDevBComb = math.sqrt(stdDevBComb/float(howmany))
    stdDevWComb = math.sqrt(stdDevWComb/float(howmany))
    
    
        
    #Statistics
    num = howmany/100.0
    print("Statistics: Remove(" + str(remove) + ") Reshuffle(" + str(allowReshuffle) + ")")
    print("Completed Greedy: \t" + str(completeGreedy/num) + "%")
    print("Average Greedy: \t" + str(averageGreedy))
    print("Standard Deviation Greedy: \t" + str(stdDevGreedy))
    print("Completed Least Card: \t" + str(completeLeastCard/num) + "%")
    print("Average Least Card: \t" + str(averageLeastCard))
    print("Standard Deviation Least Card: \t" + str(stdDevLeastCard))
    print("Completed Most Card: \t" + str(completeMostCard/num)+ "%")
    print("Average Most Card: \t" + str(averageMostCard))
    print("Standard Deviation Most Card: \t" + str(stdDevMostCard))
    print("Completed Least Set: \t" + str(completeLeastSet/num) + "%")
    print("Average Least Set: \t" + str(averageLeastSet))
    print("Standard Deviation Least Set: \t" + str(stdDevLeastSet))
    print("Completed Most Set: \t" + str(completeMostSet/num) + "%")
    print("Average Most Set: \t" + str(averageMostSet))
    print("Standard Deviation Most Set: \t" + str(stdDevMostSet))
    print("Completed Best Comb: \t" + str(completeBComb/num) + "%")
    print("Average Best Comb: \t" + str(averageBComb))
    print("Standard Deviation Best Comb: \t" + str(stdDevBComb))
    print("Completed Worst Comb: \t" + str(completeWComb/num) + "%")
    print("Average Worst Comb: \t" + str(averageWComb))
    print("Standard Deviation Worst Comb: \t" + str(stdDevWComb))
    print("------------------------------------------")
    
 
if __name__ == '__main__':
#     goNuts(numGames)
#     goNuts(numGames, 6)
#     goNuts(numGames, 12)
#     goNuts(numGames, 0, True)
#     goNuts(numGames, 6, True)
    numGames = 1000
    goNuts(numGames)
    goNuts(numGames, 6)
    goNuts(numGames, 12)
#     goNuts(numGames, 0, True)
#     goNuts(numGames, 6, True)
#     goNuts(numGames, 12, True)
