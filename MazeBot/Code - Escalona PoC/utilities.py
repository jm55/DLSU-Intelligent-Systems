import os
import re

from tile import tile

def chk(): #To check if the script/class imports correctly.
    print("This is utilities.py")

def bar(length:int, fillchar:chr="="):
    print("".center(length, fillchar))

def header():
    h = "".center(40,"=") + "\n"
    h += "CSINTSY".center(40," ") + "\n"
    h += "MazeBot".center(40," ") + "\n"
    h += "Cruzada, Escalona, Francisco, Loyola".center(40," ") + "\n"
    h += "".center(40,"=") + "\n"
    return h

def terminate(reason:str, status:int=0):
    cls()
    print(header())
    print("SAFETY TERMINATION:\n" + reason)
    print("\nExiting...")
    exit(status)

def read_file(filepath:str):
    if not os.path.isfile(filepath): #Check if file exists
        terminate("File not found!", 1)
    elif os.path.getsize(filepath) <= 0: #Check if file contains anything
        terminate("File is empty!", 1)
    #Get extract file contents from file
    #Suggested as a list containing per line of the maze path.
    #Suggested example return: ['....G','.####', '...#S', '.#.#.', '.#...']
    return None

def find_manhattan(xi:int, yi:int, xf:int, yf:int):
    return abs(xf-xi) + abs(yf-yi)

def find_manhattan_tile(tile_init:tile, tile_final:tile):
    return find_manhattan(tile_init.x, tile_init.y, tile_final.x, tile_final.y)

def cls(): #Execute 'cls' command on Command Prompt
    os.system("cls")