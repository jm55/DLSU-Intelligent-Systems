import numpy as np
from array import *
def define_maze():

    with open("maze.txt") as maze_file:
        str_dimension = maze_file.readline().strip()
        maze_contents = maze_file.readlines()

        for row in maze_contents:
            temp.append(row.strip())

    dimension = int(str_dimension)


    #Make maze 2d array
    maze = []
    maze.append(temp)
    #print(maze)
    
    maze = np.array(maze)

    #test
    # print(maze[0,0])
    # print(maze[0,1])
    # print(maze[0,2])
    # print(maze[0,3])
    # print(maze[0,4])
    # print(maze[0,5])
    # print(maze[0,6])
    # print(maze[0,7])
    # print(maze[0,8])
    # print(maze[0,9])


   


if __name__ == "__main__":
    temp = []
    define_maze()