'''
Created on Nov 21, 2013

@author: Thad
'''

class Set(object):

    def __init__(self, card1, card2, card3):
        self.set = [card1, card2, card3]
        
    def returnSet(self):
        return self.set