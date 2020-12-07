class Cards:
    """ playing cards """
    def __init__(self, suit, rank):
        """ each card has a suit(clubs, spades, hearts, diamonds), rank(K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, A) represented by numbers (13-0), 
            color (clubs and spades are black, hearts and diamonds are red), and boolen of whether the card is face up or down """
        self.suit = suit
        self.rank = rank
        self.color = ""
        self.face_up = False

    def change_face(self):
        """ flips the card over (toggle face up or down) """
        self.face_up = not self.face_up

    def set_card_color(self, suit):
        """ sets the card's color based on its suit """
        if suit == "C":
            self.color = "B"
        elif suit == "S":
            self.color = "B"
        elif suit == "H":
            self.color = "R"
        elif suit == "D":
            self.color = "R"
    
    def get_card_string(self):
        """ returns a string to simulate a card in the format of: '[SR]'. (S = suit, R = rank)"""
        return f'[{self.suit}{str(self.rank)}]'