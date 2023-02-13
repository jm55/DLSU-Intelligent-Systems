import os
import re
from objects import *
def chk():
    """To check if the script/class imports correctly."""
    print("This is utilities.py")

def read_maze(filepath:str):
    """Generates a 2d list of the maze and creates a grid object after completing the 
    parsing of the maze file"""
    #print(filepath)
    with open(filepath, "r") as maze_file:
        size = int(maze_file.readline())
        tiles = [[0]*size for i in range(size)]
        
        for y in range(size):
            line = maze_file.readline().strip()
            for x in range(len(line)):
                tile_type = line[x]
                tiles[x][y] = tile(x, y, tile_type)
                
        grid_obj = grid(tiles)
    #print(grid) 
    return grid_obj

def get_manhattan(pos1, pos2):
    """Returns the manhattan distance between two points"""
    return (abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]))


def cls():
    """Execute 'cls' command on Command Prompt"""
    os.system("cls")
