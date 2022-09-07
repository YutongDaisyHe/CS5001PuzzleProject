'''
CS5001
Fall 2021
Final Project -- Helper Functions

Yutong He
'''

import turtle
from time import sleep, ctime
import os
import random

from Players import Players
from Coordinates import Coordinates
from ImageInfo import ImageInfo

# set up screen and initiates turtles
from turtle_collections import *

# set constants for the size of game boards
PUZBOARD_WIDTH = 430
PUZBOARD_HEIGHT = 450
LEADERBOARD_WIDTH = 180
GAP = 50
PUZ_GAP = 5
MENU_HEIGHT = 100
BUTTON_WIDTH = 80
LOAD_HEIGHT = 76
QUIT_HEIGHT = 53


def set_splash_screen():
    '''
    Function: set_splash_screen
        Shows the splash screen and lets it linger for 3 seconds
    Parameters: None
    Returns: None. sets the splash screen image
    '''
    wn.addshape("Resources/splash_screen.gif")
    tr.shape("Resources/splash_screen.gif")
    tr.showturtle()
    sleep(3)
    tr.hideturtle()

def prompt_input():
    '''
    Function: prompt_input
        Prompts the user input on the name and the number of moves
    Parameters: None
    Returns:
        players (class instance) stores information about the player
    '''
    # get the name, set the name as Anonymous if cancel the name input
    name = wn.textinput("CS5001 Puzzle Slide", "Your Name:")
    if name == None:
        name = "Anonymous"
    # get the number of moves
    moves = wn.numinput("CS5001 Puzzle Slide - Moves",
                        "Enter the number of moves (chances) you want "
                        "(5-200)?", default=50, minval=5, maxval=200)
    # set the moves as default 50 without user input
    if moves == None:
        moves = 50
    else:
        moves = int(moves)
    players = Players(name, moves)
    return players

    
def draw_puz_board():
    '''
    Function: draw_puz_board
        Draws a puzzle board at the left side of the screen
    Parameters: None
    Returns: None
    '''
    tr.pu()
    tr.goto(- wn.window_width() / 2 + GAP, wn.window_height() / 2 - GAP)
    tr.pensize(5)
    tr.pd()
    tr.forward(PUZBOARD_WIDTH)
    tr.right(90)
    tr.forward(PUZBOARD_HEIGHT)
    tr.right(90)
    tr.forward(PUZBOARD_WIDTH)
    tr.right(90)
    tr.forward(PUZBOARD_HEIGHT)
    tr.right(90)
    

def draw_menu_board():
    '''
    Function: draw_menu_board
        Draws a menu board at the bottom of the screen
    Parameters: None
    Returns: None
    '''
    tr.pu()
    tr.goto(- wn.window_width() / 2 + GAP, - wn.window_height() / 2
            + GAP + MENU_HEIGHT)
    tr.pd()
    tr.forward(wn.window_width() - GAP * 2)
    tr.right(90)
    tr.forward(MENU_HEIGHT)
    tr.right(90)
    tr.forward(wn.window_width() - GAP * 2)
    tr.right(90)
    tr.forward(MENU_HEIGHT)
    tr.right(90)


def draw_leaderboard():
    '''
    Function: draw_leaderboard
        Draws a leaderboard at the right side of the screen
    Parameters: None
    Returns: None
    '''
    tr.pu()
    tr.goto(wn.window_width() / 2 - GAP - LEADERBOARD_WIDTH,
            wn.window_height() / 2 - GAP)
    tr.pencolor("blue")
    tr.pd()
    tr.forward(LEADERBOARD_WIDTH)
    tr.right(90)
    tr.forward(PUZBOARD_HEIGHT)
    tr.right(90)
    tr.forward(LEADERBOARD_WIDTH)
    tr.right(90)
    tr.forward(PUZBOARD_HEIGHT)
    tr.right(90)


