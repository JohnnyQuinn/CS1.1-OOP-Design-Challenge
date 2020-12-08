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
        layout = Layout()
        layout.build_table()
        pile = layout.pile
        self.render_layout(layout.get_tables(), pile=pile)
        pass

    def commands(self, user_input):
        """ takes in the user commands and reacts appropiately """
        if user_input == "quit":
            if self.__game_running == True:
                user_response = input("\nAre you sure you want to quit? (yes/no):\n")
                if user_response == "yes":
                    self.__game_running = False
                elif user_response == "no":
                    self.messages("enter cmd")
        if user_input == "new game":
            if self.__game_running == True:
                user_response = input("\nAre you sure you want to start a new game? (yes/no):\n")
                if user_response == "yes":
                    self.start_game()
                elif user_response == "no":
                    self.messages("enter cmd")
            else:
                self.start_game()
            
    def render_layout(self, *args, pile):
        """ renders layout of pile, foundations, and tables. Takes in tables(1-7) and sorts them out to be printed to the terminal. """
        print("\n\n\n\n")
        self.messages("legend")
        self.print_seperator()
        print("Pile:                       (1)  (2)  (3)  (4)         <- Foundations")

        #renders pile card
        print("[XX]" + self.__current_pile_card + "                       [  ] [  ] [  ] [  ]")

        self.print_seperator()
        print("(1)     (2)    (3)    (4)    (5)    (6)    (7)         <- Tables")
        self.print_seperator()

        table_grid = []
        tables = args[0]

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
    

    def games_master(self):
        """ manages the rules of the game """
        pass

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
            print("[XX] = Face down card\n[  ] = empty space")
        #message for user to enter command
        if message == "enter cmd":
            print("\n(Type 'help' for list of commands)\nEnter command:")

    @staticmethod
    def print_seperator():
        print("---------------------------------------------------------------------")

game = Game()
game.run()