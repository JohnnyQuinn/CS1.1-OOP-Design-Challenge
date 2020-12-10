class Cards:
    """ playing cards """
    def __init__(self, suit, rank):
        """ each card has a suit(clubs, spades, hearts, diamonds), rank(K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2, A) represented by numbers (12-1), 
            color (clubs and spades are black, hearts and diamonds are red), and boolen of whether the card is face up or down """
        self.suit = suit #string
        self.rank = rank #int
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
        """ returns a string to simulate a card in the format of: '[RS]'. (R = rank, S = suit).
            If rank is 1, 11, 12, 13 then rank is converted into letter rank (A, J, Q, K)"""
        rank = ""
        if self.rank < 2 or self.rank > 10:
            if self.rank == 1:
                rank = "A"
            elif self.rank == 11:
                rank = "J"
            elif self.rank == 12:
                rank = "Q"
            elif self.rank == 13:
                rank = "K"
        else:
            rank = str(self.rank)
        return f'[{rank}{self.suit}]'