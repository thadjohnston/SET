'''
Created on Oct 22, 2013

@author: Thad
'''

import DeckHandler
import Set
import random

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
        c1 = self.board[k]
        del self.board[k]
        #self.removed.append(self.board[j])
        c2 = self.board[j]
        del self.board[j]
        #self.removed.append(self.board[i])
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
        
        for set in sets:
            cards = set.returnSet()
            for card in cards:
                for secondCard in (self.board + self.deck):
                    thirdCard = Set.predictThird(card, secondCard)
                    print(thirdCard)
                
    
if __name__ == '__main__':
     deck = DeckHandler.DeckHandler()
     p = Player(deck.shuffle(), True)
     #print DeckHandler.printFormattedDeck(p.deck)
     setsFound = p.playGame()
     print len(setsFound)
     for s in setsFound:
         print s
