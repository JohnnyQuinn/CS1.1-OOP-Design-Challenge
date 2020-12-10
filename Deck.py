from Card import Cards
import random

class Deck():
    """ deck made up of playing cards """
    def __init__(self):
        """ a deck is made up of 52 playing cards, contains all the cards, and has a boolean state of whether or not it is shuffled"""
        self.main_deck = [] 
        self._is_shuffled = False 

    def __shuffle(self):
        """ shuffles all 52 cards 3 times over """
        for i in range(3):
            random.shuffle(self.main_deck)
            i += 1
        

    def build_deck(self):
        """ builds out the entire deck (shuffled 3 times)"""
        self.__build_suit("C")
        self.__build_suit("S")
        self.__build_suit("H")
        self.__build_suit("D")
        self.__shuffle()

    
    def __build_suit(self, suit):
        """ creates a set of cards that consists of all the ranks of a particular suit and also sets color of cards """
        suit_deck = []
        for i in range(1, 14):
            card = Cards(suit, rank = i)
            card.set_card_color(suit)
            suit_deck.append(card)
        self.main_deck += suit_deck