def draw_gameboard(players):
    '''
    Function: draw_gameboard
        Calls functions to draw a game board with a puzzle board, a
        leadaer board, and a menu board.
    Parameters: players (class instance) information about players
    Returns: None
    '''
    draw_puz_board()
    draw_menu_board()
    draw_leaderboard()
    # show contents in leaderboard
    show_leaders(players)
    

def show_thumbnail(image_dict):
    '''
    Function: show_thumbnail
        Shows the thumbnail image on the top of the leaderboard
    Parameters:
        image_dict (dict) a dictionary containing information about the
        chosen image
    Returns: None. Shows the image in the leaderboard.
    '''
    thumbnail_dir = image_dict["thumbnail"].strip("\n")
    thumbnail_len = int(image_dict["size"])
    thumb_tr.pu()
    thumb_tr.goto(wn.window_width() / 2 - GAP * 2 - PUZ_GAP,
                  wn.window_height() / 2 - GAP - thumbnail_len / 2)
    wn.addshape(thumbnail_dir)
    thumb_tr.shape(thumbnail_dir)
    thumb_tr.showturtle()


def show_error(message):
    '''
    Function: show_error
        Show file error message using turtle and update the error log
    Parameters: message (str) specific error message
    Returns: None. 
    '''
    try:
        # error turtle to show error messages
        error_tr = turtle.Turtle()
        error_tr.hideturtle()
        error_tr.speed("fastest")
        error_tr.pu()
        error_tr.goto(0, 0)
        if "leaderboard" in message:
            wn.addshape("Resources/leaderboard_error.gif")
            error_tr.shape("Resources/leaderboard_error.gif")
            error_tr.showturtle()
        else:
            wn.addshape("Resources/file_error.gif")
            error_tr.shape("Resources/file_error.gif")
            error_tr.showturtle()
        sleep(2)
        error_tr.hideturtle()
    
        if not os.path.exists("5001_puzzle.err"):
            with open("5001_puzzle.err", mode="w") as outfile:
                time_str = ctime()
                outline = time_str + ":Error: " + message + "\n"
                outfile.write(outline)
        else:
            with open("5001_puzzle.err", mode="a") as outfile:
                time_str = ctime()
                outline = time_str + ":Error: " + message + "\n"
                outfile.write(outline)
    except OSError:
        print("Cannot process file 5001_puzzle.err "
              "LOCATION: helper.show_error()")
        
    
def write_leaders(players):
    '''
    Function: write_leaders
        Write players of the game to a txt file
    Parameters: players (class instance) information about players
    Returns: None. Writes the information to the file.
    '''
    try:
        if not os.path.exists("leaderboard.txt"):
            with open("leaderboard.txt", mode="w") as outfile:  
                outfile.write(players.output_leaders())
        else:
            with open("leaderboard.txt", mode="a") as outfile:
                for each in players.output_leaders():
                    outfile.write(each)
    except OSError:
        message = "Could not open leaderboard.txt. "\
                  "LOCATION: helper.write_leaders()"
        show_error(message)
        
    
def show_leaders(players):
    '''
    Function: show_leaders
        Lists leaders of the game in the leaderboard.
    Parameters: players (class instance) information about players
    Returns: None. Writes the top 10 leader names in the leaderboard.
    '''
    
    tr.pu()
    tr.goto(wn.window_width() / 2 - GAP - LEADERBOARD_WIDTH
            + PUZ_GAP * 2, wn.window_height() / 2 - GAP
            - PUZ_GAP * 10)
    tr.pd()
    tr.color("blue")
    tr.write("Leaders:", font=('Arial', 17, 'normal'))
    
    try:
        print_leaders = ""
        read_leaders = []
        # sort the leaders for leaderboard
        with open("leaderboard.txt", mode="r") as infile:
            for each in infile:
                line = {}
                line["moves"] = int(each.split(" : ")[0])
                line["name"] = each.split(" : ")[1]
                read_leaders.append(line)
        read_leaders.sort(key=lambda x: x.get("moves"))
        
        # prepare to show the top 10 leaders
        if len(read_leaders) < 10:
            for player in read_leaders:
                print_leaders += (str(player["moves"]) + " : "
                                  + player["name"])
            print_leaders += "\n" * (10 - len(read_leaders))
        else:
            for player in read_leaders[:10]:
                print_leaders += (str(player["moves"]) + " : "
                                  + player["name"])
        
        leader_tr = turtle.Turtle()
        leader_tr.hideturtle()
        leader_tr.speed("fastest")
        leader_tr.clear()
        leader_tr.pu()
        leader_tr.goto(wn.window_width() / 2 - GAP - LEADERBOARD_WIDTH
                       + PUZ_GAP * 2, wn.window_height() / 2 - GAP
                       - PUZ_GAP * 60)
        leader_tr.pd()
        leader_tr.color("blue")
        leader_tr.write(print_leaders, font=('Arial', 17, 'normal'))
        
    except OSError:
        message = "Could not open leaderboard.txt. "\
                  "LOCATION: helper.show_leaders()"
        show_error(message)
        
    
