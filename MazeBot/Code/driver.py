import utilities as utils
import gui
from astar import astar

def main():
    utils.cls()

    grid = utils.read_maze(gui.ask_file())

    #inject bot at grid
    bot_loc = grid.locate_s()
    grid.tiles[bot_loc[0]][bot_loc[1]].type = 'SB'

    path = astar(grid)
    gui.print_path(grid, path)

def chk():
    print("This is driver.py")

if __name__ == "__main__":
    main()
    exit(0)