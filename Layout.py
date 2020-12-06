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
        """ builds the initial sets for the tables """
        pass

    def manage_table(self, number):
        """ manages an individual table"""
        pass

    def manage_foundation(self, number):
        """ manages an individual foundation """
        pass

    def manage_pile(self):
        """ manages the pile """
        pass