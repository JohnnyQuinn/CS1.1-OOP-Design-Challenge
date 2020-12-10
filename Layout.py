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
        
        #moves initial cards to tables
        self.__from_deck_to_table(game_deck, self.table1, 1)
        self.__from_deck_to_table(game_deck, self.table2, 2)
        self.__from_deck_to_table(game_deck, self.table3, 3)
        self.__from_deck_to_table(game_deck, self.table4, 4)
        self.__from_deck_to_table(game_deck, self.table5, 5)
        self.__from_deck_to_table(game_deck, self.table6, 6)
        self.__from_deck_to_table(game_deck, self.table7, 7)

        #adds empty element to foundations
        self.foundation1.append("  ")
        self.foundation2.append("  ")
        self.foundation3.append("  ")
        self.foundation4.append("  ")

        self.pile += game_deck
        game_deck.clear()

    def manage_table(self):
        """ manages an individual table"""
        tables = self.get_tables()
        for table in tables:
            if len(table) <= 0:
                table.append("[  ]")

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
        #checks if cmd is a table
        if "t" in cmd:
            for i in range(1, 8):
                if str(i) in cmd:
                    return self.get_tables()[i - 1]
        #checks if cmd is a foundation
        if "f" in cmd:
            for i in range(1, 5):
                if str(i) in cmd:
                    return self.get_foundations()[i - 1]
        #checks if cmd is the pile
        if "pile" in cmd:
            return self.pile
        #checks if cmd is a card rank and if so then which 
        if "S" in cmd or "s" in cmd or "C" in cmd or "c" in cmd or "D" in cmd or "d" in cmd or "H" in cmd or "h" in cmd:
            rank = ""
            for i in range(1, 14):
                if str(i) in cmd:
                    rank = str(i)
            suit = cmd[i].capitalize()
            return suit + rank

    def get_tables(self):
        """ returns all the tables(1-7) in a list"""
        return [self.table1, self.table2, self.table3, self.table4, self.table5, self.table6, self.table7]
    
    def get_foundations(self):
        return [self.foundation1, self.foundation2, self.foundation3, self.foundation4]
    
    def get_last_foundation_card(self, foundation):
        try:
            card = self.get_foundations()[foundation - 1][-1].get_card_string()
        except:
            card = "[  ]"
        return card
    
    def move_card(self, origin, destination):
        self.translate_cmd(destination).append(self.translate_cmd(origin)[-1])
        self.translate_cmd(origin).remove(self.translate_cmd(origin)[-1])
        try:
            self.translate_cmd(origin)[len(self.translate_cmd(origin)) - 1].change_face()
        except:
            pass
    
    def move_group(self, origin_table, top_card, destination_table):
        top_card_index = origin_table.index(top_card)
        group = origin_table[top_card_index, -1]
        origin_table + group 
        for card in group:
            for i in origin_table:
                if i == card:
                    origin_table.remove(origin_table.index(card))
        destination_table + group

    
layout = Layout()
layout.build_table()

