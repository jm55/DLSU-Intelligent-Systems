import time

import utilities as utils
import gui
from astar import astar

def main():
    while True:
        utils.cls()
        grid = utils.read_maze(gui.ask_file())
        rapid_search = gui.ask_rapid_search()
        manual_cont = False
        if not rapid_search:
            manual_cont = gui.ask_manual_cont()

        #inject bot at grid
        bot_loc = grid.locate_s()
        grid.tiles[bot_loc[0]][bot_loc[1]].type = 'SB'

        start = time.time()
        path = astar(grid, rapid_search, manual_cont)
        end = time.time()

        replay = True
        while replay:
            replay = gui.replay(grid, path)

        printable = None
        elapsed = None
        if rapid_search:
            elapsed = end-start
        printable = gui.print_path(grid, path, elapsed)
        
        post_search = gui.ask_post_search()
        if post_search == 1:
            utils.save_file(printable)
        elif post_search == 0:
            break

def chk():
    print("This is driver.py")

if __name__ == "__main__":
    main()
    exit(0)