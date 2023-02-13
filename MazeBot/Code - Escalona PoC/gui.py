from grid import grid
import utilities as utils
import time

def main(grid:grid):
    utils.cls()
    print(utils.header())
    print_simple_grid(grid)

#Get the contents of self.open by bot location tuple
def get_grid_list(items:list):
    output = ""
    ctr = 0
    br_limit = 6
    for item in items:
        output += str(item.locate_bot()) + " "
        ctr += 1
        if ctr == br_limit:
            ctr = 0
            output += "\n"
            output += "".center(17," ")
    return output

def replay(open:list, closed:list, cont:bool=True, goal:bool=False):
    utils.cls()
    for c in closed:
        main(c)
        print("Bot's Frontier: ", get_grid_list(open))
        print("Bot's Explored: ", get_grid_list(closed))
        time.sleep(0.25)
    if cont:
        input("\n\nPress Enter key to continue...")

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
    print("\nBot Location: ", grid.locate_bot())
    print("Bot's Distance from S: ", grid.get_bot().s_dist)
    print("Bot's Distance from G: ", grid.get_bot().g_dist)
    print("Bot's Moves Count: ", grid.g_cost)
    print("Bot's Total Move Cost (F_Cost): ", str(grid.f_cost) + " = (" + str(grid.g_cost) + " + " + str(grid.h_cost) + ")")
    

def chk(): #To check if the script/class imports correctly.
    print("This is gui.py")