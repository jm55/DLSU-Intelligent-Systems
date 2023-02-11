import numpy as np
from array import *

dimension = 0

def findStart(maze):

    count_i = 0
    count_j = 0

    for i in maze:
        count_i += 1
        for j in i:
            count_j += 1
            if j == 'S':
                return count_i, count_j
        count_j = 0
    count_i = 0

def findGoal(maze):

    count_i = 0
    count_j = 0

    for i in maze:
        count_i += 1
        for j in i:
            count_j += 1
            if j == 'G':
                return count_i, count_j
        count_j = 0
    count_i = 0


def main():

    with open('maze.txt') as maze_file:
        str_dimension = maze_file.readline().strip()
        dimension = int(str_dimension)

        maze_contents = maze_file.readlines()
        for row in maze_contents:
            maze.append(row.strip())

        # print(temp)
        # print(temp[3][4])
        # print(temp[0][4])
    
if __name__ == "__main__":
    maze = []
    main()
    i, j = findGoal(maze)
    print(i)
    print(j)

    i, j = findStart(maze)
    print(i)
    print(j)