def show_menu():
    '''
    Function: show_menu
        Show menu options in the menu board.
    Parameters: None.
    Returns: menu_pos (dict) coordinates of menu option symbols
    '''
    menu_pos = {}
    menu_pos["reset"] = (wn.window_width() / 2 - GAP - 3
                         * (BUTTON_WIDTH + GAP / 5), - wn.window_height()
                         / 2 + GAP + MENU_HEIGHT / 2)
    menu_pos["load"] = (wn.window_width() / 2 - GAP - 2
                        * (BUTTON_WIDTH + GAP / 5), - wn.window_height()
                        / 2 + GAP
                        + MENU_HEIGHT / 2)
    menu_pos["quit"] = (wn.window_width() / 2 - GAP - BUTTON_WIDTH - GAP / 5,
                        - wn.window_height() / 2 + GAP + MENU_HEIGHT / 2)

    reset_tr.pu()
    reset_tr.speed("fastest")
    reset_tr.goto(menu_pos["reset"])
    wn.addshape("Resources/resetbutton.gif")
    reset_tr.shape("Resources/resetbutton.gif")
    reset_tr.showturtle()
    
    load_tr.pu()
    load_tr.speed("fastest")
    load_tr.goto(menu_pos["load"])
    wn.addshape("Resources/loadbutton.gif")
    load_tr.shape("Resources/loadbutton.gif")
    load_tr.showturtle()
    
    quit_tr.pu()
    quit_tr.speed("fastest")
    quit_tr.goto(menu_pos["quit"])
    wn.addshape("Resources/quitbutton.gif")
    quit_tr.shape("Resources/quitbutton.gif")
    quit_tr.showturtle()
    return menu_pos


def get_image_name():
    '''
    Function: get_image_name
        Reads titles of images into a list of string.
    Parameters: None
    Returns: image_name (list) a list of string indicating image titles
    '''
    image_name = os.listdir("Images/")
    if ".DS_Store" in image_name:
        image_name.remove(".DS_Store")
    return image_name


def read_puz_file(puz_file):
    '''
    Function: read_puz_file
        Reads information about chosen puzzles in the puz file
    Parameters: puz_file (str) puz file name 
    Returns: image_info (class) a class including information
             about chosen puzzles
    '''
    try:
        with open(puz_file, mode="r") as infile:
            image_dict = {}
            for each in infile:
                line = each.split(": ")
                image_dict[line[0]] = line[1]
            return image_dict
    except OSError:
        message = f"File {puz_file} does not exist "\
                  "LOCATION: helper.read_puz_file()"
        show_error(message)


