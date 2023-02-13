import copy

import utilities as utils
from grid import grid
import gui

class bot:
    def __init__(self, init_grid):
        self.initial_grid = init_grid
        self.frontier = []
        self.explored = []

    #Finds the lowest f from the open/frontier states/nodes
    def find_lowest_f(self):
        lowest = 4096 #Arbitrary init lowest by 64^2
        idx = -1 #Index for value return

        if len(self.frontier) == 0: #Although unlikely, return None if no contents in frontier list
            return None

        for o in range(len(self.frontier)):
            if self.frontier[o].f_cost < lowest:
                lowest = self.frontier[o].f_cost
                idx = o

        return self.frontier[idx] #Return grid item w/ lowest f

    #Based from SebLague's AStar Pseudocode
    def a_star(self):
        self.frontier.append(self.initial_grid) #Start frontier with initial_grid/state

        while True:
            ongoing = self.find_lowest_f() #ongoing node as one with the lowest f_cost
            self.remove_ongoing_frontier(ongoing) #Remove ongoing from open
            self.explored.append(ongoing) #Add ongoing to closed

            #Check if goal
            if ongoing.check_if_goal():
                #Do a final replay
                gui.replay(self.frontier, self.explored, False)
                utils.cls()

                #Display final state
                gui.main(ongoing)

                #Notify user for Goal has been reached.
                print("\nGOAL REACHED!")
                
                #Return to driver
                input("Press any to key to proceed to complete replay...")
                break

            #Check for adjacent tiles of the ongoing bot
            for adjacent in ongoing.bot_adjacent(): 
                if adjacent == None: #Skip if cannot move on adjacent
                    continue
                new_grid = self.new_grid(ongoing, adjacent[0], adjacent[1]) #Create a new grid for the adjacent
                if new_grid != None or self.find_in_frontier(new_grid) == -1: #Skips the out of bounds and walls
                    if self.find_in_explored(new_grid) == -1: #Check if not a duplicate
                        if new_grid.f_cost < ongoing.f_cost or self.find_in_frontier(new_grid) == -1: #Check if cost of adjacent is less or not in frontier
                            self.frontier.append(new_grid)   

            #Conduct replay on how move turned out                         
            gui.replay(self.frontier, self.explored)
    
    #Remove a given grid from explored list
    def remove_ongoing_explored(self, ongoing:grid):
        idx = self.find_in_frontier(ongoing)
        if idx > -1:
            self.explored.pop(idx)
            
    #Remove a given grid from frontier list    
    def remove_ongoing_frontier(self, ongoing:grid):
        #return None
        idx = self.find_in_frontier(ongoing)
        #print("open idx: ", idx)
        if idx > -1:
            self.frontier.pop(idx)

    #Creates a new grid from the ongoing grid where its bot is then immediately updated.
    def new_grid(self, ongoing:grid, x:int, y:int):
        new_grid = copy.deepcopy(ongoing) #Using = alone is just reference 
        new_grid.update_bot(x,y)
        return new_grid

    #Check if a new_grid item is already found in the open list of states
    #Checks if pos of new_grid's bot is found on any item in self.frontier
    def find_in_frontier(self, new_grid: grid):
        for o in range(len(self.frontier)):
            if self.frontier[o].locate_bot() == new_grid.locate_bot():
                return o
        return -1

    #Check if a new_grid item is already found in the closed list of states
    #Checks if pos of new_grid's bot is found on any item in self.explored
    def find_in_explored(self, new_grid:grid):
        for c in range(len(self.explored)):
            if self.explored[c].locate_bot() == new_grid.locate_bot():
                return c
        return -1