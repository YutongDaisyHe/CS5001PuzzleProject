'''
CS5001
Fall 2021
Final Project -- Players class

Yutong He
'''


class Players:
    '''
        class: Players
        Attributes: name, moves, played_moves
        Methods: __init__, __str__, set_played_moves, get_info,
                 output_leaders
    '''

    def __init__(self, name, moves, played_moves=0):
        '''
        Constructor -- creates new instances
        Parameters:
           self -- the current object
           name (str) -- the name of the player
           moves (int) -- the number of player input moves
           played_moves (int) -- (optional) the number of played moves
        '''
        self.name = name
        self.moves = moves
        self.played_moves = played_moves

    def __str__(self):
        '''
        Method -- returns a string representing the player information
        Parameters:
            self -- the current object
        Returns: output (str) -- information about the player
        '''
        output = (f"name: {self.name}\n"
                  f"moves: {self.moves}\n"
                  f"played_moves: {self.played_moves}\n")
        return output

    def set_played_moves(self, new_moves):
        '''
        Method -- sets the updated played_moves
        Parameters:
            self -- the current object
            new_moves (int) -- the added played moves 
        Returns: None.
        '''
        self.played_moves += new_moves

    def get_info(self):
        '''
        Method -- gets the information on the current instance
        Parameters:
           self -- the current object
        Returns:
           info (dict) a dictionary containing information about the
           player
        '''
        info = {}
        info["name"] = self.name
        info["moves"] = self.moves
        info["played_moves"] = self.played_moves
        return info

    def output_leaders(self):
        '''
        Method -- returns the information in string
        Parameters:
           self -- the current object
        Returns: (str) the information for the leaderboard
        '''
        return " " + str(self.played_moves) + " : " + self.name + "\n"
