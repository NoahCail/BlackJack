"""Classes and functions that track money bet in the game by specific players"""

class Player():
    """Class for a specific black jack player"""

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def __repr__(self):
        return self.name


def player_setup():
    name = input('What is your name?: ')
    balance = int(input('What is your starting balance?: '))
    player = Player(name, balance)
    # TODO: Stores the player info in the database
    return player

