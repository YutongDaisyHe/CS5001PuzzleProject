'''
CS5001
Fall 2021
Final Project puzzle_game (driver function)

Yutong He
'''

from helper import *

def main():
    # show the splash screen and prompt user input
    set_splash_screen()
    players = prompt_input()

    # initiate the game
    draw_gameboard(players)
    # use mario.puz as the default puzzle file to start
    image = load_puzzles("mario.puz", "shuffled", players)

    # start game
    wn.onclick(lambda x, y: click(x, y, image, players))
    
if __name__ == "__main__":
    main()