def set_puzzle_grid(puzzle_length, x, y):
    '''
    Function: set_puzzle_grid
        Sets puzzle grid in the puzzle board.
    Parameters:
        puzzle_length (int) size of each puzzle piece
        x (int) indicating the position at x axis
        y (int) indicating the position at y axis
    Returns: None. 
    '''
    tr.pu()
    tr.speed("fastest")
    tr.goto(x - puzzle_length / 2, y + puzzle_length / 2)
    tr.pencolor("black")
    tr.pensize(3)
    tr.pd()
    tr.forward(puzzle_length)
    tr.right(90)
    tr.forward(puzzle_length)
    tr.right(90)
    tr.forward(puzzle_length)
    tr.right(90)
    tr.forward(puzzle_length)
    tr.right(90)


def place_puzzles(puz_len, puz_total, image_dict, status):
    '''
    Function: place_puzzles
        Algorithm of placing the puzzle pieces
    Parameters:
        puz_len (int) puzzle piece size
        puz_total (int) total number of puzzle pieces
        image_dict (dict) metadata information about selected image
        status (str) indicating shuffled or reset status
    Returns: position_dict (dict) indexes and coordinates of puzzle
             position
    '''
    start_point = (- wn.window_width() / 2 + GAP + PUZ_GAP * 2
                   + puz_len / 2, wn.window_height() / 2 - 1.5 * GAP
                   - PUZ_GAP - puz_len / 2)
    position_dict = {}

    # initiates index
    reset_index = 1
    
    shuffled_index_lst = []
    for each in range(1, puz_total + 1):
        shuffled_index_lst.append(each)
    random.shuffle(shuffled_index_lst)
    shuffled_counter = 0

    for i in range(int(start_point[1]), int(start_point[1])
                       - int(puz_total ** 0.5 * (puz_len + PUZ_GAP)),
                       - puz_len - PUZ_GAP):
            for j in range(int(start_point[0]), int(puz_total ** 0.5)
                           * (puz_len + PUZ_GAP) + int(start_point[0]),
                           puz_len + PUZ_GAP):
                set_puzzle_grid(puz_len, j, i)
                
                puz_images = turtle.Turtle()
                puz_images.hideturtle()
                puz_images.speed("fastest")
                puz_images.pu()
                puz_images.goto(j, i)

                if status == "reset":
                    image_dir = image_dict[f"{reset_index}"].strip("\n")
                    wn.addshape(image_dir)
                    puz_images.shape(image_dir)
                    # store the center coordinates of each puzzle piece
                    position_dict[reset_index] = [(j, i), image_dir]
                    reset_index += 1
                    
                else:
                    shuffled_index = shuffled_index_lst[shuffled_counter]
                    image_dir = image_dict[f"{shuffled_index}"].strip("\n")
                    wn.addshape(image_dir)
                    puz_images.shape(image_dir)
                    
                    # store the center coordinates of each puzzle piece
                    position_dict[shuffled_counter + 1] = [(j, i), image_dir]
                    shuffled_counter += 1
                puz_images.showturtle()
    show_thumbnail(image_dict)
    return position_dict           
    
    
def load_puzzles(puzzle, status, players):
    '''
    Function: load_puzzles
        Load puzzle pictures in puzzle board.
    Parameters:
        puzzle (str) puz file name of the loaded puzzle
        status (str) indicating shuffled or reset status
        players (class instance) information about the player 
    Returns: image (class instance) about the image information
    '''
    try:
        # show menu buttons and return the button coordinates
        menu_pos = show_menu()
        
        # get information about the chosen puzzle
        image_dict = read_puz_file(puzzle)
        puz_total = int(image_dict["number"])
        row_total = int(puz_total ** 0.5)
        puz_len = int(image_dict["size"])
        if row_total not in [2, 3, 4]:
            raise OSError
        # place puzzles in the puzzle board
        position_dict = place_puzzles(puz_len, puz_total, image_dict, status)
        
        # store image information in the class instance
        image = ImageInfo(image_dict["name"].strip("\n") + ".puz",
                          int(image_dict["number"]),
                          int(image_dict["size"]),
                          image_dict["thumbnail"] .strip("\n"),
                          dict(list(image_dict.items())[4:]),
                          position_dict,
                          menu_pos)
        return image   
    except OSError:
        message = f"Cannot process the malfomed puzzle file {puzzle} "\
                  "LOCATION: helper.load_puzzles()"
        show_error(message)
        

