'''
Created on Oct 22, 2013

@author: Thad
'''

import DeckHandler
import Set
import random
import sys

class Player(object):

    def __init__(self, deck, allow = False):
        #print(deck)
        self.deck = deck
        self.board = []
        self.removed = []
        self.numSets = 0
        self.allowReshuffle = allow
        
    def playGame(self):
        sets = []
        while self.canStillPlay():# and self.setPresent():
            s = self.findSet()
            if s:
                sets.append(s)
                self.numSets = self.numSets + 1
            else:
                if self.allowReshuffle:
                    self.resetDeck()
                else:
                    return sets
        return sets
            
        
    def canStillPlay(self):
        if len(self.deck) == 0 and self.setExists():
            return True
        if len(self.deck) >= 3:
            while len(self.board) < 12 and len(self.board) >= 0:
                self.board.append(self.deck.pop())
            return True
        return False
    
    def resetDeck(self):
        while len(self.board) > 0:
            self.deck.append(self.board.pop())
        random.shuffle(self.deck)
        while len(self.board) < 12 and len(self.board) >= 0:
            self.board.append(self.deck.pop())
    
    def findSet(self):
        for i in range(len(self.board)-2):
            for j in range(i+1, len(self.board)-1):
                for k in range(j+1, len(self.board)):
                    if self.isSet(self.board[i], self.board[j], self.board[k]):
                        return self.takeSet(i, j, k)
        return False
    
    def setExists(self):
        for i in range(len(self.board)-2):
            for j in range(i+1, len(self.board)-1):
                for k in range(j+1, len(self.board)):
                    if self.isSet(self.board[i], self.board[j], self.board[k]):
                        return True
        return False
    
    def setPresent(self):
        for i in range(len(self.board)-2):
            for j in range(i+1, len(self.board)-1):
                for k in range(j+1, len(self.board)):
                    if self.isSet(self.board[i], self.board[j], self.board[k]):
                        return True
        return False
    
    def takeSet(self, i, j, k):
        c1 = self.board[k]
        del self.board[k]
        c2 = self.board[j]
        del self.board[j]
        c3 = self.board[i]
        del self.board[i]
        return Set.Set(c1, c2, c3)
    
    def isSet(self, c1, c2, c3):
        return self.numberSet(c1, c2, c3) and self.colorSet(c1, c2, c3) and self.patternSet(c1, c2, c3) and self.shapeSet(c1, c2, c3)
                
    def numberSet(self, c1, c2, c3):
        if c1.getNumber() == c2.getNumber() and c2.getNumber() == c3.getNumber():
            return True
        if c1.getNumber() != c2.getNumber() and c2.getNumber() != c3.getNumber() and c3.getNumber() != c1.getNumber():
            return True
        return False
    
    def colorSet(self, c1, c2, c3):   
        if c1.getColor() == c2.getColor() and c2.getColor() == c3.getColor():
            return True
        if c1.getColor() != c2.getColor() and c2.getColor() != c3.getColor() and c3.getColor() != c1.getColor():
            return True
        return False
    
    def patternSet(self, c1, c2, c3):
        if c1.getPattern() == c2.getPattern() and c2.getPattern() == c3.getPattern():
            return True
        if c1.getPattern() != c2.getPattern() and c2.getPattern() != c3.getPattern() and c3.getPattern() != c1.getPattern():
            return True
        return False
    
    def shapeSet(self, c1, c2, c3): 
        if c1.getShape() == c2.getShape() and c2.getShape() == c3.getShape():
            return True
        if c1.getShape() != c2.getShape() and c2.getShape() != c3.getShape() and c3.getShape() != c1.getShape():
            return True
        return False  
    
class GreedyPlayer(Player):
    def __init__(self, deck, allow):
        Player.__init__(self, deck, allow)
        
def getLeastCard(board, deck, sets):
    minSet = -1
    minExistingSets = -1
    numSetsForCard = 0
    setNum = 0
    
    for eachSet in sets:
        cards = eachSet.returnSet()
        for card in cards:
            for secondCard in (board + deck):
                if secondCard != card:
                    thirdCard = Set.predictThird(card, secondCard)
                    if thirdCard in (board + deck):
                        numSetsForCard += 1
            if minExistingSets == -1 or numSetsForCard < minExistingSets:
#                     print (numSetsForCard)
                minExistingSets = numSetsForCard
                minSet = setNum
        numSetsForCard = 0
        setNum += 1
    return sets[minSet]


