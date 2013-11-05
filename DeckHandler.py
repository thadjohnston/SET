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
        '''test'''

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
        return random.shuffle(self.getCopy())
        
    def getNewCards(self):
        newCards = self.shuffled[0:2]
        del self.shuffled[0:2]
        return newCards
    
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
    
    

# if __name__ == '__main__':
#     d = Deck()
#     d.createDeck()
#     print()
#     deck1 = d.getCopy()
#     deck2 = d.getCopy()
#     random.shuffle(deck1)
#     random.shuffle(deck2)
#     print(deck1)
#     print(deck2)