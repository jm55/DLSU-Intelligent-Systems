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

def ask_post_search():
    entry = input("\nMenu:\nS/s - Save Output\nX/x - Exit without Saving Output\nEnter - Repeat Runtime\n\nEnter Selection: ")
    if entry.lower() == 's':
        return 1
    elif entry.lower() == 'x':
        return 0
    else:
        return 2

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

def replay(grid:grid, path:list):
    pos = []
    if len(path) == 0 or path == None:
        return False
    for p in path:
        pos.append(p.get_pos())
    for p in path:
        utils.cls()
        header()
        draw_grid(grid,p.get_pos()[0], p.get_pos()[1])
        print("Bot Coordinate:", p.get_pos())
        print_lists("Recommended Path Coordinate:", path)
        time.sleep(0.2)
    if input("Enter Y/N to replay: ").lower() == 'n':
        return False
    else:
        return True

def print_path(grid:grid, path:list, time_elapsed:float):
    if len(path) == 0:
        header()
        draw_grid(grid)
        print("NO RECOMMENDED PATH DETECTED FOR GIVEN MAZE!")
        print("\nA* Search Time: " + str(time_elapsed) + "s")
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
    print_lists("Recommended Path Coordinate: ", pos)
    print_lists("Recommended Path Directions: ", direction)
    print("Time taken: " + str(time_elapsed) + "s")
    return [grid.grid_as_string(), pos, direction]

#Prints the major components of a grid printout
def main(grid:grid, frontier:list, explored:list, rapid_search:bool, cont:bool=True):
    if not rapid_search:
        utils.cls()
        header()
        print("A* Searching...\n")
        print("NOTICE: THIS DOES NOT SHOW THE OPTIMAL PATH YET\nAS THE UI ITERATES THROUGH THE EXPLORED LIST.\n")
        for e in explored:
            pos = e.get_pos()
            if grid.tiles[pos[0]][pos[1]].type == ".": 
                grid.tiles[pos[0]][pos[1]].type = 'E'
            elif "F" in grid.tiles[pos[0]][pos[1]].type:
                grid.tiles[pos[0]][pos[1]].type += "E"
        for f in frontier:
            pos = f.get_pos()
            if grid.tiles[pos[0]][pos[1]].type == ".": 
                grid.tiles[pos[0]][pos[1]].type = 'F'
        draw_grid(grid)
        if speedup(frontier, explored):
            print("Display Speedup Mode\n")
        print_lists("Bot's Frontier (" + str(len(frontier)) + "): ", frontier)
        print_lists("Bot's Explored (" + str(len(explored)) + "): ", explored)
        if speedup(frontier, explored):
            time.sleep(0.01)
        else:
            time.sleep(0.25)
        if cont and not speedup(frontier, explored):
            input("\n\nPress Enter to continue...")

def speedup(frontier:list, explored:list):
    return len(frontier) > 20 or len(explored) > 20

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
    br_limit = 8
    for l in list:
        if type(l) == tile:
            output += str(l.get_pos()) + " "
        else:
            output += str(l).strip() + " "
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
    output = "   "
    for x in range(size): 
        output += str(x) + " "
    output += "\n   "
    for x in range(size): 
        output += "- "
    output += "\n"
    for y in range(size):
        output += str(y) + "| "
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