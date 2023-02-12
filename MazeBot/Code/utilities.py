import os
import re

def chk(): #To check if the script/class imports correctly.
    print("This is utilities.py")

def readfile(filename):
    #Get extract file contents from file
    #Suggested as a list containing per line of the maze path.
    #Suggested example return: ['....G','.####', '...#S', '.#.#.', '.#...']

    maze = []

    with open(filename) as maze_file:
        str_dimension = maze_file.readline().strip()
        
        global dimension
        dimension = int(str_dimension)

        maze_contents = maze_file.readlines()
        for row in maze_contents:
            maze.append(row.strip())

    return maze

def cls(): #Execute 'cls' command on Command Prompt
    os.system("cls")

if __name__ == "__main__":
    maze = readfile('maze.txt')
    print(maze)