'''
CS5001
Fall 2021
Final Project -- turtle_collections

Yutong He
'''

import turtle

# set up screen and initiates turtles
wn = turtle.Screen()
wn.screensize(400, 300)
wn.title("CS5001 Sliding Puzzle Game")

# tr for drawing splash screen, and game boards
tr = turtle.Turtle()
tr.hideturtle()
tr.speed("fastest")

# thumb_tr for showing thumbnail images
thumb_tr = turtle.Turtle()
thumb_tr.hideturtle()
thumb_tr.speed("fastest")

# shows status message in menu board
status_tr = turtle.Turtle()
status_tr.hideturtle()
status_tr.speed("fastest")
        
# turtles for reset, load, and quit buttons
reset_tr = turtle.Turtle()
reset_tr.hideturtle()
reset_tr.speed("fastest")

load_tr = turtle.Turtle()
load_tr.hideturtle()
load_tr.speed("fastest")

quit_tr = turtle.Turtle()
quit_tr.hideturtle()
quit_tr.speed("fastest")

# eraser turtle to erase puzzles
eraser = turtle.Turtle()
eraser.hideturtle()
eraser.speed("fastest")
