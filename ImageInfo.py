'''
CS5001
Fall 2021
Final Project -- ImageInfo class

Yutong He
'''


class ImageInfo:
    '''
        class: ImageInfo
        Attributes: name, number, size, thumbnail, pieces, position,
                    menu_pos
        Methods: __init__, __str__, swap_dir, get_info
    '''

    def __init__(self, name, number, size, thumbnail, pieces, position,
                 menu_pos):
        '''
        Constructor -- creates new instances of a coordinate
        Parameters:
           self -- the current object
           name (str) -- the name of the image file
           number (int) -- the number of image pieces
           size (int) -- the integer indicating the length of a piece
           thumbnail (str) -- the directory of the thumbnail image
           pieces (dictionary) -- a dictionary of the directiory of
               pieces, using strings of index numbers as keys  
           position (dictionary) -- a dictionary of each piece's
               position, using integers as keys which indicate the
               position of piece from left to right, top to bottom
               (from 1 to total number of pieces). Values are lists of
               coordinate tuples and strings of directory of image
           menu_pos (dict) -- a dictionary of the coordinates of menu
               icons using "reset", "load", and "quit" as keys
        '''
        self.name = name
        self.number = number
        self.size = size
        self.thumbnail = thumbnail
        self.pieces = pieces
        self.position = position
        self.menu_pos = menu_pos

    def __str__(self):
        '''
        Method -- returns a string representing the image information
        Parameters:
            self -- the current object
        Returns: a string indicating the information about the puz
                 image file
        '''
        output = (f"name: {self.name}\n"
                  f"number: {self.number}\n"
                  f"size: {self.size}\n"
                  f"thumbnail: {self.thumbnail}\n")
        output_pieces = ""
        for piece_key, piece_value in self.pieces.items():
            output_pieces += piece_key + ": " + str(piece_value)
        output_position = ""
        for position_key, position_value in self.position.items():
            output_position += (str(position_key) + ": "
                                + str(position_value) + "\n")
        output_menu = ""
        for menu_key, menu_value in self.menu_pos.items():
            output_menu += (str(menu_key) + ": " + str(menu_value) + "\n")
        return (output + output_pieces + "\n" + output_position + "\n"
                + output_menu)

    def swap_dir(self, from_index, blank_index):
        '''
        Method -- resets new values to puzzle position
        Parameters:
           self -- the current object
           from_index (int) -- indicating the location of the non-blank
           blank_index (int) -- indicating the location of the blank
        Returns None.
        '''
        temp = self.position[blank_index][1]
        self.position[blank_index][1] = self.position[from_index][1]
        self.position[from_index][1] = temp

    def get_info(self):
        '''
        Method -- gets the information on the current instance
        Parameters:
           self -- the current object
        Returns:
           info (dict) a dictionary containing information of
           the chosen image file
        '''
        info = {}
        info["name"] = self.name
        info["number"] = self.number
        info["size"] = self.size
        info["thumbnail"] = self.thumbnail
        info["pieces"] = self.pieces
        info["position"] = self.position
        info["menu_pos"] = self.menu_pos
        return info