def erase_puzzles(image):
    '''
    Function: erase_puzzles
        Erase puzzle pictures in puzzle board.
    Parameters:
        image (class instance) information about the current puzzle
    Returns: None
    '''
    # get information about the chosen puzzle
    puz_len = image.get_info()["size"]
    puz_total = image.get_info()["number"]
    start_point = (- wn.window_width() / 2 + GAP + PUZ_GAP * 2
                   + puz_len / 2, wn.window_height() / 2 - 1.5 * GAP
                   - PUZ_GAP - puz_len / 2)
    
    for i in range(int(start_point[1]), int(start_point[1])
                       - int(puz_total ** 0.5 * (puz_len + PUZ_GAP)),
                       - puz_len - PUZ_GAP):
            for j in range(int(start_point[0]), int(puz_total ** 0.5)
                           * (puz_len + PUZ_GAP) + int(start_point[0]),
                           puz_len + PUZ_GAP):
                eraser.pu()
                eraser.goto(j - puz_len / 2 - PUZ_GAP,
                            i + puz_len / 2 + PUZ_GAP)
                eraser.pencolor("white")
                eraser.fillcolor("white")
                eraser.pensize(5)
                eraser.pd()
                eraser.begin_fill()
                eraser.forward(puz_len + PUZ_GAP)
                eraser.right(90)
                eraser.forward(puz_len + PUZ_GAP)
                eraser.right(90)
                eraser.forward(puz_len + PUZ_GAP)
                eraser.right(90)
                eraser.forward(puz_len + PUZ_GAP)
                eraser.right(90)
                eraser.end_fill()

            
def check_result(image):
    '''
    Function: check_result
        Check if the player wins or loses
    Parameters:
        image (class instance) puz file name of the loaded puzzle
    Returns: True or False (bool) win or lose
    '''
    # compare the directory of pieces with the same index
    pieces_lst = list(image.get_info()["pieces"].items())
    position_lst = list(image.get_info()["position"].items())
    counter = 0
    for i in range(image.get_info()["number"]):
        if (int(pieces_lst[i][0]) == position_lst[i][0]
            and pieces_lst[i][1].strip("\n") == position_lst[i][1][1]):
            counter += 1
    if counter == image.get_info()["number"]:
        return True
    return False


def get_pos(x, y, image):
    '''
    Function: get_pos
        Get coordinates for clicked position, blank puzzle piece, and
        menu buttons
    Parameters:
        x (float) x coordinate of mouse click position
        y (float) y coordinate of mouse click position
        image (class instance) information about the image
    Returns: pos (dict) a dictionary using click_pos, blank_pos,
             blank_pos_key, reset_pos, load_pos, and quit_pos as
             keys. Corresponding tuples or int as values.
    '''
    pos = {}
    # get the coordinates of the clicked position
    coor = Coordinates(x, y)
    pos["click_pos"] = coor.get_coordinates()

    # get the coordinates of the blank puzzle piece
    for num in range(1, image.get_info()["number"] + 1): 
        if "blank.gif" in image.get_info()["pieces"][str(num)]:
            blank_index = str(num)
    blank_dir = image.get_info()["pieces"][blank_index].strip("\n")
    pos_lst = list(image.get_info()["position"].items())
    for each in pos_lst:
        if each[1][1] == blank_dir:
            index = pos_lst.index(each)
    blank_pos_key = pos_lst[index][0]
    pos["blank_pos"] = image.get_info()["position"][blank_pos_key][0]
    pos["blank_pos_key"] = blank_pos_key

    # get the coordinates of the menu buttons
    pos["reset_pos"] = image.get_info()["menu_pos"]["reset"]
    pos["load_pos"] = image.get_info()["menu_pos"]["load"]
    pos["quit_pos"] = image.get_info()["menu_pos"]["quit"]
    
    return pos
    

