from objects import *
import utilities as utils
import time

def ask_file():
    header()
    filename = input("Enter filename (include .txt; Leave empty for default file \'maze.txt\'): ")
    if filename == "":
        return "maze.txt"
    else:
        return filename

def ask_save_file():
    entry = input("\nExit choices:\nS/s - Save Output\nAny Key - Exit without Saving Output\nEnter: ")
    if entry.lower() == 's':
        return True
    else:
        return False

def ask_manual_cont():
    entry = input("Enable manual progression (Y/N): ")
    if entry.lower() == 'y':
        return True
    else:
        return False  

def ask_rapid_search():
    entry = input("Enable rapid search (Y/N): ")
    if entry.lower() == 'y':
        return True
    else:
        return False    

def print_path(grid:grid, path:list, time_elapsed:float):
    if len(path) == 0:
        header()
        draw_grid(grid)
        print("NO RECOMMENDED PATH DETECTED FOR GIVEN MAZE!")
        print("Time taken: " + str(time_elapsed) + "s")
        return [grid.grid_as_string(),[],[]]
    prev_pos = path[0].get_pos()
    pos = []
    direction = []
    for p in path:
        pos.append(p.get_pos())
        direction.append(utils.find_direction(prev_pos, p.get_pos()))
        prev_pos = p.get_pos()
    utils.cls()
    header()
    print("Recommended Path Direction Grid:")
    print_direction_grid(grid, pos, direction)
    print("Total Move Count: " + str(len(path)))
    print("\nRecommended Path Coordinate:")
    print(pos)
    print("\nRecommended Path Direction:")
    print(direction)
    print("Time taken: " + str(time_elapsed) + "s")
    return [grid.grid_as_string(), pos, direction]

#Prints the major components of a grid printout
def main(grid:grid, frontier:list, explored:list, rapid_search:bool, cont:bool=True):
    if not rapid_search:
        for e in explored:
            utils.cls()
            header()
            pos = e.get_pos()
            print("Bot's Location: ", pos)
            draw_grid(grid, pos[0], pos[1])
            print_lists("Bot's Frontier: ", frontier)
            print_lists("Bot's Explored: ", explored)
            time.sleep(0.1)
        if cont:
            input("\n\nPress Enter to continue...")

def print_direction_grid(grid:grid, pos:list, direction:list):
    #draw_grid(grid)
    for ctr in range(len(pos)):
        indiv_pos = pos[ctr]
        grid.tiles[indiv_pos[0]][indiv_pos[1]].type = direction[ctr]
    draw_grid(grid)

#Used for printing contents (x,y) of frontier/explored
def print_lists(label:str, list:list):
    output = label
    ctr = 0
    br_limit = 6
    for l in list:
        output += str(l.get_pos()) + " "
        ctr += 1
        if ctr >= br_limit:
            ctr = 0
            output += "\n"
            output += "".center(len(label), " ")
    print(output)

#Draws the grid
def draw_grid(grid:grid, bot_x:int=-1, bot_y:int=-1):
    if bot_x > -1 and bot_y > -1:
        grid.update_bot(bot_x,bot_y)
    size = grid.get_size()
    output = ""
    for y in range(size):
        for x in range(size):
            output += grid.get_tiles()[x][y].type + " "
        output += "\n"
    print(output)

def header():
    print("".center(40,"="))
    print("MazeBot: MCO1".center(40," "))
    print("CSINTSY S14".center(40," "))
    print("Cruzada, Escalona, Francisco, Loyola".center(40," "))
    print("".center(40,"="))
    print("")