#DO THIS
def getMostCard(board, deck, sets):
    minSet = -1
    maxExistingSets = -1
    numSetsForCard = 0
    setNum = 0
    
    for eachSet in sets:
        cards = eachSet.returnSet()
        for card in cards:
            for secondCard in (board + deck):
                if secondCard != card:
                    thirdCard = Set.predictThird(card, secondCard)
                    if thirdCard in (board + deck):
#                             print( card, secondCard, thirdCard)
                        numSetsForCard += 1
            if maxExistingSets == -1 or numSetsForCard > maxExistingSets:
                
                maxExistingSets = numSetsForCard
                minSet = setNum
        numSetsForCard = 0
        setNum += 1
    return sets[minSet]

#DO THIS
def getMostSet(board, deck, sets):
    maxSet = -1
    maxExistingSets = -1
    numSetsForSet = 0
    setNum = 0
    
    for eachSet in sets:
        cards = eachSet.returnSet()
        for card in cards:
            for secondCard in (board + deck):
                if secondCard != card:
                    thirdCard = Set.predictThird(card, secondCard)
                    if thirdCard in (board + deck):
                        numSetsForSet += 1
        if maxExistingSets == -1 or numSetsForSet > maxExistingSets:
                
            maxExistingSets = numSetsForSet
            maxSet = setNum
        numSetsForSet = 0
        setNum += 1
    return sets[maxSet]


def getLeastSet(board, deck, sets):
    minSet = -1
    minExistingSets = -1
    numSetsForSet = 0
    setNum = 0
    
    for eachSet in sets:
        cards = eachSet.returnSet()
        for card in cards:
            for secondCard in (board + deck):
                if secondCard != card:
                    thirdCard = Set.predictThird(card, secondCard)
                    if thirdCard in (board + deck):
                        numSetsForSet += 1
        if minExistingSets == -1 or numSetsForSet < minExistingSets:
            minExistingSets = numSetsForSet
            minSet = setNum
        numSetsForSet = 0
        setNum += 1
    return sets[minSet]

def bestCombinatoric(board, deck, sets):
    bestSet = -1
    setNum = 0
    bestNumDiff = 0
    bestCombinatoric = {1:2, 2:3, 3:2, 4:1}
    
    for eachSet in sets:
        cards = eachSet.returnSet()
        numDiffScore = bestCombinatoric[cards[0].numDifferences(cards[1])]
        if bestSet == -1 or numDiffScore > bestNumDiff:
            bestNumDiff = numDiffScore
            bestSet = setNum
        setNum += 1
    return sets[bestSet]

def worstCombinatoric(board, deck, sets):
    bestSet = -1
    setNum = 0
    bestNumDiff = 0
    bestCombinatoric = {1:2, 2:1, 3:2, 4:3}
    
    for eachSet in sets:
        cards = eachSet.returnSet()
        numDiffScore = bestCombinatoric[cards[0].numDifferences(cards[1])]
        if bestSet == -1 or numDiffScore > bestNumDiff:
            bestNumDiff = numDiffScore
            bestSet = setNum
        setNum += 1
    return sets[bestSet]
        
class StrategicPlayer(Player):
    
    def __init__(self, deck, func=getLeastCard, allow=False):
        Player.__init__(self, deck, allow)
        self.heuristic = func
        
    def findSet(self):
        foundSet = False
        currentSets = []
        for i in range(len(self.board)-2):
            for j in range(i+1, len(self.board)-1):
                for k in range(j+1, len(self.board)):
                    if self.isSet(self.board[i], self.board[j], self.board[k]):
                        currentSets.append(Set.Set(self.board[i], self.board[j], self.board[k]))
                        foundSet = True
        if foundSet:
            chosenSet = self.heuristic(self.board, self.deck, currentSets)
#             print(chosenSet)
            cards = chosenSet.returnSet()
            self.removed.append(cards[0])
            self.removed.append(cards[1])
            self.removed.append(cards[2])
            
            self.board.remove(cards[0])
            self.board.remove(cards[1])
            self.board.remove(cards[2])
            
            return Set.Set(cards[0], cards[1], cards[2])
        return False      
    
if __name__ == '__main__':
        
        #p = Player(deck.shuffle(), False)
        completeGames = 0
        for i in range(100):
            deck = DeckHandler.DeckHandler()
            deck = deck.shuffle()
            lc = StrategicPlayer(deck, False)
            setsFound = lc.playGame()
            if len(setsFound) == 27:
                completeGames += 1
        #print DeckHandler.printFormattedDeck(p.deck)
#         setsFound = p.playGame()
        print('Number of complete games: ' + str(completeGames))
#         print(lc.board)
#         for s in setsFound:
#             print(s)