def check_click_pos(pos, row, size):
    '''
    Function: check_click_pos
        Check the click position 
    Parameters:
        pos (dict) a dictionary using click_pos, blank_pos,
             blank_pos_key, reset_pos, load_pos, and quit_pos as
             keys. Corresponding tuples or int as values.
        row (int) number of puzzle rows
        size (int) puzzle piece length
    Returns: flag (str) indicating the click position
    '''
    # obtain coordinates from the pos dictionary
    blank_pos = pos["blank_pos"]
    click_pos = pos["click_pos"]
    reset_pos = pos["reset_pos"]
    load_pos = pos["load_pos"]
    quit_pos = pos["quit_pos"]
    flag = ""
    
    # check if click inside the game board
    if (- wn.window_width() / 2 + GAP + PUZ_GAP * 2 <= click_pos[0]
        <= - wn.window_width() / 2 + GAP + PUZ_GAP * 2 + (size + PUZ_GAP)
        * row) and (wn.window_height() / 2 - 1.5 * GAP - PUZ_GAP
                    - (size + PUZ_GAP) * row <= click_pos[1]
                    <= wn.window_height() / 2 - 1.5 * GAP - PUZ_GAP):
    
        # check if click at the right or left side of the blank piece
        if (blank_pos[0] + 0.5 * size + PUZ_GAP <= click_pos[0]
            <= blank_pos[0] + 1.5 * size + PUZ_GAP and blank_pos[1]
            - 0.5 * size <= click_pos[1] <= blank_pos[1] + 0.5 * size):
            flag = "right"
        elif (blank_pos[0] - 1.5 * size - PUZ_GAP <= click_pos[0]
              <= blank_pos[0] - 0.5 * size - PUZ_GAP and blank_pos[1]
              - 0.5 * size <= click_pos[1] <= blank_pos[1] + 0.5 * size):
            flag = "left"
            
        # check if click at the top or bottom side of the blank piece
        elif (blank_pos[1] + 0.5 * size + PUZ_GAP <= click_pos[1]
              <= blank_pos[1] + 1.5 * size + PUZ_GAP and blank_pos[0]
              - 0.5 * size <= click_pos[0] <= blank_pos[0] + 0.5 * size):
            flag = "top"
        elif (blank_pos[1] - 1.5 * size - PUZ_GAP <= click_pos[1]
              <= blank_pos[1] - 0.5 * size - PUZ_GAP and blank_pos[0]
              - 0.5 * size <= click_pos[0] <= blank_pos[0] + 0.5 * size):
            flag = "bottom"
        
    # check if click on the menu buttons
    elif (reset_pos[0] - BUTTON_WIDTH / 2 <= click_pos[0] <= reset_pos[0]
          + BUTTON_WIDTH / 2 and reset_pos[1] - BUTTON_WIDTH / 2
          <= click_pos[1] <= reset_pos[1] + BUTTON_WIDTH / 2):
        flag = "reset"
    elif (load_pos[0] - BUTTON_WIDTH / 2 <= click_pos[0] <= load_pos[0]
          + BUTTON_WIDTH / 2 and load_pos[1] - LOAD_HEIGHT / 2
          <= click_pos[1] <= load_pos[1] + LOAD_HEIGHT / 2):
        flag = "load"
    elif (quit_pos[0] - BUTTON_WIDTH / 2 <= click_pos[0] <= quit_pos[0]
          + BUTTON_WIDTH / 2 and quit_pos[1] - QUIT_HEIGHT / 2
          <= click_pos[1] <= quit_pos[1] + QUIT_HEIGHT / 2):
        flag = "quit"
    # click at other blank areas
    else:
        flag = "other"
    return flag


