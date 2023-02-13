from objects import *
from utilities import *
from astar import *


#print(get_manhattan(pos1.get_pos(), pos2.get_pos()))

grid = read_maze("maze.txt")
# tiles = generate_tiles(grid)

# tiles = generate_tiles(from_txt)
# grid_obj = grid(tiles)
# grid_obj.get_index("S")
# print(tiles)



path = astar(grid)
print(path)