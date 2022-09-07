'''
CS5001
Fall 2021
Final Project -- Coordinates class

Yutong He
'''


class Coordinates:
    '''
        class: Coordinates
        Attributes: x_coordinate, y_coordinate
        Methods: __init__, __str__, set_x, set_y, set_coordinates,
                 get_x, get_y, get_coordinates
    '''

    def __init__(self, x_coordinate, y_coordinate):
        '''
        Constructor -- creates new instances of a coordinate
        Parameters:
           self -- the current object
           x_coordinate (float) -- the float indicating x coordinate
           y_coordinate (float) -- the float indicating y coordinate
        '''
        self.x = x_coordinate
        self.y = y_coordinate

    def __str__(self):
        '''
        Method -- returns a string that represents the current
                  coordinates
        Parameters:
           self -- the current object
        Returns a string indicating the current coordinates
        '''
        return f"coordinates: ({self.x}, {self.y})"

    def set_x(self, new_x_coordinate):
        '''
        Method -- sets new value to instance's x coordinate
        Parameters:
           self -- the current object
        Returns None.
        '''
        self.x = new_x_coordinate

    def set_y(self, new_y_coordinate):
        '''
        Method -- sets new value to instance's y coordinate
        Parameters:
           self -- the current object
        Returns None.
        '''
        self.y = new_y_coordinate
        
    def set_coordinates(self, new_x_coordinate, new_y_coordinate):
        '''
        Method -- sets new value to instance's coordinates
        Parameters:
           self -- the current object
        Returns None.
        '''
        self.x = new_x_coordinate
        self.y = new_y_coordinate

    def get_x(self):
        '''
        Method -- gets the value of the current instance's x coordinate
        Parameters:
           self -- the current object
        Returns the value of the x coordinate
        '''
        return self.x

    def get_y(self):
        '''
        Method -- gets the value of the current instance's y coordinate
        Parameters:
           self -- the current object
        Returns the value of the y coordinate
        '''
        return self.y
    
    def get_coordinates(self):
        '''
        Method -- gets the value of the current instance's coordinates
        Parameters:
           self -- the current object
        Returns the value of the coordinates
        '''
        return self.x, self.y