def swap(flag, image, blank_pos_key):
    '''
    Function: swap
        Swap clicked puzzle with the blank puzzle if applicable
    Parameters:
        flag (str) indicating clicked position
        image (class instance) information about the image
        blank_pos_key (int) indicating the blank piece position in the
            game board labeled from 1 to number of pieces in left to
            right, top to bottom order
    Returns: None.
    '''
    blank_tr = turtle.Turtle()
    blank_tr.hideturtle()
    blank_tr.pu()
    blank_tr.speed("fastest")
    from_tr = turtle.Turtle()
    from_tr.hideturtle()
    from_tr.pu()
    from_tr.speed("fastest")
    
    position_dict = image.get_info()["position"]
    row = image.get_info()["number"] ** 0.5
    # if clicked at the right piece next to the blank piece
    if flag == "right":
        image.swap_dir(blank_pos_key + 1, blank_pos_key)
        from_tr.goto(position_dict[blank_pos_key + 1][0])
        wn.addshape(position_dict[blank_pos_key + 1][1])
        from_tr.shape(position_dict[blank_pos_key + 1][1])
        
    # if clicked at the left piece next to the blank piece
    elif flag == "left":
        image.swap_dir(blank_pos_key - 1, blank_pos_key)
        from_tr.goto(position_dict[blank_pos_key - 1][0])
        wn.addshape(position_dict[blank_pos_key - 1][1])
        from_tr.shape(position_dict[blank_pos_key - 1][1])
        
    # if clicked at the top piece next to the blank piece    
    elif flag == "top":
        image.swap_dir(blank_pos_key - row, blank_pos_key)
        from_tr.goto(position_dict[blank_pos_key - row][0])
        wn.addshape(position_dict[blank_pos_key - row][1])
        from_tr.shape(position_dict[blank_pos_key - row][1])
        
    # if clicked at the bottom piece next to the blank piece
    elif flag == "bottom":
        image.swap_dir(blank_pos_key + row, blank_pos_key)
        from_tr.goto(position_dict[blank_pos_key + row][0])
        wn.addshape(position_dict[blank_pos_key + row][1])
        from_tr.shape(position_dict[blank_pos_key + row][1])
        
    from_tr.showturtle()  
    blank_tr.goto(position_dict[blank_pos_key][0])
    wn.addshape(position_dict[blank_pos_key][1])
    blank_tr.shape(position_dict[blank_pos_key][1])
    blank_tr.showturtle()
    

def click_menu_buttons(flag, image, players):
    '''
    Function: click_menu_buttons
        Update the game status based on the clicked menu buttons
    Parameters:
        flag (str) indicating clicked position
        image (class instance) information about the image
        players (class instance) information about the player
    Returns: None.
    '''
    message_tr = turtle.Turtle()
    message_tr.hideturtle()
    message_tr.speed("fastest")
    # if clicked on quit
    if flag == "quit":
        message_tr.pu()
        message_tr.goto(0, 0)
        wn.addshape("Resources/quitmsg.gif")
        message_tr.shape("Resources/quitmsg.gif")
        message_tr.showturtle()
        sleep(3)
        wn.addshape("Resources/credits.gif")
        message_tr.shape("Resources/credits.gif")
        sleep(3)
        wn.bye()
    # if clicked on reset or load
    else:
        new_players = Players(players.get_info()["name"],
                              players.get_info()["moves"])
        if flag == "reset":
            erase_puzzles(image)
            image = load_puzzles(image.get_info()["name"], "reset",
                                 new_players)
            wn.onclick(lambda x, y: click(x, y, image, players))
        elif flag == "load":
            try:
                # get a list of puz file names in the directory
                image_name = get_image_name()
                # show file_warning message if there are over 10 files
                if len(image_name) > 10:
                    message_tr.pu()
                    message_tr.goto(0, 0)
                    wn.addshape("Resources/file_warning.gif")
                    message_tr.shape("Resources/file_warning.gif")
                    message_tr.showturtle()
                    sleep(3)
                    message_tr.hideturtle()
                # show list of file names
                image_name_str = ""
                for each in image_name:
                    image_name_str += each + ".puz" + "\n"
                name = wn.textinput("Load Puzzle",
                                    "Enter the name of the "
                                    "puzzle you wish to load. "
                                    "Choices are:\n"
                                    f"{image_name_str}")
                # if click ok or cancel without any input
                if name == None or name == "":
                    wn.onclick(lambda x, y: click(x, y, image, players))
                # check invalid user input
                elif name + "\n" not in image_name_str:
                    raise OSError
                    wn.onclick(lambda x, y: click(x, y, image, players))
                else:
                    thumb_tr.hideturtle()
                    erase_puzzles(image)
                    status_tr.clear()
                    status_tr.pu()
                    status_tr.goto(- wn.window_width() / 2 + 2 * GAP,
                                   - wn.window_height() / 2 + GAP
                                   + MENU_HEIGHT / 2 - PUZ_GAP * 4)
                    status_tr.pd()
                    status_tr.write("Player Moves: ",
                                    font=('Arial', 24, 'normal', 'bold'))
                    image = load_puzzles(name, "shuffled", new_players)
                    wn.onclick(lambda x, y: click(x, y, image, new_players))
            except OSError:
                message = f"File {name} does not exist "\
                          "LOCATION: helper.click_menu_buttons()"
                show_error(message)

    
