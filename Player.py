'''
Created on Oct 22, 2013

@author: Thad
'''

import DeckHandler
import Set

class Player(object):

    def __init__(self, deck):
        #print(deck)
        self.deck = deck
        self.board = []
        self.removed = []
        self.numSets = 0
        
    def playGame(self):
        
        while self.canStillPlay() and self.setPresent():
            if self.findSet():
                return
                self.numSets = self.numSets + 1
                print(self.numSets)
            else:
                return
            
        
    def canStillPlay(self):
        if len(self.deck) >= 3:
            while len(self.board) < 12 and len(self.board) >= 0:
                self.board.append(self.deck.pop())
            return True
        return False
    
    def findSet(self):
        for i in range(len(self.board)-2):
            for j in range(i+1, len(self.board)-1):
                for k in range(j+1, len(self.board)):
                    if self.isSet(self.board[i], self.board[j], self.board[k]):
                        self.takeSet(i, j, k)
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
        #take from the end so as not to fuck it up
        #self.removed.append(self.board[k])
        del self.board[k]
        #self.removed.append(self.board[j])
        del self.board[j]
        #self.removed.append(self.board[i])
        del self.board[i]
    
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
    
    def __init__(self, deck):
        Player.__init__(self, deck)
        
        
class LeastConflict(Player):
    
    def __init__(self, deck):
        Player.__init__(self, deck)
        
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
            chosenSet = self.getBestSet(currentSets)
    
        return foundSet
    
    def getBestSet(self, sets):
        minSet = -1
        
        minExistingSets = -1
        numSetsForCard = 0
        
        setNum = 0
        
        for eachSet in sets:
            cards = eachSet.returnSet()
            for card in cards:
                for secondCard in (self.board + self.deck):
                    if secondCard != card:
                        thirdCard = Set.predictThird(card, secondCard)
                        if thirdCard in (self.board + self.deck):
                            print card, secondCard, thirdCard
                            numSetsForCard += 1
                if minExistingSets == -1 or numSetsForCard < minExistingSets:
                    minExistingSets = numSetsForCard
                    minSet = setNum
            setNum += 1
        return sets[minSet]

                        
                
    
        
    
if __name__ == '__main__':
    pass
    