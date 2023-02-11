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
    print(maze)

if __name__ == "__main__":
    temp = []
    define_maze()

