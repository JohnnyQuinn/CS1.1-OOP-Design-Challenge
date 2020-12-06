from Layout import Layout

class Game(Layout):
    """ manages and runs the game """
    def __init__(self):
        """ games has a state of running and whether or not the player has won"""
        self.game_running = False
        self.game_won = False

    def start_game(self):
        """ starts the game """
        self.build_table()
        pass

    def commands(self):
        """ takes in the user commands and reacts appropiately """
        pass

    def render(self):
        """ renders the game in the terminal """
        pass

    def games_master(self):
        """ manages the rules of the game """
        pass

    def messages(self):
        """ manages the messages and prompts for the user """
        pass