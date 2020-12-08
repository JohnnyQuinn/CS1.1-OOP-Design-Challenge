from Layout import Layout

class Game(Layout):
    """ manages and runs the game """
    def __init__(self):
        """ games has a state of running and whether or not the player has won"""
        self.__game_running = False
        self.__game_won = False

    def run(self):
        self.__game_running = True
        self.messages("start")
        while self.__game_running == True:
            self.commands(input())

    def start_game(self):
        """ starts the game """
        layout = Layout()
        layout.build_table()
        self.render_table(layout.get_tables())
        pass

    def commands(self, input):
        """ takes in the user commands and reacts appropiately """
        if input == "quit":
            self.__game_running = False
        if input == "new game":
            self.start_game()
        
    def render_tables(self, layout):
        """ takes in the current card layout and renders the tables """
        self.print_seperator()
            
    def render_table(self, *args):
        """ takes in tables(1-7) and sorts them out to be printed to the terminal """
        table_grid = []
        tables = args[0]

        # creates a list consis
        for i in range(0, 49):
            table_grid.append("    ")
        for column in range(0, 7, 1):
            stop = 42+column
            i = 0
            for row in range(column, stop, 7):
                try:
                    table_grid[row] = tables[column][i].get_card_string()
                except:
                    pass
                i += 1

        final_string = ""
        print(table_grid)

        for i in range(0, 49, 1):
            if i != 0:
                if (i % 7) == 0:
                    final_string += "\n"

            final_string += table_grid[i] + " "

        print(final_string)


    def games_master(self):
        """ manages the rules of the game """
        pass

    def messages(self, message):
        """ manages the messages and prompts for the user """
        if message == "start":
            print("\n\n")
            print("- * Welcome to Terminal Solitaire! * -")
            self.print_seperator()
            print("new game | to start new game")
            print("quit     | to quit")
            self.print_seperator()
            print("Type a command to continue:")

    def print_seperator(self):
        print("----------------------------------")

    print("[??]         [  ][  ][  ][  ]")
    print(" (1) (2) (3) (4) (5) (6) (7)")
    print("[  ][  ][  ][  ][  ][  ][  ]")

game = Game()
game.run()