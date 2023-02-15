import time
import math

import astar
import utilities as utils
from objects import *

def header():
    utils.cls()
    print("MazeBot Test.py")
    print("Cruzada, Escalona, Francisco, Loyola\n")

def print_results(results, passing_rate=None):
    header()
    for r in results:
        print("File: " + r[0] + " (" + "{:.4f}".format(r[2]) + "s) = " + r[1])
    if passing_rate != None:
        print("\nSuccess rate: " + "{:.2f}".format(passing_rate) + "%")

test_files = ["test_1.txt", "test_2.txt", "test_3.txt", "test_4.txt", "test_5.txt", 
              "test_6.txt", "test_7.txt", "test_8.txt", "test_9.txt", "end_3.txt", 
              "end_4.txt", "end_6.txt", "end_8.txt", "end_10.txt", "end_20.txt", 
              "end_30.txt", "end_40.txt", "end_50.txt", "end_64.txt"] #Assumes to be placed in mazes folder
test_results = [True, False, False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True] #True if has path, False if otherwise
results = []
passed = 0

if len(test_files) != len(test_results):
    header()
    print("Kindly double check content of test_files and test_results.")
    exit(0)

header()
print("Searching...")
for i in range(len(test_files)):
    print_results(results)
    print("Running " + test_files[i] + "...")
    grid = utils.read_maze("mazes\\" + test_files[i])
    rapid_search = False
    manual_cont = False

    #inject bot at grid
    bot_loc = grid.locate_s()
    grid.tiles[bot_loc[0]][bot_loc[1]].type = 'SB'

    start = time.time()
    path = astar.astar(grid, rapid_search, manual_cont)
    end = time.time()
    
    if (len(path) > 0) == test_results[i]:
        passed += 1
        results.append([test_files[i], " Passed! ", end-start])
    else:
        results.append([test_files[i], " Failed! ", end-start])

print_results(results, (passed/len(test_files))*100)