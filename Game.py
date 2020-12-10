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
        if "np" in user_input:
            layout.manage_pile("next card")
            self.render_layout()
        #moves card from one location to another
        if "mv" in user_input and "to" in user_input:
            #splits user_input string into list 
            mv_cmd_list = list(user_input.split(" "))
            play = mv_cmd_list[0]
            origin = mv_cmd_list[1]
            destination = mv_cmd_list[3]
            self.games_master(play, origin, destination)
        #moves a group of cards from one location to another
        if "mvg" in user_input:
            mvg_cmd_list = list(user_input.split(" "))
            play = mvg_cmd_list[0]
            table = mvg_cmd_list[1]
            top_card = mvg_cmd_list[2]
            destination = mvg_cmd_list[4]
            self.games_master(play, table, top_card, destination)
        #get list of commands 
        if "help" in user_input:
            self.messages("help")

    def render_layout(self):
        """ renders layout of pile, foundations, and tables. Takes in tables(1-7) and sorts them out to be printed to the terminal. """
        #saves all tables to tables
        tables = layout.get_tables()

        #for when the table_grid needs more rows
        table_grid_extension = 0

        table_grid_max = 49

        #gets the largest table length
        max_table_len = len(tables[0])
        for table in tables:
            if len(table) > max_table_len:
                max_table_len = len(table)
        print(f'max_length_len: {max_table_len}')
        #sets the amount of rows needed to be added if there is a table with more than 7
        if max_table_len > 7:
            table_grid_extension = max_table_len - 7
            table_grid_extension *= 7
            table_grid_max += table_grid_extension
            print(f'table_grid_extension: {table_grid_extension}')
            print(f'table_grid_max: {table_grid_max}')

        print("\n\n\n\n")
        self.messages("legend")
        self.print_seperator()
        print("Pile:                      (F1) (F2) (F3) (F4)         <- Foundations")

        #renders pile card
        print("[XX]" + layout.manage_pile("current card") + f"                   {layout.get_last_foundation_card(1)} {layout.get_last_foundation_card(2)} {layout.get_last_foundation_card(3)} {layout.get_last_foundation_card(4)}")

        self.print_seperator()
        print("(T1)   (T2)   (T3)   (T4)   (T5)   (T6)   (T7)         <- Tables")
        self.print_seperator()

        table_grid = []

        # creates a list consisting of 49 empty spaces. Treated like a 7x7 grid
        for i in range(0, table_grid_max):
            table_grid.append("    ")

        # populates table grid. Starts with column, then goes into each row of that column, then goes to next column. 
        for column in range(0, 7, 1):
            stop = 43+column
            i = 0
            for row in range(column, stop+table_grid_extension, 7):
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
        for i in range(0, table_grid_max, 1):
            if i != 0:
                if (i % 7) == 0:
                    table_grid_string += "\n"

            table_grid_string += table_grid[i] + "   "

        print(table_grid_string)
        self.messages("enter cmd")

    def games_master(self, play, origin, destination, group_destination = ""):
        """ manages the rules of the game """
        print(origin)
        print(destination)
        #checks if the play is to move a card
        if play == "mv":
            origin_list = layout.translate_cmd(origin)
            destination_list = layout.translate_cmd(destination)
            origin_card = origin_list[-1]
            destination_card = destination_list[-1]
            try:
                print(f'Last move:\n{origin_card.get_card_string()} -> {destination_card.get_card_string()}')
            except:
                pass
            #checking if the origin or the destination is not a foundation table
            if "f" not in origin and "f" not in destination:
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
            #if origin or destination is a foundation table
            else:
                if destination_card != "  ":
                    if origin_card.color != destination_card.color:
                        self.messages("illegal")
                    else:
                        if origin_card.rank < destination_card.rank:
                            self.messages("illegal")
                        elif origin_card.rank - destination_card.rank != 1:
                            self.messages("illegal")
                        else:
                            layout.move_card(origin, destination)
                            self.render_layout()
                else:
                    layout.move_card(origin, destination)
                    self.render_layout()
        #checks if the play is to move a group of cards
        elif play == "mvg":
            if "f" in group_destination or "pile" in group_destination:
                self.messages("illegal")
                return
            else:
                destination_table = layout.translate_cmd(group_destination)
                destination_card = destination_table[-1]
            origin_table = layout.translate_cmd(origin)
            top_card = layout.translate_cmd(destination)
            if top_card.color == destination_card.color:
                    self.messages("illegal")
            else:
                if top_card.rank > destination_card.rank:
                    self.messages("illegal")
                elif destination_card.rank - origin_card.rank != 1:
                    self.messages("illegal")
                else:
                    layout.move_group(origin_table, top_card, destination_table)
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
        if message == "help":
            print("\nnew game                     | to start new game\nquit                         | to quit game\nmv (origin) to (destination) | to move card\nnp                          | to get next pile card")
    @staticmethod
    def print_seperator():
        print("---------------------------------------------------------------------")

game = Game()
game.run()