import utilities as utils
import gui
from astar import astar

def main():
    utils.cls()

    grid = utils.read_maze(gui.ask_file())
    rapid_search = gui.ask_rapid_search()

    #inject bot at grid
    bot_loc = grid.locate_s()
    grid.tiles[bot_loc[0]][bot_loc[1]].type = 'SB'

    path = astar(grid, rapid_search)
    printable = gui.print_path(grid, path)
    if gui.ask_save_file():
        utils.save_file(printable)

def chk():
    print("This is driver.py")

if __name__ == "__main__":
    main()
    exit(0)