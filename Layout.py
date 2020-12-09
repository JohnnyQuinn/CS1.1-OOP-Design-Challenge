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
        """ places the initial cards in the tables (28 cards) and puts the rest in the pile (24 cards) """
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

        self.pile += game_deck
        game_deck.clear()

    def manage_table(self, number):
        """ manages an individual table"""
        pass

    def manage_foundation(self, number):
        """ manages an individual foundation """
        pass

    def manage_pile(self, cmd):
        """ manages the pile """
        #moves card in the front (index -1) to back (index 0)
        if "next card" in cmd:
            self.pile.insert(0, self.pile.pop(-1))
        if "current card" in cmd:
            self.pile[-1].change_face()
            return self.pile[-1].get_card_string()
    
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

    def translate_cmd(self, cmd):
        if "t" in cmd:
            for i in range(1, 8, 1):
                if str(i) in cmd:
                    return self.get_tables()[i - 1]
        if "f" in cmd:
            for i in range(1, 5, 1):
                if str(i) in cmd:
                    return self.get_foundations()[i - 1]
        if "pile" in cmd:
            return self.pile


    def get_tables(self):
        """ returns all the tables(1-7) in a list"""
        return [self.table1, self.table2, self.table3, self.table4, self.table5, self.table6, self.table7]
    
    def get_foundations(self):
        return [self.foundation1, self.foundation2, self.foundation3, self.foundation4]
    
    def move_card(self, origin, destination):
        self.translate_cmd(destination).append(self.translate_cmd(origin)[-1])
        self.translate_cmd(origin).remove(self.translate_cmd(origin)[-1])
        self.translate_cmd(origin)[len(self.translate_cmd(origin)) - 1].change_face()
    
layout = Layout()
layout.build_table()

