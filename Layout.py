from Deck import Deck

class Layout:
    """ Layout of the game, organizes the cards' placement """
    def __init__(self):
        """ layout is made up of 7 tables, 4 foundations, and 1 pile"""
        self.table1 = []
        self.table2 = []
        self.table3 = []
        self.table4 = []
        self.table5 = []
        self.table6 = []
        self.table7 = []
        self.foundation1 = []
        self.foundation2 = []
        self.foundation3 = []
        self.foundation4 = []
        self.pile = [] 
    
    def build_table(self):
        """ places the initial cards in the tables """
        deckObj = Deck()
        deckObj.build_deck()
        game_deck = deckObj.main_deck
        
        self.__from_deck_to_table(game_deck, self.table1, 1)
        self.__from_deck_to_table(game_deck, self.table2, 2)
        self.__from_deck_to_table(game_deck, self.table3, 3)
        self.__from_deck_to_table(game_deck, self.table4, 4)
        self.__from_deck_to_table(game_deck, self.table5, 5)
        self.__from_deck_to_table(game_deck, self.table6, 6)
        self.__from_deck_to_table(game_deck, self.table7, 7)

    def manage_table(self, number):
        """ manages an individual table"""
        pass

    def manage_foundation(self, number):
        """ manages an individual foundation """
        pass

    def manage_pile(self):
        """ manages the pile """
        pass
    
    @staticmethod
    def __from_deck_to_table(deck, table, amount):
        """ takes a card from the main deck and puts it in an individual table. 
            Also flips the last card that was placed in the table to face up  """
        for i in range(amount):
            card = deck[-1]
            deck.remove(card) 
            table.append(card)
            i += 1
        
        table[-1].change_face()

        

layout = Layout()
layout.build_table()
