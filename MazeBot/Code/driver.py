from objects import *
from utilities import *
from astar import *


def main():
    grid = read_maze("maze.txt")
    path = astar(grid)
    print(path)
def chk():
    print("This is driver.py")

if __name__ == "__main__":
    main()
    exit(0)