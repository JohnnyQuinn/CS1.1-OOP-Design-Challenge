from Layout import Layout

class Game(Layout):
    """ manages and runs the game """
    def __init__(self):
        """ games has a state of running and whether or not the player has won"""
        self.__game_running = False
        self.__game_won = False
        self.__current_pile_card = ""

    def run(self):
        self.messages("start")
        self.commands(input())
        while self.__game_running == True:
            self.commands(input())

    def start_game(self):
        """ starts the game """
        self.__game_running = True
        global layout
        layout = Layout()
        layout.build_table()
        self.render_layout()

    def commands(self, user_input):
        """ takes in the user commands and reacts appropiately """
        if "quit" in user_input:
            if self.__game_running == True:
                user_response = input("\nAre you sure you want to quit? (yes/no):\n")
                if "yes" in user_response:
                    self.__game_running = False
                elif "no" in user_response:
                    self.messages("enter cmd")
        if "new game" in user_input:
            if self.__game_running == True:
                user_response = input("\nAre you sure you want to start a new game? (yes/no):\n")
                if "yes" in user_response:
                    self.start_game()
                elif "no" in user_response:
                    self.messages("enter cmd")
            else:
                self.start_game()
        # show next card in the pile
        if "next pile" in user_input:
            layout.manage_pile("next card")
            self.render_layout()
        #moves card from one location to another
        if "mv" in user_input and "to" in user_input:
            #splits user_input string into list 
            mv_cmd_list = list(user_input.split(" "))
            origin = mv_cmd_list[1]
            destination = mv_cmd_list[3]
            self.games_master(origin, destination)

    def render_layout(self):
        """ renders layout of pile, foundations, and tables. Takes in tables(1-7) and sorts them out to be printed to the terminal. """
       
        tables = layout.get_tables()

        print("\n\n\n\n")
        self.messages("legend")
        self.print_seperator()
        print("Pile:                      (F1) (F2) (F3) (F4)         <- Foundations")

        #renders pile card
        print("[XX]" + layout.manage_pile("current card") + "                   [  ] [  ] [  ] [  ]")

        self.print_seperator()
        print("(T1)   (T2)   (T3)   (T4)   (T5)   (T6)   (T7)         <- Tables")
        self.print_seperator()

        table_grid = []

        # creates a list consisting of 49 empty spaces. Treated like a 7x7 grid
        for i in range(0, 49):
            table_grid.append("    ")

        # populates table grid. Starts with column, then goes into each row of that column, then goes to next column. 
        for column in range(0, 7, 1):
            stop = 43+column
            i = 0
            for row in range(column, stop, 7):
                try:
                    if tables[column][i].face_up == True:
                        table_grid[row] = tables[column][i].get_card_string()
                    elif tables[column][i].face_up == False:
                        table_grid[row] = "[XX]"
                except:
                    pass
                i += 1

        #goes through table_grid and adds cards, line breaks, and spacing to table_grid_string
        table_grid_string = ""
        for i in range(0, 49, 1):
            if i != 0:
                if (i % 7) == 0:
                    table_grid_string += "\n"

            table_grid_string += table_grid[i] + "   "

        print(table_grid_string)
        self.messages("enter cmd")

    def games_master(self, origin, destination):
        """ manages the rules of the game """
        origin_list = layout.translate_cmd(origin)
        destination_list = layout.translate_cmd(destination)
        origin_card = origin_list[-1]
        destination_card = destination_list[-1]

        print(f'Last move:\n{origin_card.get_card_string()} -> {destination_card.get_card_string()}')

        if origin_card.color == destination_card.color:
            self.messages("illegal")
        else:
            if origin_card.rank > destination_card.rank:
                self.messages("illegal")
            elif destination_card.rank - origin_card.rank != 1:
                self.messages("illegal")
            else:
                layout.move_card(origin, destination)
                self.render_layout()

    def messages(self, message):
        """ manages the messages and prompts for the user """
        #initial message to user
        if message == "start":
            print("\n\n")
            print("- * Welcome to Terminal Solitaire! * -")
            self.print_seperator()
            print("new game | to start new game")
            print("quit     | to quit")
            self.print_seperator()
            print("Type a command to continue:")
        #legend for what symbols mean
        if message == "legend":
            print("[XX] = Face down card | C = Clubs | S = Spades  | A = Ace   | K = King\n[  ] = empty space    | H = Hearts| D = Diamonds| Q = Queen | J = Jack")
        #message for user to enter command
        if message == "enter cmd":
            print("\n(Type 'help' for list of commands)\nEnter command:")
        if message == "illegal":
            print("Illegal move. Please try again.")
            self.messages("enter cmd")
    @staticmethod
    def print_seperator():
        print("---------------------------------------------------------------------")

game = Game()
game.run()