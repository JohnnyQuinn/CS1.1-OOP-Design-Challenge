from Card import Cards

class Deck():
    """ deck made up of playing cards """
    def __init__(self):
        """ a deck is made up of 52 playing cards, contains all the cards, and has a boolean state of whether or not it is shuffled"""
        self.__amount = 52
        self.deck = []
        self._is_shuffled = False

    def shuffle(self):
        """ shuffles all 52 cards """
        pass

    def build_deck(self):
        """ builds out the entire deck"""
        self.build_suit("C")
        self.build_suit("S")
        self.build_suit("H")
        self.build_suit("D")


    def build_suit(self, suit):
        """ creates a set of cards that consists of all the ranks of a particular suit """
        suit_deck = []
        for i in range(13):
            card = Cards(suit, rank = i)
            card.set_card_color(suit)
            suit_deck.append(card)
        self.deck += suit_deck

deck = Deck()
deck.build_deck()
print(deck.deck)
for card in deck.deck:
    print(f'{card.suit} {card.rank} {card.color}')