def click(x, y, image, players):
    '''
    Function: click
        Mouse click event function to swap the puzzle or ignore the click
    Parameters:
        x (float) x coordinate of mouse click position
        y (float) y coordinate of mouse click position
        image (class instance) information about the image
        players (class instance) information about the player
    Returns: None.
    '''
    # get coordinates of clicked position, blank piece, and menu buttons
    pos = get_pos(x, y, image)
    
    row = int(image.get_info()["number"] ** 0.5)
    size = image.get_info()["size"]

    # check the clicked postion
    flag = check_click_pos(pos, row, size)

    # swap clicked puzzle with the blank puzzle if clicked accordingly
    blank_pos_key = pos["blank_pos_key"]
        
    if flag in ["right", "left", "top", "bottom"]:
        swap(flag, image, blank_pos_key)
        
        # update the played moves in the players class instance
        players.set_played_moves(1)
        
        # check if won
        end_tr = turtle.Turtle()
        end_tr.hideturtle()
        end_tr.speed("fastest")
        done = check_result(image)
        
        status_tr.pu()
        status_tr.goto(- wn.window_width() / 2 + 2 * GAP,
                       - wn.window_height() / 2 + GAP + MENU_HEIGHT / 2
                       - PUZ_GAP * 4)
        if done and (players.get_info()['played_moves']
                     <= players.get_info()['moves']):
            status_tr.clear()
            status_tr.pd()
            status_tr.write("Player Moves: "
                            f"{players.get_info()['played_moves']}",
                            font=('Arial', 24, 'normal', 'bold'))
            end_tr.pu()
            end_tr.goto(0, 0)
            wn.addshape("Resources/winner.gif")
            end_tr.shape("Resources/winner.gif")
            end_tr.showturtle()
            # update information into leaderboard.txt 
            write_leaders(players)
            sleep(3)
            wn.addshape("Resources/credits.gif")
            end_tr.shape("Resources/credits.gif")
            sleep(3)
            wn.bye()
        # check if lost
        elif not done and (players.get_info()['played_moves']
                           > players.get_info()['moves']):
            end_tr.pu()
            end_tr.goto(0, 0)
            wn.addshape("Resources/Lose.gif")
            end_tr.shape("Resources/Lose.gif")
            end_tr.showturtle()
            sleep(3)
            wn.addshape("Resources/credits.gif")
            end_tr.shape("Resources/credits.gif")
            sleep(3)
            wn.bye()
        # if neither won or lost
        else:
            status_tr.clear()
            status_tr.pd()
            status_tr.write("Player Moves: "
                            f"{players.get_info()['played_moves']}",
                            font=('Arial', 24, 'normal', 'bold'))
    # check if clicked on menu buttons
    elif flag in ["reset", "quit", "load"]:
        click_menu_buttons(flag, image, players)
