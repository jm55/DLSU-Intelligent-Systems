import time

import astar
import utilities as utils
from objects import *

def header():
    utils.cls()
    print("MazeBot Test.py")
    print("Cruzada, Escalona, Francisco, Loyola\n")

def print_results(results, passing_rate=None, lap=None):
    header()
    if lap != None:
        print("Lap: " + str(lap))
    for r in results:
        print("File: " + r[0] + " Size: " + str(r[3]) + " (" + "{:.4f}".format(r[2]) + "s) = " + r[1])
    if passing_rate != None:
        print("\nSuccess rate: " + "{:.2f}".format(passing_rate) + "%")


rapid_search = True
manual_cont = False
test_files = [("test_1.txt", True), ("test_2.txt", False), ("test_3.txt", False), ("test_4.txt", False), ("test_5.txt", False), 
              ("test_6.txt", True), ("test_7.txt", True), ("test_8.txt", True), ("test_9.txt", True), ("end_3.txt", True), 
              ("end_4.txt", True), ("end_6.txt", True), ("end_8.txt", True), ("end_10.txt", True), ("end_20.txt", True), 
              ("end_30.txt", True), ("end_40.txt", True), ("end_50.txt", True), ("end_64.txt", True)] #Assumes to be placed in mazes folder
results = []
passed = 0
ave_results = [0] * len(test_files)
ctr = 0

header()
laps = int(input("Enter laps: "))

print("Searching...")
for l in range(laps):
    for test in range(len(test_files)):
        t = test_files[test]
        print_results(results,None,l+1)
        print("Running " + t[0] + "...")
        grid = utils.read_maze("mazes\\" + t[0])

        #inject bot at grid
        bot_loc = grid.locate_s()
        grid.tiles[bot_loc[0]][bot_loc[1]].type = 'SB'

        start = time.time()
        path = astar.astar(grid, rapid_search, manual_cont, True)
        end = time.time()
        
        if (len(path) > 0) == t[1]:
            passed += 1
            results.append([t[0], " Passed! ", end-start, grid.get_size()])
            ave_results[test] += end-start
        else:
            results.append([t[0], " Failed! ", end-start, grid.get_size()])
        grid = None
    print_results(results, (passed/len(test_files))*100)
    results = []

header()
print("Laps: " + str(laps))
print("Average Times:")
for r in range(len(ave_results)):
    ave_results[r] /= laps
for t in range(len(test_files)):
    print(test_files[t][0] + ": " + "{:.4f}".format(ave_results[t]))