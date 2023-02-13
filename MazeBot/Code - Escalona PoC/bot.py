import copy

import utilities as utils
from grid import grid
import gui

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
            current = self.find_lowest_f() #Current node as one with the lowest f_cost
            self.remove_current_open(current) #Remove current from open
            self.closed.append(current) #Add current to closed

            #Check if goal
            if current.check_if_goal():
                gui.replay(self.open, self.closed, False, True)
                utils.cls()
                gui.main(current)
                print("\nGOAL REACHED!")
                input("Press any to key to proceed to complete replay...")
                break #Returns to driver

            for neighbor in current.neighbor_bot(): #Check for neighbors of current
                if neighbor == None:
                    continue
                new_grid = self.new_grid(current, neighbor[0], neighbor[1]) #Create a new grid for the neighbor
                if new_grid != None or self.find_in_open(new_grid) == -1: #Skips the out of bounds and walls
                    #print(new_grid.get_costs())
                    #print("Current: ", current.locate_bot(), ", Neighbor: ", neighbor, " ", self.find_in_closed(new_grid), new_grid.f_cost, current.f_cost)
                    if self.find_in_closed(new_grid) == -1: #Check if not a duplicate
                        if new_grid.f_cost < current.f_cost or self.find_in_open(new_grid) == -1:
                            self.open.append(new_grid)                            
            gui.replay(self.open, self.closed)
    
    def test_print_open(self):
        for o in self.open:
            o.test_print()

    def test_print_closed(self):
        for c in self.closed:
            c.test_print()

    def remove_current_closed(self, current:grid):
        #return None
        idx = self.find_in_open(current)
        #print("closed idx: ", idx)
        if idx > -1:
            self.closed.pop(idx)
            
    def remove_current_open(self, current:grid):
        #return None
        idx = self.find_in_open(current)
        #print("open idx: ", idx)
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

    def heuristic(self):
        return None