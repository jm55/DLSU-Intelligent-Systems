import copy

import utilities as utils
from grid import grid

class bot:
    def __init__(self, init_grid):
        self.initial_grid = init_grid
        self.open = []
        self.closed = []

    def find_lowest_f(self):
        lowest = 4096 #Arbitrary init lowest by 64^2
        idx = -1

        if len(self.open) == 0:
            return None

        for o in range(len(self.open)):
            if self.open[o].f_cost < lowest:
                lowest = self.open[o].f_cost
                idx = o
        return self.open[idx] #Return grid item w/ lowest f

    #Based from SebLague's AStar Pseudocode
    def a_star(self):
        
        self.open.append(self.initial_grid)

        while True:
            self.test_print_open()
            print("Open: ", self.get_open_list())
            print("Closed: ", self.get_closed_list())

            current = self.find_lowest_f() #Current node as one with the lowest f_cost
            self.remove_current_open(current) #Remove current from open
            self.closed.append(current) #Add current to closed

            #Check if goal
            if current.check_if_goal():
                break

            for neighbor in current.neighbor_bot(): #Check for neighbors of current
                if neighbor == None:
                    continue
                new_grid = self.new_grid(current, neighbor[0], neighbor[1]) #Create a new grid for the neighbor
                if new_grid != None or self.find_in_open(new_grid) == -1: #Skips the out of bounds and walls
                    print(new_grid.get_costs())
                    print("Current: ", current.locate_bot(), ", Neighbor: ", neighbor, " ", self.find_in_closed(new_grid), new_grid.f_cost, current.f_cost)
                    if self.find_in_closed(new_grid) == -1: #Check if not a duplicate
                        if new_grid.f_cost < current.f_cost or self.find_in_open(new_grid) == -1:
                            self.open.append(new_grid)
            '''
            foreach neighbour of the current node
                if neighbour is not traversable or neighbour is in CLOSED
                        skip to the next neighbour
 
                if new path to neighbour is shorter OR neighbour is not in OPEN
                        set f_cost of neighbour
                        set parent of neighbour to current
                        if neighbour is not in OPEN
                                add neighbour to OPEN
            '''
            input("Enter to continue...")
            utils.cls()
    
    def test_print_open(self):
        for o in self.open:
            o.test_print()

    def remove_current_closed(self, current:grid):
        #return None
        idx = self.find_in_open(current)
        print("closed idx: ", idx)
        if idx > -1:
            self.closed.pop(idx)
            
    def remove_current_open(self, current:grid):
        #return None
        idx = self.find_in_open(current)
        print("open idx: ", idx)
        if idx > -1:
            self.open.pop(idx)

    #Creates a new grid from the current grid where its bot is then immediately updated.
    def new_grid(self, current:grid, x:int, y:int):
        new_grid = copy.deepcopy(current) #Using = alone is just reference 
        new_grid.update_bot(x,y)
        return new_grid

    #Check if a new_grid item is already found in the open list of states
    #Checks if pos of new_grid's bot is found on any item in self.open
    def find_in_open(self, new_grid: grid):
        for o in range(len(self.open)):
            if self.open[o].locate_bot() == new_grid.locate_bot():
                return o
        return -1

    #Check if a new_grid item is already found in the closed list of states
    #Checks if pos of new_grid's bot is found on any item in self.closed
    def find_in_closed(self, new_grid:grid):
        for c in range(len(self.closed)):
            if self.closed[c].locate_bot() == new_grid.locate_bot():
                return c
        return -1

    #Get the contents of self.open by bot location tuple
    def get_open_list(self):
        open_list = []
        for o in self.open:
            open_list.append(o.locate_bot())
        return str(open_list)

    #Get the contents of self.closed by bot location tuple
    def get_closed_list(self):
        closed_list = []
        for o in self.closed:
            closed_list.append(o.locate_bot())
        return str(closed_list)

    def heuristic(self):
        return None