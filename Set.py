'''
Created on Nov 21, 2013

@author: Thad
'''
from DeckHandler import Card 

class Set(object):

    def __init__(self, card1, card2, card3):
        self.set = [card1, card2, card3]
        
    def __str__(self):
        return '[' + str(self.set[0]) + ', ' + str(self.set[1]) + ', ' + str(self.set[2]) + ']'
    
    def __repr__(self):
        return '[' + str(self.set[0]) + ', ' + str(self.set[1]) + ', ' + str(self.set[2]) + ']'
    
    def returnSet(self):
        return self.set
    
def predictThird(card1, card2):
    if card1.getNumber() == card2.getNumber(): number = card1.getNumber()
    else:
        numbers = [1,2,3]
        numbers.remove(card1.getNumber())
        numbers.remove(card2.getNumber())
        number = numbers[0]
   
    if card1.getColor() == card2.getColor(): color = card1.getColor()
    else:
        colors = ['green', 'red', 'purple']
        colors.remove(card1.getColor())
        colors.remove(card2.getColor())
        color = colors[0]
        
    if card1.getPattern() == card2.getPattern(): pattern = card1.getPattern()
    else:
        patterns = ['solid', 'striped', 'outlined']
        patterns.remove(card1.getPattern())
        patterns.remove(card2.getPattern())
        pattern = patterns[0]
        
    if card1.getShape() == card2.getShape(): shape = card1.getShape()
    else:
        shapes = ['oval', 'diamond', 'squiggle']
        shapes.remove(card1.getShape())
        shapes.remove(card2.getShape())
        shape = shapes[0]
    return Card(number, color, pattern, shape)
        
if __name__ == '__main__':
#     card1 = Card(2, 'green', 'solid', 'oval')
#     card2 = Card(2, 'red', 'striped', 'oval')
#     card3 = predictThird(card1, card2)
#     print(card3)
#     s = Set(card1, card2, card3)
#     print s
    pass
    
