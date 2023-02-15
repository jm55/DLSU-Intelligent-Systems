import time
import math

import astar
import utilities as utils
from objects import *


test_files = ["test_1.txt", "test_2.txt", "test_3.txt", "test_4.txt", "test_5.txt", "test_6.txt", "test_7.txt"]
test_results = [True, False, False, False, False, True, True] #True if has path, False if otherwise
results = []
passed = 0
for i in range(len(test_files)):
    grid = utils.read_maze(test_files[i])
    rapid_search = True
    manual_cont = False

    #inject bot at grid
    bot_loc = grid.locate_s()
    grid.tiles[bot_loc[0]][bot_loc[1]].type = 'SB'

    start = time.time()
    path = astar.astar(grid, rapid_search, manual_cont, True)
    end = time.time()

    if (len(path) > 0) == test_results[i]:
        passed += 1
        results.append([test_files[i], " Passed! ", end-start])
    else:
        results.append([test_files[i], " Failed! ", end-start])

for r in results:
    print("File: " + r[0] + " (" + "{:.4f}".format(r[2]) + "s) = " + r[1])
print("\nSuccess rate: " + str((passed/len(test_files))*100))