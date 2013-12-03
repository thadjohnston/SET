'''
Created on Oct 22, 2013

@author: Thad
'''
import random
import copy

class DeckHandler(object):

    def __init__(self):
        self.deck = []
        self.shuffled = []
        self.numbers = [1, 2, 3]
        self.colors = ['green', 'red', 'purple']
        self.patterns = ['solid', 'striped', 'outlined']
        self.shapes = ['oval', 'diamond', 'squiggle']
        self.createDeck()
        
    def __str__(self):
        s = ""
        numCards = len(self.deck)
        c = 0
        for i in range(numCards/3):
            for j in range(3):
                s += str(self.deck[c]) + "  "
                c += 1
            s += "\n"
        return s
    
    def createDeck(self):
        for number in self.numbers:
            for color in self.colors:
                for pattern in self.patterns:
                    for shape in self.shapes:
                        self.deck.append(Card(number, color, pattern, shape))
                        
    def printDeck(self):
        for card in self.deck:
            print(card)
            
    def getCopy(self):
        return copy.deepcopy(self.deck)
    
    def getDeck(self):
        return self.deck
    
    def shuffle(self):
        random.shuffle(self.deck)
        return self.deck
        
    def dropCards(self, numToDrop):
        self.shuffle()
        for i in range(numToDrop):
            c = self.deck[0]
            self.deck.remove(c)
            #print( str(i) + "  " + str(c))
        
    def getNewCards(self):
        newCards = self.shuffled[0:2]
        del self.shuffled[0:2]
        return newCards
    
def printFormattedDeck(deck):
    s = ""
    numCards = len(deck)
    c = 0
    for i in range(numCards/3):
        for j in range(3):
            s += str(deck[c]) + "  "
            c += 1
        s += "\n"
    return s
    
class Card(object):
    def __init__(self, number, color, pattern, shape):
        self.number = number
        self.color = color
        self.pattern = pattern
        self.shape = shape
        
    def __str__(self):
        return '(' + str(self.number) + ', ' + self.color + ', ' + self.pattern + ', ' + self.shape + ')'
    
    def __repr__(self):
        return '(' + str(self.number) + ', ' + self.color + ', ' + self.pattern + ', ' + self.shape + ')'
    
    def getNumber(self):
        return self.number
    
    def getColor(self):
        return self.color
    
    def getPattern(self):
        return self.pattern
    
    def getShape(self):
        return self.shape
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.getNumber() == other.getNumber() and self.getColor() == other.getColor() and self.getPattern() == other.getPattern() and self.getShape() == other.getShape()
        else:
            return False
        
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.getNumber() != other.getNumber() or self.getColor() != other.getColor() or self.getPattern() != other.getPattern() or self.getShape() != other.getShape()
        else:
            return False
    
if __name__ == '__main__':
    d = DeckHandler()
    #d.createDeck()
    #print "-----------------------------------------------------------"
    #print d.shuffle()
    #print d
    #print len(d.deck)
    #print "-----------------------------------------------------------"
    #d.dropCards(41)
    #print "-----------------------------------------------------------"
    #print d
    #print "-----------------------------------------------------------"
    #print len(d.deck)