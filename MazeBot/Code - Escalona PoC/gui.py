from grid import grid
import utilities as utils

def main(grid):
    utils.cls()
    print(utils.header())
    print_simple_grid(grid)

def ask_filepath():
    utils.cls()
    print(utils.header())
    fp = input("Enter filename (include .txt; Empty defaults to maze.txt): ")
    utils.cls()
    if fp == "":
        return "maze.txt"
    else:
        return fp

def print_simple_grid(grid:grid):
    tiles = grid.get_tiles()
    size = grid.get_size()
    print("MAZE GRID")
    utils.bar(size*2)
    for y in range(size):
        row = ""
        for x in range(size):
            tile = tiles[y][x].get_attributes()
            row = row + tile[0] + " "
        print(row)
    utils.bar(size*2)
    print("\nStart Location:", grid.locate_s())
    print("Goal Location: ", grid.locate_g())
    utils.bar(size*2)
    print("Bot Location: ", grid.locate_bot())
    print("Distance from S: ", grid.get_bot().s_dist)
    print("Distance from G: ", grid.get_bot().g_dist)
    print("Moves Count: ", grid.g_cost)
    print("Total Move Cost (F_Cost): ", str(grid.f_cost) + " = (" + str(grid.g_cost) + " + " + str(grid.h_cost) + ")")
    

def chk(): #To check if the script/class imports correctly.
    print("This is gui.py")